#!/usr/bin/env node
/**
 * Page QA: accessibility (axe-core, WCAG 2.1 A/AA), horizontal overflow at phone width,
 * broken images, broken local links/anchors, and screenshots.
 *
 * Usage:
 *   node Build_Tools/test_pages.js <root_dir> <page.html> [<page.html> ...] [--shots <dir>]
 * Pages are paths relative to root_dir. A tiny static server serves root_dir so
 * absolute links ("/blog/") resolve the way they will on a real host.
 * Exit code 1 if any page has a violation.
 */
const fs = require('fs');
const http = require('http');
const path = require('path');

function loadPlaywright() {
  for (const c of ['playwright', '/opt/node22/lib/node_modules/playwright']) {
    try { return require(c); } catch (e) { /* next */ }
  }
  throw new Error('Playwright not found');
}

const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.woff2': 'font/woff2', '.xml': 'application/xml',
  '.txt': 'text/plain', '.json': 'application/json', '.ico': 'image/x-icon', '.pdf': 'application/pdf' };

function serve(root) {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let p = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
      let file = path.join(root, p);
      if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
      if (!fs.existsSync(file)) { res.writeHead(404); res.end('not found'); return; }
      res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
      fs.createReadStream(file).pipe(res);
    });
    server.listen(0, '127.0.0.1', () => resolve(server));
  });
}

(async () => {
  const args = process.argv.slice(2);
  const shotIdx = args.indexOf('--shots');
  const shotsDir = shotIdx >= 0 ? args.splice(shotIdx, 2)[1] : null;
  const [root, ...pages] = args;
  const server = await serve(path.resolve(root));
  const base = `http://127.0.0.1:${server.address().port}`;
  const axeSrc = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  let failures = 0;
  for (const rel of pages) {
    const url = `${base}/${rel.replace(/index\.html$/, '')}`;
    const problems = [];
    for (const vp of [{ name: 'desktop', width: 1280, height: 900 }, { name: 'mobile', width: 375, height: 800 }]) {
      const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
      const page = await ctx.newPage();
      const failedRequests = [];
      page.on('response', (r) => { if (r.status() >= 400 && r.url().startsWith(base)) failedRequests.push(`${r.status()} ${r.url().slice(base.length)}`); });
      page.on('pageerror', (e) => problems.push(`[${vp.name}] JS error: ${e.message}`));
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      if (overflow > 1) problems.push(`[${vp.name}] horizontal overflow of ${overflow}px`);
      const brokenImgs = await page.evaluate(async () => {
        const imgs = [...document.images];
        for (const i of imgs) { i.loading = 'eager'; }
        await Promise.all(imgs.map((i) => (i.complete ? null : new Promise((r) => { i.onload = i.onerror = r; }))));
        return imgs.filter((i) => !i.naturalWidth).map((i) => i.getAttribute('src'));
      });
      brokenImgs.forEach((s) => problems.push(`[${vp.name}] broken image ${s}`));
      failedRequests.forEach((f) => problems.push(`[${vp.name}] failed request ${f}`));
      if (vp.name === 'desktop') {
        await page.addScriptTag({ content: axeSrc });
        const res = await page.evaluate(async () => axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] } }));
        res.violations.forEach((v) => problems.push(`[axe] ${v.id} (${v.impact}): ${v.help} → ${v.nodes.slice(0, 3).map((n) => n.target.join(' ')).join(' | ')}`));
        // local links and anchors
        const links = await page.evaluate(() => [...document.querySelectorAll('a[href]')].map((a) => a.getAttribute('href')));
        for (const href of [...new Set(links)]) {
          if (/^(https?:|mailto:|tel:)/.test(href)) continue;
          if (href.startsWith('#')) {
            if (href.length > 1) {
              const ok = await page.evaluate((id) => !!document.getElementById(id), href.slice(1));
              if (!ok) problems.push(`[links] missing anchor ${href}`);
            }
            continue;
          }
          const target = new URL(href, url).toString();
          const r = await page.request.get(target);
          if (r.status() >= 400) problems.push(`[links] ${r.status()} ${href}`);
        }
      }
      if (shotsDir) {
        fs.mkdirSync(shotsDir, { recursive: true });
        const name = rel.replace(/\/?index\.html$/, '').replace(/[\/.]/g, '_') || 'home';
        await page.screenshot({ path: path.join(shotsDir, `${name}_${vp.name}.png`), fullPage: true });
      }
      await ctx.close();
    }
    if (problems.length) { failures += 1; console.log(`FAIL ${rel}`); problems.forEach((p) => console.log('   ', p)); } else console.log(`PASS ${rel}`);
  }
  await browser.close();
  server.close();
  console.log(`${pages.length - failures}/${pages.length} pages passed`);
  process.exit(failures ? 1 : 0);
})();

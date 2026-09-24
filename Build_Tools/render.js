#!/usr/bin/env node
/**
 * Render HTML files to PNG or PDF with headless Chromium (Playwright).
 *
 * Usage:
 *   node render.js jobs.json
 *
 * jobs.json is an array of jobs:
 *   { "html": "/abs/path/file.html", "out": "/abs/path/out.png", "type": "png",
 *     "width": 1200, "height": 630, "scale": 2, "fullPage": false, "selector": null }
 *   { "html": "/abs/path/doc.html", "out": "/abs/path/doc.pdf", "type": "pdf",
 *     "format": "Letter", "landscape": false, "margin": {"top":"0","bottom":"0","left":"0","right":"0"},
 *     "displayHeaderFooter": false, "footerTemplate": "" }
 */
const fs = require('fs');
const path = require('path');

function loadPlaywright() {
  const candidates = ['playwright', '/opt/node22/lib/node_modules/playwright'];
  for (const c of candidates) {
    try { return require(c); } catch (e) { /* try next */ }
  }
  throw new Error('Playwright not found. Install it with `npm i -g playwright` and a Chromium browser.');
}

(async () => {
  const jobsFile = process.argv[2];
  if (!jobsFile) { console.error('usage: node render.js jobs.json'); process.exit(2); }
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  let ok = 0;
  try {
    for (const job of jobs) {
      const context = await browser.newContext({
        viewport: { width: job.width || 1200, height: job.height || 800 },
        deviceScaleFactor: job.scale || 1,
      });
      const page = await context.newPage();
      await page.goto('file://' + path.resolve(job.html), { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      fs.mkdirSync(path.dirname(job.out), { recursive: true });
      if (job.type === 'pdf') {
        await page.emulateMedia({ media: 'print' });
        await page.pdf({
          path: job.out,
          format: job.format || 'Letter',
          landscape: !!job.landscape,
          printBackground: true,
          preferCSSPageSize: job.preferCSSPageSize !== false,
          margin: job.margin || { top: '0', bottom: '0', left: '0', right: '0' },
          displayHeaderFooter: !!job.displayHeaderFooter,
          headerTemplate: job.headerTemplate || '<span></span>',
          footerTemplate: job.footerTemplate || '<span></span>',
        });
      } else {
        const opts = { path: job.out, fullPage: !!job.fullPage, omitBackground: !!job.transparent };
        if (job.selector) {
          await page.locator(job.selector).screenshot(opts);
        } else {
          await page.screenshot(opts);
        }
      }
      await context.close();
      ok += 1;
      console.log('rendered', path.relative(process.cwd(), job.out));
    }
  } finally {
    await browser.close();
  }
  console.log(`done: ${ok}/${jobs.length}`);
})().catch((err) => { console.error(err); process.exit(1); });

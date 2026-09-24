# 03 · Website (Eleventy static site)

**Status: built and tested locally. Not deployed.** No domain has been bought, no hosting account created, and nothing is public. Preview builds are marked `noindex`, and `robots.txt` blocks all crawlers until a site URL is configured.

| | |
|---|---|
| Generator | [Eleventy](https://www.11ty.dev/) 3.1.6 (Node ≥ 18) |
| Hosting plan | Cloudflare Pages, Free plan (500 builds/month, per Cloudflare's limits page, checked 24 Sept 2026) |
| Analytics plan | Cloudflare Web Analytics: cookie-free, one-click enable for Pages projects |
| Pages | Home, Articles, 5 category pages, 20 articles, Resources, Newsletter, About, Contact, Editorial policy, Affiliate disclosure, Privacy (draft), Terms (draft), 404, `/bundle/` landing page |
| SEO | Per-page titles and meta descriptions, canonical URLs, Open Graph images (one per article), JSON-LD (Article, BreadcrumbList, WebSite), `sitemap.xml`, `robots.txt`, Atom feed, internal links and related articles |
| Accessibility | Skip link, landmarks, visible focus, WCAG AA contrast, responsive tables, alt text |

## Run it locally

```bash
cd Content_Automation_Business/03_Website
npm install
npm run serve          # preview with ALL articles at http://localhost:8080
npm run build          # production build: approved/published articles only
npm test               # preview build + HTML validation + accessibility/link/mobile tests
```

## Where things live

| Path | What |
|---|---|
| `../04_Blog_Articles/*.md` | Articles (source of truth). Copied into `src/blog/posts/` at build time by `scripts/sync-articles.mjs` |
| `src/_data/site.js` | Site settings. Reads `STORE_URL`, `SITE_URL`, `NEWSLETTER_URL` and `SUPPORT_EMAIL` from `Build_Tools/launch_config.py` (env vars override) |
| `src/_data/categories.json`, `products.json` | Topics and product cards |
| `src/_includes/` | Layouts (base, article, page) and partials (header, footer, newsletter, cards, product CTA) |
| `src/assets/` | CSS, JS (copy buttons), self-hosted fonts (OFL), images, OG images |
| `src/downloads/` | Free Invoice Tracker Starter (.xlsx), with formulas tested by `Build_Tools/build_invoice_starter.py` |
| `src/_headers` | Security and cache headers for Cloudflare Pages |
| `.htmlvalidate.json` | HTML validation rules |

## The approval gate

`npm run build` only includes articles with `status: approved` or `status: published`. Today all 20 are `ready-for-review`, so a production build contains **0 articles** by design. Approve articles (see `04_Blog_Articles/README.md`) before deploying.

The build always starts by deleting `_site/`, so an unapproved article from an earlier preview can never be deployed by accident.

## Deploy to Cloudflare Pages (needs your approval and accounts)

1. **Buy a domain** (see `02_Branding` for name notes; availability not verified). Optional: you can launch on the free `*.pages.dev` address first.
2. Create a free Cloudflare account, then **Workers & Pages → Create → Pages → Connect to Git** and select this repository.
3. Build settings:
   - **Root directory:** `Content_Automation_Business/03_Website`
   - **Build command:** `npm run build`
   - **Output directory:** `_site`
   - **Environment variable:** `NODE_VERSION` = `22`
   - **Environment variable:** `SITE_URL` = your final URL (e.g. `https://bandofone.co`). This switches off the preview banner and `noindex`, and enables canonical URLs and the sitemap.
4. Deploy, then add your **custom domain** under the project's Custom domains tab.
5. **Analytics:** in the Pages project open **Metrics** and select **Enable** under Web Analytics (Cloudflare docs: "Enable Web Analytics · Cloudflare Pages"). No code change is needed. (Alternatively, set `CF_ANALYTICS_TOKEN` to use the JS beacon.)
6. **Search Console (free):** add the domain property in Google Search Console, verify via DNS, and submit `https://YOURDOMAIN/sitemap.xml`. Do the same in Bing Webmaster Tools if you like.

## Connect the newsletter (after you create a MailerLite or Kit account)

- Set `NEWSLETTER_URL` in `Build_Tools/launch_config.py` to your hosted signup page (MailerLite and Kit both provide one). Every "Get the starter kit" button then points there.
- Until then, the Newsletter page states that signup opens at launch, and **no form collects email addresses**.
- Setup details and the email sequence: `../07_Email_Newsletter/`.

## Before you publish: checklist

- [ ] `SITE_URL`, `SUPPORT_EMAIL`, `NEWSLETTER_URL` and `STORE_URL` set (search the build for `add before launch`: there should be no matches)
- [ ] Privacy policy and terms completed (bracketed fields) and reviewed
- [ ] Articles you want live set to `status: approved`, and facts re-checked if older than 90 days
- [ ] `npm test` passes
- [ ] Web Analytics enabled; sitemap submitted to Search Console

## Test results (24 Sept 2026, preview build with all 20 articles)

- **html-validate:** 0 errors across all pages
- **axe-core (WCAG 2.1 A/AA):** 0 violations on 37 pages
- **Mobile (375px):** no horizontal overflow on any page
- **Links:** every internal link, anchor and image resolves; external links are not fetched by the test
- **Approval gate:** production build contained 0 articles while all were `ready-for-review`

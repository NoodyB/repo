# 07 · Gumroad storefront package

**Status: draft, unpublished.** No Gumroad account, product or page has been created, and no payment system is connected.

| File / folder | What it is |
|---|---|
| `Pricing_Strategy.md` | Recommended prices, launch-offer mechanics, refund policy and the decisions that need your approval |
| `BandOfOne_Pricing_Calculator.xlsx` | Live calculator: fees, net per sale, Discover sales, refunds, affiliates, break-even. Change the blue inputs. |
| `Listings/` | Ready-to-paste listing copy per product (A, B, C, bundle, free kit): title, slug, summary, description, details, tags, FAQ, support, post-purchase message |
| `images/` | Gumroad covers (1280×720), thumbnails (600×600) and preview images, all made from the real product files |
| `Bundle_Landing_Page/` | Standalone, responsive bundle landing page for your website (self-hosted fonts and images). Buy buttons go live once `STORE_URL` is set in `Build_Tools/launch_config.py`. |
| `Gumroad_Setup_Guide.md` | Step-by-step setup, test purchase and launch-code instructions |

## Recommended prices (pending approval)

| Product | Price | Net per direct sale |
|---|---|---|
| A · The Solo Admin Playbook | $24 | $20.10 |
| B · The Client Desk | $29 | $24.46 |
| C · The Band of One Prompt Library | $19 | $15.75 |
| Bundle (A + B + C) | $49 | $41.88 |
| Free Client Admin Starter Kit | $0 | – |

## Rebuild

```bash
python3 Build_Tools/build_pricing.py         # calculator (then recalc: see Build_Tools/README)
python3 Build_Tools/build_store_images.py    # covers, thumbnails, previews
python3 Build_Tools/build_landing_page.py    # landing page
node Build_Tools/test_pages.js Digital_Products_Business/07_Gumroad_Storefront/Bundle_Landing_Page index.html
```

Landing page QA (2026-09-24): axe-core WCAG 2.1 A/AA, no violations; no horizontal overflow at 375px; all images, local links and anchors resolve.

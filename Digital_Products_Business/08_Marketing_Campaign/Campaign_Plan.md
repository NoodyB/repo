# 30-day product launch campaign plan (Month 2)

**Status: fully drafted, nothing published, posted, sent or scheduled.** Every external step needs your approval.

## How it fits with the content business

Band of One runs one brand and one set of social accounts for both businesses, so the plan is sequenced to avoid double-posting:

| | Month 1: Content (`Content_Automation_Business/05_Social_Media_Content`) | Month 2: Product launch (this folder) |
|---|---|---|
| Goal | Build an audience and an email list with free articles and the starter kit | Launch the products to that audience |
| Videos | 30 (drive to articles and the starter kit) | 30 (teach with real product content; about 1 in 3 asks for a sale) |
| Posts | 15 educational + 10 promotional (free resources) | 15 educational + 10 promotional (products) |
| Email | Welcome + 5-email onboarding + weekly issue | 5-email launch sequence (to opted-in subscribers only) |

Launching into an audience of zero rarely works, so Month 1 comes first. If the store is ready before Month 1 finishes, the launch can move earlier, but keep at least two weeks of content before Day 1 of Month 2.

## Objectives (what "working" means, measured, not promised)

1. **Verify the storefront end to end** with a test purchase before launch (a pass/fail check).
2. **Get first real buyers and feedback.** Track orders, refunds and reasons, and questions asked.
3. **Learn which product and message resonates.** Track bundle share of orders and which posts and videos drive store visits (use UTM links).

No sales, revenue or conversion targets are set here: there's no baseline data yet. After launch, set targets from your real Month 1–2 numbers (see `09_Business_Dashboard`).

## Offer

| Product | Price | Launch code `FOUNDING` (days 8–21, real end date) |
|---|---|---|
| The Solo Admin Playbook | $24 | −$5 |
| The Client Desk | $29 | −$5 |
| The Band of One Prompt Library | $19 | −$4 |
| Complete Bundle | $49 ($72 separately) | −$10 |
| Client Admin Starter Kit | Free | – |

14-day refund policy on all paid products. Rationale and fee math: `07_Gumroad_Storefront/Pricing_Strategy.md`.

## Phases (Month 2 days)

| Days | Phase | Social | Email | Store |
|---|---|---|---|---|
| 1–7 | Pre-launch | Behind-the-build, product tours, free prompts (P-V01–07) | Email 1 on Day 5 | Products set up, **unpublished**; test purchase done |
| 8 | Launch | "It's live" video + post (P-V08, P-P02) | Email 2 | **Publish** (your approval); create `FOUNDING` code |
| 9–19 | Launch window | Product demos, FAQ, who it's not for | Email 3 (Day 12), Email 4 (Day 17) | Answer questions within 2 business days |
| 20–21 | Close | "Ends tomorrow" / "Last day" | Email 5 (Day 21) | Code expires automatically |
| 22–30 | Post-launch | Back to teaching; upgrade path; feedback request | Weekly newsletter resumes | Log refunds and reasons; collect feedback |

## Channels (effort-limited for one person)

| Channel | Why | Frequency |
|---|---|---|
| Short-form vertical video: TikTok, Instagram Reels, YouTube Shorts (same video) | Pew Research (2025) found YouTube used by 84% of U.S. adults and Instagram by 50% (92% and 62% among 30–49-year-olds) | 1 a day |
| LinkedIn (text + native video) | Where consultants, freelancers and B2B service providers network | 4–5 a week |
| Email (MailerLite) | The one channel you own; highest intent | Per the sequence |
| Website + bundle landing page | Where posts and emails send people | Always on |

Source for usage figures: Pew Research Center, "Americans' Social Media Use 2025" (survey Feb–Jun 2025, 5,022 adults).

## Budget: $0

| Item | Cost | Note |
|---|---|---|
| Social posting | $0 | Native apps; optional free scheduler tiers |
| Graphics | $0 | Rendered in `graphics/` from brand assets |
| Email | $0 | MailerLite Free up to 250 subscribers |
| Store | $0 up front | Gumroad fees per sale only |
| Paid ads | **None** | Not recommended until organic data shows which message converts. Any ad spend needs your approval. |

## Assets in this folder

| Asset | File |
|---|---|
| 30 video ideas, scripts and captions | `Month2_Launch_Video_Ideas_Scripts_Captions.md` |
| 15 educational + 10 promotional posts | `Month2_Launch_Educational_and_Promotional_Posts.md` |
| Scheduler import (CSV) | `Month2_Launch_Calendar_scheduler_import.csv` |
| 60-day calendar (both months, dates by formula, status tracking) | `BandOfOne_60-Day_Social_Calendar.xlsx` |
| 5 launch emails | `Emails/Launch_Email_Sequence.md` |
| Lead magnet | `Lead_Magnet/BandOfOne_Client-Admin-Starter-Kit_FREE.pdf` |
| Bundle landing page | `../07_Gumroad_Storefront/Bundle_Landing_Page/index.html` (published on the site at `/bundle/`) |
| Graphics | `graphics/carousels/` (7 carousels, 49 slides), `graphics/promo_cards/` (10), `graphics/video_covers/` (30) |
| Source files (edit these, then rebuild) | `source/launch_videos.yaml`, `source/launch_posts.yaml` → `python3 Build_Tools/build_social.py` |

## Tracking

- Add UTM parameters to every link: `?utm_source=instagram&utm_medium=social&utm_campaign=launch-m2&utm_content=P-V08`
- Record weekly in `09_Business_Dashboard`: store visits (from Gumroad analytics), orders by product, refunds, email opens/clicks, and posts published.
- Keep a "questions asked" log. It's the best source for FAQ updates and future products.

## Guardrails

- No testimonials until real customers give them with permission. No "bestseller" or sales-count claims.
- No fake urgency: the only deadline is the real `FOUNDING` end date.
- Don't post in communities (Reddit, Facebook groups) where self-promotion is against the rules.
- Every public post, email and store listing needs your approval before it goes out.

## Approvals needed from you

1. Brand name and handles (check availability of your chosen handle on each platform)
2. Prices, refund policy and the `FOUNDING` code window
3. The store going live (Gumroad) and a test purchase
4. Every email send and social post (or a standing approval for the calendar as written)

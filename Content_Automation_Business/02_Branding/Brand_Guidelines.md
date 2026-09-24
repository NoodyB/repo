# Welcome to the brand

**Band of One** is one brand shared by two businesses:

1. **Digital products:** guides, templates and prompt libraries sold on Gumroad.
2. **Content:** a website, newsletter and social channels that teach the same audience for free.

These guidelines keep everything we publish recognizably ours: products, articles, videos and emails. They are written for you *and* for any AI assistant producing content for the brand. Paste the relevant section into your prompt when you generate new material.

!!! note "Status"
    "Band of One" is a **working name** pending your approval and a trademark check. All files are built so the name can be swapped: change `Build_Tools/brand.py` and re-run the generators.

# Brand foundation

## Who we serve

People who run a **service business on their own**: freelance designers, writers, developers, marketers, consultants, coaches, virtual assistants, bookkeepers and photographers. They are good at their craft and tired of the admin that surrounds it.

## The problem we solve

A business of one has to be the salesperson, project manager, accountant and marketer at once. Admin eats the week, invoices get paid late, and every new AI tool promises to fix it while adding another subscription.

## What we promise

**Small, specific, tested systems for the admin side of a one-person business.** Fewer prompts, better outcomes, and no new subscription required.

## Positioning statement

*For people who run a service business on their own, Band of One is the practical, no-hype guide to handling client admin with AI and a few simple systems. Unlike AI-tool listicles and 10,000-prompt bundles, we give you complete workflows, with templates you can copy, and we say plainly what AI should not do.*

## Unique value proposition (short forms)

- **Primary:** Practical AI systems for businesses of one.
- **Benefit-led:** Spend less of your week on admin, without buying another tool.
- **Proof-led:** Real workflows, working templates, honest tool notes.

## Personality

| We are | We are not |
|---|---|
| Calm and practical | Hype-driven ("10x your income!") |
| Specific: real examples, real numbers with sources | Vague: "leverage AI to transform your business" |
| Honest about limits | Pretending AI can run your business for you |
| Warm and peer-to-peer | Corporate or preachy |
| Tool-agnostic | Tied to one app or one AI vendor |

# Voice and tone

## How we write

1. **Lead with the job to be done.** "Send a payment reminder that gets a reply" beats "Invoice optimization strategies."
2. **Use plain words.** Short sentences. Explain any jargon once.
3. **Show, don't claim.** Include a template, an example or a screenshot instead of an adjective.
4. **Be honest about uncertainty.** Say "in our testing" or "according to [source, date]", or say we haven't tested it.
5. **Respect the reader's clients.** Never suggest tricks that deceive the people our readers serve.

## Words we use and avoid

| Use | Avoid |
|---|---|
| business of one, solo business, one-person business | solopreneur hustle, grindset |
| system, workflow, checklist, template | hack, secret, cheat code |
| draft with AI, then edit | let AI do it all |
| save time (with a specific example) | guaranteed results, passive income, make $X |
| client, customer | "users" (unless software) |

## Claims policy (non-negotiable)

- No income or results guarantees. No fabricated testimonials, reviews, case studies or "we tested 50 tools" claims.
- Statistics always carry a source and date.
- Reviews state whether a tool was **tested hands-on** (and when) or **researched** from public information.
- Affiliate relationships are disclosed clearly and close to the link.

# Color

## Palette

| Swatch | Name | HEX | RGB | Use for |
|---|---|---|---|---|
| <span class="sw" style="background:#1B2430"></span> | **Ink** | `#1B2430` | 27, 36, 48 | Body text, dark backgrounds |
| <span class="sw" style="background:#FBF8F3"></span> | **Paper** | `#FBF8F3` | 251, 248, 243 | Page backgrounds |
| <span class="sw" style="background:#0F6B64"></span> | **Band Teal** (primary) | `#0F6B64` | 15, 107, 100 | Logo disc, links, primary buttons |
| <span class="sw" style="background:#0A4A45"></span> | **Deep Teal** | `#0A4A45` | 10, 74, 69 | Headers, hover states, dark panels |
| <span class="sw" style="background:#E3F1EE"></span> | **Mist** | `#E3F1EE` | 227, 241, 238 | Tip boxes, light panels |
| <span class="sw" style="background:#E8663D"></span> | **Signal Orange** | `#E8663D` | 232, 102, 61 | The logo band, large graphic accents **only** |
| <span class="sw" style="background:#B8471F"></span> | **Rust** | `#B8471F` | 184, 71, 31 | Accent text, "Buy" buttons, warnings |
| <span class="sw" style="background:#F6C85F"></span> | **Butter** | `#F6C85F` | 246, 200, 95 | Highlights, badges, reversed logo band |
| <span class="sw" style="background:#E4DED3"></span> | **Stone** | `#E4DED3` | 228, 222, 211 | Borders and dividers |
| <span class="sw" style="background:#56606B"></span> | **Slate** | `#56606B` | 86, 96, 107 | Secondary text, captions |

## Accessibility (WCAG 2.x contrast, measured)

| Combination | Ratio | Passes |
|---|---|---|
| Ink on Paper | 14.78:1 | AAA text |
| Slate on Paper | 6.04:1 | AA text |
| Teal on Paper (links) | 5.99:1 | AA text |
| White on Teal (buttons) | 6.35:1 | AA text |
| White on Rust (buttons) | 5.30:1 | AA text |
| Ink on Butter (badges) | 9.95:1 | AAA text |
| White on Signal Orange | 3.28:1 | **Large text / graphics only.** Never use for body text or small buttons. |

**Proportion:** about 60% Paper or white, 25% Ink, 10% Teal, 5% accents (Orange, Butter, Rust).

# Typography

| Role | Typeface | Weights | Fallback |
|---|---|---|---|
| Headlines, covers, logo | **Fraunces** (serif; SIL Open Font License) | 600 SemiBold, 700 Bold; 400 Italic for emphasis | Georgia, serif |
| Body, UI, spreadsheets | **Inter** (sans-serif; SIL OFL) | 400, 500, 600, 700 | system-ui, Arial, sans-serif |
| Prompts, code, data | **JetBrains Mono** (monospace; SIL OFL) | 400, 600 | Consolas, monospace |

All three are free Google Fonts under the SIL Open Font License, which allows commercial use and embedding in PDFs. Font files and licenses are in `02_Branding/fonts/`.

**Type scale (print):** H1 27pt · H2 16.5pt · H3 12.6pt · body 10.6pt · captions 8.8pt.
**Type scale (web):** H1 2.4rem · H2 1.6rem · H3 1.25rem · body 1.0625rem (17px) · line height 1.65.

# Logo

## The mark

A numeral **1** sits inside a teal disc, held by an open **band** of Signal Orange: one person, held together by good systems. The gap in the band keeps it light and forward-moving.

## Files (in `02_Branding/logo/`)

| File | Use |
|---|---|
| `band-of-one-horizontal.svg` / `.png` | Default logo for websites, documents and headers |
| `band-of-one-horizontal-reversed.svg` / `.png` | On Ink or dark photos |
| `band-of-one-stacked.svg` / `.png` | Square-ish spaces, covers, merch |
| `band-of-one-mark.svg` / `.png` | Avatars, favicons, stickers |
| `band-of-one-app-icon.svg` / `.png` | Social profile pictures, app icons |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` | Website |

## Rules

- **Clear space:** keep empty space around the logo at least equal to the height of the "1".
- **Minimum size:** horizontal logo 120px wide on screen (1.1in in print); mark 20px.
- **Don't** stretch, recolor outside the palette, add shadows, put the full-color logo on busy photos, or rewrite the wordmark in another font.
- The italic *of* is always Teal (Butter on dark backgrounds).

# Graphic language

- **The band:** a thick open ring in Signal Orange (or Butter on dark). Use it as a frame on covers and thumbnails, echoing the logo.
- **Discs:** solid Teal circles as background shapes.
- **Cards:** white or Mist rectangles with 8px corner radius and 1px Stone borders. Used for prompts, tips and checklists.
- **Imagery:** real interface screenshots, simple diagrams, and our own templates. **No stock photos posing as customers. No AI-generated "people" presented as real.**
- **Icons:** simple line icons, 2px stroke, Ink or Teal.

# Product packaging system

Every product shares one visual system so the bundle feels like a set.

| Element | Rule |
|---|---|
| Cover | Ink background, orange band + teal disc on the right, Fraunces title, product-type kicker in Butter, horizontal reversed logo bottom-left |
| Product color code | Guide = Teal disc · Workbook = Butter band · Prompt Library = Rust band (keeps them distinct in thumbnails) |
| File names | `BandOfOne_<Product>_v1.0.<ext>` (e.g., `BandOfOne_Solo-Admin-Playbook_v1.0.pdf`) |
| Versioning | v1.0 at launch; minor fixes → v1.1; bigger updates → v2.0; changes logged in each product's `CHANGELOG.md` |
| Included in every ZIP | `START-HERE.pdf`, the product files, `LICENSE.txt`, `CHANGELOG.md` |
| Gumroad thumbnail | 1:1 square (1600×1600) plus a 1280×720 cover image |

# Social profiles

| Platform | Handle to reserve | Profile image | Banner |
|---|---|---|---|
| Instagram, TikTok, YouTube, Pinterest, LinkedIn, X/Threads | `@bandofonehq` (check availability) | `social/avatar-400.png` | `social/` folder (sized per platform) |

Short bios live in `Content_Automation_Business/02_Branding/Content_Brand_Strategy.md`.

# Decisions you need to approve

1. The working name **Band of One** and domain choice (see *Brand Name Options*).
2. The palette and logo (changeable in `Build_Tools/brand.py` + `make_logo.py`).
3. Handles to reserve.

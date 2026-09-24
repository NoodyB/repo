"""Build the bundle landing page (standalone, self-hosted assets) for the Band of One Complete Bundle.

Store links come from launch_config.py. While STORE_URL is empty the page shows a
"preview" banner and the buy buttons scroll to the pricing section instead of a store.
Run: python3 Build_Tools/build_landing_page.py
"""
import html
import shutil

from PIL import Image

from brand import COLORS as C, ROOT
from launch_config import NEWSLETTER_URL, SITE_URL, STORE_URL

DP = ROOT / "Digital_Products_Business"
OUT = DP / "07_Gumroad_Storefront" / "Bundle_Landing_Page"
ASSETS = OUT / "assets"
NODE = ROOT / "Build_Tools" / "node_modules" / "@fontsource"
STORE_TMP = ROOT / "Build_Tools" / ".tmp" / "store"
FONTS = {
    "inter-400.woff2": NODE / "inter/files/inter-latin-400-normal.woff2",
    "inter-600.woff2": NODE / "inter/files/inter-latin-600-normal.woff2",
    "inter-700.woff2": NODE / "inter/files/inter-latin-700-normal.woff2",
    "fraunces-600.woff2": NODE / "fraunces/files/fraunces-latin-600-normal.woff2",
    "fraunces-700.woff2": NODE / "fraunces/files/fraunces-latin-700-normal.woff2",
    "fraunces-400-italic.woff2": NODE / "fraunces/files/fraunces-latin-400-italic.woff2",
}
SLUGS = {"bundle": "complete-bundle", "playbook": "solo-admin-playbook", "desk": "client-desk", "prompts": "prompt-library"}
PRICES = {"bundle": 49, "playbook": 24, "desk": 29, "prompts": 19}


def buy(key):
    return f"{STORE_URL.rstrip('/')}/l/{SLUGS[key]}" if STORE_URL else "#pricing"


def prepare_assets():
    shutil.rmtree(ASSETS, ignore_errors=True)
    (ASSETS / "fonts").mkdir(parents=True)
    for name, src in FONTS.items():
        shutil.copy(src, ASSETS / "fonts" / name)
    shutil.copy(DP / "02_Branding/logo/band-of-one-horizontal.svg", ASSETS / "logo.svg")
    shutil.copy(DP / "02_Branding/logo/band-of-one-horizontal-on-dark.svg", ASSETS / "logo-on-dark.svg")
    shutil.copy(DP / "02_Branding/logo/favicon.svg", ASSETS / "favicon.svg")
    # product covers from the real PDFs (rendered by build_store_images.py) + real screenshots
    covers = {"cover-playbook.webp": "playbook_p1.png", "cover-desk.webp": "deskguide_p1.png", "cover-prompts.webp": "prompts_p1.png"}
    for out, src in covers.items():
        im = Image.open(STORE_TMP / src).convert("RGB")
        im.thumbnail((560, 725))
        im.save(ASSETS / out, "WEBP", quality=86)
    shots = {
        "shot-dashboard.webp": DP / "04_Premium_Template/screenshot_dashboard.png",
        "shot-prompts.webp": DP / "07_Gumroad_Storefront/images/C_preview_1_cards.png",
        "shot-worksheets.webp": DP / "07_Gumroad_Storefront/images/A_preview_2_worksheets.png",
    }
    for out, src in shots.items():
        im = Image.open(src).convert("RGB")
        im.thumbnail((1400, 900))
        im.save(ASSETS / out, "WEBP", quality=84)
    Image.open(DP / "07_Gumroad_Storefront/images/D_bundle_cover.png").convert("RGB").resize((1200, 675)).save(
        ASSETS / "og-bundle.jpg", "JPEG", quality=86)


def page():
    preview_banner = "" if STORE_URL else (
        '<div class="preview-banner" role="note">Preview: store links are not connected yet. '
        'Buttons scroll to the pricing section until <code>STORE_URL</code> is set in <code>launch_config.py</code>.</div>')
    canonical = f'<link rel="canonical" href="{SITE_URL.rstrip("/")}/bundle/">' if SITE_URL else ""
    og_url = f'<meta property="og:url" content="{SITE_URL.rstrip("/")}/bundle/">' if SITE_URL else ""
    starter = NEWSLETTER_URL or "#starter"
    faqs = [
        ("Do I need a paid AI subscription?", "No. The prompts work in the free tiers of ChatGPT, Claude, Gemini and Copilot. Paid tiers can handle longer inputs such as call transcripts."),
        ("Does The Client Desk work in Google Sheets?", "Yes. Upload the file to Google Drive, open it and choose File → Save as Google Sheets. It also works in Excel 2010 or later and LibreOffice Calc. Apple Numbers hasn't been tested."),
        ("Is it safe to use AI with client information?", "The playbook and the prompt library both show you how to redact names and confidential details before pasting, and which data settings to check in your AI assistant."),
        ("Is any of this legal, tax or financial advice?", "No. Templates that touch contracts, fees or late payments are communication aids. Check local rules with a qualified professional."),
        ("I already bought one product. Can I upgrade?", "Yes. Reply to your receipt email and you'll get a code worth what you paid."),
        ("What if it isn't useful for me?", "Email within 14 days of purchase for a full refund. Just tell us briefly what didn't work."),
        ("How do updates work?", "Updates within version 1.x are free. The latest files are available from your purchase."),
    ]
    faq_html = "\n".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faqs)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Band of One Complete Bundle: playbook, client tracker and 100 AI prompts</title>
<meta name="description" content="A practical admin system for one-person service businesses: a 38-page playbook, a client and invoice workbook for Excel and Google Sheets, and 100 detailed AI prompts. $49.">
{canonical}
<meta property="og:type" content="product">
<meta property="og:title" content="The Band of One Complete Bundle">
<meta property="og:description" content="Playbook + Client Desk workbook + 100-prompt library: one admin system for a business of one.">
<meta property="og:image" content="assets/og-bundle.jpg">
{og_url}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{{font-family:Inter;src:url(assets/fonts/inter-400.woff2) format("woff2");font-weight:400;font-display:swap}}
@font-face{{font-family:Inter;src:url(assets/fonts/inter-600.woff2) format("woff2");font-weight:600;font-display:swap}}
@font-face{{font-family:Inter;src:url(assets/fonts/inter-700.woff2) format("woff2");font-weight:700;font-display:swap}}
@font-face{{font-family:Fraunces;src:url(assets/fonts/fraunces-600.woff2) format("woff2");font-weight:600;font-display:swap}}
@font-face{{font-family:Fraunces;src:url(assets/fonts/fraunces-700.woff2) format("woff2");font-weight:700;font-display:swap}}
@font-face{{font-family:Fraunces;src:url(assets/fonts/fraunces-400-italic.woff2) format("woff2");font-weight:400;font-style:italic;font-display:swap}}
:root{{--ink:{C['ink']};--paper:{C['paper']};--teal:{C['teal']};--deep:{C['deep_teal']};--mist:{C['mist']};--orange:{C['orange']};--rust:{C['rust']};--butter:{C['butter']};--stone:{C['stone']};--slate:{C['slate']};--radius:14px}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
img{{max-width:100%;height:auto;display:block}}
a{{color:var(--teal)}}
a:focus-visible,button:focus-visible,summary:focus-visible{{outline:3px solid var(--butter);outline-offset:3px;border-radius:6px}}
.skip{{position:absolute;left:-999px;top:8px;background:var(--ink);color:#fff;padding:8px 14px;border-radius:8px;z-index:10}}
.skip:focus{{left:12px}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 20px}}
h1,h2,h3{{font-family:Fraunces,Georgia,serif;line-height:1.12;letter-spacing:-.015em;margin:0 0 .5em}}
h1{{font-size:clamp(2.1rem,5vw,3.6rem);font-weight:700}}
h1 em,h2 em{{font-style:italic;font-weight:400;color:var(--butter)}}
h2{{font-size:clamp(1.7rem,3.4vw,2.5rem);font-weight:700}}
h3{{font-size:1.3rem;font-weight:600}}
.kicker{{font-weight:700;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--rust);margin:0 0 .6em}}
.dark .kicker{{color:var(--butter)}}
.btn{{display:inline-block;background:var(--rust);color:#fff;text-decoration:none;font-weight:700;padding:14px 24px;border-radius:999px;border:2px solid var(--rust)}}
.btn:hover{{background:#9C3B19;border-color:#9C3B19}}
.btn.ghost{{background:transparent;color:inherit;border-color:currentColor}}
.preview-banner{{background:var(--butter);color:var(--ink);text-align:center;font-size:.9rem;padding:8px 16px}}
header.site{{padding:18px 0}}
header.site .wrap{{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}}
header.site img{{height:34px;width:auto}}
header.site nav{{display:flex;gap:18px;flex-wrap:wrap;font-weight:600;font-size:.95rem}}
header.site nav a{{color:var(--ink);text-decoration:none}}
header.site nav a:hover{{text-decoration:underline}}
.dark{{background:var(--ink);color:var(--paper)}}
.dark a:not(.btn){{color:var(--butter)}}
.hero{{padding:56px 0 72px;overflow:hidden}}
.hero .grid{{display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center}}
.hero p.lead{{font-size:1.2rem;color:#EDE8DF;max-width:34em}}
.hero .ctas{{display:flex;gap:14px;flex-wrap:wrap;margin:26px 0 14px}}
.hero .small{{font-size:.92rem;color:#D9D2C5}}
.stack{{position:relative;height:430px}}
.stack img{{position:absolute;width:62%;border-radius:4px;box-shadow:0 18px 40px rgba(0,0,0,.45)}}
.stack img:nth-child(1){{left:0;top:0;transform:rotate(-4deg)}}
.stack img:nth-child(2){{left:19%;top:28px;transform:rotate(0)}}
.stack img:nth-child(3){{left:38%;top:56px;transform:rotate(4deg)}}
section{{padding:72px 0}}
.problem .cards,.products .cards,.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.card{{background:#fff;border:1px solid var(--stone);border-radius:var(--radius);padding:24px}}
.stat{{font-family:Fraunces,Georgia,serif;font-size:2.6rem;font-weight:700;color:var(--teal);line-height:1}}
.src{{font-size:.8rem;color:var(--slate)}}
.products .card img{{width:100%;max-width:220px;margin:0 auto 18px;box-shadow:0 10px 26px rgba(27,36,48,.25);border-radius:3px}}
.products .card ul{{padding-left:1.1em;margin:.6em 0}}
.price-tag{{font-weight:700;color:var(--slate)}}
.connect{{background:var(--mist)}}
.connect ul{{columns:2;column-gap:40px;padding-left:1.1em}}
.connect li{{break-inside:avoid;margin-bottom:.6em}}
.steps .card b{{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--teal);color:#fff;margin-bottom:10px}}
.gallery{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.gallery figure{{margin:0;background:#fff;border:1px solid var(--stone);border-radius:var(--radius);overflow:hidden}}
.gallery figcaption{{padding:12px 16px;font-size:.92rem;color:var(--slate)}}
.fit{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.fit ul{{padding-left:1.1em}}
.pricing .table{{display:grid;grid-template-columns:1.2fr 1fr;gap:22px;align-items:stretch}}
.pricing .bundle{{background:var(--ink);color:var(--paper);border-radius:var(--radius);padding:32px}}
.pricing .bundle .kicker{{color:var(--butter)}}
.pricing .bundle .amount{{font-family:Fraunces,Georgia,serif;font-size:3.4rem;font-weight:700;line-height:1}}
.pricing .bundle .was{{color:#D9D2C5}}
.pricing .single{{list-style:none;padding:0;margin:0}}
.pricing .single li{{display:flex;justify-content:space-between;gap:12px;align-items:center;background:#fff;border:1px solid var(--stone);border-radius:12px;padding:16px 18px;margin-bottom:12px}}
.pricing .single a{{font-weight:700}}
.guarantee{{margin-top:18px;font-size:.95rem;color:var(--slate)}}
details{{background:#fff;border:1px solid var(--stone);border-radius:12px;padding:14px 18px;margin-bottom:10px}}
summary{{cursor:pointer;font-weight:700}}
details p{{margin:.6em 0 0}}
.starter{{background:var(--mist)}}
.starter .wrap{{display:flex;gap:28px;align-items:center;justify-content:space-between;flex-wrap:wrap}}
footer{{padding:40px 0;font-size:.9rem}}
.pt0{{padding-top:0}}
.mt{{margin-top:20px}}
footer .wrap{{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}
footer p{{margin:.3em 0}}
@media (max-width:900px){{
 .hero .grid,.pricing .table,.fit{{grid-template-columns:1fr}}
 .problem .cards,.products .cards,.steps,.gallery{{grid-template-columns:1fr}}
 .stack{{height:auto;min-height:300px;max-width:420px}}
 .connect ul{{columns:1}}
 section{{padding:52px 0}}
}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{preview_banner}
<header class="site dark"><div class="wrap">
  <a href="{SITE_URL or '#'}" aria-label="Band of One home"><img src="assets/logo-on-dark.svg" alt="Band of One" width="170" height="34"></a>
  <nav aria-label="Page sections"><a href="#inside">What's inside</a><a href="#how">How it works</a><a href="#pricing">Pricing</a><a href="#faq">FAQ</a></nav>
</div></header>
<main id="main">
<section class="hero dark" aria-labelledby="hero-title"><div class="wrap grid">
  <div>
    <p class="kicker">The Complete Bundle</p>
    <h1 id="hero-title">The admin system for a <em>business of one</em></h1>
    <p class="lead">A practical playbook, a client-and-invoice workbook and 100 detailed AI prompts, designed to work together so client admin stops eating your week.</p>
    <div class="ctas"><a class="btn" href="{buy('bundle')}">Get the bundle for ${PRICES['bundle']}</a><a class="btn ghost" href="#inside">See what's inside</a></div>
    <p class="small">Instant download · Excel, Google Sheets &amp; PDF · 14-day refund policy</p>
  </div>
  <div class="stack" aria-hidden="true">
    <img src="assets/cover-playbook.webp" alt="" width="560" height="725" loading="eager">
    <img src="assets/cover-desk.webp" alt="" width="560" height="725" loading="eager">
    <img src="assets/cover-prompts.webp" alt="" width="560" height="725" loading="eager">
  </div>
</div></section>

<section class="problem" aria-labelledby="problem-title"><div class="wrap">
  <p class="kicker">Why this exists</p>
  <h2 id="problem-title">When you're the whole business, you're also the whole back office</h2>
  <p>Inquiries, proposals, onboarding, updates, invoices, reminders, testimonials. None of it is the work you're paid for, and all of it has to be done.</p>
  <div class="cards">
    <div class="card"><div class="stat">36%</div><p>of the work week went on admin tasks, on average, in a 2023 survey of 251 US entrepreneurs.</p><p class="src">Source: <a href="https://www.timeetc.com/resources/how-to-achieve-more/the-big-price-of-small-tasks-how-entrepreneurs-may-be-unwittingly-keeping-their-businesses-small/">Time etc, "The Big Price of Small Tasks"</a> (survey 22–28 Sept 2023)</p></div>
    <div class="card"><div class="stat">29%</div><p>of freelancer invoices were paid at least one day late, in data from over 100,000 freelancers.</p><p class="src">Source: <a href="https://www.hellobonsai.com/blog/late-freelance-payment">Bonsai, "How often do freelancers get paid late?"</a> (updated Jan 2026)</p></div>
    <div class="card"><div class="stat">&lt;20%</div><p>of US firms with four or fewer employees reported using AI, far behind larger firms.</p><p class="src">Source: <a href="https://www.census.gov/library/stories/2026/05/ai-use-businesses.html">U.S. Census Bureau, Business Trends and Outlook Survey</a> (May 2026)</p></div>
  </div>
</div></section>

<section class="products" id="inside" aria-labelledby="inside-title"><div class="wrap">
  <p class="kicker">What's inside</p>
  <h2 id="inside-title">Three products. One system.</h2>
  <div class="cards">
    <article class="card">
      <img src="assets/cover-playbook.webp" alt="Cover of The Solo Admin Playbook" width="560" height="725" loading="lazy">
      <h3>The Solo Admin Playbook</h3>
      <p><strong>How</strong> to set it up. 38-page PDF + editable DOCX.</p>
      <ul><li>Admin audit that ranks what to fix first</li><li>Safe AI setup: what to paste, what to redact</li><li>Six client workflows, from inquiry to referral</li><li>SOP library and a weekly admin review</li></ul>
      <p class="price-tag">${PRICES['playbook']} on its own</p>
    </article>
    <article class="card">
      <img src="assets/cover-desk.webp" alt="Cover of The Client Desk user guide" width="560" height="725" loading="lazy">
      <h3>The Client Desk</h3>
      <p><strong>Where</strong> it lives. Excel &amp; Google Sheets workbook + 13-page guide.</p>
      <ul><li>Clients, projects and invoices in one file</li><li>Dashboard of what needs attention this week</li><li>Days overdue and the next reminder stage (A–E)</li><li>No macros; tested formulas; sample data</li></ul>
      <p class="price-tag">${PRICES['desk']} on its own</p>
    </article>
    <article class="card">
      <img src="assets/cover-prompts.webp" alt="Cover of The Band of One Prompt Library" width="560" height="725" loading="lazy">
      <h3>The Prompt Library</h3>
      <p><strong>What</strong> to say. 100 prompts; PDF, spreadsheet, CSV, DOCX.</p>
      <ul><li>11 categories across the client lifecycle</li><li>Objective, inputs, output format and tip for each</li><li>Guardrails against invented prices and promises</li><li>Search tab and Notion-ready CSV</li></ul>
      <p class="price-tag">${PRICES['prompts']} on its own</p>
    </article>
  </div>
</div></section>

<section class="connect" aria-labelledby="connect-title"><div class="wrap">
  <h2 id="connect-title">Built to work together</h2>
  <ul>
    <li><strong>Same IDs everywhere.</strong> The playbook's workflows point to prompts like PROP-01 and PAY-02, and The Client Desk's Prompt Log uses the same IDs.</li>
    <li><strong>One reminder schedule.</strong> The playbook's five-stage payment reminders are the stages The Client Desk calculates for each invoice.</li>
    <li><strong>One weekly review.</strong> The agenda is in the playbook, the live numbers are in The Client Desk, and the review-assistant prompt (OPS-05) is in the library.</li>
    <li><strong>Tool-agnostic.</strong> Works with the AI assistant and spreadsheet app you already use. No new subscriptions.</li>
  </ul>
</div></section>

<section id="how" aria-labelledby="how-title"><div class="wrap">
  <p class="kicker">Your first week</p>
  <h2 id="how-title">How it works</h2>
  <div class="steps">
    <div class="card"><b>1</b><h3>Give your AI context</h3><p>Run two prompts to create your business brief and voice profile. Every other prompt uses them.</p></div>
    <div class="card"><b>2</b><h3>Audit your admin</h3><p>Score your recurring tasks in the playbook's audit and pick the one or two workflows to fix first.</p></div>
    <div class="card"><b>3</b><h3>Set up The Client Desk</h3><p>Fill in Settings, clear the sample data and add your clients and open invoices. About ten minutes.</p></div>
  </div>
  <p class="mt">Then book a weekly 45-minute admin review. The playbook gives you the agenda, and The Client Desk shows you what's due.</p>
</div></section>

<section aria-labelledby="look-title" class="pt0"><div class="wrap">
  <h2 id="look-title">A look inside</h2>
  <div class="gallery">
    <figure><img src="assets/shot-dashboard.webp" alt="The Client Desk dashboard showing follow-ups due, invoices needing a reminder and pipeline by stage, with fictional sample data" loading="lazy" width="1400" height="820"><figcaption>The Client Desk dashboard (sample data)</figcaption></figure>
    <figure><img src="assets/shot-prompts.webp" alt="Two pages of the Prompt Library showing fully specified prompt cards for invoicing and payment" loading="lazy" width="1400" height="788"><figcaption>Prompt cards: objective, inputs, prompt, output</figcaption></figure>
    <figure><img src="assets/shot-worksheets.webp" alt="Playbook worksheet pages for the admin audit and weekly review" loading="lazy" width="1400" height="788"><figcaption>Playbook worksheets</figcaption></figure>
  </div>
</div></section>

<section aria-labelledby="fit-title" class="pt0"><div class="wrap">
  <h2 id="fit-title">Is it for you?</h2>
  <div class="fit">
    <div class="card"><h3>A good fit if you…</h3><ul><li>run a one-person service business (freelance, consulting, coaching, VA, design, development, writing)</li><li>handle your own inquiries, proposals and invoices</li><li>want a simple system rather than another app</li><li>are curious about AI but want to stay in control of what goes to clients</li></ul></div>
    <div class="card"><h3>Probably not for you if you…</h3><ul><li>need a multi-user CRM, automatic invoicing or bank feeds</li><li>want legal, tax or accounting advice</li><li>are looking for AI prompts for images, code or social media growth</li></ul></div>
  </div>
</div></section>

<section class="pricing pt0" id="pricing" aria-labelledby="pricing-title"><div class="wrap">
  <p class="kicker">Pricing</p>
  <h2 id="pricing-title">One price for the whole system</h2>
  <div class="table">
    <div class="bundle">
      <p class="kicker">Complete Bundle</p>
      <p><span class="amount">${PRICES['bundle']}</span> <span class="was">vs. ${PRICES['playbook'] + PRICES['desk'] + PRICES['prompts']} separately</span></p>
      <p>The Solo Admin Playbook, The Client Desk and The Prompt Library. One download, free 1.x updates.</p>
      <p><a class="btn" href="{buy('bundle')}">Get the bundle</a></p>
    </div>
    <div>
      <h3>Or buy them separately</h3>
      <ul class="single">
        <li><span>The Solo Admin Playbook</span><span>${PRICES['playbook']} · <a href="{buy('playbook')}">Buy</a></span></li>
        <li><span>The Client Desk</span><span>${PRICES['desk']} · <a href="{buy('desk')}">Buy</a></span></li>
        <li><span>The Prompt Library</span><span>${PRICES['prompts']} · <a href="{buy('prompts')}">Buy</a></span></li>
      </ul>
      <p class="guarantee"><strong>14-day refund policy.</strong> If it isn't useful for your business, email within 14 days for a full refund.</p>
    </div>
  </div>
  <p class="src mt">Prices in USD. Sales tax or VAT may be added at checkout depending on your location. Checkout is handled by Gumroad.</p>
</div></section>

<section id="faq" class="pt0" aria-labelledby="faq-title"><div class="wrap">
  <h2 id="faq-title">Questions</h2>
  {faq_html}
</div></section>

<section class="starter" id="starter" aria-labelledby="starter-title"><div class="wrap">
  <div><h2 id="starter-title">Not ready yet? Start free.</h2><p>Get the Client Admin Starter Kit (10 prompts and a 30-minute weekly review checklist) plus one practical admin idea a week by email. Unsubscribe any time.</p></div>
  <a class="btn" href="{starter}">Get the free starter kit</a>
</div></section>
</main>

<footer class="dark"><div class="wrap">
  <div><img src="assets/logo-on-dark.svg" alt="Band of One" width="150" height="30"><p>Practical AI systems for businesses of one.</p></div>
  <div><p>Educational products and templates. Results depend on how you use them; no specific time savings or income are promised. Nothing here is legal, tax or financial advice.</p>
  <p>© 2026 Band of One{' · <a href="' + SITE_URL.rstrip('/') + '/privacy/">Privacy</a> · <a href="' + SITE_URL.rstrip('/') + '/terms/">Terms</a>' if SITE_URL else ''}</p></div>
</div></footer>
</body>
</html>
"""


def main():
    prepare_assets()
    (OUT / "index.html").write_text(page(), encoding="utf-8")
    print(OUT / "index.html")


if __name__ == "__main__":
    main()

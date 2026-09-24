"""Build the free lead magnet: The Client Admin Starter Kit (10 prompts + weekly review checklist).

Used by both businesses: the product funnel (Gumroad $0 / newsletter signup) and the content site's newsletter.
Run: python3 Build_Tools/build_lead_magnet.py
"""
import shutil

from brand import COLORS as C, ROOT
from build_prompt_library import EXTRA_CSS, load, prompt_card_html
from covers import product_cover
from docbuilder import build_pdf
from launch_config import STORE_URL, link

PICKS = ["SET-01", "LEAD-01", "DISC-05", "PROP-01", "ONB-01", "DEL-01", "DEL-07", "PAY-02", "RET-02", "OPS-05"]
OUT_DIR = ROOT / "Digital_Products_Business" / "08_Marketing_Campaign" / "Lead_Magnet"
MIRROR = ROOT / "Content_Automation_Business" / "07_Email_Newsletter" / "Lead_Magnet"
STEM = "BandOfOne_Client-Admin-Starter-Kit_FREE"

CSS = EXTRA_CSS + f"""
.check{{list-style:none;padding:0;margin:4pt 0 10pt}}
.check li{{position:relative;padding:3.6pt 0 3.6pt 22pt;border-bottom:1px solid {C['stone']};font-size:10pt}}
.check li::before{{content:'';position:absolute;left:0;top:5pt;width:10pt;height:10pt;border:1.4px solid {C['teal']};border-radius:2.5px}}
.cta{{border:1px solid {C['stone']};border-left:5px solid {C['teal']};border-radius:8px;padding:10pt 14pt;margin:10pt 0;background:#fff}}
"""


def md(items):
    by = {i["id"]: i for i in items}
    parts = ["""# Start here

This free kit gives you **10 prompts** for the admin moments that come up every week in a service business, plus a **30-minute weekly review checklist** to keep it all running.

They're taken, unchanged, from *The Band of One Prompt Library* (100 prompts). They work with ChatGPT, Claude, Gemini, Copilot and similar assistants, including free tiers.

## Three rules before you start

1. **Run SET-01 first.** It creates a one-page business brief. Paste it wherever a prompt says `[BUSINESS BRIEF]`.
2. **Redact before you paste.** Replace client names, emails, amounts tied to named clients and anything confidential with placeholders like `[CLIENT NAME]`. Check your assistant's data settings too.
3. **You decide what gets sent.** Read every draft for facts, prices, dates and promises before it goes to a client. The prompts ask the AI not to invent them. Check that it didn't.

| # | Prompt | Use it when |
|---|---|---|
""" + "\n".join(f"| {n} | **{p}** {by[p]['title']} | {by[p]['use_case']} |" for n, p in enumerate(PICKS, 1)) + "\n"]
    parts.append("# The 10 prompts\n\n" + "\n".join(prompt_card_html(by[p]) for p in PICKS) + "\n")
    parts.append("""# Your 30-minute weekly review

Block the same half hour every week. Work down the list and tick each item.

**1. Clear the decks (5 min)**
<ul class="check"><li>Inbox and messages processed; tasks captured in one list or tracker</li><li>Anything waiting on a client noted with a follow-up date</li></ul>

**2. Pipeline (5 min)**
<ul class="check"><li>Every new inquiry has had a reply (LEAD-01)</li><li>Follow-ups due this week sent or scheduled</li><li>Proposals out: next-action date set for each</li></ul>

**3. Money (10 min)**
<ul class="check"><li>Invoices for finished work sent</li><li>Overdue invoices checked; the right reminder sent (PAY-02)</li><li>Payments received recorded</li></ul>

**4. Next week (5 min)**
<ul class="check"><li>Client work and deadlines blocked in the calendar</li><li>Weekly client updates drafted (DEL-01)</li></ul>

**5. Improve one thing (5 min)**
<ul class="check"><li>One repeated task turned into a template, checklist or saved prompt</li></ul>

!!! tip "Shortcut"
    Paste your (redacted) task list, open invoices and next week's calendar into **OPS-05** and ask for the review. It sorts follow-ups, reminders and risks for you to check.

# Want the full system?

<div class="cta" markdown="1">

**The Band of One Prompt Library** has all 100 prompts across 11 categories, from discovery calls to tough conversations, with a searchable spreadsheet version.

**The Solo Admin Playbook** is a 38-page guide to building the whole admin system, with worksheets.

**The Client Desk** is a spreadsheet for your pipeline, projects, invoices and reminder stages, with a dashboard.

Details and prices: """ + link(STORE_URL, "STORE LINK") + """

</div>

You don't need any of them to use this kit. The 10 prompts and the checklist work on their own.

---

**License:** Free for personal business use. Please share the sign-up link rather than the file. Band of One · """ + "Version 1.0 · September 2026" + """

**Not professional advice:** the prompts are communication aids, not legal, tax or financial advice.
""")
    return "\n".join(parts)


def main():
    items = load()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cover = product_cover("Free starter kit · Band of One", "The Client Admin<br><em>Starter Kit</em>",
                          "10 AI prompts for the admin you do every week, plus a 30-minute weekly review checklist.",
                          ["Reply to inquiries, summarize calls, draft proposals", "Onboarding, updates, scope changes, reminders",
                           "Testimonials and a weekly admin review", "Works with free AI assistants", "Privacy and review rules included"],
                          ring=C["teal"], disc=C["rust"], big="10", big_size="170pt", big_top="7.0in", big_right="0.55in")
    out = OUT_DIR / f"{STEM}.pdf"
    build_pdf(md(items), out, {"title": "The Client Admin Starter Kit", "subtitle": "10 AI prompts + weekly review checklist",
                               "footer_left": "The Client Admin Starter Kit · Free · Band of One"},
              cover_html=cover, extra_css=CSS, number_chapters=False, include_h2=False)
    MIRROR.mkdir(parents=True, exist_ok=True)
    shutil.copy(out, MIRROR / out.name)
    print(out)


if __name__ == "__main__":
    main()

"""Build Product C: The Band of One Prompt Library (PDF, XLSX with search, CSV, Markdown, DOCX).

Run: python3 Build_Tools/build_prompt_library.py
"""
import csv
import glob
import html
import re
from pathlib import Path

import yaml
from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

from brand import COLORS as C, ROOT
from covers import product_cover
from docbuilder import build_docx, build_pdf

LIB = ROOT / "Digital_Products_Business" / "05_AI_Prompt_Library"
SRC = LIB / "source"
STEM = "BandOfOne_Prompt-Library_v1.0"
CATEGORY_ORDER = [
    ("SET", "Setup & Foundations", "Give your AI assistant the context it needs, once: your business brief, your voice, and your privacy habits."),
    ("LEAD", "Leads & Inquiries", "Reply fast, qualify well, and follow up without sounding pushy."),
    ("DISC", "Discovery & Sales Calls", "Prepare, run and follow up on discovery calls that lead to good-fit projects."),
    ("PROP", "Proposals & Pricing", "Draft specific proposals, structure options and protect your scope. You set the prices; AI never does."),
    ("ONB", "Onboarding", "Turn a 'yes' into a smooth, professional start."),
    ("DEL", "Delivery & Client Communication", "Updates, feedback, delays, scope changes and meeting notes: the everyday communication of client work."),
    ("PAY", "Invoicing & Getting Paid", "Invoice clearly and follow up on a predictable, respectful schedule."),
    ("RET", "Offboarding, Testimonials & Referrals", "Finish well, earn honest testimonials and keep relationships warm."),
    ("MKT", "Content & Marketing", "Turn your expertise into useful content without inventing results or hype."),
    ("OPS", "Systems, SOPs & Planning", "Document processes, decide what to automate and plan your weeks and quarters."),
    ("HARD", "Tough Conversations", "Calm, honest language for the conversations nobody enjoys."),
]


def load():
    items = []
    for f in sorted(glob.glob(str(SRC / "*.yaml"))):
        items += yaml.safe_load(open(f))
    order = {p: i for i, (p, _, _) in enumerate(CATEGORY_ORDER)}
    items.sort(key=lambda x: (order[x["id"].split("-")[0]], int(x["id"].split("-")[1])))
    assert len(items) == 100, len(items)
    return items


def esc(s):
    return html.escape(str(s), quote=False)


def md_intro():
    return """# How to use this library

These 100 prompts cover the admin of a service business from first inquiry to final invoice. Each one is built to produce a **specific, reusable output**, not a generic answer.

## Every prompt has the same parts

| Part | What it tells you |
|---|---|
| **Objective** | The job the prompt does |
| **When to use** | The moment in your week or client lifecycle it's for |
| **Inputs** | What you paste or fill in. `[PLACEHOLDERS]` are in square brackets and capitals |
| **Prompt** | The text to copy into your AI assistant |
| **Output** | What you should get back |
| **Tip** and **Pairs with** | How to get more from it, and related prompts |

## Five rules for great results

1. **Start with context.** Create your business brief (SET-01) and voice profile (SET-02) first. Paste them where a prompt says `[BUSINESS BRIEF]` or `[VOICE PROFILE]`, or save them as custom instructions (SET-04).
2. **Replace every placeholder.** If you don't have the information, delete that part of the prompt rather than leaving a placeholder for the AI to guess.
3. **Redact client details.** Replace names, emails, account numbers and anything confidential with placeholders before pasting. See SET-03 and check your assistant's data settings.
4. **You set prices, dates and promises.** The prompts tell the AI not to invent them. Check that it didn't.
5. **Edit before you send.** Read every draft for facts, promises, tone and one client-specific detail. AI drafts; you decide.

!!! tip "Works with any assistant"
    These prompts are written in plain language and work with ChatGPT, Claude, Gemini, Microsoft Copilot and similar assistants, including free tiers. Output quality varies by model and by how much context you provide.

Your download also includes a spreadsheet version with a **Search** tab, and a CSV you can import into Notion, Airtable or Google Sheets.

"""


def md_category_index(items):
    rows = ["| Category | IDs | Prompts |", "|---|---|---|"]
    for p, name, _ in CATEGORY_ORDER:
        its = [i for i in items if i["id"].startswith(p + "-")]
        rows.append(f"| {name} | {its[0]['id']} – {its[-1]['id']} | {len(its)} |")
    return ("# The 100 prompts at a glance\n\n" + "\n".join(rows) + "\n\n<div class=\"idx\" markdown=\"1\">\n\n"
            + "\n".join(f"- **{i['id']}**: {i['title']}" for i in items) + "\n\n</div>\n\n")


def prompt_card_html(i):
    inputs = "".join(f"<li>{esc(x)}</li>" for x in i["inputs"])
    pairs = ", ".join(i.get("pairs_with") or []) or "—"
    tip = f'<div class="pc-row"><span class="pc-l">Tip</span><span>{esc(i["tips"])}</span></div>' if i.get("tips") else ""
    return f"""<div class="pc" id="{i['id']}">
<div class="pc-head"><span class="pc-id">{i['id']}</span><span class="pc-title">{esc(i['title'])}</span></div>
<div class="pc-row"><span class="pc-l">Objective</span><span>{esc(i['objective'])}</span></div>
<div class="pc-row"><span class="pc-l">When to use</span><span>{esc(i['use_case'])}</span></div>
<div class="pc-row"><span class="pc-l">Inputs</span><ul>{inputs}</ul></div>
<div class="pc-prompt">{esc(i['prompt'].strip())}</div>
<div class="pc-row"><span class="pc-l">Output</span><span>{esc(i['output_format'])}</span></div>
{tip}<div class="pc-row"><span class="pc-l">Pairs with</span><span>{pairs}</span></div>
</div>"""


def md_body_for_pdf(items):
    out = []
    for p, name, blurb in CATEGORY_ORDER:
        its = [i for i in items if i["id"].startswith(p + "-")]
        out.append(f"# {name}\n\n<p class=\"lede\">{blurb}</p>\n")
        for i in its:
            out.append(prompt_card_html(i) + "\n")
    return "\n".join(out)


def md_plain(items, escape_brackets=False):
    """Portable Markdown (for the .md and .docx versions). Pandoc reads '[X]: text' as a link
    definition, so the DOCX build escapes brackets outside code blocks."""
    e = (lambda t: str(t).replace("[", "\\[").replace("]", "\\]")) if escape_brackets else str
    out = [md_intro()]
    for p, name, blurb in CATEGORY_ORDER:
        out.append(f"# {name}\n\n{blurb}\n")
        for i in [x for x in items if x["id"].startswith(p + "-")]:
            out.append(f"## {i['id']} · {i['title']}\n")
            out.append(f"**Objective:** {e(i['objective'])}\n\n**When to use:** {e(i['use_case'])}\n\n**Inputs:**\n")
            out.extend(f"- {e(x)}" for x in i["inputs"])
            out.append("\n**Prompt:**\n\n```text\n" + i["prompt"].strip() + "\n```\n")
            out.append(f"**Output:** {e(i['output_format'])}\n")
            if i.get("tips"):
                out.append(f"**Tip:** {e(i['tips'])}\n")
            if i.get("pairs_with"):
                out.append(f"**Pairs with:** {', '.join(i['pairs_with'])}\n")
    out.append(LICENSE_MD)
    return "\n".join(out)


LICENSE_MD = """# About and license

**The Band of One Prompt Library**, version 1.0 (September 2026), by Band of One.

**License (summary):** You may use these prompts in your own business, adapt them freely, and use their outputs (emails, documents, posts) however you like. You may not resell, share or redistribute the library, or publish substantial parts of it (for example, in your own prompt pack or course). Full terms are in `LICENSE.txt`.

**How it was made:** The prompts were drafted with AI assistance and reviewed against a written checklist: specific objective, clear inputs, a defined output format, and guardrails against invented facts, prices or promises.

**Not professional advice:** Prompts touching on contracts, fees or late payment are communication aids, not legal or financial advice.

**Support & updates:** Use the contact details on your purchase receipt or the product page. Version 1.x updates are free.
"""

EXTRA_CSS = f"""
body{{font-size:10pt;line-height:1.5}}
.idx ul{{columns:2;column-gap:22pt;font-size:8.8pt;line-height:1.35;padding-left:0;list-style:none}}
.idx li{{break-inside:avoid;margin:0 0 2.5pt}}
.lede{{font-size:11pt;color:{C['slate']};margin:-4pt 0 14pt}}
.pc{{border:1px solid {C['stone']};border-radius:9px;padding:10pt 12pt 8pt;margin:0 0 12pt;break-inside:avoid;background:#fff}}
.pc-head{{display:flex;align-items:baseline;gap:9pt;margin-bottom:6pt;border-bottom:1px solid {C['stone']};padding-bottom:5pt}}
.pc-id{{font-family:'JetBrains Mono';font-weight:600;font-size:9pt;color:#fff;background:{C['teal']};border-radius:4px;padding:1.5pt 6pt}}
.pc-title{{font-family:Fraunces;font-weight:600;font-size:13pt;color:{C['ink']}}}
.pc-row{{display:flex;gap:8pt;font-size:9pt;line-height:1.45;margin:2.5pt 0}}
.pc-row>span:last-child,.pc-row ul{{flex:1}}
.pc-l{{flex:0 0 72pt;font-weight:700;font-size:7.6pt;letter-spacing:.08em;text-transform:uppercase;color:{C['rust']};padding-top:1.5pt}}
.pc-row ul{{margin:0;padding-left:12pt}}
.pc-row li{{margin:0 0 1pt}}
.pc-prompt{{font-family:'JetBrains Mono',monospace;font-size:8.3pt;line-height:1.5;white-space:pre-wrap;background:#F4F7F6;border:1px solid #D5E6E2;border-left:4px solid {C['teal']};border-radius:6px;padding:7pt 9pt;margin:6pt 0}}
"""


def build_pdf_version(items):
    md = md_intro() + md_category_index(items) + md_body_for_pdf(items) + "\n[[pagebreak]]\n\n" + LICENSE_MD
    cover = product_cover("The Prompt Library · Band of One", "The Band of One<br><em>Prompt Library</em>",
                          "100 detailed AI prompts for client work and admin in a business of one: from first inquiry to final invoice.",
                          ["11 categories across the client lifecycle", "Objective, inputs, output format &amp; use case for each",
                           "Guardrails against invented facts &amp; prices", "Works with ChatGPT, Claude, Gemini &amp; Copilot",
                           "Searchable spreadsheet + CSV included"],
                          ring=C["rust"], disc=C["teal"], big="100", big_size="118pt", big_top="7.35in", big_right="0.5in")
    return build_pdf(md, LIB / f"{STEM}.pdf",
                     {"title": "The Band of One Prompt Library", "subtitle": "100 AI prompts for client work and admin",
                      "footer_left": "The Band of One Prompt Library · v1.0"},
                     cover_html=cover, extra_css=EXTRA_CSS, number_chapters=False, include_h2=False)


# ------------------------------------------------------------------ spreadsheet

def build_xlsx(items):
    F = "Arial"
    thin = Side(style="thin", color="D9D4CA")
    B = Border(left=thin, right=thin, top=thin, bottom=thin)
    HF = PatternFill("solid", fgColor=C["deep_teal"][1:])
    HFONT = Font(name=F, bold=True, color="FFFFFF")
    wb = Workbook()
    # Search sheet
    s = wb.active
    s.title = "Search"
    s.sheet_view.showGridLines = False
    s["B1"] = "The Band of One Prompt Library: Search"
    s["B1"].font = Font(name=F, bold=True, size=18, color=C["deep_teal"][1:])
    s["B2"] = "Type a keyword (e.g., invoice, proposal, scope, testimonial) in the yellow box. Matching prompts appear below. Full text is on the Prompts tab."
    s["B2"].font = Font(name=F, italic=True, size=10, color=C["slate"][1:])
    s["B4"] = "Keyword:"
    s["B4"].font = Font(name=F, bold=True, size=12)
    s["C4"] = "invoice"
    s["C4"].fill = PatternFill("solid", fgColor="FFF8E1")
    s["C4"].font = Font(name=F, size=12, bold=True)
    s["C4"].border = B
    s["E4"] = "Category filter:"
    s["E4"].font = Font(name=F, bold=True, size=12)
    s["F4"] = "All"
    s["F4"].fill = PatternFill("solid", fgColor="FFF8E1")
    s["F4"].font = Font(name=F, size=12, bold=True)
    s["F4"].border = B
    dv = DataValidation(type="list", formula1="=Categories!$A$3:$A$14", allow_blank=False)
    s.add_data_validation(dv)
    dv.add("F4")
    s["B5"] = '=COUNT(Prompts!$N$3:$N$102)&" matching prompt(s)"'
    s["B5"].font = Font(name=F, size=10, color=C["rust"][1:], bold=True)
    heads = ["#", "ID", "Title", "Category", "Objective"]
    widths = [5, 10, 40, 30, 70]
    for j, (h, w) in enumerate(zip(heads, widths)):
        c = s.cell(row=7, column=1 + j, value=h)
        c.font, c.fill, c.border = HFONT, HF, B
        s.column_dimensions[chr(65 + j)].width = w
    for k in range(1, 101):
        r = 7 + k
        s[f"A{r}"] = f'=IF({k}>COUNT(Prompts!$N$3:$N$102),"",{k})'
        m = f"MATCH({k},Prompts!$N$3:$N$102,0)"
        s[f"B{r}"] = f'=IFERROR(INDEX(Prompts!$A$3:$A$102,{m}),"")'
        s[f"C{r}"] = f'=IFERROR(INDEX(Prompts!$C$3:$C$102,{m}),"")'
        s[f"D{r}"] = f'=IFERROR(INDEX(Prompts!$B$3:$B$102,{m}),"")'
        s[f"E{r}"] = f'=IFERROR(INDEX(Prompts!$D$3:$D$102,{m}),"")'
        for col in "ABCDE":
            s[f"{col}{r}"].font = Font(name=F, size=10)
            s[f"{col}{r}"].alignment = Alignment(vertical="top", wrap_text=col in "CE")
    s.freeze_panes = "A8"
    # Prompts sheet
    p = wb.create_sheet("Prompts")
    p["A1"] = "All 100 prompts. Use the filter arrows, or the Search tab. Columns L–M are for your own notes."
    p["A1"].font = Font(name=F, italic=True, color=C["slate"][1:])
    heads = ["ID", "Category", "Title", "Objective", "When to use", "Inputs", "Prompt", "Output format", "Tip", "Pairs with", "Favorite (Y)", "My notes", "Match", "Match rank"]
    widths = [10, 24, 34, 44, 40, 44, 90, 40, 40, 16, 10, 30, 8, 8]
    for j, (h, w) in enumerate(zip(heads, widths)):
        c = p.cell(row=2, column=1 + j, value=h)
        c.font, c.fill, c.border = HFONT, HF if j < 12 else PatternFill("solid", fgColor=C["slate"][1:]), B
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        p.column_dimensions[chr(65 + j)].width = w
    for k, i in enumerate(items):
        r = 3 + k
        vals = [i["id"], i["category"], i["title"], i["objective"], i["use_case"], "\n".join(i["inputs"]), i["prompt"].strip(),
                i["output_format"], i.get("tips") or "", ", ".join(i.get("pairs_with") or [])]
        for j, v in enumerate(vals):
            c = p.cell(row=r, column=1 + j, value=v)
            c.font = Font(name=F if j != 6 else "Consolas", size=9)
            c.alignment = Alignment(vertical="top", wrap_text=True)
            c.border = B
        for col in "KL":
            p[f"{col}{r}"].fill = PatternFill("solid", fgColor="FFF8E1")
            p[f"{col}{r}"].border = B
        # search match: keyword in id/category/title/objective/use/prompt and category filter
        p[f"M{r}"] = (f'=IF(AND(OR(Search!$F$4="All",Search!$F$4=B{r}),OR(Search!$C$4="",'
                      f'ISNUMBER(SEARCH(Search!$C$4,A{r}&" "&B{r}&" "&C{r}&" "&D{r}&" "&E{r}&" "&G{r})))),1,0)')
        p[f"N{r}"] = f'=IF(M{r}=1,COUNTIF($M$3:M{r},1),"")'
        for col in "MN":
            p[f"{col}{r}"].font = Font(name=F, size=9, color=C["slate"][1:])
        p.row_dimensions[r].height = 150
    p.freeze_panes = "D3"
    p.auto_filter.ref = "A2:L102"
    dvk = DataValidation(type="list", formula1='"Y"', allow_blank=True)
    p.add_data_validation(dvk)
    dvk.add("K3:K102")
    # Categories sheet
    cs = wb.create_sheet("Categories")
    cs["A1"] = "Categories"
    cs["A1"].font = Font(name=F, bold=True, size=14, color=C["deep_teal"][1:])
    for j, h in enumerate(["Category", "ID prefix", "Prompts", "Your favorites", "What it's for"]):
        c = cs.cell(row=2, column=1 + j, value=h)
        c.font, c.fill, c.border = HFONT, HF, B
    cs["A3"] = "All"
    cs["C3"] = "=COUNTA(Prompts!$A$3:$A$102)"
    cs["D3"] = '=COUNTIF(Prompts!$K$3:$K$102,"Y")'
    for k, (pre, name, blurb) in enumerate(CATEGORY_ORDER):
        r = 4 + k
        cs[f"A{r}"], cs[f"B{r}"], cs[f"E{r}"] = name, pre, blurb
        cs[f"C{r}"] = f'=COUNTIF(Prompts!$B$3:$B$102,A{r})'
        cs[f"D{r}"] = f'=COUNTIFS(Prompts!$B$3:$B$102,A{r},Prompts!$K$3:$K$102,"Y")'
    for row in cs["A3:E14"]:
        for c in row:
            c.font = Font(name=F, size=10)
            c.border = B
            c.alignment = Alignment(vertical="top", wrap_text=True)
    for col, w in zip("ABCDE", [36, 10, 10, 13, 80]):
        cs.column_dimensions[col].width = w
    # How to use
    h = wb.create_sheet("How to use", 0)
    h.sheet_view.showGridLines = False
    h.column_dimensions["A"].width = 3
    h.column_dimensions["B"].width = 110
    lines = [
        ("The Band of One Prompt Library: spreadsheet edition", Font(name=F, bold=True, size=16, color=C["deep_teal"][1:])),
        ("Works in Excel, Google Sheets (upload → Save as Google Sheets) and LibreOffice.", Font(name=F, italic=True, color=C["slate"][1:])),
        ("", None),
        ("1. Search tab: type a keyword in the yellow box; pick a category to narrow results.", Font(name=F, size=11)),
        ("2. Prompts tab: the full library. Copy the Prompt column into your AI assistant and replace every [PLACEHOLDER].", Font(name=F, size=11)),
        ("3. Mark favorites with Y and keep your own tweaks in 'My notes'. The Categories tab counts your favorites.", Font(name=F, size=11)),
        ("4. Start with SET-01 (business brief) and SET-02 (voice profile). Most prompts work better with them.", Font(name=F, size=11)),
        ("5. Redact client names and confidential details before pasting (SET-03), and check your assistant's data settings.", Font(name=F, size=11)),
        ("6. You set prices, dates and promises. Check every draft before sending it to a client.", Font(name=F, size=11)),
        ("", None),
        ("Tip: grey columns M–N on the Prompts tab power the Search tab. Leave them in place.", Font(name=F, size=10, color=C["slate"][1:])),
        ("License: personal business use by the purchaser. Don't resell or redistribute. See LICENSE.txt.", Font(name=F, size=10, color=C["slate"][1:])),
    ]
    for k, (t, f) in enumerate(lines, start=2):
        h[f"B{k}"] = t
        if f:
            h[f"B{k}"].font = f
    for ws in wb.worksheets:
        ws.sheet_properties.tabColor = C["teal"][1:]
    wb.active = 1
    out = LIB / f"{STEM}_Searchable.xlsx"
    wb.save(out)
    return out


def build_csv(items):
    out = LIB / f"{STEM}.csv"
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Category", "Title", "Objective", "When to use", "Inputs", "Prompt", "Output format", "Tip", "Pairs with"])
        for i in items:
            w.writerow([i["id"], i["category"], i["title"], i["objective"], i["use_case"], " | ".join(i["inputs"]),
                        i["prompt"].strip(), i["output_format"], i.get("tips") or "", ", ".join(i.get("pairs_with") or [])])
    return out


if __name__ == "__main__":
    items = load()
    plain = md_plain(items)
    (LIB / f"{STEM}.md").write_text("# The Band of One Prompt Library\n\n100 AI prompts for client work and admin in a business of one. "
                                    "Version 1.0 · September 2026.\n\n" + plain)
    print(build_csv(items))
    print(build_xlsx(items))
    build_docx(md_plain(items, escape_brackets=True), LIB / f"{STEM}_editable.docx",
               {"title": "The Band of One Prompt Library", "subtitle": "100 AI prompts for client work and admin · v1.0"})
    print(build_pdf_version(items))

"""Package the products into customer-ready ZIPs (each with START-HERE.pdf, LICENSE.txt, CHANGELOG.md).

Run after the product builders:  python3 Build_Tools/build_packages.py
Outputs: Digital_Products_Business/06_Customer_Ready_Products/*.zip + MANIFEST.md
"""
import hashlib
import shutil
import zipfile
from pathlib import Path

from brand import COLORS as C, ROOT
from docbuilder import build_pdf

DP = ROOT / "Digital_Products_Business"
OUT = DP / "06_Customer_Ready_Products"
STAGE = ROOT / "Build_Tools" / ".tmp" / "packages"
VERSION, DATE = "1.0", "2026-09-24"
SUPPORT = "Use the contact details on your purchase receipt or on the product page."

PRODUCTS = {
    "playbook": {
        "name": "The Solo Admin Playbook",
        "stem": "BandOfOne_Solo-Admin-Playbook_v1.0",
        "files": [
            (DP / "03_Digital_Guide/BandOfOne_Solo-Admin-Playbook_v1.0.pdf", "The 38-page playbook. Read on screen or print it."),
            (DP / "03_Digital_Guide/BandOfOne_Solo-Admin-Playbook_v1.0_editable.docx",
             "Editable version for Word, Google Docs or LibreOffice. Copy the templates and worksheets from here."),
        ],
        "steps": [
            "Read **How to use this playbook** (page 2). It takes five minutes.",
            "Do the **admin audit** in Chapter 2. It shows you which workflows to fix first.",
            "Set up your AI assistant safely with Chapter 3 before pasting any client information.",
            "Follow **Your next seven days** near the end: one small step per day.",
        ],
        "extra": "The playbook includes the 17 prompts it refers to. You don't need any other product to use it.",
    },
    "clientdesk": {
        "name": "The Client Desk",
        "stem": "BandOfOne_The-Client-Desk_v1.0",
        "files": [
            (DP / "04_Premium_Template/BandOfOne_The-Client-Desk_v1.0.xlsx",
             "The workbook: pipeline, projects, invoices and reminder stages, admin audit, prompt log, SOP library, weekly review and dashboard."),
            (DP / "04_Premium_Template/BandOfOne_The-Client-Desk_User-Guide_v1.0.pdf", "The 13-page user guide: setup, every tab explained, and troubleshooting."),
        ],
        "steps": [
            "**Open the workbook.** In Excel, double-click it. In Google Sheets, upload it to Drive, open it and choose **File → Save as Google Sheets**. LibreOffice Calc opens it directly.",
            "Fill in the **Settings** tab: business name, payment terms, currency label, review day and services.",
            "Look around the **sample business** (rows marked SAMPLE), then clear the yellow cells of those rows. Don't delete whole rows.",
            "Add your real clients and open invoices, then check the **Dashboard**.",
        ],
        "extra": "Yellow cells are for typing, grey cells are calculated. The user guide's Troubleshooting section covers most questions.",
    },
    "prompts": {
        "name": "The Band of One Prompt Library",
        "stem": "BandOfOne_Prompt-Library_v1.0",
        "files": [
            (DP / "05_AI_Prompt_Library/BandOfOne_Prompt-Library_v1.0.pdf", "All 100 prompts in 11 categories, with an index. Best for reading and browsing."),
            (DP / "05_AI_Prompt_Library/BandOfOne_Prompt-Library_v1.0_Searchable.xlsx",
             "Spreadsheet version with a Search tab (type a keyword), filters, favorites and a notes column."),
            (DP / "05_AI_Prompt_Library/BandOfOne_Prompt-Library_v1.0.csv", "Plain data to import: Notion (**Import → CSV**), Airtable (**Add or import → CSV file**) or Google Sheets."),
            (DP / "05_AI_Prompt_Library/BandOfOne_Prompt-Library_v1.0_editable.docx", "Editable document version for Word, Google Docs or LibreOffice."),
            (DP / "05_AI_Prompt_Library/BandOfOne_Prompt-Library_v1.0.md", "Markdown version for Notion, Obsidian or any notes app."),
        ],
        "steps": [
            "Run **SET-01** (business brief) and **SET-02** (voice profile) first. Most other prompts ask for them.",
            "Save the results as custom instructions in your assistant (**SET-04**) so you don't paste them every time.",
            "Open the spreadsheet's **Search** tab and type the task you're facing (for example: *invoice*, *scope*, *testimonial*).",
            "Replace every `[PLACEHOLDER]`, redact client details (**SET-03**), and read each draft before sending it.",
        ],
        "extra": "",
    },
}
BUNDLE = {"name": "The Band of One Complete Bundle", "stem": "BandOfOne_Complete-Bundle_v1.0"}


def license_text(product_name):
    return f"""BAND OF ONE CUSTOMER LICENSE
Product: {product_name} (version {VERSION})
Licensor: Band of One, the seller named on your purchase receipt

This is a plain-language license. By downloading or using the files you agree to it.

1. WHO MAY USE IT
   The person or single business that bought it. "Your business" includes you and
   the employees or contractors working on your business.

2. WHAT YOU MAY DO
   - Use, edit and adapt the files for your own business.
   - Use anything you create with them (emails, proposals, documents, posts,
     spreadsheets filled with your data) with your own clients, without credit.
   - Print copies and keep backups for your own use.

3. WHAT YOU MAY NOT DO
   - Resell, sublicense, share, give away or lend the files, in original or edited
     form, or upload them anywhere others can download them.
   - Include substantial parts of them in a product, template, prompt pack, course
     or membership that you sell or give away.
   - Use them in a dataset for training or fine-tuning an AI model that others can use.
   - Claim that you wrote the original product.
   For a team or multi-business license, contact the seller.

4. NO PROFESSIONAL ADVICE
   The products are general education and templates. They are not legal, tax,
   accounting or financial advice. Check contract wording, payment terms and tax
   questions with a qualified professional where you work.

5. NO WARRANTY; LIMITATION OF LIABILITY
   The files are provided "as is". Results depend on how you use them, and no
   specific outcome (time saved, income, payment speed) is promised. To the extent
   the law allows, the seller's total liability is limited to the price you paid.

6. REFUNDS AND UPDATES
   Refunds follow the policy shown on the product page when you bought it.
   Updates within version 1.x are free for existing customers.

7. ENDING THE LICENSE
   The license ends if you break these terms. You must then delete your copies.

Questions: {SUPPORT}
"""


def changelog(product_name, files):
    listing = "\n".join(f"  - `{Path(f).name}`" for f in files)
    return f"""# Changelog: {product_name}

## {VERSION} ({DATE})

- First release.
- Included files:
{listing}
  - `START-HERE.pdf`, `LICENSE.txt`, `CHANGELOG.md`
"""


START_CSS = f"""
body{{font-size:9.3pt;line-height:1.42}}
h1{{font-size:19pt;margin-bottom:6pt}}
h2{{font-size:13pt;margin:11pt 0 4pt}}
td,th{{padding:3.5pt 7pt !important}}
li{{margin-bottom:1.5pt}}
.hero{{display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid {C['teal']};padding-bottom:10pt;margin-bottom:14pt}}
.hero img{{height:30pt}}
.hero .v{{font-size:8.5pt;color:{C['slate']}}}
h1{{margin-top:0}}
table td:first-child{{white-space:nowrap;font-family:'JetBrains Mono',monospace;font-size:8.3pt}}
"""


def start_here(key, spec, out_pdf, bundle_parts=None):
    logo = (ROOT / "Digital_Products_Business/02_Branding/logo/band-of-one-horizontal.svg").as_uri()
    hero = f'<div class="hero"><img src="{logo}" alt="Band of One"><div class="v">Version {VERSION} · {DATE}</div></div>'
    if bundle_parts:
        rows = "\n".join(f"| `{folder}/` | {PRODUCTS[k]['name']} |" for folder, k in bundle_parts)
        steps = """1. **Start with the Prompt Library's SET-01 and SET-02** to create your business brief and voice profile.
2. **Read the Playbook's Chapters 1–3** and do the admin audit.
3. **Set up The Client Desk** (Settings tab, then clear the sample rows) and enter your clients and open invoices.
4. **Book a weekly review**: the Playbook's Chapter 13 and the Client Desk's Weekly Review tab work together.

Each folder has its own `START-HERE.pdf` with setup steps for that product."""
        md = f"""# Start here: {spec['name']}

Thank you for your purchase. This bundle contains all three Band of One products.

| Folder | Product |
|---|---|
{rows}

## Suggested order

{steps}
"""
    else:
        rows = "\n".join(f"| `{Path(src).name}` | {desc} |" for src, desc in spec["files"])
        steps = "\n".join(f"{n}. {s}" for n, s in enumerate(spec["steps"], 1))
        md = f"""# Start here: {spec['name']}

Thank you for your purchase. Here's what's in your download and how to get going in about ten minutes.

## What's inside

| File | What it's for |
|---|---|
{rows}
| `LICENSE.txt` | What you can and can't do with the files (plain language) |
| `CHANGELOG.md` | Version history |

## First steps

{steps}

{spec['extra']}
"""
    md += f"""
## Good practice with AI tools

- **Redact before you paste.** Replace client names, contact details and confidential information with placeholders.
- **You decide.** Check every AI draft for facts, prices, dates and promises before it reaches a client.
- **Not professional advice.** Templates that touch contracts, fees or late payments are communication aids. Check legal or tax questions with a qualified professional.

## Help and updates

{SUPPORT} Updates within version 1.x are free.

**License in one line:** use it in your own business as much as you like; don't share or resell the files. Full terms are in `LICENSE.txt`.
"""
    build_pdf(md, out_pdf, {"title": f"Start here: {spec['name']}", "footer_left": f"{spec['name']} · Start here"},
              toc=False, no_cover=True, number_chapters=False, extra_css=START_CSS, front_matter_html=hero)


def stage_product(key, spec, root_dir):
    root_dir.mkdir(parents=True, exist_ok=True)
    for src, _ in spec["files"]:
        assert Path(src).exists(), src
        shutil.copy(src, root_dir / Path(src).name)
    (root_dir / "LICENSE.txt").write_text(license_text(spec["name"]))
    (root_dir / "CHANGELOG.md").write_text(changelog(spec["name"], [s for s, _ in spec["files"]]))
    start_here(key, spec, root_dir / "START-HERE.pdf")


def zip_dir(folder: Path, out_zip: Path):
    out_zip.unlink(missing_ok=True)
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in sorted(folder.rglob("*")):
            if f.is_file():
                info = zipfile.ZipInfo(str(Path(folder.name) / f.relative_to(folder)), date_time=(2026, 9, 24, 12, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, f.read_bytes())
    return out_zip


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    shutil.rmtree(STAGE, ignore_errors=True)
    OUT.mkdir(parents=True, exist_ok=True)
    zips = []
    for key, spec in PRODUCTS.items():
        d = STAGE / spec["stem"]
        stage_product(key, spec, d)
        zips.append((spec["name"], zip_dir(d, OUT / f"{spec['stem']}.zip")))
    # bundle
    b = STAGE / BUNDLE["stem"]
    parts = [("1_Solo-Admin-Playbook", "playbook"), ("2_The-Client-Desk", "clientdesk"), ("3_Prompt-Library", "prompts")]
    for folder, key in parts:
        shutil.copytree(STAGE / PRODUCTS[key]["stem"], b / folder)
    (b / "LICENSE.txt").write_text(license_text(BUNDLE["name"] + " (all three products)"))
    (b / "CHANGELOG.md").write_text(changelog(BUNDLE["name"], [f"{f}/" for f, _ in parts]))
    start_here("bundle", BUNDLE, b / "START-HERE.pdf", bundle_parts=parts)
    zips.append((BUNDLE["name"], zip_dir(b, OUT / f"{BUNDLE['stem']}.zip")))

    lines = ["# Customer-ready packages (manifest)", "",
             f"Built {DATE} by `Build_Tools/build_packages.py`. Upload each ZIP as the product file on Gumroad. "
             "Don't edit the ZIPs by hand: change the source, rebuild, and re-run the packager.", "",
             "| Package | ZIP | Size | SHA-256 |", "|---|---|---|---|"]
    for name, z in zips:
        lines.append(f"| {name} | `{z.name}` | {z.stat().st_size / 1e6:.2f} MB | `{sha256(z)[:16]}…` |")
    lines += ["", "## Contents", ""]
    for name, z in zips:
        with zipfile.ZipFile(z) as zz:
            lines.append(f"**{z.name}**\n")
            lines += [f"- `{i.filename}` ({i.file_size / 1024:,.0f} KB)" for i in zz.infolist()]
            lines.append("")
    (OUT / "MANIFEST.md").write_text("\n".join(lines))
    for name, z in zips:
        print(f"{z.name}: {z.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()

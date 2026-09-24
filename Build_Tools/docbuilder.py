"""Band of One document engine: Markdown -> branded PDF (+ editable DOCX).

Features
- Cover page (separate, no footer) + body with running footer and page numbers
- Automatic table of contents with real page numbers (two-pass render)
- Callout boxes:   !!! tip "Title"   (tip | note | warning | example | prompt | worksheet | checklist | source)
- Checklists:      - [ ] item
- Worksheet lines: [[lines:5]]     Empty box: [[box:140]]     Page break: [[pagebreak]]
- Tables, fenced code, footnote-style source lists

Usage (from Python):
    from docbuilder import build_pdf, build_docx
    build_pdf(md_text, out_pdf, meta)
"""
from __future__ import annotations

import html as htmlmod
import re
import shutil
import subprocess
from pathlib import Path

import markdown
from pypdf import PdfReader, PdfWriter

from brand import BRAND_NAME, COLORS, BUILD, font_face_css
from render import run, write_html

LOGO_DIR = BUILD.parent / "Digital_Products_Business" / "02_Branding" / "logo"

# ----------------------------------------------------------------------------- CSS

BASE_CSS = """
:root{--ink:%(ink)s;--paper:%(paper)s;--teal:%(teal)s;--deep:%(deep_teal)s;--mist:%(mist)s;
--orange:%(orange)s;--rust:%(rust)s;--butter:%(butter)s;--stone:%(stone)s;--slate:%(slate)s;}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:'Inter',system-ui,sans-serif;color:var(--ink);font-size:10.6pt;line-height:1.58;background:#fff}
h1,h2,h3,h4{font-family:'Fraunces',Georgia,serif;color:var(--ink);line-height:1.18;margin:0}
h1{font-size:27pt;font-weight:700;letter-spacing:-.01em;margin:0 0 14pt}
h2{font-size:16.5pt;font-weight:600;margin:22pt 0 8pt;color:var(--deep)}
h3{font-size:12.6pt;font-weight:600;margin:16pt 0 5pt}
h4{font-family:'Inter';font-size:9pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin:14pt 0 4pt}
p{margin:0 0 8pt}
a{color:var(--teal);text-decoration:underline;text-underline-offset:2px}
strong{font-weight:600}
ul,ol{margin:0 0 9pt;padding-left:18pt}
li{margin:0 0 3pt}
li>p{margin:0}
hr{border:0;border-top:1px solid var(--stone);margin:16pt 0}
code{font-family:'JetBrains Mono',monospace;font-size:8.8pt;background:var(--mist);padding:1px 4px;border-radius:3px}
pre{font-family:'JetBrains Mono',monospace;font-size:8.6pt;line-height:1.5;background:#F4F7F6;border:1px solid #D5E6E2;
  border-left:4px solid var(--teal);border-radius:6px;padding:10pt 12pt;white-space:pre-wrap;word-break:break-word;margin:6pt 0 12pt;break-inside:avoid}
pre code{background:none;padding:0;font-size:inherit}
blockquote{margin:10pt 0;padding:8pt 14pt;border-left:4px solid var(--butter);background:#FFF9EA;color:var(--ink);border-radius:0 6px 6px 0}
blockquote p:last-child{margin:0}
table{border-collapse:collapse;width:100%%;margin:6pt 0 14pt;font-size:9.2pt;break-inside:auto}
thead{display:table-header-group}
tr{break-inside:avoid}
th{background:var(--deep);color:#fff;font-weight:600;text-align:left;padding:6pt 8pt;border:1px solid var(--deep)}
td{padding:5.5pt 8pt;border:1px solid var(--stone);vertical-align:top}
td:empty{height:23pt;background:#fff}
sup.ref{font-size:7pt;color:var(--teal);font-weight:600;margin-left:1px}
tbody tr:nth-child(even) td{background:#FAF8F4}
img{max-width:100%%}
.page-break{break-after:page;height:0}
/* callouts */
.admonition{border-radius:8px;padding:10pt 13pt 6pt;margin:10pt 0 14pt;break-inside:avoid;border:1px solid transparent}
.admonition-title{font-family:'Inter';font-weight:700;font-size:8.4pt;letter-spacing:.09em;text-transform:uppercase;margin:0 0 5pt}
.admonition.tip{background:var(--mist);border-color:#C6E2DC}.admonition.tip .admonition-title{color:var(--deep)}
.admonition.note{background:#F3F1EC;border-color:var(--stone)}.admonition.note .admonition-title{color:var(--slate)}
.admonition.warning{background:#FDF0EA;border-color:#F2C9B8}.admonition.warning .admonition-title{color:var(--rust)}
.admonition.example{background:#fff;border:1px solid var(--stone);border-left:5px solid var(--orange)}.admonition.example .admonition-title{color:var(--rust)}
.admonition.prompt{background:#F4F7F6;border:1px solid #D5E6E2;border-left:5px solid var(--teal)}.admonition.prompt .admonition-title{color:var(--teal)}
.admonition.prompt p,.admonition.prompt li{font-family:'JetBrains Mono',monospace;font-size:8.6pt;line-height:1.55}
.admonition.worksheet{background:#fff;border:1.5px dashed var(--teal)}.admonition.worksheet .admonition-title{color:var(--teal)}
.admonition.checklist{background:#FFF9EA;border-color:#F3DFA8}.admonition.checklist .admonition-title{color:#8A6212}
.admonition.source{background:#fff;border-color:var(--stone);font-size:8.8pt}.admonition.source .admonition-title{color:var(--slate)}
/* checklists */
li.task{list-style:none;margin-left:-15pt;padding-left:19pt;position:relative}
li.task::before{content:'';position:absolute;left:0;top:2.5pt;width:10pt;height:10pt;border:1.4px solid var(--teal);border-radius:2.5px;background:#fff}
li.task.done::before{background:var(--teal)}
/* worksheet helpers */
.lines{margin:4pt 0 10pt;break-inside:avoid}
.lines span{display:block;height:21pt;border-bottom:1px solid #C9CFD3}
.box{border:1px solid #C9CFD3;border-radius:6px;margin:4pt 0 10pt;background:#fff}
/* chapter openers */
.chapter-label{font-family:'Inter';font-size:8.6pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--rust);margin:0 0 6pt}
section.chapter{break-before:page}
section.chapter:first-of-type{break-before:auto}
section.chapter.nobreak{break-before:auto;margin-top:26pt}
.lede{font-size:12.2pt;line-height:1.55;color:var(--slate);margin:0 0 14pt}
/* TOC */
.toc{break-after:page}
.toc h1{margin-bottom:18pt}
.toc ol{list-style:none;padding:0;margin:0}
.toc li{display:flex;align-items:baseline;gap:6pt;margin:0 0 6pt}
.toc li.l1{font-family:'Fraunces';font-weight:600;font-size:12.2pt;margin-top:9pt}
.toc li.l2{font-size:9.8pt;color:var(--slate);padding-left:16pt}
.toc .dots{flex:1;border-bottom:1px dotted #B8BEC4;transform:translateY(-3pt)}
.toc .num{font-variant-numeric:tabular-nums;min-width:18pt;text-align:right}
.small{font-size:8.8pt;color:var(--slate)}
.muted{color:var(--slate)}
.kicker{font-family:'Inter';font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:8.4pt;color:var(--teal)}
.two-col{columns:2;column-gap:18pt}
.center{text-align:center}
"""


def _css() -> str:
    return BASE_CSS % COLORS


PAGE_CSS = """
@page{size:Letter;margin:0.78in 0.82in 0.9in 0.82in}
"""

FOOTER_TEMPLATE = """
<div style="width:100%;font-family:Inter,Arial,sans-serif;font-size:7.5pt;color:#56606B;padding:0 0.82in;display:flex;justify-content:space-between;">
<span>{left}</span><span><span class="pageNumber"></span></span></div>
"""

# ----------------------------------------------------------------------------- Markdown preprocessing

_ADMON = re.compile(r'^!!! (\w+)(?: "([^"]*)")?\s*$')


REF = re.compile(r"\^\[(\d+(?:[,–-]\s?\d+)*)\]\^")


def _preprocess(md_text: str) -> str:
    """Convert custom tokens to HTML-friendly markdown before python-markdown runs."""
    md_text = REF.sub(r'<sup class="ref">[\1]</sup>', md_text)
    out = []
    for line in md_text.splitlines():
        m = re.fullmatch(r"\s*\[\[lines:(\d+)\]\]\s*", line)
        if m:
            out.append('<div class="lines">' + "<span></span>" * int(m.group(1)) + "</div>")
            continue
        m = re.fullmatch(r"\s*\[\[box:(\d+)\]\]\s*", line)
        if m:
            out.append(f'<div class="box" style="height:{int(m.group(1))}pt"></div>')
            continue
        if re.fullmatch(r"\s*\[\[pagebreak\]\]\s*", line):
            out.append('<div class="page-break"></div>')
            continue
        out.append(line)
    return "\n".join(out)


def _postprocess(html: str) -> str:
    # task list items
    html = re.sub(r"<li>\s*\[ \]\s*", '<li class="task">', html)
    html = re.sub(r"<li>\s*\[[xX]\]\s*", '<li class="task done">', html)
    html = re.sub(r"<li>\s*<p>\s*\[ \]\s*", '<li class="task"><p>', html)
    return html


def md_to_html(md_text: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "admonition", "attr_list", "sane_lists", "md_in_html", "footnotes"],
        output_format="html5",
    )
    return _postprocess(md.convert(_preprocess(md_text)))


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


NO_BREAK_PREFIXES = ("appendix b", "appendix c", "about and license", "appendix e")


def split_chapters(body_html: str, number_chapters: bool = True):
    """Wrap each <h1> section in <section class=chapter> and collect TOC entries."""
    parts = re.split(r"(?=<h1[ >])", body_html)
    sections, toc, chapter_no = [], [], 0
    for part in parts:
        if not part.strip():
            continue
        m = re.match(r"<h1[^>]*>(.*?)</h1>", part, re.S)
        if m:
            title_html = m.group(1)
            title_txt = htmlmod.unescape(re.sub(r"<[^>]+>", "", title_html))
            skip_number = title_txt.lower().startswith(("appendix", "sources", "about", "how to use", "introduction", "conclusion", "your next", "license", "quick start", "welcome"))
            label = ""
            if number_chapters and not skip_number:
                chapter_no += 1
                label = f'<p class="chapter-label">Chapter {chapter_no}</p>'
            anchor = slugify(title_txt)
            part = part.replace(m.group(0), f'{label}<h1 id="{anchor}">{title_html}</h1>', 1)
            toc.append((1, title_txt, anchor))
            for h2 in re.finditer(r"<h2[^>]*>(.*?)</h2>", part, re.S):
                t = htmlmod.unescape(re.sub(r"<[^>]+>", "", h2.group(1)))
                toc.append((2, t, slugify(t)))
            cls = "chapter nobreak" if any(title_txt.lower().startswith(x) for x in NO_BREAK_PREFIXES) else "chapter"
            sections.append(f'<section class="{cls}">{part}</section>')
        else:
            sections.append(f"<section>{part}</section>")
    return "\n".join(sections), toc


def toc_html(toc, numbers=None, include_h2=True, title="Contents"):
    items = []
    for i, (lvl, text, anchor) in enumerate(toc):
        if lvl == 2 and not include_h2:
            continue
        num = numbers[i] if numbers and numbers[i] else "00"
        items.append(
            f'<li class="l{lvl}"><span>{htmlmod.escape(text)}</span><span class="dots"></span><span class="num">{num}</span></li>'
        )
    return f'<nav class="toc"><h1>{title}</h1><ol>{"".join(items)}</ol></nav>'


def _norm(s: str) -> str:
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _find_pages(pdf_path: Path, toc, toc_pages: int, include_h2=True):
    reader = PdfReader(str(pdf_path))
    texts = [_norm(p.extract_text() or "") for p in reader.pages]
    numbers, start = [], toc_pages
    for lvl, text, _ in toc:
        if lvl == 2 and not include_h2:
            numbers.append(None)
            continue
        key = _norm(text)[:60]
        found = None
        # Prefer a page that opens with the heading (chapters start on a new page), so a
        # mention in an earlier index or table isn't mistaken for the heading itself.
        for i in range(start, len(texts)):
            if key and key in texts[i][: len(key) + 20]:
                found = i
                break
        if found is None:
            for i in range(start, len(texts)):
                if key and key in texts[i]:
                    found = i
                    break
        if found is None:
            numbers.append("")
        else:
            numbers.append(str(found + 1))
            start = found
    return numbers


def page_html(inner: str, extra_css: str = "", title: str = "") -> str:
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{htmlmod.escape(title)}</title>
<style>{font_face_css()}\n{_css()}\n{PAGE_CSS}\n{extra_css}</style></head><body>{inner}</body></html>"""


# ----------------------------------------------------------------------------- Cover

def default_cover(meta: dict) -> str:
    """Full-bleed cover page used when a custom cover isn't supplied."""
    logo = (LOGO_DIR / "band-of-one-horizontal-on-dark.svg").as_uri()
    mark = (LOGO_DIR / "band-of-one-mark.svg").as_uri()
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_face_css()}
@page{{size:Letter;margin:0}}
html,body{{margin:0;width:8.5in;height:11in;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{background:{COLORS['ink']};color:{COLORS['paper']};font-family:Inter,sans-serif}}
.page{{position:relative;width:8.5in;height:11in;overflow:hidden;background:{COLORS['ink']}}}
.ring{{position:absolute;right:-2.9in;bottom:-2.2in;width:7.2in;height:7.2in;border-radius:50%;border:0.5in solid {COLORS['orange']}}}
.disc{{position:absolute;right:-2.1in;bottom:-1.3in;width:5.3in;height:5.3in;border-radius:50%;background:{COLORS['teal']}}}
.wrap{{position:absolute;left:0.85in;right:0.85in;top:0.8in;bottom:0.8in;display:flex;flex-direction:column}}
.kicker{{font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:10pt;color:{COLORS['butter']}}}
h1{{font-family:Fraunces,serif;font-weight:700;font-size:44pt;line-height:1.02;letter-spacing:-.015em;margin:18pt 0 16pt;max-width:6.2in;position:relative}}
.sub{{font-size:14pt;line-height:1.45;max-width:4.9in;color:#E9E4DA;position:relative}}
.meta{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end}}
.meta img{{height:0.62in;position:relative}}
.tag{{font-size:9pt;color:#F3EFE7;text-align:right;line-height:1.5;position:relative;max-width:2.6in}}
</style></head><body>
<div class="page"><div class="ring"></div><div class="disc"></div>
<div class="wrap"><div class="kicker">{htmlmod.escape(meta.get('kicker',''))}</div>
<h1>{meta.get('title_html', htmlmod.escape(meta['title']))}</h1>
<div class="sub">{htmlmod.escape(meta.get('subtitle',''))}</div>
<div class="meta"><img src="{logo}" alt="Band of One"><div class="tag">{meta.get('cover_note','')}</div></div></div></div>
</body></html>"""


# ----------------------------------------------------------------------------- Build

def build_pdf(md_text: str, out_pdf: Path, meta: dict, cover_html: str | None = None,
              toc: bool = True, include_h2: bool = True, number_chapters: bool = True,
              extra_css: str = "", front_matter_html: str = "", back_matter_html: str = "",
              no_cover: bool = False) -> Path:
    """Render markdown to a branded PDF. meta: title, subtitle, kicker, footer_left."""
    out_pdf = Path(out_pdf)
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    body_html = md_to_html(md_text)
    chapters, toc_entries = split_chapters(body_html, number_chapters=number_chapters)
    stem = slugify(meta["title"])[:40]
    footer = FOOTER_TEMPLATE.format(left=htmlmod.escape(meta.get("footer_left", f"{BRAND_NAME} · {meta['title']}")))
    tmp = BUILD / ".tmp"
    tmp.mkdir(exist_ok=True)

    def render_body(numbers):
        toc_block = toc_html(toc_entries, numbers, include_h2) if toc else ""
        html = page_html(front_matter_html + toc_block + chapters + back_matter_html, extra_css, meta["title"])
        path = write_html(f"{stem}-body.html", html)
        body_pdf = tmp / f"{stem}-body.pdf"
        run([{"html": path, "out": body_pdf, "type": "pdf", "displayHeaderFooter": True,
              "footerTemplate": footer, "margin": {"top": "0.78in", "bottom": "0.9in", "left": "0.82in", "right": "0.82in"}}])
        return body_pdf

    body_pdf = render_body(None)
    if toc:
        # count TOC + front matter pages by locating the first chapter title
        reader = PdfReader(str(body_pdf))
        first_key = _norm(toc_entries[0][1])[:60] if toc_entries else ""
        toc_pages = 0
        for i, p in enumerate(reader.pages):
            t = _norm(p.extract_text() or "")
            if i > 0 and first_key and first_key in t and not t.startswith(_norm("Contents")):
                toc_pages = i
                break
        numbers = _find_pages(body_pdf, toc_entries, toc_pages, include_h2)
        body_pdf = render_body(numbers)

    sources = [body_pdf]
    if not no_cover:
        cover = cover_html or default_cover(meta)
        cover_path = write_html(f"{stem}-cover.html", cover)
        cover_pdf = tmp / f"{stem}-cover.pdf"
        run([{"html": cover_path, "out": cover_pdf, "type": "pdf", "width": 816, "height": 1056}])
        sources.insert(0, cover_pdf)

    writer = PdfWriter()
    for src in sources:
        for page in PdfReader(str(src)).pages:
            writer.add_page(page)
    writer.add_metadata({"/Title": meta["title"], "/Author": BRAND_NAME, "/Subject": meta.get("subtitle", "")})
    with open(out_pdf, "wb") as f:
        writer.write(f)
    return out_pdf


# ----------------------------------------------------------------------------- DOCX

REFERENCE_DOCX = BUILD / "templates" / "reference.docx"


def _ensure_reference_docx():
    """Create a brand-styled pandoc reference.docx once."""
    if REFERENCE_DOCX.exists():
        return REFERENCE_DOCX
    import pypandoc
    from docx import Document
    from docx.shared import Pt, RGBColor

    REFERENCE_DOCX.parent.mkdir(parents=True, exist_ok=True)
    pandoc = pypandoc.get_pandoc_path()
    with open(REFERENCE_DOCX, "wb") as f:
        subprocess.run([pandoc, "--print-default-data-file", "reference.docx"], stdout=f, check=True)
    doc = Document(str(REFERENCE_DOCX))

    def rgb(h):
        h = h.lstrip("#")
        return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

    styles = doc.styles
    for name, font, size, color, bold in [
        ("Normal", "Inter", 10.5, COLORS["ink"], False),
        ("Body Text", "Inter", 10.5, COLORS["ink"], False),
        ("First Paragraph", "Inter", 10.5, COLORS["ink"], False),
        ("Compact", "Inter", 10.5, COLORS["ink"], False),
        ("Title", "Fraunces", 30, COLORS["ink"], True),
        ("Subtitle", "Inter", 13, COLORS["slate"], False),
        ("Heading 1", "Fraunces", 22, COLORS["ink"], True),
        ("Heading 2", "Fraunces", 15, COLORS["deep_teal"], True),
        ("Heading 3", "Fraunces", 12.5, COLORS["ink"], True),
        ("Heading 4", "Inter", 10, COLORS["teal"], True),
        ("Block Text", "Inter", 10.5, COLORS["ink"], False),
        ("Source Code", "JetBrains Mono", 9, COLORS["ink"], False),
    ]:
        try:
            st = styles[name]
        except KeyError:
            continue
        st.font.name = font
        st.font.size = Pt(size)
        st.font.color.rgb = rgb(color)
        st.font.bold = bold
        rpr = st.element.get_or_add_rPr()
        rfonts = rpr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts")
        if rfonts is not None:
            for attr in ("ascii", "hAnsi", "cs", "eastAsia"):
                rfonts.set(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{attr}", font)
    doc.save(str(REFERENCE_DOCX))
    return REFERENCE_DOCX


def _md_for_docx(md_text: str) -> str:
    """Translate custom syntax into plain pandoc markdown."""
    md_text = REF.sub(lambda m: "^\\[" + m.group(1) + "\\]^", md_text)
    out, in_admon, admon_indent = [], False, 4
    for line in md_text.splitlines():
        m = _ADMON.match(line)
        if m:
            kind, title = m.group(1), (m.group(2) or m.group(1).title())
            out.append(f"> **{title}**")
            out.append(">")
            in_admon = True
            continue
        if in_admon:
            if line.startswith("    "):
                out.append("> " + line[4:])
                continue
            if not line.strip():
                out.append(">")
                continue
            in_admon = False
        lm = re.fullmatch(r"\s*\[\[lines:(\d+)\]\]\s*", line)
        if lm:
            out.extend(["", *(["\\_" * 60 + "\n"] * int(lm.group(1)))])
            continue
        if re.fullmatch(r"\s*\[\[box:(\d+)\]\]\s*", line):
            out.extend(["", "\\_" * 60, ""])
            continue
        if re.fullmatch(r"\s*\[\[pagebreak\]\]\s*", line):
            out.append('\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n')
            continue
        if re.fullmatch(r"\|(\s*\|)+\s*", line):
            # keep blank worksheet rows: pandoc drops fully empty table rows
            line = "|" + "|".join(["\\ " * 12] * (line.count("|") - 1)) + "|"
        line = re.sub(r"^(\s*)- \[ \] ", r"\1- ☐ ", line)
        line = re.sub(r"^(\s*)- \[[xX]\] ", r"\1- ☑ ", line)
        line = re.sub(r"\{:[^}]*\}", "", line)
        out.append(line)
    return "\n".join(out)


def build_docx(md_text: str, out_docx: Path, meta: dict) -> Path:
    import pypandoc

    ref = _ensure_reference_docx()
    out_docx = Path(out_docx)
    out_docx.parent.mkdir(parents=True, exist_ok=True)
    header = f"---\ntitle: \"{meta['title']}\"\nsubtitle: \"{meta.get('subtitle','')}\"\nauthor: \"{BRAND_NAME}\"\n---\n\n"
    text = header + _md_for_docx(md_text)
    extra = ["--reference-doc", str(ref)]
    if meta.get("docx_toc", True):
        extra += ["--toc", "--toc-depth=2"]
    pypandoc.convert_text(text, "docx", format="markdown+pipe_tables+raw_attribute", outputfile=str(out_docx), extra_args=extra)
    return out_docx

"""Build Product A: The Solo Admin Playbook (PDF + DOCX + combined Markdown source).

Run: python3 Build_Tools/build_playbook.py
"""
import re
import shutil
from pathlib import Path

from brand import COLORS as C, ROOT, font_face_css
from covers import product_cover
from docbuilder import build_docx, build_pdf
from render import run, write_html

GUIDE = ROOT / "Digital_Products_Business" / "03_Digital_Guide"
SRC = GUIDE / "source"
IMG = SRC / "images"
LOGO = ROOT / "Digital_Products_Business" / "02_Branding" / "logo"
TITLE = "The Solo Admin Playbook"
SUBTITLE = "A practical system for handling client admin with AI, for freelancers, consultants and coaches who run the whole show."
VERSION = "1.0"
FILE_STEM = "BandOfOne_Solo-Admin-Playbook_v1.0"

PARTS = ["01_front_and_foundations.md", "02_client_workflows.md", "03_money_systems_review.md", "04_appendices.md"]


def lifecycle_diagram():
    stages = [("1", "Inquiry"), ("2", "Discovery"), ("3", "Proposal"), ("4", "Onboarding"), ("5", "Delivery"), ("6", "Payment"), ("7", "Offboarding")]
    nodes = "".join(
        f'<div class="n"><div class="dot{" alt" if i in (3,4) else (" end" if i in (5,6) else "")}">{n}</div><div class="lbl">{t}</div></div>'
        for i, (n, t) in enumerate(stages)
    )
    html = f"""<!doctype html><html><head><style>{font_face_css()}
html,body{{margin:0;background:#fff}}
.w{{width:1600px;height:560px;position:relative;font-family:Inter,sans-serif;color:{C['ink']}}}
.line{{position:absolute;left:130px;right:130px;top:190px;height:8px;background:{C['stone']};border-radius:4px}}
.row{{position:absolute;left:60px;right:60px;top:120px;display:flex;justify-content:space-between}}
.n{{width:180px;text-align:center}}
.dot{{width:140px;height:140px;margin:0 auto;border-radius:50%;background:{C['teal']};color:{C['paper']};font-family:Fraunces;font-weight:700;font-size:64px;display:flex;align-items:center;justify-content:center;border:10px solid #fff;box-shadow:0 0 0 6px {C['orange']}}}
.dot.alt{{background:{C['deep_teal']}}}
.dot.end{{background:{C['ink']}}}
.lbl{{margin-top:18px;font-weight:700;font-size:30px}}
.ph{{position:absolute;top:36px;font-weight:700;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:{C['rust']}}}
.br{{position:absolute;top:78px;height:14px;border:3px solid {C['stone']};border-bottom:0;border-radius:10px 10px 0 0}}
.loop{{position:absolute;left:150px;right:150px;top:400px;height:90px;border:5px dashed {C['teal']};border-top:0;border-radius:0 0 60px 60px}}
.loopt{{position:absolute;left:0;right:0;top:505px;text-align:center;font-size:26px;color:{C['deep_teal']};font-weight:600}}
</style></head><body><div class="w">
<div class="ph" style="left:210px">Win the work</div><div class="br" style="left:95px;width:620px"></div>
<div class="ph" style="left:810px">Do the work</div><div class="br" style="left:760px;width:420px"></div>
<div class="ph" style="left:1215px">Close the loop</div><div class="br" style="left:1215px;width:300px"></div>
<div class="line"></div><div class="row">{nodes}</div>
<div class="loop"></div><div class="loopt">Referrals &amp; repeat work start the next cycle</div>
</div></body></html>"""
    IMG.mkdir(parents=True, exist_ok=True)
    p = write_html("lifecycle.html", html)
    run([{"html": p, "out": IMG / "lifecycle.png", "type": "png", "width": 1600, "height": 560, "scale": 1, "selector": ".w"}])


def cover_html():
    logo = (LOGO / "band-of-one-horizontal-on-dark.svg").as_uri()
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_face_css()}
@page{{size:Letter;margin:0}}
html,body{{margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{position:relative;width:8.5in;height:11in;overflow:hidden;background:{C['ink']};color:{C['paper']};font-family:Inter,sans-serif}}
.ring{{position:absolute;right:-2.6in;top:4.7in;width:7.4in;height:7.4in;border-radius:50%;border:0.55in solid {C['orange']}}}
.disc{{position:absolute;right:-1.75in;top:5.55in;width:5.7in;height:5.7in;border-radius:50%;background:{C['teal']}}}
.one{{position:absolute;right:0.8in;top:6.3in;font-family:Fraunces;font-weight:800;font-size:250pt;line-height:1;color:{C['paper']};opacity:.95}}
.wrap{{position:absolute;left:0.85in;top:0.85in;right:0.85in}}
.kicker{{font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:10pt;color:{C['butter']}}}
h1{{font-family:Fraunces,serif;font-weight:700;font-size:54pt;line-height:.98;letter-spacing:-.02em;margin:16pt 0 18pt}}
h1 em{{font-style:italic;font-weight:400;color:{C['butter']}}}
.sub{{font-size:14.5pt;line-height:1.45;max-width:5.1in;color:#EDE8DF}}
ul{{list-style:none;padding:0;margin:26pt 0 0;font-size:11pt;line-height:1.9;color:#EDE8DF}}
ul li::before{{content:'';display:inline-block;width:8pt;height:8pt;border-radius:50%;background:{C['orange']};margin-right:9pt;transform:translateY(-1pt)}}
.foot{{position:absolute;left:0.85in;bottom:0.75in}}
.foot img{{height:0.6in}}
.ver{{position:absolute;left:0.85in;bottom:0.45in;font-size:8.5pt;color:#BDB6A8}}
</style></head><body><div class="page">
<div class="ring"></div><div class="disc"></div><div class="one">1</div>
<div class="wrap"><div class="kicker">The Guide · Band of One</div>
<h1>The Solo<br>Admin <em>Playbook</em></h1>
<div class="sub">{SUBTITLE}</div>
<ul><li>Admin audit &amp; priority scoring</li><li>Safe AI setup: brief, voice, privacy</li><li>Six client workflows with templates</li><li>Getting paid: a 5-stage reminder system</li><li>SOPs, light automation &amp; weekly review</li></ul></div>
<div class="foot"><img src="{logo}"></div><div class="ver">Version {VERSION} · September 2026</div>
</div></body></html>"""


EXTRA_CSS = f"""
body{{font-size:10.2pt;line-height:1.52}}
.admonition.prompt p,.admonition.prompt li{{font-size:8.3pt;line-height:1.5}}
h2{{margin-top:18pt}}
figure,p>img{{display:block;margin:6pt 0 12pt}}
img[alt^="The client lifecycle"]{{width:86%;margin:0 auto;border:1px solid {C['stone']};border-radius:8px}}
"""


def combined_markdown():
    text = "\n\n".join((SRC / p).read_text() for p in PARTS)
    return text


def build():
    lifecycle_diagram()
    md = combined_markdown()
    (GUIDE / f"{FILE_STEM}_source.md").write_text(md)
    md_pdf = md.replace("](images/", f"]({IMG.as_uri()}/")
    meta = {"title": TITLE, "subtitle": SUBTITLE, "kicker": "The Guide · Band of One", "footer_left": f"The Solo Admin Playbook · v{VERSION} · Band of One"}
    cover = product_cover("The Guide · Band of One", "The Solo<br>Admin <em>Playbook</em>", SUBTITLE, ["Admin audit &amp; priority scoring", "Safe AI setup: brief, voice, privacy", "Six client workflows with templates", "Getting paid: a 5-stage reminder system", "SOPs, light automation &amp; weekly review"])
    pdf = build_pdf(md_pdf, GUIDE / f"{FILE_STEM}.pdf", meta, cover_html=cover, extra_css=EXTRA_CSS, include_h2=False)
    # DOCX: pandoc resolves images relative to cwd; use absolute paths
    md_docx = md.replace("](images/", f"]({IMG}/")
    build_docx(md_docx, GUIDE / f"{FILE_STEM}_editable.docx", meta)
    print("built", pdf)


if __name__ == "__main__":
    build()

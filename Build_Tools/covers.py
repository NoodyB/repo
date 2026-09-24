"""Shared cover designs for Band of One products and lead magnets (US Letter, print-safe)."""
from brand import COLORS as C, ROOT, font_face_css

LOGO = ROOT / "Digital_Products_Business" / "02_Branding" / "logo"


def product_cover(kicker, title_html, subtitle, bullets, ring=None, disc=None, big="1", version="Version 1.0 · September 2026", big_size="250pt", big_top="6.55in", big_right="0.45in"):
    ring = ring or C["orange"]
    disc = disc or C["teal"]
    logo = (LOGO / "band-of-one-horizontal-on-dark.svg").as_uri()
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_face_css()}
@page{{size:Letter;margin:0}}
html,body{{margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{position:relative;width:8.5in;height:11in;overflow:hidden;background:{C['ink']};color:{C['paper']};font-family:Inter,sans-serif}}
.ring{{position:absolute;right:-3.6in;top:4.75in;width:7.4in;height:7.4in;border-radius:50%;border:0.55in solid {ring}}}
.disc{{position:absolute;right:-2.2in;top:6.15in;width:5.7in;height:5.7in;border-radius:50%;background:{disc}}}
.one{{position:absolute;right:{big_right};top:{big_top};font-family:Fraunces;font-weight:800;font-size:{big_size};line-height:1;color:{C['paper']};opacity:.95;text-align:right}}
.wrap{{position:absolute;left:0.85in;top:0.85in;right:0.85in}}
.kicker{{font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:10pt;color:{C['butter']}}}
h1{{font-family:Fraunces,serif;font-weight:700;font-size:54pt;line-height:.98;letter-spacing:-.02em;margin:16pt 0 18pt}}
h1 em{{font-style:italic;font-weight:400;color:{C['butter']}}}
.sub{{font-size:14.5pt;line-height:1.45;max-width:5.1in;color:#EDE8DF}}
ul{{list-style:none;padding:0;margin:26pt 0 0;font-size:11pt;line-height:1.9;color:#EDE8DF;max-width:4.6in}}
ul li::before{{content:'';display:inline-block;width:8pt;height:8pt;border-radius:50%;background:{ring};margin-right:9pt;transform:translateY(-1pt)}}
.foot{{position:absolute;left:0.85in;bottom:0.75in}}
.foot img{{height:0.6in}}
.ver{{position:absolute;left:0.85in;bottom:0.45in;font-size:8.5pt;color:#BDB6A8}}
</style></head><body><div class="page">
<div class="ring"></div><div class="disc"></div><div class="one">{big}</div>
<div class="wrap"><div class="kicker">{kicker}</div><h1>{title_html}</h1><div class="sub">{subtitle}</div><ul>{lis}</ul></div>
<div class="foot"><img src="{logo}"></div><div class="ver">{version}</div>
</div></body></html>"""

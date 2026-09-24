"""Export logo PNGs, social avatars/banners, OG image, brand board, fonts and the brand guidelines PDF.

Run:  python3 Build_Tools/make_brand_assets.py
"""
import shutil
from pathlib import Path

from brand import COLORS, ROOT, TAGLINE, font_face_css, ttf
from render import run, write_html

DP_BRAND = ROOT / "Digital_Products_Business" / "02_Branding"
CA_BRAND = ROOT / "Content_Automation_Business" / "02_Branding"
LOGO = DP_BRAND / "logo"
C = COLORS


def svg_png_job(svg_name, out, width, height, bg="transparent", scale=1, pad=0):
    uri = (LOGO / svg_name).as_uri()
    html = f"""<html><head><style>html,body{{margin:0;background:{bg}}}
    .w{{width:{width}px;height:{height}px;display:flex;align-items:center;justify-content:center;padding:{pad}px;box-sizing:border-box}}
    img{{max-width:100%;max-height:100%}}</style></head><body><div class="w"><img src="{uri}"></div></body></html>"""
    p = write_html(f"logo-{Path(out).stem}.html", html)
    return {"html": p, "out": out, "type": "png", "width": width, "height": height, "scale": scale,
            "transparent": bg == "transparent", "selector": ".w"}


def banner_html(w, h, headline_size, sub_size, show_sub=True, left=None, maxw=None):
    logo = (LOGO / "band-of-one-horizontal-on-dark.svg").as_uri()
    ring = int(h * 1.35)
    return f"""<!doctype html><html><head><style>{font_face_css()}
html,body{{margin:0}}
.b{{width:{w}px;height:{h}px;background:{C['ink']};position:relative;overflow:hidden;font-family:Inter,sans-serif;color:{C['paper']}}}
.ring{{position:absolute;width:{ring}px;height:{ring}px;border-radius:50%;border:{int(h*0.09)}px solid {C['orange']};right:{-int(ring*0.28)}px;top:{int((h-ring)/2)}px}}
.disc{{position:absolute;width:{int(ring*0.68)}px;height:{int(ring*0.68)}px;border-radius:50%;background:{C['teal']};right:{-int(ring*0.12)}px;top:{int((h-ring*0.68)/2)}px}}
.t{{position:absolute;left:{left if left is not None else int(w*0.06)}px;top:50%;transform:translateY(-50%);max-width:{maxw or int(w*0.58)}px}}
.t img{{height:{int(headline_size*1.25)}px;display:block;margin-bottom:{int(headline_size*0.5)}px}}
.h{{font-family:Fraunces,serif;font-weight:600;font-size:{headline_size}px;line-height:1.12;letter-spacing:-.01em}}
.s{{margin-top:{int(sub_size*0.8)}px;font-size:{sub_size}px;color:{C['butter']};font-weight:600;letter-spacing:.04em}}
</style></head><body><div class="b"><div class="ring"></div><div class="disc"></div>
<div class="t"><img src="{logo}"><div class="h">{TAGLINE}</div>{'<div class="s">Guides · Templates · Prompts · A weekly newsletter</div>' if show_sub else ''}</div></div></body></html>"""


def og_html():
    mark = (LOGO / "band-of-one-horizontal.svg").as_uri()
    return f"""<!doctype html><html><head><style>{font_face_css()}
html,body{{margin:0}}
.b{{width:1200px;height:630px;background:{C['paper']};position:relative;overflow:hidden;font-family:Inter,sans-serif;color:{C['ink']}}}
.ring{{position:absolute;width:700px;height:700px;border-radius:50%;border:56px solid {C['orange']};right:-420px;top:-35px}}
.disc{{position:absolute;width:470px;height:470px;border-radius:50%;background:{C['teal']};right:-300px;top:80px}}
.t{{position:absolute;left:80px;top:86px;width:760px}}
.t img{{height:78px}}
.h{{font-family:Fraunces,serif;font-weight:700;font-size:60px;line-height:1.05;letter-spacing:-.015em;margin-top:48px}}
.s{{margin-top:26px;font-size:25px;color:{C['slate']};line-height:1.4;max-width:680px}}
</style></head><body><div class="b"><div class="ring"></div><div class="disc"></div>
<div class="t"><img src="{mark}"><div class="h">Practical AI systems for businesses of one.</div>
<div class="s">Workflows, templates and honest tool notes for people who run a service business on their own.</div></div></div></body></html>"""


def brand_board_html():
    logo = (LOGO / "band-of-one-horizontal.svg").as_uri()
    rev = (LOGO / "band-of-one-horizontal-on-dark.svg").as_uri()
    mark = (LOGO / "band-of-one-mark.svg").as_uri()
    sw = "".join(
        f'<div class="sw"><div class="chip" style="background:{C[k]}"></div><b>{n}</b><span>{C[k]}</span></div>'
        for k, n in [("ink", "Ink"), ("paper", "Paper"), ("teal", "Band Teal"), ("deep_teal", "Deep Teal"), ("mist", "Mist"),
                     ("orange", "Signal Orange"), ("rust", "Rust"), ("butter", "Butter"), ("stone", "Stone"), ("slate", "Slate")]
    )
    return f"""<!doctype html><html><head><style>{font_face_css()}
html,body{{margin:0}}
.b{{width:1600px;height:1000px;background:{C['paper']};font-family:Inter,sans-serif;color:{C['ink']};display:grid;grid-template-columns:1fr 1fr;gap:28px;padding:56px;box-sizing:border-box}}
.card{{background:#fff;border:1px solid {C['stone']};border-radius:14px;padding:32px;position:relative;overflow:hidden}}
.k{{font-weight:700;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:{C['teal']};margin-bottom:18px}}
.dark{{background:{C['ink']};border:0}}
.row{{display:flex;gap:26px;align-items:center}}
.sws{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}}
.sw{{font-size:13px}} .sw b{{display:block;margin-top:8px}} .sw span{{color:{C['slate']};font-family:'JetBrains Mono'}}
.chip{{height:64px;border-radius:10px;border:1px solid rgba(0,0,0,.08)}}
.f1{{font-family:Fraunces;font-weight:700;font-size:54px;line-height:1.05}}
.f2{{font-size:18px;line-height:1.5;color:{C['slate']};margin-top:12px}}
.f3{{font-family:'JetBrains Mono';font-size:15px;margin-top:14px;background:{C['mist']};padding:10px 12px;border-radius:8px}}
.btn{{display:inline-block;background:{C['rust']};color:#fff;font-weight:600;padding:12px 20px;border-radius:8px;margin-top:16px;font-size:16px}}
.btn2{{display:inline-block;background:{C['teal']};color:#fff;font-weight:600;padding:12px 20px;border-radius:8px;margin:16px 0 0 10px;font-size:16px}}
.tag{{font-family:Fraunces;font-style:italic;font-size:26px;color:{C['deep_teal']};margin-top:22px}}
</style></head><body><div class="b">
<div class="card"><div class="k">Logo</div><img src="{logo}" style="height:96px"><div class="row" style="margin-top:34px"><img src="{mark}" style="height:120px"><div class="card dark" style="padding:22px"><img src="{rev}" style="height:64px"></div></div>
<div class="tag">Practical AI systems for businesses of one.</div></div>
<div class="card"><div class="k">Color</div><div class="sws">{sw}</div></div>
<div class="card"><div class="k">Type</div><div class="f1">Fraunces for headlines</div><div class="f2">Inter for body copy, interfaces and spreadsheets: clear, friendly and readable at small sizes.</div><div class="f3">JetBrains Mono → prompts & data</div></div>
<div class="card"><div class="k">Buttons & callouts</div><div><span class="btn">Get the Playbook</span><span class="btn2">Read the guide</span></div>
<div style="margin-top:22px;background:{C['mist']};border:1px solid #C6E2DC;border-radius:10px;padding:16px 18px;font-size:16px;line-height:1.5"><b style="color:{C['deep_teal']};font-size:12px;letter-spacing:.12em;text-transform:uppercase">Tip</b><br>Draft with AI, then edit in your own voice. Never paste client secrets into a chat tool.</div></div>
</div></body></html>"""


def build():
    for d in (DP_BRAND, CA_BRAND):
        (d / "logo").mkdir(parents=True, exist_ok=True)
        (d / "social").mkdir(parents=True, exist_ok=True)
    jobs = []
    # logo PNG exports
    jobs.append(svg_png_job("band-of-one-horizontal.svg", LOGO / "band-of-one-horizontal.png", 1200, 280, scale=2))
    jobs.append(svg_png_job("band-of-one-horizontal-reversed.svg", LOGO / "band-of-one-horizontal-reversed.png", 1200, 280, bg=C["ink"], scale=2))
    jobs.append(svg_png_job("band-of-one-stacked.svg", LOGO / "band-of-one-stacked.png", 800, 700, scale=2, pad=20))
    jobs.append(svg_png_job("band-of-one-mark.svg", LOGO / "band-of-one-mark-1024.png", 1024, 1024))
    jobs.append(svg_png_job("band-of-one-mark.svg", LOGO / "band-of-one-mark-512.png", 512, 512))
    jobs.append(svg_png_job("band-of-one-app-icon.svg", LOGO / "band-of-one-app-icon-512.png", 512, 512))
    jobs.append(svg_png_job("favicon.svg", LOGO / "favicon-32.png", 32, 32))
    jobs.append(svg_png_job("favicon.svg", LOGO / "favicon-192.png", 192, 192))
    jobs.append(svg_png_job("band-of-one-app-icon.svg", LOGO / "apple-touch-icon.png", 180, 180))
    # social
    social = DP_BRAND / "social"
    jobs.append(svg_png_job("band-of-one-app-icon.svg", social / "avatar-400.png", 400, 400))
    for name, w, h, hs, ss, sub in [
        ("linkedin-banner-1584x396", 1584, 396, 40, 18, True),
        ("x-header-1500x500", 1500, 500, 46, 20, True),
        ("facebook-cover-1640x624", 1640, 624, 52, 22, True),
    ]:
        p = write_html(f"{name}.html", banner_html(w, h, hs, ss, sub))
        jobs.append({"html": p, "out": social / f"{name}.png", "type": "png", "width": w, "height": h})
    p = write_html("og-default.html", og_html())
    jobs.append({"html": p, "out": social / "og-default-1200x630.png", "type": "png", "width": 1200, "height": 630})
    p = write_html("brand-board.html", brand_board_html())
    jobs.append({"html": p, "out": DP_BRAND / "Brand_Board.png", "type": "png", "width": 1600, "height": 1000})
    run(jobs)

    # YouTube: text must sit inside the centered 1546x423 safe area
    p = write_html("youtube-safe.html", banner_html(2560, 1440, 60, 26, True, left=560, maxw=1300))
    run([{"html": p, "out": social / "youtube-banner-2560x1440.png", "type": "png", "width": 2560, "height": 1440}])

    # fonts + licenses
    fonts_dir = DP_BRAND / "fonts"
    fonts_dir.mkdir(exist_ok=True)
    for fam, weights in [("fraunces", ["400Regular", "400Regular_Italic", "600SemiBold", "700Bold"]),
                         ("inter", ["400Regular", "500Medium", "600SemiBold", "700Bold"]),
                         ("mono", ["400Regular", "600SemiBold"])]:
        for w in weights:
            src = ttf(fam, w)
            shutil.copy(src, fonts_dir / src.name)
    nm = ROOT / "Build_Tools" / "node_modules" / "@expo-google-fonts"
    shutil.copy(nm / "fraunces" / "LICENSE_FONT", fonts_dir / "OFL-Fraunces.txt")
    shutil.copy(nm / "inter" / "LICENSE_FONT", fonts_dir / "OFL-Inter.txt")
    shutil.copy(nm / "jetbrains-mono" / "LICENSE_FONT", fonts_dir / "OFL-JetBrainsMono.txt")
    (fonts_dir / "README.txt").write_text(
        "Brand fonts (SIL Open Font License 1.1 - free for commercial use, embedding and redistribution).\n"
        "Install them (double-click each .ttf) so the editable DOCX/XLSX files display as designed.\n"
        "Original sources: Google Fonts (fonts.google.com) - Fraunces, Inter, JetBrains Mono.\n"
    )

    # mirror to content business branding folder
    for sub in ("logo", "social", "fonts"):
        dst = CA_BRAND / sub
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(DP_BRAND / sub, dst)
    shutil.copy(DP_BRAND / "Brand_Board.png", CA_BRAND / "Brand_Board.png")
    print("brand assets done")


if __name__ == "__main__":
    build()

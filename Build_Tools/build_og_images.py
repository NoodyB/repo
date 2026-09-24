"""Social share (Open Graph) images, 1200x630, one per article + a site default.

Reads front matter from Content_Automation_Business/04_Blog_Articles/*.md.
Run: python3 Build_Tools/build_og_images.py [slug ...]   (no args = all articles)
"""
import html
import shutil
import sys

import yaml

from brand import COLORS as C, ROOT, font_face_css
from render import run, write_html

ARTICLES = ROOT / "Content_Automation_Business" / "04_Blog_Articles"
OUT = ROOT / "Content_Automation_Business" / "03_Website" / "src" / "assets" / "og"
LOGO = (ROOT / "Content_Automation_Business/02_Branding/logo/band-of-one-horizontal-on-dark.svg").as_uri()
CATS = {"client-workflows": ("Client Workflows", C["orange"]), "getting-paid": ("Getting Paid", C["butter"]),
        "ai-done-right": ("AI, Done Right", C["mist"]), "systems-sops": ("Systems & SOPs", "#8FC7BE"),
        "tools-honestly": ("Tools, Honestly", C["rust"])}


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def card(title, cat, badge):
    name, ring = CATS.get(cat, ("Band of One", C["orange"]))
    size = 64 if len(title) < 60 else (56 if len(title) < 80 else 48)
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_face_css()}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:{C['ink']};color:{C['paper']};font-family:Inter,sans-serif}}
.ring{{position:absolute;right:-170px;top:250px;width:560px;height:560px;border-radius:50%;border:44px solid {ring}}}
.disc{{position:absolute;right:-60px;top:360px;width:340px;height:340px;border-radius:50%;background:{C['teal']}}}
.wrap{{position:absolute;left:72px;top:64px;right:250px}}
.cat{{font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:20px;color:{C['butter']}}}
h1{{font-family:Fraunces,serif;font-weight:700;font-size:{size}px;line-height:1.08;letter-spacing:-.015em;margin:22px 0 0}}
.badge{{display:inline-block;margin-left:14px;font-size:16px;letter-spacing:.08em;padding:4px 12px;border-radius:999px;background:{C['mist']};color:{C['deep_teal']}}}
.logo{{position:absolute;left:72px;bottom:54px;height:44px}}
</style></head><body><div class="ring"></div><div class="disc"></div>
<div class="wrap"><div class="cat">{html.escape(name)}{badge_html}</div><h1>{html.escape(title)}</h1></div>
<img class="logo" src="{LOGO}"></body></html>"""


def main(slugs=None):
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = []
    for f in sorted(ARTICLES.glob("*.md")):
        if f.name == "README.md":
            continue
        fm = front_matter(f)
        if slugs and fm["slug"] not in slugs:
            continue
        badge = {"tested": "TESTED", "researched": "RESEARCHED"}.get(fm.get("review_type"), "")
        jobs.append({"html": write_html(f"og_{fm['slug']}.html", card(fm["title"], fm["category"], badge)),
                     "out": OUT / f"{fm['slug']}.png", "type": "png", "width": 1200, "height": 630, "scale": 1})
    run(jobs)
    shutil.copy(ROOT / "Content_Automation_Business/02_Branding/social/og-default-1200x630.png", OUT / "default.png")
    print(f"{len(jobs)} article images + default -> {OUT}")


if __name__ == "__main__":
    main(sys.argv[1:] or None)

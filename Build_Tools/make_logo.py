"""Generate Band of One logo SVGs with all text converted to vector paths.

Outputs go to both brand folders so each business folder is self-contained.
Run:  python3 Build_Tools/make_logo.py
"""
import math
import shutil
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

from brand import COLORS, ROOT, ttf

OUT_DIRS = [
    ROOT / "Digital_Products_Business" / "02_Branding" / "logo",
    ROOT / "Content_Automation_Business" / "02_Branding" / "logo",
]


class Shaper:
    """Shape text with HarfBuzz (kerning + ligatures) and emit SVG path data."""

    def __init__(self, font_path: Path):
        self.font_path = font_path
        blob = hb.Blob.from_file_path(str(font_path))
        self.face = hb.Face(blob)
        self.hbfont = hb.Font(self.face)
        self.tt = TTFont(str(font_path))
        self.upem = self.tt["head"].unitsPerEm
        self.glyphset = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()

    def path(self, text: str, size: float, x: float, baseline: float, tracking: float = 0.0):
        """Return (svg_path_d, advance_width_px) for text at font-size `size`."""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {"kern": True, "liga": True})
        scale = size / self.upem
        pen = SVGPathPen(self.glyphset)
        cursor = 0.0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = self.order[info.codepoint]
            gx = x + (cursor + pos.x_offset) * scale
            gy = baseline - pos.y_offset * scale
            # font units are y-up; SVG is y-down
            tpen = TransformPen(pen, (scale, 0, 0, -scale, gx, gy))
            self.glyphset[name].draw(tpen)
            cursor += pos.x_advance + tracking * self.upem
        return pen.getCommands(), cursor * scale

    def bounds(self, text: str, size: float):
        from fontTools.pens.boundsPen import BoundsPen

        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {"kern": True})
        scale = size / self.upem
        bp = BoundsPen(self.glyphset)
        cursor = 0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = self.order[info.codepoint]
            tpen = TransformPen(bp, (scale, 0, 0, -scale, cursor * scale, 0))
            self.glyphset[name].draw(tpen)
            cursor += pos.x_advance
        return bp.bounds  # xMin, yMin(top, negative), xMax, yMax


def arc_path(cx, cy, r, start_deg, end_deg):
    """Clockwise SVG arc from start to end angle (degrees, 0 = +x axis, clockwise positive)."""
    def pt(a):
        rad = math.radians(a)
        return cx + r * math.cos(rad), cy + r * math.sin(rad)

    x1, y1 = pt(start_deg)
    x2, y2 = pt(end_deg)
    sweep = (end_deg - start_deg) % 360
    large = 1 if sweep > 180 else 0
    return f"M{x1:.2f} {y1:.2f} A{r} {r} 0 {large} 1 {x2:.2f} {y2:.2f}"


def mark_elements(ox=0.0, oy=0.0, size=128.0, circle_fill=None, ring=None, numeral=None):
    """Logo mark: a '1' held inside a band (open ring). Designed on a 128px grid."""
    circle_fill = circle_fill or COLORS["teal"]
    ring = ring or COLORS["orange"]
    numeral = numeral or COLORS["paper"]
    s = size / 128.0
    cx, cy = ox + 64 * s, oy + 64 * s
    one = Shaper(ttf("fraunces", "800ExtraBold"))
    fsize = 76 * s
    b = one.bounds("1", fsize)
    gw, gh = b[2] - b[0], b[3] - b[1]
    gx = cx - gw / 2 - b[0]
    gy = cy - (b[1] + gh / 2)  # baseline placement so glyph box is centered
    d, _ = one.path("1", fsize, gx, gy)
    return (
        f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{45 * s:.2f}" fill="{circle_fill}"/>'
        f'<path d="{arc_path(cx, cy, 56.5 * s, -32, 262)}" fill="none" stroke="{ring}" '
        f'stroke-width="{8.5 * s:.2f}" stroke-linecap="round"/>'
        f'<path d="{d}" fill="{numeral}"/>'
    )


def wordmark(x, baseline, size, color, of_color=None):
    """'Band of One' — Fraunces SemiBold with an italic 'of'. Returns (svg, width)."""
    of_color = of_color or COLORS["teal"]
    semi = Shaper(ttf("fraunces", "600SemiBold"))
    ital = Shaper(ttf("fraunces", "400Regular_Italic"))
    track = -0.01
    parts = []
    d1, w1 = semi.path("Band", size, x, baseline, track)
    space = size * 0.26
    d2, w2 = ital.path("of", size, x + w1 + space, baseline, track)
    d3, w3 = semi.path("One", size, x + w1 + space + w2 + space, baseline, track)
    parts.append(f'<path d="{d1}" fill="{color}"/>')
    parts.append(f'<path d="{d2}" fill="{of_color}"/>')
    parts.append(f'<path d="{d3}" fill="{color}"/>')
    return "".join(parts), w1 + space + w2 + space + w3


def svg(w, h, body, bg=None, title="Band of One"):
    bgrect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
        f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
        f"<title>{title}</title>{bgrect}{body}</svg>\n"
    )


def build():
    files = {}
    # 1. Mark only (transparent + app-icon style)
    files["band-of-one-mark.svg"] = svg(128, 128, mark_elements())
    files["band-of-one-app-icon.svg"] = svg(
        512, 512,
        f'<rect width="512" height="512" rx="112" fill="{COLORS["paper"]}"/>'
        + mark_elements(56, 56, 400),
    )
    files["band-of-one-mark-reversed.svg"] = svg(
        128, 128, mark_elements(ring=COLORS["butter"], circle_fill=COLORS["teal"]), bg=COLORS["ink"]
    )

    # 2. Horizontal lockup
    for variant, color, of_color, bg, ring in [
        ("", COLORS["ink"], COLORS["teal"], None, COLORS["orange"]),
        ("-reversed", COLORS["paper"], COLORS["butter"], COLORS["ink"], COLORS["butter"]),
    ]:
        wm, ww = wordmark(0, 0, 64, color, of_color)
        pad = 8
        mark_size = 112
        total_w = pad + mark_size + 26 + ww + pad
        total_h = mark_size + pad * 2
        baseline = pad + mark_size / 2 + 64 * 0.36
        wm, ww = wordmark(pad + mark_size + 26, baseline, 64, color, of_color)
        files[f"band-of-one-horizontal{variant}.svg"] = svg(
            total_w, total_h, mark_elements(pad, pad, mark_size, ring=ring) + wm, bg=bg
        )
        if variant:
            # transparent version for placing on dark artwork (covers, banners)
            files["band-of-one-horizontal-on-dark.svg"] = svg(
                total_w, total_h, mark_elements(pad, pad, mark_size, ring=ring) + wm
            )

    # 3. Stacked lockup
    wm_probe, ww = wordmark(0, 0, 56, COLORS["ink"])
    W = max(ww + 32, 240)
    mark_size = 150
    wm, ww = wordmark((W - ww) / 2, 16 + mark_size + 70, 56, COLORS["ink"])
    files["band-of-one-stacked.svg"] = svg(W, 16 + mark_size + 96, mark_elements((W - mark_size) / 2, 16, mark_size) + wm)

    # 4. Wordmark only
    wm, ww = wordmark(4, 60, 64, COLORS["ink"])
    files["band-of-one-wordmark.svg"] = svg(ww + 8, 80, wm)

    # 5. Favicon (simplified: no ring gap detail lost at 16px, thicker ring)
    files["favicon.svg"] = svg(64, 64, mark_elements(0, 0, 64))

    for out in OUT_DIRS:
        out.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (out / name).write_text(content)
    print(f"wrote {len(files)} SVGs to {len(OUT_DIRS)} folders")


if __name__ == "__main__":
    build()

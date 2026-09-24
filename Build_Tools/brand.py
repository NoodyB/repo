"""Band of One brand tokens shared by every build script.

Change a value here and re-run the generators to update logos, PDFs,
workbooks and images consistently.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "Build_Tools"
NODE_MODULES = BUILD / "node_modules"

BRAND_NAME = "Band of One"
TAGLINE = "Practical AI systems for businesses of one."
SHORT_TAGLINE = "For businesses of one."
WEBSITE_PLACEHOLDER = "bandofone.co"  # placeholder until you buy a domain
SUPPORT_EMAIL_PLACEHOLDER = "hello@bandofone.co"  # replace before launch

COLORS = {
    "ink": "#1B2430",        # primary text
    "paper": "#FBF8F3",      # page background
    "teal": "#0F6B64",       # primary brand color, links, buttons
    "deep_teal": "#0A4A45",  # dark surfaces, hover
    "mist": "#E3F1EE",       # light teal panels
    "orange": "#E8663D",     # decorative accent only (not for small text)
    "rust": "#B8471F",       # accessible accent for text/buttons
    "butter": "#F6C85F",     # highlights, badges
    "stone": "#E4DED3",      # borders, dividers
    "slate": "#56606B",      # secondary text
    "white": "#FFFFFF",
}

FONTS = {
    "display": "Fraunces",
    "body": "Inter",
    "mono": "JetBrains Mono",
}


def ttf(family: str, weight: str) -> Path:
    """Path to an OFL TTF shipped in @expo-google-fonts (e.g. ttf('fraunces', '600SemiBold'))."""
    pkg = {"fraunces": "fraunces", "inter": "inter", "mono": "jetbrains-mono"}[family]
    prefix = {"fraunces": "Fraunces", "inter": "Inter", "mono": "JetBrainsMono"}[family]
    return NODE_MODULES / "@expo-google-fonts" / pkg / weight / f"{prefix}_{weight}.ttf"


def font_face_css(base_url: str = None) -> str:
    """@font-face rules for HTML rendering. Uses local woff2 files from @fontsource."""
    fs = NODE_MODULES / "@fontsource"
    rules = []
    spec = [
        ("Fraunces", "fraunces", [(400, "normal"), (400, "italic"), (600, "normal"), (600, "italic"), (700, "normal"), (800, "normal")]),
        ("Inter", "inter", [(400, "normal"), (400, "italic"), (500, "normal"), (600, "normal"), (700, "normal"), (800, "normal")]),
        ("JetBrains Mono", "jetbrains-mono", [(400, "normal"), (600, "normal")]),
    ]
    for family, pkg, variants in spec:
        for weight, style in variants:
            f = fs / pkg / "files" / f"{pkg}-latin-{weight}-{style}.woff2"
            url = f.as_uri() if base_url is None else f"{base_url}/{f.name}"
            rules.append(
                f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
                f"font-display:swap;src:url('{url}') format('woff2');}}"
            )
    return "\n".join(rules)

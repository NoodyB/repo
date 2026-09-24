"""Build Brand Guidelines + name-check PDFs and copy them to both branding folders."""
import shutil
from pathlib import Path
from brand import ROOT
from docbuilder import build_pdf

DP = ROOT / "Digital_Products_Business" / "02_Branding"
CA = ROOT / "Content_Automation_Business" / "02_Branding"
EXTRA = ".sw{display:inline-block;width:26px;height:18px;border-radius:4px;border:1px solid rgba(0,0,0,.12);vertical-align:middle}"


def strip_front_matter(text):
    if text.startswith("---"):
        end = text.index("---", 3)
        return text[end + 3:].lstrip()
    return text


if __name__ == "__main__":
    md = (DP / "Brand_Guidelines.md").read_text()
    out = build_pdf(md, DP / "Brand_Guidelines.pdf",
                    {"title": "Brand Guidelines", "subtitle": "Identity, voice, color, type, logo and packaging for both Band of One businesses.",
                     "kicker": "Band of One · Version 1.0 · September 2026", "cover_note": "Working name, pending owner approval"},
                    extra_css=EXTRA, number_chapters=False)
    shutil.copy(out, CA / "Brand_Guidelines.pdf")
    shutil.copy(DP / "Brand_Guidelines.md", CA / "Brand_Guidelines.md")
    md2 = strip_front_matter((DP / "Brand_Name_Options_and_Conflict_Check.md").read_text())
    build_pdf(md2, DP / "Brand_Name_Options_and_Conflict_Check.pdf",
              {"title": "Brand Name Options & Conflict Check", "subtitle": "Five shortlisted names, the preliminary screen, and why Band of One was selected.",
               "kicker": "Band of One · Preliminary, not legal clearance"}, toc=False, number_chapters=False)
    print("ok")


def build_content_brand():
    md = (CA / "Content_Brand_Strategy.md").read_text()
    build_pdf(md, CA / "Content_Brand_Strategy.pdf",
              {"title": "Content Brand Strategy", "subtitle": "Shared-brand decision, audience profiles, editorial style guide, bios and visual rules for the content business.",
               "kicker": "Band of One · Content Business · v1.0"}, number_chapters=False)


if __name__ == "__main__":
    build_content_brand()

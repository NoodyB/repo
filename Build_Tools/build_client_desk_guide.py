"""Build the Client Desk user guide PDF (+ DOCX)."""
from brand import COLORS as C, ROOT
from covers import product_cover
from docbuilder import build_docx, build_pdf

D = ROOT / "Digital_Products_Business" / "04_Premium_Template"

if __name__ == "__main__":
    md = (D / "User_Guide_source.md").read_text()
    shot = (D / "screenshot_dashboard.png").as_uri()
    # insert a screenshot after the "What's inside" table
    md_pdf = md.replace("## The color key", f"![The Client Desk dashboard with sample data]({shot})\n\n## The color key", 1)
    cover = product_cover("The Workbook · Band of One", "The Client<br><em>Desk</em>",
                          "User guide for the solo business command center: clients, pipeline, invoices, reminders and your weekly review in one spreadsheet.",
                          ["Works in Excel, Google Sheets &amp; LibreOffice", "Automatic due dates &amp; reminder stages A–E", "Dashboard of next actions and overdue invoices",
                           "Admin audit with priority scoring", "Tested formulas, sample data included"],
                          ring=C["butter"], disc=C["teal"], big="$")
    extra = "img[alt^='The Client Desk dashboard']{width:100%;border:1px solid #E4DED3;border-radius:6px;margin:4pt 0 12pt}"
    build_pdf(md_pdf, D / "BandOfOne_The-Client-Desk_User-Guide_v1.0.pdf",
              {"title": "The Client Desk: User Guide", "subtitle": "", "footer_left": "The Client Desk · User Guide · v1.0 · Band of One"},
              cover_html=cover, extra_css=extra, number_chapters=False, include_h2=False)
    build_docx(md, D / "BandOfOne_The-Client-Desk_User-Guide_v1.0_editable.docx",
               {"title": "The Client Desk: User Guide", "subtitle": "Band of One · v1.0"})
    print("ok")

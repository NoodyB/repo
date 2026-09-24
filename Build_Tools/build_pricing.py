"""Build the pricing calculator workbook (live formulas) for the Gumroad storefront.

Run: python3 Build_Tools/build_pricing.py   (then recalc with the xlsx skill's recalc.py; the test does this)
"""
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

from brand import COLORS as C, ROOT

OUT = ROOT / "Digital_Products_Business" / "07_Gumroad_Storefront" / "BandOfOne_Pricing_Calculator.xlsx"

# (name, intro price, regular price, regular price of parts if bundle)
PRODUCTS = [
    ("A · The Solo Admin Playbook", 19, 24),
    ("B · The Client Desk", 24, 29),
    ("C · The Band of One Prompt Library", 15, 19),
    ("Bundle · All three products", 39, 49),
]
FEES_SOURCE = "Source: Gumroad Help, 'Gumroad's fees' (gumroad.com/help/article/66-gumroads-fees), checked 2026-09-24."

F = "Arial"
thin = Side(style="thin", color="D9D4CA")
B = Border(left=thin, right=thin, top=thin, bottom=thin)
HEAD = PatternFill("solid", fgColor=C["deep_teal"][1:])
INPUT = PatternFill("solid", fgColor="FFF8E1")
CALC = PatternFill("solid", fgColor="F2F2F2")
BLUE = Font(name=F, color="0000FF")
BLACK = Font(name=F)
GREEN = Font(name=F, color="008000")
USD = '$#,##0.00;($#,##0.00);"-"'
PCT = '0.0%;(0.0%);"-"'


def head(ws, row, labels, widths=None):
    for j, h in enumerate(labels):
        c = ws.cell(row=row, column=2 + j, value=h)
        c.font = Font(name=F, bold=True, color="FFFFFF")
        c.fill, c.border = HEAD, B
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    if widths:
        for j, w in enumerate(widths):
            ws.column_dimensions[chr(66 + j)].width = w


def main():
    wb = Workbook()
    a = wb.active
    a.title = "Assumptions"
    a.sheet_view.showGridLines = False
    a.column_dimensions["A"].width = 2
    a["B1"] = "Band of One: Pricing calculator"
    a["B1"].font = Font(name=F, bold=True, size=16, color=C["deep_teal"][1:])
    a["B2"] = "Blue text on yellow = inputs you can change. Black = formulas. Green = links to this sheet from other tabs. No sales forecasts: this workbook only does per-sale and break-even math."
    a["B2"].font = Font(name=F, italic=True, size=9, color=C["slate"][1:])
    head(a, 4, ["Assumption", "Value", "Notes / source"], [44, 12, 90])
    rows = [
        ("Gumroad fee on direct sales (percent)", 0.10, PCT, FEES_SOURCE),
        ("Gumroad fee on direct sales (fixed, per sale)", 0.50, USD, FEES_SOURCE),
        ("Card processing (percent)", 0.029, PCT, FEES_SOURCE + " PayPal fees differ; card rate used as the base case."),
        ("Card processing (fixed, per sale)", 0.30, USD, FEES_SOURCE),
        ("Gumroad Discover marketplace fee (flat, incl. processing)", 0.30, PCT, FEES_SOURCE + " Applies only to sales Gumroad's marketplace brings you."),
        ("Refund rate (assumption)", 0.05, PCT, "ASSUMPTION, not data: 5% of sales refunded. Replace with your real rate after 30+ sales (Dashboard → Refunds)."),
        ("Affiliate commission (if an affiliate made the sale)", 0.0, PCT, "0% by default. Gumroad lets you set 1–75%; fees are shared in proportion (gumroad.com/help/article/333). Try 30% to see the effect."),
        ("Monthly tool costs to cover", 0.0, USD, "Launch plan costs $0/month. Example: MailerLite Comfort is $10.80/mo billed yearly for 500 subscribers (mailerlite.com/pricing, checked 2026-09-24)."),
    ]
    for k, (label, val, fmt, note) in enumerate(rows):
        r = 5 + k
        a[f"B{r}"], a[f"C{r}"], a[f"D{r}"] = label, val, note
        a[f"B{r}"].font, a[f"D{r}"].font = BLACK, Font(name=F, size=9, color=C["slate"][1:])
        a[f"C{r}"].font, a[f"C{r}"].fill, a[f"C{r}"].number_format = BLUE, INPUT, fmt
        a[f"D{r}"].alignment = Alignment(wrap_text=True, vertical="top")
        for col in "BCD":
            a[f"{col}{r}"].border = B
    a["C10"].comment = Comment("Assumption only. Replace with your observed refund rate once you have real sales.", "Band of One")
    a["B14"] = ("Refund math used: Gumroad returns its own fee on the refunded amount but keeps the card-processing portion "
                "(same source). So a refunded sale costs you the processing fee.")
    a["B14"].font = Font(name=F, size=9, italic=True, color=C["slate"][1:])
    a["B15"] = ("Sales tax/VAT: the calculator treats your price as tax-exclusive revenue. Check Gumroad's current tax help pages for how tax "
                "is collected in your buyers' locations.")
    a["B15"].font = Font(name=F, size=9, italic=True, color=C["slate"][1:])

    s = wb.create_sheet("Per-sale math")
    s.sheet_view.showGridLines = False
    s.column_dimensions["A"].width = 2
    s["B1"] = "What you keep from one sale"
    s["B1"].font = Font(name=F, bold=True, size=14, color=C["deep_teal"][1:])
    s["B2"] = "Prices are inputs (blue on yellow). Everything else is calculated from the Assumptions tab."
    s["B2"].font = Font(name=F, italic=True, size=9, color=C["slate"][1:])
    labels = ["Product", "Price tier", "Price", "Gumroad fee", "Processing", "Net: direct sale", "Fees as % of price",
              "Net: Discover sale", "Expected net per sale after refunds", "Net if affiliate sale", "Sales/month to cover tools"]
    head(s, 4, labels, [34, 11, 10, 11, 11, 12, 11, 12, 14, 12, 12])
    s.row_dimensions[4].height = 44
    r = 5
    for name, intro, regular in PRODUCTS:
        for tier, price in (("Intro", intro), ("Regular", regular)):
            s[f"B{r}"], s[f"C{r}"], s[f"D{r}"] = name, tier, price
            s[f"D{r}"].font, s[f"D{r}"].fill = BLUE, INPUT
            s[f"E{r}"] = f"=D{r}*Assumptions!$C$5+Assumptions!$C$6"
            s[f"F{r}"] = f"=D{r}*Assumptions!$C$7+Assumptions!$C$8"
            s[f"G{r}"] = f"=D{r}-E{r}-F{r}"
            s[f"H{r}"] = f"=IF(D{r}=0,0,(E{r}+F{r})/D{r})"
            s[f"I{r}"] = f"=D{r}*(1-Assumptions!$C$9)"
            # refunded share loses the processing fee; kept share keeps the net
            s[f"J{r}"] = f"=(1-Assumptions!$C$10)*G{r}-Assumptions!$C$10*F{r}"
            s[f"K{r}"] = f"=G{r}*(1-Assumptions!$C$11)"
            s[f"L{r}"] = f'=IF(Assumptions!$C$12=0,0,IF(J{r}<=0,"n/a",ROUNDUP(Assumptions!$C$12/J{r},0)))'
            for col in "BCDEFGHIJKL":
                c = s[f"{col}{r}"]
                c.border = B
                if col not in "BCD":
                    c.fill = CALC
                    c.font = BLACK
                if col in "DEFGIJK":
                    c.number_format = USD
            s[f"H{r}"].number_format = PCT
            s[f"B{r}"].font = Font(name=F, bold=tier == "Intro")
            r += 1
    last = r - 1
    s[f"B{r + 1}"] = "Bundle saving vs. buying all three separately"
    s[f"B{r + 1}"].font = Font(name=F, bold=True)
    s[f"C{r + 2}"], s[f"C{r + 3}"] = "Intro", "Regular"
    s[f"D{r + 2}"] = "=(D5+D7+D9)-D11"
    s[f"D{r + 3}"] = "=(D6+D8+D10)-D12"
    s[f"E{r + 2}"] = "=IF((D5+D7+D9)=0,0,D{0}/(D5+D7+D9))".format(r + 2)
    s[f"E{r + 3}"] = "=IF((D6+D8+D10)=0,0,D{0}/(D6+D8+D10))".format(r + 3)
    for rr in (r + 2, r + 3):
        s[f"D{rr}"].number_format, s[f"E{rr}"].number_format = USD, PCT
        s[f"F{rr}"] = "saved / % off"
        s[f"F{rr}"].font = Font(name=F, size=9, color=C["slate"][1:])
    s.freeze_panes = "D5"

    # Price comparison evidence (static observations, dated)
    e = wb.create_sheet("Market price evidence")
    e.column_dimensions["A"].width = 2
    e["B1"] = "Observed prices of comparable listings (snapshot 2026-09-24; Etsy prices can include temporary sales)"
    e["B1"].font = Font(name=F, bold=True, size=12, color=C["deep_teal"][1:])
    head(e, 3, ["Comparable to", "Listing (as shown)", "Price shown (USD)", "Where"], [22, 70, 16, 40])
    ev = [
        ("C · Prompt Library", "100 AI Prompts for Etsy Sellers | ChatGPT Claude Gemini Prompt Pack", 5.49, "Etsy search 'chatgpt prompts small business'"),
        ("C · Prompt Library", "ChatGPT Prompts for Work & Business (100)", 8.99, "Etsy search 'chatgpt prompts small business'"),
        ("C · Prompt Library", "Claude AI Skill Pack | 1000 Skills for Small Business", 14.67, "Etsy search 'chatgpt prompts small business'"),
        ("C · Prompt Library", "ChatGPT Prompts for Small Business 210+ AI Automation Templates", 19.00, "Etsy search 'chatgpt prompts small business'"),
        ("B · Client Desk", "Client Tracker Excel CRM (inDeoDesignStudio)", 18.71, "Etsy search 'freelance client tracker spreadsheet'"),
        ("B · Client Desk", "Notion Freelancer Template CRM (GraceAndGrow)", 23.55, "Etsy search 'freelance client tracker spreadsheet'"),
        ("B · Client Desk", "Real estate transaction tracker", 24.99, "Etsy search 'freelance client tracker spreadsheet'"),
        ("A · Playbook / Bundle", "Client onboarding Canva bundle (AmmaRoseDesigns)", 37.00, "Etsy search 'client onboarding template freelancer'"),
        ("A · Playbook / Bundle", "Creative Business Hub (Notion)", 97.00, "Etsy search 'client onboarding template freelancer'"),
    ]
    for k, row in enumerate(ev):
        for j, v in enumerate(row):
            c = e.cell(row=4 + k, column=2 + j, value=v)
            c.font, c.border = Font(name=F, size=10), B
        e.cell(row=4 + k, column=4).number_format = USD
    e[f"B{5 + len(ev)}"] = "Full list: Digital_Products_Business/01_Market_Research/Marketplace_Observations_2026-09-24.csv"
    e[f"B{5 + len(ev)}"].font = Font(name=F, size=9, italic=True, color=C["slate"][1:])
    for ws in wb.worksheets:
        ws.sheet_properties.tabColor = C["teal"][1:]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(OUT, "rows", 5, "to", last)


if __name__ == "__main__":
    main()

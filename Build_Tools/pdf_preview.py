"""Render PDF pages into a single contact-sheet PNG for quick visual QA.

python3 pdf_preview.py file.pdf out.png [first_page] [count] [cols]
"""
import sys
import pypdfium2 as pdfium
from PIL import Image


def contact_sheet(pdf, out, first=1, count=6, cols=3, width=520):
    doc = pdfium.PdfDocument(pdf)
    n = len(doc)
    pages = list(range(first - 1, min(n, first - 1 + count)))
    imgs = []
    for i in pages:
        page = doc[i]
        scale = width / page.get_width()
        imgs.append(page.render(scale=scale).to_pil().convert("RGB"))
    if not imgs:
        raise SystemExit("no pages")
    h = max(im.height for im in imgs)
    rows = (len(imgs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (width + 16) + 16, rows * (h + 16) + 16), (200, 200, 200))
    for k, im in enumerate(imgs):
        r, c = divmod(k, cols)
        sheet.paste(im, (16 + c * (width + 16), 16 + r * (h + 16)))
    sheet.save(out)
    print(f"{pdf}: {n} pages; sheet -> {out}")


if __name__ == "__main__":
    a = sys.argv
    contact_sheet(a[1], a[2], int(a[3]) if len(a) > 3 else 1, int(a[4]) if len(a) > 4 else 6, int(a[5]) if len(a) > 5 else 3)

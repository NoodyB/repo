"""Verify customer ZIPs: integrity, required files, every file opens, no build/source files leak in.

Run: python3 Build_Tools/tests/test_packages.py
"""
import csv
import io
import sys
import zipfile
from pathlib import Path

from docx import Document
from openpyxl import load_workbook
from pypdf import PdfReader

OUT = Path(__file__).resolve().parents[2] / "Digital_Products_Business" / "06_Customer_Ready_Products"
REQUIRED = {"START-HERE.pdf", "LICENSE.txt", "CHANGELOG.md"}
FORBIDDEN = (".py", ".yaml", ".js", ".env", ".DS_Store", "__pycache__", "source/")
EXPECTED_COUNTS = {"Solo-Admin-Playbook": 5, "The-Client-Desk": 5, "Prompt-Library": 8, "Complete-Bundle": 21}

fails = 0


def check(ok, msg):
    global fails
    fails += not ok
    print("PASS" if ok else "FAIL", msg)


for z in sorted(OUT.glob("*.zip")):
    with zipfile.ZipFile(z) as zz:
        check(zz.testzip() is None, f"{z.name}: CRC ok")
        names = [n for n in zz.namelist() if not n.endswith("/")]
        top = {n.split("/")[0] for n in names}
        check(len(top) == 1, f"{z.name}: single top-level folder {top}")
        base = {n.split("/", 1)[1] for n in names}
        check(REQUIRED <= base, f"{z.name}: START-HERE, LICENSE, CHANGELOG at top level")
        check(not any(f in n for n in names for f in FORBIDDEN), f"{z.name}: no source/build files")
        key = next(k for k in EXPECTED_COUNTS if k in z.name)
        check(len(names) == EXPECTED_COUNTS[key], f"{z.name}: {len(names)} files (expected {EXPECTED_COUNTS[key]})")
        for n in names:
            data = zz.read(n)
            try:
                if n.endswith(".pdf"):
                    ok = len(PdfReader(io.BytesIO(data)).pages) > 0
                elif n.endswith(".xlsx"):
                    wb = load_workbook(io.BytesIO(data), data_only=True)
                    ok = len(wb.sheetnames) >= 4
                elif n.endswith(".docx"):
                    ok = len(Document(io.BytesIO(data)).paragraphs) > 50
                elif n.endswith(".csv"):
                    ok = len(list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))) == 100
                else:
                    text = data.decode("utf-8")
                    ok = len(text) > 100 and "add before launch" not in text
            except Exception as e:  # noqa: BLE001
                ok = False
                print("   ", n, e)
            if not ok:
                check(False, f"{z.name}: {n} opens")
        print(f"     {z.name}: all {len(names)} files opened")

print(f"\n{'ALL PASSED' if not fails else f'{fails} FAILURE(S)'}")
sys.exit(1 if fails else 0)

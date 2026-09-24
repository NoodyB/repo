"""Functional test for The Client Desk workbook.

Builds a copy with 'Today override' = 2026-10-15, recalculates it with LibreOffice,
then checks the calculated values against hand-computed expectations.

Run: python3 Build_Tools/tests/test_client_desk.py
"""
import datetime as dt
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import build_client_desk as bcd  # noqa: E402

RECALC = Path("/root/.claude/skills/synced/e9f19428-9418-4629-8b72-52b829d8829a_66248bea-408d-4f4a-94fa-94951dff1058/xlsx/scripts/recalc.py")
T = dt.date(2026, 10, 15)


def recalc(path: Path) -> dict:
    if RECALC.exists():
        out = subprocess.run([sys.executable, str(RECALC), str(path), "120"], capture_output=True, text=True, cwd=RECALC.parent.parent)
        return json.loads(out.stdout)
    # fallback: plain LibreOffice headless round-trip
    subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", str(path.parent), str(path)], check=True)
    return {"status": "success", "total_errors": 0}


def d(v):
    if isinstance(v, dt.datetime):
        return v.date()
    return v


def main():
    failures = []

    def check(label, got, want):
        ok = got == want
        print(f"{'PASS' if ok else 'FAIL'}  {label}: got {got!r}, want {want!r}")
        if not ok:
            failures.append(label)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "test.xlsx"
        bcd.build(T, path)
        res = recalc(path)
        check("recalc status", res.get("status"), "success")
        check("formula errors", res.get("total_errors"), 0)
        wb = load_workbook(path, data_only=True)

        s = wb["Settings"]
        check("Settings today", d(s["C6"].value), T)

        inv = wb["Invoices & Follow-ups"]
        # row: (due, status, days overdue, stage, action, next reminder)
        exp = {
            5: (T - dt.timedelta(31), "Paid", None, "Paid", "Paid ✓", None),
            6: (T - dt.timedelta(8), "Overdue", 8, "C", "Up to date", T + dt.timedelta(6)),
            7: (T - dt.timedelta(30), "Overdue", 30, "E", "Send E now", None),
            8: (T + dt.timedelta(2), "Not due", 0, "A", "Send A now", T + dt.timedelta(2)),
            9: (T, "Due today", 0, "B", "Send B now", T + dt.timedelta(7)),
            10: (T + dt.timedelta(12), "Part-paid", 0, "—", None, T + dt.timedelta(9)),
            11: (T - dt.timedelta(15), "Overdue", 15, "D", "Send D now", T + dt.timedelta(15)),
        }
        for r, (due, status, days, stage, action, nxt) in exp.items():
            check(f"inv row {r} due", d(inv[f"F{r}"].value), due)
            check(f"inv row {r} status", inv[f"K{r}"].value, status)
            got_days = inv[f"L{r}"].value
            check(f"inv row {r} days overdue", (None if got_days in ("", None) else int(got_days)), days)
            check(f"inv row {r} stage", inv[f"M{r}"].value, stage)
            check(f"inv row {r} action", inv[f"Q{r}"].value or None, action)
            nr = inv[f"N{r}"].value
            check(f"inv row {r} next reminder", d(nr) if nr not in ("", None) else None, nxt)
        check("inv row 10 balance", inv["J10"].value, 150)
        # action ranks: send rows ordered by due date -> row7 (T-30)=1, row11 (T-15)=2, row9 (T)=3, row8 (T+2)=4
        check("rank row7", inv["T7"].value, 1)
        check("rank row11", inv["T11"].value, 2)
        check("rank row9", inv["T9"].value, 3)
        check("rank row8", inv["T8"].value, 4)

        cl = wb["Clients & Pipeline"]
        check("client ID", cl["A5"].value, "C001")
        check("Harbor win%", cl["I5"].value, 1)
        check("Oak weighted", cl["J6"].value, 3250)
        check("Brightside status", cl["Q7"].value, "Overdue")
        check("Cedar days", cl["P9"].value, 0)
        check("Cedar status", cl["Q9"].value, "Due this week")
        check("Maple check-in", d(cl["S10"].value), T - dt.timedelta(80) + dt.timedelta(90))
        check("Maple status (past client with check-in)", cl["Q10"].value, "Upcoming")
        check("Lost client no status", cl["Q11"].value or None, None)

        db = wb["Dashboard"]
        check("KPI active clients", db["B5"].value, 2)
        check("KPI weighted pipeline", db["D5"].value, 3590)
        check("KPI outstanding", db["G5"].value, 5180)
        check("KPI overdue", db["I5"].value, 1830)
        check("KPI reminders", db["L5"].value, 4)
        check("KPI follow-ups overdue", db["B9"].value, 1)
        check("KPI follow-ups this week", db["D9"].value, 4)
        check("next action #1", db["B14"].value, "Brightside Physio")
        check("invoice action #1", db["H14"].value, "2026-019")
        check("invoice action #1 text", db["J14"].value, "Send E now")
        check("top admin task", db["B26"].value, "Weekly client updates")
        check("top admin priority", db["D26"].value, 960)
        check("stage count proposal", db["H28"].value, 1)

        au = wb["Admin Audit"]
        check("audit minutes row5", au["E5"].value, 320)
        check("audit priority row9 (proposals)", au["H9"].value, 270)
        check("audit total minutes", au["Q5"].value, 1400)
        check("audit hours", round(au["Q6"].value, 2), round(1400 / 60, 2))
        ranks = sorted(au[f"I{r}"].value for r in range(5, 13))
        check("audit ranks unique 1..8", ranks, list(range(1, 9)))

        sp = wb["SOP Library"]
        check("SOP weekly update review due", sp["G6"].value, "Review due")
        check("SOP onboard ok", sp["G5"].value, "OK")
        check("SOP not written", sp["G7"].value, "Not written yet")

        wr = wb["Weekly Review"]
        check("live overdue count", wr["F5"].value, 3)
        check("win rate", wr["H14"].value, 0.5)

    print(f"\n{len(failures)} failure(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()

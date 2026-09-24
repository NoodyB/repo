---
title: "How to Track Invoices and Payment Reminders in Google Sheets or Excel (Tested Formulas)"
description: "Build an invoice tracker that calculates due dates, days overdue and the next payment reminder. Tested formulas for Google Sheets and Excel, plus a free file."
slug: track-invoices-in-a-spreadsheet
category: getting-paid
date: 2026-09-24
updated: 2026-09-24
review_type: tested
tested_note: "Formulas tested on 24 September 2026 by recalculating in LibreOffice Calc against eight scenarios with known answers (paid, not due, heads-up window, due today, 7/8, 15 and 45 days overdue). They use only functions available in Excel, Google Sheets and LibreOffice."
status: ready-for-review
tags: [spreadsheets, invoices, Google Sheets, Excel]
product_cta: desk
download: "/downloads/BandOfOne_Invoice-Tracker-Starter.xlsx"
related: [payment-reminder-schedule, what-to-include-on-an-invoice, spreadsheet-vs-notion-vs-crm]
sources:
  - title: "Bonsai, How often do freelancers get paid late? (updated Jan 2026)"
    url: "https://www.hellobonsai.com/blog/late-freelance-payment"
    accessed: 2026-09-24
---

You don't need accounting software to know which invoices need attention. A spreadsheet with a handful of formulas can tell you, every time you open it, what's due, what's overdue and which reminder to send next.

This tutorial builds that tracker step by step. The formulas work in **Google Sheets, Excel and LibreOffice**, and we tested them against eight scenarios before publishing. You can also [download the free starter file](/downloads/BandOfOne_Invoice-Tracker-Starter.xlsx) and skip to using it.

## What the tracker does

For each invoice you type a few details. The sheet calculates:

- The **due date**
- A **status**: Not due, Due today, Overdue or Paid
- **Days overdue**
- The **reminder stage due** (A–E), matching our [five-stage payment reminder schedule](/blog/payment-reminder-schedule/)
- An **action**: "Send C", "Up to date" and so on

## Step 1: Set up the columns

Put a "Today" cell at the top so every formula uses the same date:

- **A1:** `Today`
- **B1:** `=TODAY()`

Then headers in row 3 and your first invoice in row 4:

| Column | Header | You type or it calculates |
|---|---|---|
| A | Invoice # | type |
| B | Client | type |
| C | Amount | type |
| D | Issue date | type |
| E | Terms (days) | type (e.g., 14) |
| F | Due date | **formula** |
| G | Paid date | type when paid |
| H | Status | **formula** |
| I | Days overdue | **formula** |
| J | Reminder stage due | **formula** |
| K | Last reminder sent | type (A–E) when you send one |
| L | Action | **formula** |

**Tip:** color the "type" columns light yellow and the formula columns light grey, so it's obvious where to type.

## Step 2: Due date

In **F4**:

```text
=IF(D4="","",D4+E4)
```

If there's no issue date yet, the cell stays blank. Otherwise it adds the payment terms. Format column F as a date.

## Step 3: Status

In **H4**:

```text
=IF(D4="","",IF(G4<>"","Paid",IF($B$1<F4,"Not due",IF($B$1=F4,"Due today","Overdue"))))
```

The `$B$1` is the Today cell. The dollar signs keep it fixed when you copy the formula down.

## Step 4: Days overdue

In **I4**:

```text
=IF(OR(D4="",G4<>""),"",MAX(0,$B$1-F4))
```

Paid invoices show nothing, and invoices that aren't due yet show 0.

## Step 5: Which reminder is due

Our schedule has five stages: **A** three days before the due date, **B** on the due date, **C** 7 days overdue, **D** 14 days, **E** 30 days. In **J4**:

```text
=IF(OR(D4="",G4<>""),"",IF($B$1>=F4+30,"E",IF($B$1>=F4+14,"D",IF($B$1>=F4+7,"C",IF($B$1>=F4,"B",IF($B$1>=F4-3,"A","—"))))))
```

It checks from the latest stage backwards and returns the first one that applies. A dash means no reminder is due yet.

## Step 6: What to do now

When you send a reminder, type its letter in **column K**. Then in **L4**:

```text
=IF(OR(J4="",J4="—"),"",IF(K4="","Send "&J4,IF(CODE(J4)>CODE(K4),"Send "&J4,"Up to date")))
```

`CODE` turns a letter into a number, so the formula can tell that stage "D" comes after "C". If the stage due is later than the last one you sent, it says **Send D**; otherwise **Up to date**.

## Step 7: Copy down and highlight

Select F4:L4 and copy the formulas down as many rows as you need (the starter file has 50). Then add two conditional-formatting rules:

- **Status = "Overdue"** → light red fill
- **Action starts with "Send"** → light yellow fill (custom formula: `=LEFT($L4,4)="Send"`)

In Google Sheets: **Format → Conditional formatting**. In Excel: **Home → Conditional Formatting → New Rule → Use a formula**.

## How we tested it

We built the sheet with a fixed "today" date and eight invoices with known answers, then recalculated it in LibreOffice Calc and compared every result:

| Scenario | Expected status | Days overdue | Stage | Action |
|---|---|---|---|---|
| Paid before the due date | Paid | – | – | – |
| Due in 12 days | Not due | 0 | — | – |
| Due in 3 days | Not due | 0 | A | Send A |
| Due today, A already sent | Due today | 0 | B | Send B |
| 8 days late, C already sent | Overdue | 8 | C | Up to date |
| 15 days late, nothing sent | Overdue | 15 | D | Send D |
| 45 days late, D sent | Overdue | 45 | E | Send E |
| Exactly 7 days late, B sent | Overdue | 7 | C | Send C |

All eight matched, and empty rows stayed blank. The functions used (IF, OR, MAX, CODE, TODAY) are standard in Excel, Google Sheets and LibreOffice.

## Using it every week

Open the sheet during your [weekly admin review](/blog/weekly-admin-review/), filter or sort by **Action**, and send whatever says "Send". Then record the stage in column K. It takes minutes, and nothing slips. That matters, because late payment is common: Bonsai's data from over 100,000 freelancers found 29% of invoices were paid at least a day late (Bonsai, updated January 2026).

## When to outgrow it

A spreadsheet is enough for most solo businesses. Consider dedicated invoicing software when you need automatic reminders, online payments built in, or multi-currency accounting, or when your accountant asks for it. For a broader comparison, see [spreadsheet vs Notion vs CRM](/blog/spreadsheet-vs-notion-vs-crm/).

**Want the full version?** The free starter tracks invoices only. *The Client Desk* adds clients and pipeline, projects, a dashboard of what needs attention this week, and a weekly review, all built on the same tested approach.

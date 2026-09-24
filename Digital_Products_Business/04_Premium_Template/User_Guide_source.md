# Welcome to The Client Desk

**The Client Desk** is a single spreadsheet that runs the admin side of a one-person service business: clients and pipeline, projects, invoices, payment reminders, your admin audit, your prompt and SOP libraries, and a weekly review. It's the tracker that goes with *The Solo Admin Playbook*, but it works on its own too.

## What's inside

| Tab | What it does |
|---|---|
| **Start Here** | Setup steps and the color key |
| **Dashboard** | Everything that needs attention, calculated from the other tabs |
| **Clients & Pipeline** | One row per client or lead: stage, value, next action and date |
| **Projects** | Milestones, deposits and your weekly-update day |
| **Invoices & Follow-ups** | Due dates, status, days overdue and the next reminder stage (A–E) |
| **Admin Audit** | Your recurring admin tasks, scored and ranked by priority |
| **Prompt Log** | The AI prompts you actually use (IDs match the Band of One Prompt Library) |
| **SOP Library** | An index of your procedures and when each needs a review |
| **Weekly Review** | The 45-minute agenda, live numbers, and a weekly log |
| **Settings** | Business name, payment terms, currency label, dropdown lists and reminder timing |

## The color key

- **Yellow cells: type here.**
- **Grey cells: calculated.** Don't type over them.
- **Slate-colored headers: helper columns** the Dashboard needs. Leave them in place.

# Quick start (10 minutes)

## 1. Open the file

| App | How |
|---|---|
| **Microsoft Excel** (2010 or later, Windows or Mac) | Double-click the `.xlsx` file. If Excel shows "Protected View", click **Enable Editing**. |
| **Google Sheets** | Go to Google Drive → **New → File upload** → choose the file → open it → **File → Save as Google Sheets**. Work in the Google Sheets copy. |
| **LibreOffice Calc** | Open the file normally. |
| **Apple Numbers** | Not tested. We recommend Excel, Google Sheets or LibreOffice (all free options exist). |

!!! tip "Tested"
    Every formula was recalculated in LibreOffice and checked against hand-calculated expected values with an automated test (over 60 checks) before release. The workbook uses only widely supported functions (INDEX, MATCH, COUNTIFS, SUMIFS, RANK and so on) so it behaves the same in Excel and Google Sheets.

## 2. Settings

Open **Settings** and fill in:

- **Your business name**, shown on the Dashboard.
- **Default payment terms (days)**, used when an invoice's own terms cell is blank.
- **Currency code**, used as a label on the Dashboard (e.g., USD, GBP, EUR).
- **Weekly review day.**
- **Services list**, which feeds the Service dropdown on the Clients tab.

Leave **Today override** blank. The workbook then uses your computer's date.

## 3. Clear the sample business

The file comes with a fictional sample business so you can see how everything works. Every sample row says **SAMPLE** in its Notes column. To remove it:

1. On each tab, select the **yellow** cells of the sample rows.
2. Press **Delete** (or Backspace in Google Sheets).

**Don't delete whole rows.** That removes the formulas in the grey cells. If it happens anyway, see *Troubleshooting*.

!!! note "Why the sample dates always look current"
    Sample dates are formulas based on "today", so the demo always looks realistic. When you type your own dates, they replace those formulas.

## 4. Add your first client and invoice

- **Clients & Pipeline:** type the client name, choose a **Stage**, and always fill in **Next action** and **Next action date**. The Dashboard lists your next eight actions in date order.
- **Invoices & Follow-ups:** type the invoice number, pick the client, and enter the **Issue date** and **Amount**. Due date, status, days overdue and the reminder stage appear automatically.

That's it. Open the **Dashboard**.

# Tab by tab

## Dashboard

| Tile or section | Calculated from |
|---|---|
| Active clients | Clients in stages 4–6 (Onboarding, Delivery, Wrap-up) |
| Weighted pipeline | Project value × win % for stages 1–3 (the win % is an editable assumption on Settings) |
| Outstanding / Overdue | Unpaid invoice balances; overdue = past the due date |
| Reminders to send | Invoices where the current reminder stage is later than the last one you sent |
| Follow-ups overdue / this week | Client next-action dates before today / within 7 days |
| Invoiced / Collected this month | Invoice amounts by issue date; payments by paid date |
| Admin hours / month | Total from the Admin Audit |
| Next client actions | The 8 earliest next-action dates (excluding Lost clients) |
| Invoices needing a reminder | The 8 oldest invoices with a reminder due |
| Top admin tasks to fix first | The 3 highest priority scores from the Admin Audit |
| Clients by stage | Count and value per stage, with a chart |

## Clients & Pipeline

**Stages:** 1 Inquiry → 2 Discovery → 3 Proposal sent → 4 Onboarding → 5 Delivery → 6 Wrap-up & payment → 7 Past client (or Lost).

- **Group** is calculated: Pipeline (1–3), Active (4–6), Closed (7 and Lost).
- **Action status** is *Overdue* (date passed), *Due this week* (within 7 days) or *Upcoming*.
- **90-day check-in:** when a client moves to *7 · Past client* and you enter a **Project end date**, the check-in date appears automatically. Put "90-day check-in" as the next action so it shows on the Dashboard.

## Projects

Use one row per project. Enter the fee and deposit % and the deposit amount calculates. **Days to milestone** and the **Flag** column (Overdue / This week) help you plan. **Weekly update day** is a reminder of when each client expects their update (see Playbook Chapter 8).

## Invoices & Follow-ups

The reminder system follows the five-stage cadence from *The Solo Admin Playbook* (Chapter 9):

| Stage | Triggers (default) | Meaning |
|---|---|---|
| A | 3 days before the due date | Friendly heads-up |
| B | On the due date | "Due today" |
| C | 7 days overdue | Gentle nudge |
| D | 14 days overdue | Firm follow-up, offer a plan |
| E | 30 days overdue | Final notice (per your agreement) |

**How the Action column works:** the workbook works out which stage is due *today*. If you haven't logged that stage in **Last reminder sent**, the Action column says **"Send C now"** (for example). After you send it, choose **C** in *Last reminder sent* and enter the date; the action changes to **"Up to date"** until the next stage is due. **Next reminder date** tells you when that will be.

**Part payments:** enter what's been paid in **Amount paid**. The balance and status update (*Part-paid* while not yet due).

**Paid:** when **Amount paid** equals the amount, the status becomes **Paid** and reminders stop.

## Admin Audit

List every recurring admin task, then score it:

- **Repeatability:** 3 = nearly identical every time · 2 = similar · 1 = different every time.
- **Risk:** 1 = low stakes · 2 = money, client data or deadlines · 3 = legal, sensitive or relationship-critical.

**Priority score = (times per month × minutes each) × repeatability ÷ risk.** Rank 1 is where to start. Choose a **Decision** (Eliminate, Template, AI draft, Automate, Keep human) and note the prompt or template you'll use.

**Measuring savings honestly:** after you've changed how you do a task for a couple of weeks, re-estimate its minutes in **Minutes / month after**. Only then does the workbook show time saved. It never assumes a saving.

## Prompt Log

The 17 core prompts from the Playbook are pre-listed. Record where you saved each one, how often you use it, and your rating. The full set of 100 prompts is in *The Band of One Prompt Library* (sold separately); add any you use here.

## SOP Library

List each procedure, where it lives, when you last reviewed it and how often it should be reviewed (default 90 days). **Status** shows *Not written yet*, *OK* or *Review due*.

## Weekly Review

The agenda sits at the top. **Live numbers** (overdue invoices, reminders to send, follow-ups due) are calculated for you. Copy them into a new log row each week, add your estimate of admin hours, and note one improvement you made. After a few weeks, the log shows whether your system is working.

# Your weekly routine (15 minutes of the 45)

1. Open **Dashboard**.
2. **Next client actions:** send each follow-up (templates in the Playbook), then update that client's next action and date.
3. **Invoices needing a reminder:** send the stage shown (A–E), then log it in *Last reminder sent* and *Last reminder date*.
4. Record any payments (**Amount paid**, **Paid date**).
5. **Weekly Review** tab: copy the live numbers into a new log row.

# Customizing

| You want to… | Do this |
|---|---|
| Rename stages | Edit the text in **Settings → Client stages**. Keep eight stages; the group (Pipeline/Active/Closed) comes from the column beside it. |
| Change win % assumptions | Edit **Settings → Win probability**. |
| Change reminder timing | Edit **Settings → Days from due date** (e.g., make C = 10). |
| Add services or lead sources | Type them into the Settings lists (blank rows are provided for services). |
| Show a currency symbol | Select the money columns → Format → Number → Currency. |
| Add more rows | Select the last filled row, copy it, paste it into the rows below, then clear the yellow cells. |
| Use a different date format | Select the date columns → Format → Number → Date and pick your preferred format. |

# Troubleshooting & FAQ

**A grey cell shows a formula error or went blank after I typed in it.**
You typed over a formula. Copy the grey cell from the row above (Ctrl/Cmd + C) and paste it into the broken cell. Formulas adjust automatically.

**Dates show as numbers (e.g., 46310).**
Select the column → Format → Number → Date.

**The dropdowns don't appear in Google Sheets.**
Make sure you're working in the converted Google Sheets copy (**File → Save as Google Sheets**), not the uploaded .xlsx preview.

**The Dashboard's "as of" date is wrong.**
Check **Settings → Today override**. It should be blank for normal use.

**Can I sort or filter the tabs?**
Yes. Filters are switched on for the main tables. Sorting whole rows is fine because each row's formulas refer to that row.

**Is this accounting software?**
No. It's an organizer. Keep official financial records in the tools your accountant recommends, and follow your local invoicing requirements.

**Where is my data stored?**
Only where you save the file: your computer or your own cloud drive. The workbook doesn't connect to anything.

# License and support

**Personal business license:** the purchaser may use The Client Desk in their own business and adapt it freely for that business. You may not resell, share or redistribute the file, or pass it off as your own product. Full terms are in `LICENSE.txt`.

**Updates:** version 1.x updates are free through the store where you bought it.

**Support:** use the contact details on your purchase receipt or the product page. Please include which app you're using (Excel, Google Sheets or LibreOffice) and a screenshot of the issue with client details hidden.

*The Client Desk v1.0 · Band of One · September 2026*

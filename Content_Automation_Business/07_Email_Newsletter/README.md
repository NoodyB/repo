# 07 · Email newsletter

**Status: everything is drafted. No email account exists and nothing has been sent.** No contacts have been added. The list starts at zero and grows only through people who sign up themselves.

| File | What it is |
|---|---|
| `Welcome_and_Onboarding_Sequence.md` | Signup offer and consent wording, welcome email (delivers the kit), 5-email onboarding sequence (days 2, 4, 7, 10, 14), footer |
| `Weekly_Newsletter_Template_and_Promo_Email.md` | Weekly "one idea" template with rules and a filled example, plus an evergreen product promotion email |
| `Lead_Magnet/BandOfOne_Client-Admin-Starter-Kit_FREE.pdf` | The free lead magnet (10 prompts + weekly checklist, 10 pages). Also hosted at `/downloads/…` on the website, with a `noindex` header |
| `Subscriber_Import_Template.csv` | Column layout for importing **consented** subscribers only (e.g., when moving platforms) |
| Product launch emails | `Digital_Products_Business/08_Marketing_Campaign/Emails/Launch_Email_Sequence.md` (5 emails, sent in Month 2) |

## Platform choice: MailerLite Free to start

From the official pricing pages (checked 24 Sept 2026):

| | MailerLite Free | Kit Free |
|---|---|---|
| Subscribers | 250 | up to 10,000 |
| Emails | 2,500/month | unlimited broadcasts |
| Automations | 3 | visual automation builder and sequences **not** on free |
| Forms / landing pages | 3 forms, 1 landing page | unlimited |
| First paid tier | Comfort $10.80/mo billed yearly (500 subs) | Creator $33/mo billed yearly (1,000 subs) |

**Why MailerLite:** the welcome + onboarding sequence needs automation, and MailerLite's free plan includes it. **Capacity check (arithmetic, not a forecast):** at the 250-subscriber cap, 4 weekly issues use 1,000 of the 2,500 monthly sends, and each new subscriber's 6-email sequence uses 6 more. So the free plan fits until the list approaches the cap. **Switch or upgrade** when you pass ~200 subscribers: MailerLite Comfort, or Kit if you'd rather have a larger list and can pay for automations.

## Setup steps (you do these; needs your approval)

1. **Create a MailerLite account** with your business email. Complete their account approval steps (email platforms review new senders).
2. **Authenticate your sending domain** (SPF/DKIM records they give you, added in your DNS). This needs a domain, so buy the domain first. Unauthenticated sending tends to land in spam.
3. **Sender details:** "From" name *Band of One* or *[Your name] at Band of One*; a reply-to address you monitor; **your postal address** in the footer (CAN-SPAM requires a valid physical postal address; a registered PO box or private mailbox is acceptable, according to the FTC's compliance guide).
4. **Custom field:** `signup_source` (text). Name and email are built in.
5. **Groups:** `Newsletter` (everyone) and `Starter Kit` (signed up via the kit offer).
6. **Form:** create an embedded form or hosted landing page using the copy in `Welcome_and_Onboarding_Sequence.md`. Turn on **double opt-in**, add the consent line and privacy link, and set `signup_source` = `website-newsletter-form`. Add the subscriber to both groups.
7. **Starter kit link:** use the hosted PDF (`https://YOURDOMAIN/downloads/BandOfOne_Client-Admin-Starter-Kit_FREE.pdf`) as `[DOWNLOAD LINK]`.
8. **Automation** (1 of your 3 free automations):
   - Trigger: *subscriber joins group* `Starter Kit`
   - Email 0 (welcome) → wait 2 days → Email 1 → wait 2 days → Email 2 → wait 3 days → Email 3 → wait 3 days → Email 4 → wait 4 days → Email 5
   - Sends on days 0, 2, 4, 7, 10 and 14
9. **Test:** sign up with your own address. Check double opt-in, the welcome email, the download link, the unsubscribe link, the footer, and mobile rendering.
10. **Connect the website:** set `NEWSLETTER_URL` in `Build_Tools/launch_config.py` to the hosted form or landing page URL and rebuild. Every "Get the starter kit" button then points to it.

**Kit alternative:** the same structure works in Kit, with tags instead of groups and a "Sequence" for the onboarding emails, but sequences need a paid Kit plan.

## Importing subscribers (only with consent)

Use `Subscriber_Import_Template.csv` **only** for people who gave consent, for example when moving platforms. Keep the consent evidence columns (date, method, wording version). **Never import** clients, contacts, LinkedIn connections or anyone who didn't sign up.

## 12-week newsletter calendar

Weekly issue ("one idea a week"). Months follow the social calendar: Month 1 = content, Month 2 = product launch (launch emails are sent separately, see above), Month 3 = steady state.

| Week | Subject idea | The one idea | Go deeper |
|---|---|---|---|
| 1 | The 7-step onboarding checklist | Same steps, same order, every client | /blog/client-onboarding-checklist/ |
| 2 | One line that stops AI inventing details | `[NEED INFO]` and the other three guardrail lines | /blog/ai-prompts-for-client-emails/ |
| 3 | Decide your payment reminders once | A–E schedule | /blog/payment-reminder-schedule/ |
| 4 | Score your admin before you automate | Priority formula + 5 decisions | /blog/what-to-automate-first/ |
| 5 | Four headings that stop clients chasing you | Weekly client update | /blog/weekly-client-update-template/ |
| 6 | "Work starts once the deposit has cleared" | Deposits and milestones | /blog/deposits-and-payment-terms/ |
| 7 | A 7-field inquiry form | Intake form questions | /blog/client-intake-form-tools/ |
| 8 | Four numbers to track monthly | Admin hours, overdue, reply time, win rate | /blog/weekly-admin-review/ |
| 9 | Your first SOP in 20 minutes | SOP template + OPS-01 | /blog/sop-template-one-person-business/ |
| 10 | Training off ≠ nothing stored | AI privacy settings + redaction | /blog/client-data-privacy-ai/ |
| 11 | Scope creep: offer a choice | Two-option email | /blog/scope-creep-email-templates/ |
| 12 | One tool per job | Minimum tool stack review | /blog/minimum-tool-stack/ |

**Product mentions:** at most one issue in three, clearly labeled as our product. During the launch window (Month 2), the weekly issues stay purely educational so subscribers aren't sent two sales emails in one week.

## What to measure (record in `09_Business_Dashboard`)

Subscribers (total and new), unsubscribes, open and click rates per issue, clicks to articles and products, and replies. Don't compare against "industry benchmarks" without a source. Compare against your own previous weeks.

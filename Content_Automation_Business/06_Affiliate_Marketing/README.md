# 06 · Affiliate marketing

**Status: no applications submitted, no programs joined, no affiliate links anywhere.** Every link on the website draft goes to the tool's official page. Nothing here assumes you'll be accepted.

| File | What it is |
|---|---|
| `BandOfOne_Affiliate_Opportunities.xlsx` | 15 programs with terms captured from official pages on 24 Sept 2026 (commission, cookie, payout, approval, topics), an application tracker, a link placeholder map with formulas that block links until issued, disclosure language, and a list of programs that were closed or unverifiable |

## Which programs fit the content (and why)

Only programs for tools the articles **already discuss on their merits**:

| Priority | Programs | Relevant articles |
|---|---|---|
| 1: already mentioned in articles | MailerLite, Kit, beehiiv, Tally, Make, n8n, Notion | Newsletter comparison, tool stack, automation comparison, intake forms, client tracking |
| 2: future CRM/invoicing content | Dubsado, Bonsai, HoneyBook (referral) | Only if you write a researched or tested CRM comparison |
| 3: adjacent | Buffer, Descript, Hostinger, Amazon Associates | Only if matching content is written |

**Not available when checked:** Canva (program closed), Zapier (no public page found), Motion and Jotform (pages returned 404), ClickUp (unverifiable). Google Forms and the AI assistants have no programs we could find.

## When to apply

Many programs review your website before approving. Apply **after** the site is live with published articles, a working contact page, a privacy policy and the affiliate disclosure page. Applying with an empty site risks rejection.

## The rules (non-negotiable)

1. **No link until it's issued.** The workbook's "Issued link" column stays `[NOT ISSUED: do not use]` until a program gives you a link.
2. **Disclose before the first link**, and label every link "(affiliate link)". Set `affiliate: true` in the article's front matter, and the website adds the disclosure box automatically.
3. **Use `rel="sponsored"`** on affiliate links.
4. **Recommendations don't change.** If a non-affiliate or free option is better, the article says so.
5. **Read each program's terms.** Some forbid links in emails, paid ads or coupon sites, or require specific wording (Amazon does).
6. **Re-verify terms every 90 days.** The workbook flags stale entries in red.

Reference: FTC, ["FTC's Endorsement Guides: What People Are Asking"](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking).

## Reusable disclosure language

**Article (top, before the first link):**
> Disclosure: this article contains affiliate links, marked "(affiliate link)". If you buy through one, we may earn a commission at no extra cost to you. It never changes our recommendations.

**Comparison intro:**
> We're an affiliate for [TOOL A] and [TOOL B], which means we may earn a commission if you sign up through our links. We have no relationship with [TOOL C]. Our ratings are the same either way.

**Email:**
> This email contains an affiliate link to [TOOL]. If you sign up through it, I may earn a commission at no extra cost to you.

**Social post:**
> #ad: I earn a commission if you sign up through this link. I use/recommend it because [honest reason].

**Video:** say it out loud near the start *and* show it on screen.

**Own products:**
> This is a product we make and sell.

## How to add an issued link (step by step)

1. In the workbook, set **Status = Approved** and paste the link into **Issued link**.
2. Open the **Link Placeholder Map** tab. Rows whose Action says "Allowed" can be updated.
3. In each allowed article (`04_Blog_Articles/<slug>.md`): replace the official link with the issued link, add " (affiliate link)" after it, and set `affiliate: true` in the front matter.
4. Run the QA check (`08_Automation_Workflows`). It fails an article that has an affiliate-looking link without `affiliate: true`.
5. Approve and publish as usual.

## What this workbook does not do

It doesn't estimate commissions, conversion rates or earnings. There's no data to base them on yet. Record real clicks and commissions in the content dashboard (`09_Business_Dashboard`) once programs are active.

# The Band of One Prompt Library

100 AI prompts for client work and admin in a business of one. Version 1.0 · September 2026.

# How to use this library

These 100 prompts cover the admin of a service business from first inquiry to final invoice. Each one is built to produce a **specific, reusable output**, not a generic answer.

## Every prompt has the same parts

| Part | What it tells you |
|---|---|
| **Objective** | The job the prompt does |
| **When to use** | The moment in your week or client lifecycle it's for |
| **Inputs** | What you paste or fill in. `[PLACEHOLDERS]` are in square brackets and capitals |
| **Prompt** | The text to copy into your AI assistant |
| **Output** | What you should get back |
| **Tip** and **Pairs with** | How to get more from it, and related prompts |

## Five rules for great results

1. **Start with context.** Create your business brief (SET-01) and voice profile (SET-02) first. Paste them where a prompt says `[BUSINESS BRIEF]` or `[VOICE PROFILE]`, or save them as custom instructions (SET-04).
2. **Replace every placeholder.** If you don't have the information, delete that part of the prompt rather than leaving a placeholder for the AI to guess.
3. **Redact client details.** Replace names, emails, account numbers and anything confidential with placeholders before pasting. See SET-03 and check your assistant's data settings.
4. **You set prices, dates and promises.** The prompts tell the AI not to invent them. Check that it didn't.
5. **Edit before you send.** Read every draft for facts, promises, tone and one client-specific detail. AI drafts; you decide.

!!! tip "Works with any assistant"
    These prompts are written in plain language and work with ChatGPT, Claude, Gemini, Microsoft Copilot and similar assistants, including free tiers. Output quality varies by model and by how much context you provide.

Your download also includes a spreadsheet version with a **Search** tab, and a CSV you can import into Notion, Airtable or Google Sheets.


# Setup & Foundations

Give your AI assistant the context it needs, once: your business brief, your voice, and your privacy habits.

## SET-01 · Business brief builder

**Objective:** Create a one-page description of your business that you reuse as context in every other prompt.

**When to use:** Do this once when you start using AI for client admin; update it when your services or policies change.

**Inputs:**

- None: the AI interviews you

**Prompt:**

```text
Help me write a one-page "business brief" I can give an AI assistant before asking for help with client admin. Interview me with one question at a time (wait for each answer) covering: what I do and for whom; my 2–4 core services and typical project size; how I like to work (communication hours, response times, meeting preferences); my payment terms and policies; phrases or promises I never want used; and three examples of great client outcomes (described generally, no client names). When we're done, output the brief in this format: ## Who I am, ## Services, ## Ideal clients, ## How I work, ## Policies, ## Tone and words to avoid. Keep it under 450 words.
```

**Output:** A Markdown document with six headed sections, under 450 words.

**Tip:** Save the result in your assistant's custom instructions or project knowledge, or paste it at the start of each chat.

**Pairs with:** SET-02, SET-04

## SET-02 · Voice profile from writing samples

**Objective:** Capture how you write so AI drafts sound like you, not like a generic assistant.

**When to use:** After the business brief; refresh every few months.

**Inputs:**

- [NUMBER]: how many samples you're providing (3–5)
- [PASTE 3–5 REDACTED EMAILS]: emails you're happy with, names removed

**Prompt:**

```text
Below are [NUMBER] emails I wrote to clients (names removed). Analyze my writing style and produce a "voice profile" I can reuse in future prompts. Include: typical sentence length; greeting and sign-off habits; level of formality (1–5); words and phrases I use often; things I never do (e.g., exclamation marks, emojis, corporate phrases); how I deliver bad news; and 3 short "do this / not that" examples. Keep it under 250 words and don't invent traits that aren't in the samples.
"""[PASTE 3–5 REDACTED EMAILS]"""
```

**Output:** A short profile (≤250 words) with bullet points and 3 do/don't examples.

**Tip:** Choose emails that cover different situations (good news, a delay, a follow-up) so the profile is well-rounded.

**Pairs with:** SET-01

## SET-03 · Redaction check before pasting

**Objective:** Catch client names and sensitive details before you share text with an AI tool.

**When to use:** While you're building the redaction habit, or on long documents such as transcripts and threads.

**Inputs:**

- [PASTE TEXT]: the text you plan to use

**Prompt:**

```text
I'm about to paste text into an AI assistant. Act as a careful privacy reviewer. Scan the text between the triple quotes and list every item that could identify a person or company or expose sensitive data (names, emails, phone numbers, addresses, account numbers, prices tied to named clients, health/legal/HR details, passwords or links with tokens). Then return a redacted version that replaces each item with a clear placeholder like [CLIENT NAME] or [INVOICE AMOUNT]. Don't change anything else.
"""[PASTE TEXT]"""
```

**Output:** 1) A bulleted list of sensitive items found. 2) The full redacted text.

**Tip:** Running this inside the same assistant means the text has already been shared, so use it on text you've already partly redacted, or on non-confidential material while you learn.

**Pairs with:** SET-01

## SET-04 · Custom instructions writer

**Objective:** Turn your business brief and voice profile into compact standing instructions for your AI assistant.

**When to use:** When your assistant has a "custom instructions", "project instructions" or "personalization" field with a character limit.

**Inputs:**

- [BUSINESS BRIEF]
- [VOICE PROFILE]
- [CHARACTER LIMIT]: e.g., 1,500 characters

**Prompt:**

```text
Using my business brief and voice profile below, write standing instructions for my AI assistant in under [CHARACTER LIMIT] characters. Split them into two parts: (1) "What you should know about me" (business facts, services, policies) and (2) "How you should respond" (tone, format preferences, rules). Always include these rules: never invent prices, dates or facts about clients; mark missing information as [NEED INFO]; keep client emails under 200 words unless I ask otherwise; suggest one clarifying question when my request is ambiguous. Count the characters and confirm the total.
Business brief: """[BUSINESS BRIEF]"""
Voice profile: """[VOICE PROFILE]"""
```

**Output:** Two labeled blocks of plain text plus a character count.

**Tip:** Test the instructions with one real task (e.g., LEAD-01) and tweak.

**Pairs with:** SET-01, SET-02

## SET-05 · Service menu clarifier

**Objective:** Describe each of your services clearly, with who it's for, what's included, and what's not.

**When to use:** Before writing proposals or a services page; when clients keep misunderstanding what you offer.

**Inputs:**

- [SERVICES]: rough notes on each service
- [IDEAL CLIENT]

**Prompt:**

```text
I'm a [PROFESSION] serving [IDEAL CLIENT]. Here are rough notes about my services: """[SERVICES]""". For each service, produce: a plain-language name; a one-sentence promise focused on the client's outcome; who it's for and not for; what's included (bullets); what's not included (bullets); typical timeline; what I need from the client. Keep prices exactly as I wrote them; if I didn't give a price, write [PRICE]. Then point out any overlaps or gaps between services that could confuse a buyer.
```

**Output:** One block per service with consistent headings, then a short "overlaps and gaps" list.

**Tip:** Reuse the "not included" bullets in your proposals (PROP-06).

**Pairs with:** PROP-06, MKT-05

## SET-06 · Client FAQ builder

**Objective:** Build a set of answers to the questions clients ask again and again.

**When to use:** When you notice you're typing the same explanations; before creating an onboarding packet.

**Inputs:**

- [REPEATED QUESTIONS]: questions clients often ask
- [BUSINESS BRIEF]

**Prompt:**

```text
Using my business brief """[BUSINESS BRIEF]""", draft clear answers to these frequently asked client questions: """[REPEATED QUESTIONS]""". For each: a direct answer in 2–4 sentences in my voice, any policy it depends on, and where the answer should live (proposal, welcome email, onboarding doc, website FAQ). If my brief doesn't contain the information needed, write [NEED INFO: what's missing] instead of guessing. Add up to 5 more questions clients in my field commonly ask that I haven't listed.
```

**Output:** A table with columns Question, Answer, Depends on, Where it lives; then a list of suggested extra questions.

**Tip:** Paste the finished FAQ into your onboarding document and link it in your welcome email.

**Pairs with:** ONB-04

## SET-07 · Communication policy writer

**Objective:** Write a friendly, clear policy for response times, channels, meetings and feedback rounds.

**When to use:** Before onboarding new clients, or when boundaries have been slipping.

**Inputs:**

- [WORKING HOURS]
- [RESPONSE TIME]
- [CHANNELS]: e.g., email for decisions, Slack for quick questions
- [FEEDBACK ROUNDS]

**Prompt:**

```text
Write a short "How we'll work together" section for my client onboarding materials. Details: working hours [WORKING HOURS]; typical response time [RESPONSE TIME]; channels [CHANNELS]; meetings [MEETING PREFERENCES]; feedback process [FEEDBACK ROUNDS]; urgent issues [HOW TO FLAG URGENT]. Make it warm and confident, not defensive. Explain the reason behind each norm in one short clause (e.g., "so nothing gets lost"). Under 200 words, using bullets.
```

**Output:** A heading plus 5–7 bullets, under 200 words.

**Tip:** Put this in your welcome email (ONB-01) and your onboarding document.

**Pairs with:** ONB-01, ONB-04

## SET-08 · Tool stack audit

**Objective:** Find overlapping or unused software and decide what to keep, replace or cancel.

**When to use:** Quarterly, or when subscription costs creep up.

**Inputs:**

- [TOOL LIST]: tool, what I use it for, monthly cost, how often I use it

**Prompt:**

```text
Here is the list of software tools I pay for or rely on in my one-person business: """[TOOL LIST]""". Analyze it and produce: (1) overlaps: tools doing the same job; (2) tools I barely use relative to their cost; (3) jobs that seem to have no tool or rely on manual work; (4) a recommendation for each tool: Keep, Downgrade, Replace with [free option I already have], or Cancel, with one-line reasoning. Don't recommend new paid tools unless a gap clearly justifies it, and say what the free alternative is. Finish with the total monthly cost before and after your recommendations, based only on the prices I gave.
```

**Output:** Four short sections, then a table (Tool, Recommendation, Reason, Monthly cost), then before/after totals.

**Tip:** Check cancellation terms and data export before cancelling anything.

**Pairs with:** OPS-07

# Leads & Inquiries

Reply fast, qualify well, and follow up without sounding pushy.

## LEAD-01 · Reply to a new inquiry

**Objective:** Answer a new inquiry quickly and qualify the lead.

**When to use:** Within one business day of any new inquiry by email, form or DM.

**Inputs:**

- [BUSINESS BRIEF] and [VOICE PROFILE]
- [PASTE INQUIRY]
- [BOOKING LINK]

**Prompt:**

```text
Here is my business brief and voice profile: [PASTE]. A potential client sent this inquiry (redacted): """[PASTE INQUIRY]""". Draft a reply under 150 words that: thanks them and references one specific detail from their message; answers any direct question they asked (if I haven't given you the answer, write [NEED INFO] instead of guessing); asks the 2–3 most useful qualifying questions for my services; and ends with my booking link [BOOKING LINK]. Match my voice profile. Don't mention prices unless they asked and my brief includes them.
```

**Output:** A ready-to-edit email with subject line, under 150 words.

**Tip:** Save your best version as an email template and only use AI for the personalized first two lines.

**Pairs with:** LEAD-02, DISC-01

## LEAD-02 · Lead fit scorecard

**Objective:** Decide quickly whether a lead is a good fit before investing time.

**When to use:** When an inquiry is vague, oddly sized or outside your usual work.

**Inputs:**

- [IDEAL CLIENT CRITERIA]
- [LEAD INFO]: inquiry + anything you know

**Prompt:**

```text
My ideal client criteria: """[IDEAL CLIENT CRITERIA]""". Here's what I know about a new lead (redacted): """[LEAD INFO]""". Score the lead from 1–5 on: budget fit, timeline fit, scope fit, decision-maker access, and red flags (5 = no red flags). Explain each score in one line, quoting the evidence. Recommend one of: Book a call, Ask 2 questions first, Refer elsewhere, Politely decline. If there isn't enough information to score a criterion, say "Unknown" and give the question that would resolve it.
```

**Output:** A 5-row table (Criterion, Score, Evidence) plus a one-line recommendation and up to 3 questions.

**Tip:** This is a thinking aid. You make the final call, and politeness costs nothing even when you decline.

**Pairs with:** LEAD-01, LEAD-06

## LEAD-03 · Follow up an inquiry that went quiet

**Objective:** Re-open a conversation with a lead who stopped replying, without pressure.

**When to use:** 3–7 days after your last message with no response.

**Inputs:**

- [LAST MESSAGE SUMMARY]
- [DAYS SINCE]
- [BOOKING LINK]

**Prompt:**

```text
A potential client stopped replying [DAYS SINCE] days ago. Our last exchange: """[LAST MESSAGE SUMMARY]""". Write two alternative follow-up emails in my voice [VOICE PROFILE], each under 90 words: Version A adds something useful (a relevant tip, example or resource related to their project, without inventing facts about them); Version B is a simple, friendly check-in that makes it easy to say "not now". Neither should guilt-trip or imply urgency that doesn't exist. Include my booking link [BOOKING LINK] once.
```

**Output:** Two labeled email drafts with subject lines.

**Tip:** Send at most two follow-ups, then stop and mark the lead "cold" in your tracker.

**Pairs with:** LEAD-01

## LEAD-04 · Referral request to a happy client or peer

**Objective:** Ask for referrals in a specific, easy-to-act-on way.

**When to use:** After a successful project or a positive comment from a client or peer.

**Inputs:**

- [RELATIONSHIP]: client or peer, and context
- [IDEAL REFERRAL]: who you want to be introduced to

**Prompt:**

```text
Write a short message asking [RELATIONSHIP] for referrals. Be specific about who I'm looking for: [IDEAL REFERRAL]. Make it easy: include a two-sentence blurb about me that they can forward as-is, and say it's completely fine if nobody comes to mind. Keep it under 120 words, warm and not salesy, in my voice [VOICE PROFILE]. Don't offer a referral fee unless I've specified one here: [REFERRAL INCENTIVE OR "NONE"].
```

**Output:** One message plus a separate forwardable blurb (2 sentences).

**Tip:** Specific asks ("a physio clinic owner planning a new website") get more introductions than "anyone who needs help".

**Pairs with:** RET-05

## LEAD-05 · Personalized cold outreach (non-spammy)

**Objective:** Write a short, relevant first message to a specific prospect you've researched.

**When to use:** Occasional, targeted outreach to businesses you can genuinely help, not mass email.

**Inputs:**

- [PROSPECT RESEARCH]: public info you gathered
- [MY SERVICE]
- [OBSERVATION]: one specific thing you noticed

**Prompt:**

```text
Draft a first-contact email to a prospect. Public information I gathered: """[PROSPECT RESEARCH]""". My service: [MY SERVICE]. One specific observation: [OBSERVATION]. Requirements: under 110 words; lead with the observation, framed helpfully rather than as criticism; one sentence on how I've helped similar businesses, described generally with no invented results or client names; a low-friction ask (e.g., "Would a 3-point audit be useful?"); a line that makes it easy to say no. No flattery clichés, no fake familiarity, no false urgency. Also give 3 subject line options under 7 words.
```

**Output:** One email plus three subject lines.

**Tip:** Follow the anti-spam and consent rules that apply where you and the recipient are, and always honor opt-outs.

**Pairs with:** LEAD-02

## LEAD-06 · Polite decline (with a referral)

**Objective:** Turn down a lead gracefully and protect your reputation.

**When to use:** When the budget, timing or fit is wrong.

**Inputs:**

- [REASON]: budget, timing, scope or fit
- [ALTERNATIVE]: who or what might help them instead (optional)

**Prompt:**

```text
Write a kind, brief email declining a potential project. Reason (for me; share only what's appropriate): [REASON]. If I've provided an alternative, recommend it: [ALTERNATIVE]. Leave the door open for future work if appropriate: [YES/NO]. Under 100 words, no over-apologizing, no vague excuses, in my voice [VOICE PROFILE].
```

**Output:** A single short email.

**Tip:** A good decline often generates referrals later, because people remember being treated well.

**Pairs with:** LEAD-02

## LEAD-07 · Inquiry form questions

**Objective:** Design the questions on your website's inquiry form so leads arrive pre-qualified.

**When to use:** Setting up or improving your contact/inquiry form.

**Inputs:**

- [SERVICES]
- [MUST-KNOW INFO]: what you need to qualify a lead

**Prompt:**

```text
I offer [SERVICES]. Design an inquiry form with no more than 7 fields that collects what I need to qualify a lead: [MUST-KNOW INFO]. For each field give: the label, field type (short text, dropdown, multiple choice, date, long text), options if applicable, whether it's required, and why it helps. Include a budget question that feels respectful (ranges, including "Not sure yet"). Finish with the confirmation message the person sees after submitting (under 60 words, telling them when to expect a reply).
```

**Output:** A table of fields plus the confirmation message.

**Tip:** Fewer required fields usually means more submissions. Only require what you truly need.

**Pairs with:** LEAD-01

## LEAD-08 · DM reply to a social media inquiry

**Objective:** Respond to a direct message and move the conversation somewhere you can manage it.

**When to use:** When someone asks about your services in Instagram, LinkedIn or TikTok messages.

**Inputs:**

- [DM TEXT]
- [PLATFORM]
- [BOOKING LINK or EMAIL]

**Prompt:**

```text
Someone sent me this message on [PLATFORM]: """[DM TEXT]""". Write a short, friendly reply (under 60 words) that answers any quick question they asked (use [NEED INFO] if you don't know the answer), shows I read their message, and invites them to continue by email or my booking link [BOOKING LINK or EMAIL] so I can give them proper attention. Casual but professional; match the platform's tone.
```

**Output:** One short DM reply.

**Tip:** Log the lead in your tracker as soon as they move to email.

**Pairs with:** LEAD-01

## LEAD-09 · Waitlist or "fully booked" reply

**Objective:** Tell a good-fit lead you're booked up without losing them.

**When to use:** When you're at capacity but want the work later.

**Inputs:**

- [NEXT AVAILABLE START]
- [OPTIONS]: waitlist, smaller interim option, referral

**Prompt:**

```text
Write a reply to a good-fit potential client explaining that I'm fully booked until [NEXT AVAILABLE START]. Offer these options: [OPTIONS]. Explain the benefit of waiting in one honest sentence (e.g., focused attention), without implying scarcity that isn't real. Ask them to reply with their preferred option. Under 120 words, in my voice [VOICE PROFILE].
```

**Output:** One email with a clear choice for the reader.

**Tip:** Add waitlisted leads to your tracker with a next-action date two weeks before your availability.

**Pairs with:** LEAD-01

## LEAD-10 · Lead source analysis

**Objective:** Understand which channels bring your best clients so you invest time wisely.

**When to use:** Every quarter, using your tracker's Source and Stage columns.

**Inputs:**

- [TRACKER EXPORT]: client, source, stage, value (redacted)

**Prompt:**

```text
Here's an export of my leads and clients (redacted): """[TRACKER EXPORT]""". Summarize by source: number of leads, number that became clients, conversion rate, total and average project value. Then highlight: my best source by value, my best by conversion rate, and any source that takes effort but rarely converts. Suggest 2–3 practical adjustments for next quarter. Base everything strictly on the data; if the sample is too small to conclude anything, say so.
```

**Output:** A summary table by source, then 3 highlights and 2–3 recommendations.

**Tip:** Small numbers can mislead, so treat the output as a prompt for reflection, not a verdict.

**Pairs with:** OPS-06

# Discovery & Sales Calls

Prepare, run and follow up on discovery calls that lead to good-fit projects.

## DISC-01 · Pre-call questionnaire

**Objective:** Collect key information before a discovery call so the call is more useful.

**When to use:** Sent with the booking confirmation for discovery calls.

**Inputs:**

- [SERVICE]
- [CALL LENGTH]

**Prompt:**

```text
Create a short pre-call questionnaire (5–7 questions) for people booking a [CALL LENGTH]-minute discovery call about [SERVICE]. Questions should uncover goals, current situation, constraints (timeline, budget range, decision-makers) and what success looks like, without feeling like homework. Mark each as required or optional. Add a one-sentence intro explaining why I ask.
```

**Output:** An intro line plus a numbered question list with required/optional labels.

**Tip:** Most scheduling tools let you add these questions to the booking page.

**Pairs with:** DISC-02

## DISC-02 · Discovery call prep sheet

**Objective:** Walk into a discovery call prepared, in 10 minutes.

**When to use:** Before any discovery or sales call.

**Inputs:**

- [INQUIRY + ANY PUBLIC INFO ABOUT THEIR BUSINESS]
- [SERVICES]
- [LENGTH]

**Prompt:**

```text
I have a discovery call with a potential client. Here is what I know (redacted): """[INQUIRY + ANY PUBLIC INFO ABOUT THEIR BUSINESS]""". My services: [SERVICES]. Create a one-page call prep sheet with: (1) a 2-sentence summary of what they seem to want; (2) 5 open questions to uncover goals, constraints and decision process; (3) 3 likely objections or risks and how I might address them; (4) what I need to learn to scope the project; (5) a proposed call agenda for [LENGTH] minutes. Flag any assumptions you're making.
```

**Output:** A one-page sheet with five numbered sections.

**Tip:** Print it or keep it beside your call window, and take notes directly under each question.

**Pairs with:** DISC-05

## DISC-03 · Discovery call agenda email

**Objective:** Set expectations before the call so it starts focused.

**When to use:** The day before a discovery call.

**Inputs:**

- [CALL DATE/TIME]
- [CALL LINK]
- [AGENDA POINTS]

**Prompt:**

```text
Write a brief email confirming our discovery call on [CALL DATE/TIME] ([CALL LINK]). Include a 3–4 point agenda based on [AGENDA POINTS], one thing they could think about beforehand, and a note that it's fine to reschedule if needed. Under 110 words, friendly and organized, in my voice [VOICE PROFILE].
```

**Output:** One short confirmation email.

**Tip:** Many scheduling tools can send this automatically. Paste the result into your booking confirmation template.

**Pairs with:** DISC-02

## DISC-04 · Qualifying question bank for my niche

**Objective:** Build a tailored list of questions that reveal fit, budget and urgency.

**When to use:** Once per service; revisit when you change niche.

**Inputs:**

- [PROFESSION]
- [TYPICAL CLIENT]

**Prompt:**

```text
I'm a [PROFESSION] working with [TYPICAL CLIENT]. Write 15 discovery questions grouped under: Goals & success; Current situation; Constraints (timeline, budget, resources); Decision process; Past experience with similar providers. For each, add a one-line note on what a "good fit" answer versus a "warning sign" answer sounds like. Keep questions open-ended and non-salesy.
```

**Output:** Grouped question list, each with good-fit / warning-sign notes.

**Tip:** Use 5–6 of these per call, not all 15.

**Pairs with:** DISC-02

## DISC-05 · Call notes → summary + next steps email

**Objective:** Send a clear follow-up the same day as a call.

**When to use:** Immediately after a discovery call.

**Inputs:**

- [NOTES]: redacted notes or transcript
- [VOICE PROFILE]

**Prompt:**

```text
Here are my rough notes from a discovery call (redacted): """[NOTES]""". Using my voice profile [PASTE], write a follow-up email that: thanks them; summarizes their goals, constraints and timeline in 3–5 bullets using their words where possible; lists open questions; states the next step and date (e.g., "I'll send a proposal by [DATE]"); and stays under 200 words. After the email, separately list anything in my notes that is ambiguous or that I should clarify before writing a proposal.
```

**Output:** One email, then a separate list of ambiguities to clarify.

**Tip:** This summary becomes the input for PROP-01, so write it carefully.

**Pairs with:** PROP-01

## DISC-06 · Objection response helper

**Objective:** Prepare calm, honest responses to common objections.

**When to use:** Before calls, or after an objection you handled poorly.

**Inputs:**

- [OBJECTIONS]: e.g., price, timing, 'we'll do it ourselves'
- [SERVICE]

**Prompt:**

```text
For my [SERVICE], write responses to these objections: [OBJECTIONS]. For each: (1) what the objection often really means; (2) a clarifying question to ask first; (3) a short, honest response that respects their decision; (4) when it's better to agree it's not a fit. No pressure tactics, false scarcity or manipulation.
```

**Output:** One block per objection with four labeled parts.

**Tip:** The clarifying question is usually more valuable than the response.

**Pairs with:** DISC-02

## DISC-07 · Scope sketch from discovery notes

**Objective:** Turn a messy discovery conversation into a draft scope you can price.

**When to use:** Between the discovery call and writing the proposal.

**Inputs:**

- [DISCOVERY SUMMARY]
- [MY SERVICES AND PROCESS]

**Prompt:**

```text
Based on this discovery summary (redacted) """[DISCOVERY SUMMARY]""" and my standard process """[MY SERVICES AND PROCESS]""", sketch a draft scope: phases, deliverables per phase, client inputs required, rough effort per phase (Small / Medium / Large), and risks that could expand scope. List the questions I must answer before pricing. Don't suggest prices.
```

**Output:** A phase table (Phase, Deliverables, Client inputs, Effort, Risks) plus a question list.

**Tip:** Price from your own effort estimates and rates, never from AI suggestions.

**Pairs with:** PROP-01, PROP-06

## DISC-08 · Post-call self-review

**Objective:** Improve your discovery calls over time.

**When to use:** Right after a call, while it's fresh.

**Inputs:**

- [CALL NOTES]
- [OUTCOME]: booked, pending, lost

**Prompt:**

```text
Act as a supportive sales coach. Here are my notes from a discovery call (redacted) and the outcome so far: """[CALL NOTES]""" / [OUTCOME]. Assess: how well I uncovered goals, constraints and decision process; whether I talked too much (estimate from the notes); what I could have asked; and one thing to do differently next time. Be specific and kind, and base your comments on the notes rather than generic advice.
```

**Output:** Four short sections, ending with one clear action for next time.

**Tip:** Keep the "one thing" in your Prompt Log notes and track whether you apply it.

**Pairs with:** DISC-02

# Proposals & Pricing

Draft specific proposals, structure options and protect your scope. You set the prices; AI never does.

## PROP-01 · Proposal draft from discovery notes

**Objective:** Draft a complete, specific proposal from your call summary.

**When to use:** After the discovery follow-up (DISC-05), once you've set your price.

**Inputs:**

- [BUSINESS BRIEF] and [VOICE PROFILE]
- [SUMMARY]: discovery call summary (redacted)
- [PRICE / OPTIONS I'LL PROVIDE]

**Prompt:**

```text
Here is my business brief [PASTE], my voice profile [PASTE], and my discovery call summary (redacted): """[SUMMARY]""". Draft a proposal using this structure: 1) Your situation (3–4 sentences using the client's words), 2) Outcomes (3–5 bullets), 3) Scope (numbered deliverables), 4) Not included (5–8 bullets), 5) Timeline (milestones with client dependencies), 6) Investment: [PRICE / OPTIONS I'LL PROVIDE]. Use exactly my prices and payment terms and don't invent numbers. 7) Next step. Keep it under 700 words, plain language, no buzzwords. Mark anything you had to assume with [CHECK].
```

**Output:** A 7-section proposal document, under 700 words, with [CHECK] markers.

**Tip:** Delete any number you didn't provide. Read it aloud once before sending.

**Pairs with:** PROP-06, PROP-04, DISC-05

## PROP-02 · Three-option package builder

**Objective:** Structure good / better / best options so clients choose how, not whether.

**When to use:** When a project could reasonably be delivered at different depths.

**Inputs:**

- [SCOPE SKETCH]
- [YOUR PRICES FOR EACH OPTION]

**Prompt:**

```text
Using this scope sketch """[SCOPE SKETCH]""", structure three options (Essential, Recommended, Complete). For each: who it suits, what's included, what's excluded, timeline, and the price I set: [YOUR PRICES FOR EACH OPTION]. Make the differences obvious in a comparison table. Explain in one sentence why "Recommended" is recommended, based on the client's stated goals only. Don't invent prices or features I didn't list.
```

**Output:** A comparison table plus a short description of each option.

**Tip:** Keep options genuinely different. Artificial decoy options erode trust.

**Pairs with:** PROP-01

## PROP-03 · Pricing rationale explainer

**Objective:** Explain your price in terms of value and effort without sounding defensive.

**When to use:** When a client asks "why does it cost that much?"

**Inputs:**

- [PRICE]
- [WHAT'S INCLUDED]
- [CLIENT GOALS]

**Prompt:**

```text
A client asked why my quote is [PRICE]. What's included: """[WHAT'S INCLUDED]""". Their goals: """[CLIENT GOALS]""". Write a calm, confident reply (under 170 words) that: connects the price to the outcomes they want; briefly shows the work involved (phases, not hours, unless I say otherwise); offers a smaller alternative scope if that's appropriate: [SMALLER OPTION OR "NONE"]. No discounting unless I specify one, no apologizing, no comparisons to named competitors.
```

**Output:** One email reply.

**Tip:** If price is the only concern, offering a reduced scope protects your rate better than a discount.

**Pairs with:** PROP-02, HARD-01

## PROP-04 · Proposal follow-up sequence

**Objective:** Follow up on a sent proposal politely and consistently.

**When to use:** Day 3, day 7 and day 14 after sending a proposal.

**Inputs:**

- [PROJECT]
- [DATE SENT]
- [BOOKING LINK]

**Prompt:**

```text
I sent a proposal for [PROJECT] on [DATE SENT]. Write three follow-up emails in my voice [VOICE PROFILE]: Day 3 (one or two sentences: any questions?); Day 7 (offer a 15-minute call to walk through options, link [BOOKING LINK]); Day 14 (a gracious close-the-loop message that assumes timing isn't right and leaves the door open). Each under 80 words. No guilt, no fake deadlines.
```

**Output:** Three labeled emails with subject lines.

**Tip:** Put the dates in your tracker's next-action column the day you send the proposal.

**Pairs with:** PROP-01

## PROP-05 · Retainer proposal

**Objective:** Propose an ongoing monthly arrangement to an existing client.

**When to use:** When a client keeps coming back with similar requests.

**Inputs:**

- [HISTORY]: past projects and recurring requests
- [RETAINER TERMS I'VE DECIDED]: price, hours or deliverables, notice period

**Prompt:**

```text
Draft a short retainer proposal (under 300 words) for an existing client. Our history (redacted): """[HISTORY]""". Terms I've decided: """[RETAINER TERMS I'VE DECIDED]""". Include: why a retainer suits their pattern of requests; exactly what they get each month; what's excluded; how unused capacity is handled (per my terms); notice period; how to start. Position it as their convenience, not my revenue goal. Use only the terms I provided.
```

**Output:** A short proposal with headed sections.

**Tip:** Base the retainer on real past demand, which the history section should make visible.

**Pairs with:** PROP-01

## PROP-06 · Scope exclusions & assumptions list

**Objective:** Prevent scope creep by stating what's not included.

**When to use:** For every proposal; build a master list once per service.

**Inputs:**

- [PROFESSION]
- [DELIVERABLES]

**Prompt:**

```text
I'm a [PROFESSION] and this project includes: [DELIVERABLES]. List 10 things clients commonly assume are included in this kind of project but often aren't (e.g., extra revision rounds, copywriting, stock photos, hosting, training, ongoing support). For each, write one plain-language line for a "Not included" section and, where useful, the add-on I could offer instead. Then list 5 assumptions about the client's responsibilities (content, feedback times, access) that I should state in the proposal.
```

**Output:** Two lists, "Not included" (10 lines with optional add-ons) and "Assumptions" (5 lines).

**Tip:** Keep a master version per service and copy the relevant lines each time.

**Pairs with:** PROP-01, DEL-07

## PROP-07 · Timeline with client dependencies

**Objective:** Build a realistic timeline that makes the client's responsibilities visible.

**When to use:** In proposals and kickoff documents.

**Inputs:**

- [START DATE]
- [PHASES AND DURATIONS]
- [CLIENT INPUTS NEEDED]

**Prompt:**

```text
Create a project timeline starting [START DATE] from these phases and durations: """[PHASES AND DURATIONS]""". For each milestone, list what I deliver and what the client must provide, and by when (based on: """[CLIENT INPUTS NEEDED]"""). Add a short note explaining that the timeline shifts if client inputs arrive late, phrased collaboratively. Use calendar dates, skip weekends, and flag any [HOLIDAYS OR BREAKS] I mention.
```

**Output:** A table (Milestone, Date, I deliver, You provide by) plus a two-sentence note.

**Tip:** Double-check date arithmetic yourself; AI can miscount days.

**Pairs with:** PROP-01, ONB-05

## PROP-08 · Case study summary for proposals (from your notes)

**Objective:** Turn a past project into a short, truthful proof point.

**When to use:** When you want to reference relevant past work in a proposal.

**Inputs:**

- [PROJECT NOTES]: situation, what you did, result as the client described it
- [PERMISSION STATUS]: named / anonymized

**Prompt:**

```text
Turn these notes about a past project into a 90-word case study for proposals. Notes: """[PROJECT NOTES]""". Permission: [PERMISSION STATUS]. If anonymized, describe the client generically (e.g., "a three-location dental practice"). Structure: situation, what I did, outcome. Only state outcomes that appear in my notes, and attribute any numbers to the client ("the client reported…"). Don't embellish.
```

**Output:** A 90-word paragraph plus a one-line title.

**Tip:** Ask permission before naming clients or quoting their results.

**Pairs with:** RET-02

## PROP-09 · Price increase announcement

**Objective:** Tell existing clients about a rate change clearly and respectfully.

**When to use:** When you raise rates for retainers or repeat clients.

**Inputs:**

- [OLD RATE] and [NEW RATE]
- [EFFECTIVE DATE]
- [REASON]: optional

**Prompt:**

```text
Write an email informing an existing client that my rate will change from [OLD RATE] to [NEW RATE] effective [EFFECTIVE DATE]. Give appropriate notice as stated in our agreement: [NOTICE TERMS]. Briefly mention [REASON] if provided, without over-justifying. Thank them for the relationship and make it easy to ask questions. Under 140 words, confident and warm.
```

**Output:** One email.

**Tip:** Check your agreement's notice terms before sending.

**Pairs with:** HARD-01

## PROP-10 · Contract clause plain-language explainer

**Objective:** Help a client (and you) understand what a clause in your agreement means.

**When to use:** When a client asks about a clause, or you want to summarize your terms in plain English.

**Inputs:**

- [CLAUSE TEXT]

**Prompt:**

```text
Explain this clause from my client agreement in plain language for a non-lawyer, in under 120 words: """[CLAUSE TEXT]""". Then list 2–3 questions a client might ask about it. Don't give legal advice or say whether the clause is enforceable. End with: "This is a plain-language summary, not legal advice."
```

**Output:** A short explanation, a question list and the disclaimer line.

**Tip:** Have your agreement template reviewed by a qualified professional; this prompt only explains it.

**Pairs with:** ONB-02

## PROP-11 · Proposal self-review checklist

**Objective:** Catch gaps, vague language and risky promises before sending.

**When to use:** As the last step before any proposal goes out.

**Inputs:**

- [PROPOSAL TEXT]

**Prompt:**

```text
Review this proposal as a skeptical client and as a careful business owner: """[PROPOSAL TEXT]""". List: (1) anything vague that could cause a dispute later; (2) promises or guarantees I may not want to make; (3) missing items (payment terms, revisions, timeline dependencies, exclusions, next step); (4) jargon to simplify; (5) the single biggest improvement. Quote the exact text for each issue.
```

**Output:** Five numbered sections with quoted text and suggested fixes.

**Tip:** Fix issues yourself instead of asking AI to rewrite everything, so your voice stays intact.

**Pairs with:** PROP-01

## PROP-12 · Estimate my effort before pricing

**Objective:** Estimate your time on a project so your price reflects real effort.

**When to use:** Before setting a fixed price.

**Inputs:**

- [SCOPE]
- [MY PAST TASK TIMES]: how long similar tasks took

**Prompt:**

```text
Help me estimate effort for this scope: """[SCOPE]""". Use my past task times as the baseline: """[MY PAST TASK TIMES]""". Break the work into tasks, estimate hours for each (low / likely / high), add time for communication, revisions and project management, and total them. Flag tasks where you had to guess because I gave no baseline. Don't convert hours into a price.
```

**Output:** A task table (Task, Low, Likely, High, Basis) with totals and flagged guesses.

**Tip:** Multiply the likely total by your own rate, then sanity-check against the "high" total.

**Pairs with:** DISC-07, PROP-02

# Onboarding

Turn a 'yes' into a smooth, professional start.

## ONB-01 · Welcome email

**Objective:** Start the project with clear next steps and expectations.

**When to use:** As soon as a client says yes.

**Inputs:**

- [BUSINESS BRIEF] and [VOICE PROFILE]
- [PROJECT, TIMELINE, LINKS]

**Prompt:**

```text
Using my business brief and voice profile [PASTE], write a welcome email for a new client (redacted details: """[PROJECT, TIMELINE, LINKS]"""). Include: a warm opening that references the project; a numbered "what happens next" list (agreement, deposit, questionnaire link, kickoff booking link); my communication norms from the brief; and a friendly close. Under 220 words. Use only the links and dates I provide. Use [NEED INFO] for anything missing.
```

**Output:** One email with a numbered next-steps list, under 220 words.

**Tip:** Save the result as a template, since only the first line and links change per client.

**Pairs with:** ONB-03, SET-07

## ONB-02 · Agreement summary email

**Objective:** Send the agreement with a short, friendly summary of key terms.

**When to use:** When sending your contract for signature.

**Inputs:**

- [KEY TERMS]: scope, fee, payment schedule, revisions, cancellation
- [SIGNING LINK]

**Prompt:**

```text
Write a short email sending my client agreement for signature ([SIGNING LINK]). Summarize the key terms in 4–6 plain-language bullets based only on: """[KEY TERMS]""". Invite questions before they sign, and mention that work starts once the agreement and deposit are complete. Under 150 words. Don't add terms that aren't in my list.
```

**Output:** One email with a bullet summary.

**Tip:** The summary helps clients read the agreement. It doesn't replace it.

**Pairs with:** PROP-10

## ONB-03 · Intake questionnaire builder

**Objective:** Collect everything you need from a new client in one form.

**When to use:** When setting up onboarding for each service type.

**Inputs:**

- [PROFESSION]
- [PROJECT TYPE]

**Prompt:**

```text
I'm a [PROFESSION] starting a [PROJECT TYPE] for a client. Create an intake questionnaire of 10–15 questions grouped under: Goals & success measures; Audience/customers; Brand & preferences; Content & assets they'll provide; Access & logistics; Communication & approvals. For each question, note why I need it (one line) and mark it Required or Optional. Avoid questions I could answer myself from their website. End with a "Anything else we should know?" question.
```

**Output:** Grouped questions with purpose notes and Required/Optional labels.

**Tip:** Build it in a form tool so answers land in a spreadsheet.

**Pairs with:** ONB-01

## ONB-04 · Client onboarding document

**Objective:** Create a single "everything you need to know" document for new clients.

**When to use:** Once per service; share a copy with every new client.

**Inputs:**

- [BUSINESS BRIEF]
- [PROCESS STEPS]
- [FAQ]

**Prompt:**

```text
Create a client onboarding document (under 600 words) from my business brief """[BUSINESS BRIEF]""", my process """[PROCESS STEPS]""" and my FAQ """[FAQ]""". Sections: Welcome; How the project works (numbered phases); What I need from you and when; How we'll communicate; Feedback & approvals; Payments; Frequently asked questions; Who to contact. Friendly, scannable, second person ("you").
```

**Output:** A Markdown document with eight headed sections.

**Tip:** Export it as a PDF and link it in the welcome email.

**Pairs with:** SET-06, SET-07

## ONB-05 · Kickoff call agenda

**Objective:** Run a focused kickoff meeting that sets the project up well.

**When to use:** When scheduling the kickoff call.

**Inputs:**

- [PROJECT]
- [QUESTIONNAIRE ANSWERS]: summarized
- [CALL LENGTH]

**Prompt:**

```text
Create a [CALL LENGTH]-minute kickoff call agenda for [PROJECT]. Use the client's questionnaire answers (redacted) """[QUESTIONNAIRE ANSWERS]""" to list: items to confirm, open questions to resolve, decisions needed, and risks to discuss. Include timings for each agenda item, and end with "agree next steps & dates". Also write a 3-sentence email to send the agenda in advance.
```

**Output:** A timed agenda plus a short cover email.

**Tip:** Share the agenda 24 hours before so the client arrives prepared.

**Pairs with:** DEL-04

## ONB-06 · Asset & access request

**Objective:** Ask for files, logins and access in one clear, secure request.

**When to use:** Right after kickoff.

**Inputs:**

- [ITEMS NEEDED]
- [DEADLINE]
- [SECURE SHARING METHOD]

**Prompt:**

```text
Write an email asking a client for the assets and access I need: """[ITEMS NEEDED]""", by [DEADLINE]. Format as a checklist they can reply to. Explain how to share passwords securely using [SECURE SHARING METHOD] and ask them never to send passwords in plain email. Mention politely that the timeline starts when the items arrive. Under 180 words.
```

**Output:** One email with a checklist.

**Tip:** Offer to walk them through access on a quick call if they're not technical.

**Pairs with:** ONB-05

## ONB-07 · Project folder & naming convention

**Objective:** Create a consistent file structure for every client.

**When to use:** Once; reuse for every new client.

**Inputs:**

- [SERVICE]
- [TOOLS]: e.g., Google Drive, Dropbox

**Prompt:**

```text
Design a simple folder structure and file-naming convention for [SERVICE] projects stored in [TOOLS]. Include: top-level folders (max 7), what goes in each, a naming pattern for files with a date and version (e.g., YYYY-MM-DD_Client_Deliverable_v01), and rules for archiving when a project ends. Keep it simple enough to follow on a busy day.
```

**Output:** A folder tree, a naming pattern with 3 examples, and 3 archiving rules.

**Tip:** Save a template folder and copy it for each new client.

**Pairs with:** OPS-01

## ONB-08 · Expectations reset for a new client

**Objective:** Gently re-establish norms when a new client starts off with unrealistic expectations.

**When to use:** Early in a project, when a client expects instant replies or unlimited revisions.

**Inputs:**

- [SITUATION]
- [AGREED TERMS]

**Prompt:**

```text
A new client is expecting more than we agreed. Situation (redacted): """[SITUATION]""". Our agreed terms: """[AGREED TERMS]""". Write a friendly email that restates how we'll work (response times, revision rounds, channels), explains the benefit to them, and proposes a practical way forward. No blame, under 160 words, in my voice [VOICE PROFILE].
```

**Output:** One email.

**Tip:** Do this early. Resetting expectations in week one is far easier than in week eight.

**Pairs with:** SET-07, HARD-02

## ONB-09 · Onboarding checklist tailored to a service

**Objective:** Turn the generic onboarding checklist into one that fits your exact service.

**When to use:** Once per service.

**Inputs:**

- [SERVICE]
- [TOOLS]
- [CURRENT STEPS]: what you do now, even if messy

**Prompt:**

```text
Here's how I currently onboard clients for [SERVICE] using [TOOLS]: """[CURRENT STEPS]""". Turn it into a clean onboarding checklist in the order steps should happen, grouped into: Paperwork & payment; Welcome & information; Setup; Kickoff. Mark steps that can use a saved template (T) or could be automated later (A). Point out missing steps common in [SERVICE] projects.
```

**Output:** A grouped checklist with T/A markers and a short "missing steps" list.

**Tip:** Copy the result into your SOP library (OPS-01).

**Pairs with:** OPS-01

## ONB-10 · First-week check-in message

**Objective:** Reassure a new client and surface issues early.

**When to use:** At the end of the first week of a project.

**Inputs:**

- [PROGRESS SO FAR]
- [NEXT STEPS]

**Prompt:**

```text
Write a short end-of-first-week message to a new client. Progress so far: """[PROGRESS SO FAR]""". Coming up: """[NEXT STEPS]""". Ask one question that invites honest feedback about how things are going so far. Under 110 words, warm and specific, in my voice [VOICE PROFILE].
```

**Output:** One short email or message.

**Tip:** Log any concerns they raise in the Notes column of your tracker.

**Pairs with:** DEL-01

# Delivery & Client Communication

Updates, feedback, delays, scope changes and meeting notes: the everyday communication of client work.

## DEL-01 · Weekly client update

**Objective:** Turn rough notes into a clear five-minute weekly update.

**When to use:** Every week for each active client.

**Inputs:**

- [NOTES]: bullets you jotted during the week (redacted)
- [VOICE PROFILE]

**Prompt:**

```text
Turn my rough notes into a weekly client update using this structure: Done this week / Next week / Needed from you (with dates) / Risks or decisions. Notes (redacted): """[NOTES]""". Keep it under 150 words, in my voice [VOICE PROFILE]. If my notes mention a delay, state it plainly with the new expected date. Don't soften it into vagueness, and don't invent reasons.
```

**Output:** A four-part update email under 150 words.

**Tip:** Keep a running notes file per client during the week, since it makes this a two-minute job.

**Pairs with:** DEL-04, DEL-02

## DEL-02 · Delay notification

**Objective:** Tell a client about a delay early, honestly and with a plan.

**When to use:** As soon as you know a milestone will slip.

**Inputs:**

- [MILESTONE]
- [ORIGINAL DATE] and [NEW DATE]
- [REASON]
- [WHAT I'M DOING ABOUT IT]

**Prompt:**

```text
Write an email telling a client that [MILESTONE] will move from [ORIGINAL DATE] to [NEW DATE]. Reason (share appropriately): [REASON]. What I'm doing about it: [WHAT I'M DOING ABOUT IT]. Structure: the news first, one sentence of context, the plan, the impact on later milestones, and whether they need to do anything. Take responsibility where it's mine, no excessive apology, under 150 words, in my voice [VOICE PROFILE].
```

**Output:** One email.

**Tip:** Delays reported early damage trust far less than delays discovered late.

**Pairs with:** DEL-01

## DEL-03 · Consolidated feedback request

**Objective:** Get one clear, consolidated round of feedback instead of scattered comments.

**When to use:** When sharing a draft or milestone for review.

**Inputs:**

- [DELIVERABLE]
- [REVIEW LINK]
- [FEEDBACK DEADLINE]
- [QUESTIONS I NEED ANSWERED]

**Prompt:**

```text
Write an email sharing [DELIVERABLE] for review ([REVIEW LINK]). Ask for one consolidated set of feedback by [FEEDBACK DEADLINE], gathered from everyone on their side. Guide their review with these questions: [QUESTIONS I NEED ANSWERED]. Explain the difference between "must change" and "nice to have" and ask them to label comments that way. Mention what's in scope for this round per our agreement: [REVISION TERMS]. Under 170 words.
```

**Output:** One email with numbered review questions.

**Tip:** Specific review questions produce more useful feedback than "what do you think?"

**Pairs with:** DEL-05

## DEL-04 · Meeting notes → summary & action items

**Objective:** Turn meeting notes or a transcript into decisions, actions and a follow-up email.

**When to use:** After every client meeting.

**Inputs:**

- [NOTES]: notes or transcript (redacted; recorded only with consent)

**Prompt:**

```text
Here are notes or a transcript from a client meeting (redacted): """[NOTES]""". Produce: (1) a 3-sentence summary; (2) decisions made; (3) action items as a table with Owner, Task, Due date (write "TBC" if no date was agreed; don't invent dates); (4) open questions. Then draft a short follow-up email to the client that confirms decisions and action items.
```

**Output:** Summary, decisions list, action table, open questions, then a follow-up email.

**Tip:** Send the follow-up the same day. It becomes the record if memories differ later.

**Pairs with:** DEL-01

## DEL-05 · Feedback triage

**Objective:** Sort messy client feedback into clear, in-scope actions.

**When to use:** When feedback arrives as a long email, many comments or conflicting opinions.

**Inputs:**

- [FEEDBACK]
- [AGREED SCOPE]

**Prompt:**

```text
Sort this client feedback (redacted) """[FEEDBACK]""" against our agreed scope """[AGREED SCOPE]""". Output a table with: Comment (paraphrased), Type (fix / change / new request / question / conflict), In scope? (yes / no / unclear), Proposed action. Then list conflicting comments that need the client to decide, and draft 2–3 clarifying questions to send back.
```

**Output:** A triage table, a conflicts list and 2–3 clarifying questions.

**Tip:** Out-of-scope items go to DEL-07 before any work starts.

**Pairs with:** DEL-07, DEL-03

## DEL-06 · Status report for a longer project

**Objective:** Give stakeholders a clear monthly view of progress, budget and risks.

**When to use:** Monthly on projects longer than six weeks or with several stakeholders.

**Inputs:**

- [MILESTONES AND STATUS]
- [BUDGET USED]: if applicable
- [RISKS]

**Prompt:**

```text
Create a one-page monthly status report from: milestones & status """[MILESTONES AND STATUS]"""; budget/time used """[BUDGET USED]"""; risks """[RISKS]""". Sections: Overall status (On track / At risk / Off track, with one-line reason); Milestones (table); Budget/time; Risks & mitigations; Decisions needed from the client; Next month. Use only my data. If a status can't be determined, say so.
```

**Output:** A one-page report with six sections.

**Tip:** Send before a short monthly call, not instead of one.

**Pairs with:** DEL-01

## DEL-07 · Scope change request email

**Objective:** Quote extra work before doing it, without awkwardness.

**When to use:** Whenever a request falls outside the agreed scope.

**Inputs:**

- [SCOPE]
- [REQUEST]
- [PRICE / TIME IMPACT I'LL PROVIDE]

**Prompt:**

```text
A client asked for something outside our agreed scope. Agreed scope: """[SCOPE]""". Their request: """[REQUEST]""". Draft a friendly, confident email that: thanks them for the idea; notes it's outside the current scope (without blaming); offers 2 options, (a) add it now for [PRICE / TIME IMPACT I'LL PROVIDE] or (b) park it for a later phase; and asks them to confirm which option they prefer before I start. Under 170 words, in my voice.
```

**Output:** One email with two clearly labeled options.

**Tip:** Log approved changes in writing (email is fine) before starting the work.

**Pairs with:** PROP-06, DEL-05

## DEL-08 · Approval request for a milestone

**Objective:** Get explicit sign-off before moving to the next phase.

**When to use:** At the end of each phase or milestone.

**Inputs:**

- [MILESTONE]
- [WHAT WAS DELIVERED]
- [NEXT PHASE]

**Prompt:**

```text
Write an email asking the client to formally approve [MILESTONE]. Summarize what was delivered: """[WHAT WAS DELIVERED]""". Explain what approval means (we move to [NEXT PHASE]; later changes to this milestone may be treated as new requests per our agreement: [CHANGE TERMS]). Ask them to reply "Approved" or list remaining must-change items by [DATE]. Under 150 words, clear and friendly.
```

**Output:** One email with a clear reply instruction.

**Tip:** If an invoice is tied to this milestone, send it right after approval.

**Pairs with:** PAY-01

## DEL-09 · Handling a vague request

**Objective:** Clarify an unclear client request before spending time on it.

**When to use:** When a client asks for something like "make it pop" or "can you look at the site?"

**Inputs:**

- [REQUEST]
- [PROJECT CONTEXT]

**Prompt:**

```text
A client sent a vague request: """[REQUEST]""". Project context: """[PROJECT CONTEXT]""". Write a short reply that shows willingness to help and asks 2–3 specific questions (with example answers they can pick from) so I can understand exactly what they want. Under 100 words, in my voice [VOICE PROFILE].
```

**Output:** One short reply with multiple-choice style questions.

**Tip:** Offering example answers speeds up replies from busy clients.

**Pairs with:** DEL-05

## DEL-10 · Out-of-office / capacity notice

**Objective:** Tell clients about time off or reduced availability in advance.

**When to use:** 1–2 weeks before holidays or planned time off.

**Inputs:**

- [DATES]
- [COVERAGE]: what happens while you're away
- [DEADLINES AFFECTED]

**Prompt:**

```text
Write an advance notice to clients that I'll be away [DATES]. What happens meanwhile: [COVERAGE]. Deadlines affected: [DEADLINES AFFECTED]. Ask them to send anything they need from me before [CUTOFF DATE]. Also write a matching 2-sentence auto-reply. Friendly, under 130 words total for the email.
```

**Output:** One advance-notice email plus an auto-reply.

**Tip:** Add the cutoff date to each client's next action in your tracker.

**Pairs with:** DEL-01

## DEL-11 · Explaining a technical issue simply

**Objective:** Explain a technical problem to a non-technical client without jargon.

**When to use:** When something breaks or a technical constraint affects the project.

**Inputs:**

- [TECHNICAL DETAILS]
- [IMPACT ON CLIENT]
- [OPTIONS]

**Prompt:**

```text
Explain this technical issue to a non-technical client: """[TECHNICAL DETAILS]""". Impact on them: [IMPACT ON CLIENT]. Options: [OPTIONS]. Use a short everyday analogy if helpful, avoid jargon (or define it once), state what I recommend and why, and what I need them to decide. Under 180 words. Don't overstate certainty. If I haven't confirmed a cause, say it's the likely cause.
```

**Output:** One email with a clear recommendation and decision request.

**Tip:** Check the analogy isn't misleading, since simple shouldn't mean inaccurate.

**Pairs with:** DEL-02

## DEL-12 · Presentation outline for a deliverable

**Objective:** Present your work in a way that frames decisions, not opinions.

**When to use:** Before presenting a design, strategy or report to a client.

**Inputs:**

- [DELIVERABLE]
- [CLIENT GOALS]
- [KEY DECISIONS]

**Prompt:**

```text
Create an outline for presenting [DELIVERABLE] to a client in 20 minutes. Their goals: """[CLIENT GOALS]""". Key decisions I made and why: """[KEY DECISIONS]""". Structure: recap of goals; walkthrough linking each decision to a goal; what I considered and rejected; questions to guide their feedback; next steps. Include timings.
```

**Output:** A timed outline with speaking notes per section.

**Tip:** Tying each decision to a stated goal reduces "I just don't like it" feedback.

**Pairs with:** DEL-03

## DEL-13 · Thread summarizer

**Objective:** Catch up on a long email thread quickly and see what's actually needed.

**When to use:** When returning to a project after time away, or a thread gets long.

**Inputs:**

- [THREAD]: redacted email thread

**Prompt:**

```text
Summarize this email thread (redacted) """[THREAD]""" for me in: (1) 5 bullet summary; (2) decisions made, with who made them and when; (3) open questions and who owes an answer; (4) commitments I made; (5) suggested next reply in one or two sentences. Quote key phrases where precision matters.
```

**Output:** Five labeled sections.

**Tip:** Verify commitments against the original emails before acting on them.

**Pairs with:** DEL-04

## DEL-14 · Client check-in on a quiet project

**Objective:** Re-engage a client who has gone quiet mid-project.

**When to use:** When you're waiting on client input past its due date.

**Inputs:**

- [WHAT I'M WAITING FOR]
- [ORIGINAL DUE DATE]
- [IMPACT ON TIMELINE]

**Prompt:**

```text
A client hasn't sent [WHAT I'M WAITING FOR], which was due [ORIGINAL DUE DATE]. Write a friendly nudge that restates what's needed, explains the timeline impact ([IMPACT ON TIMELINE]), and offers an easy way forward (e.g., a 15-minute call, or a simplified version of what I need). Under 110 words, no guilt, in my voice [VOICE PROFILE].
```

**Output:** One short email.

**Tip:** If two nudges get no answer, pause the project in writing per your agreement.

**Pairs with:** HARD-04

# Invoicing & Getting Paid

Invoice clearly and follow up on a predictable, respectful schedule.

## PAY-01 · Invoice email

**Objective:** Send an invoice with a short, clear cover message.

**When to use:** Every time you send an invoice.

**Inputs:**

- [INVOICE NUMBER], [AMOUNT], [DUE DATE], [PAYMENT LINK]
- [WHAT IT COVERS]

**Prompt:**

```text
Write a short email to accompany invoice [INVOICE NUMBER] for [AMOUNT], covering [WHAT IT COVERS], due [DUE DATE]. Include the payment link [PAYMENT LINK], a one-line thank-you tied to the work, and a note to reply if anything looks wrong. Under 80 words.
```

**Output:** One short email with subject line.

**Tip:** Put the invoice number and due date in the subject line.

**Pairs with:** PAY-02

## PAY-02 · Payment reminder sequence personalizer

**Objective:** Send the right reminder, at the right stage, in the right tone.

**When to use:** For any unpaid invoice approaching or past its due date.

**Inputs:**

- [RELATIONSHIP], [INVOICE NUMBER], [AMOUNT], [DATE], [X] days overdue, previous reminders
- [RELEVANT TERMS]: from your agreement

**Prompt:**

```text
I need to send a payment reminder. Context (redacted): client relationship [NEW / LONG-TERM / DIFFICULT], invoice [NUMBER] for [AMOUNT], due [DATE], currently [X] days overdue, previous reminders sent: [LIST]. My agreement says: """[RELEVANT TERMS]""". Draft the next reminder at stage [A/B/C/D/E]. Keep the tone [FRIENDLY / FIRM / FORMAL] and under 120 words, in my voice [VOICE PROFILE]. Only mention fees or consequences that appear in my agreement text. Include the payment link placeholder [LINK].
```

**Output:** One reminder email with subject line.

**Tip:** The Client Desk workbook tells you which stage (A–E) is due for each invoice.

**Pairs with:** PAY-03, PAY-04

## PAY-03 · Payment plan offer

**Objective:** Offer a structured way for a struggling client to pay.

**When to use:** When a client says they can't pay in full right now.

**Inputs:**

- [BALANCE]
- [PLAN I'M WILLING TO OFFER]

**Prompt:**

```text
A client can't pay the full balance of [BALANCE] right now. Write an email offering this plan: [PLAN I'M WILLING TO OFFER] (e.g., three payments on specific dates). Ask them to confirm in writing, state what happens to ongoing work during the plan per my terms [TERMS], and keep a supportive, practical tone. Under 150 words.
```

**Output:** One email with the payment schedule as a short list.

**Tip:** Get the plan confirmed in writing and track each payment separately.

**Pairs with:** PAY-02

## PAY-04 · Final notice (per your agreement)

**Objective:** Send a formal final notice that states agreed next steps.

**When to use:** About 30 days overdue after earlier reminders.

**Inputs:**

- [INVOICE DETAILS]
- [HISTORY]: reminders sent and dates
- [NEXT STEP FROM AGREEMENT]

**Prompt:**

```text
Write a formal but courteous final notice for invoice [INVOICE DETAILS]. History of reminders: [HISTORY]. State the final payment date [FINAL DATE] and the next step exactly as my agreement describes it: [NEXT STEP FROM AGREEMENT]. Don't threaten anything outside my agreement or the law, and don't add fees I haven't listed. Invite them to contact me today to resolve it. Under 150 words.
```

**Output:** One formal email.

**Tip:** Before escalating (collections, small claims), check the rules that apply where you and the client are.

**Pairs with:** PAY-02

## PAY-05 · Payment terms section for proposals

**Objective:** Write clear, fair payment terms in plain language.

**When to use:** When creating or updating your proposal template.

**Inputs:**

- [TERMS I'VE DECIDED]: deposit, schedule, due days, methods, late policy

**Prompt:**

```text
Turn these payment terms into a clear "Payment terms" section for my proposals: """[TERMS I'VE DECIDED]""". Use short bullets: deposit, schedule, due dates, how to pay, what happens if payment is late (only what I specified), and refunds/cancellation if provided. Plain language, no legalese, under 130 words. Add a note reminding me to confirm the terms match my signed agreement.
```

**Output:** A headed bullet list plus a note to me.

**Tip:** Your agreement is the source of truth. This section summarizes it.

**Pairs with:** PROP-01

## PAY-06 · Deposit request

**Objective:** Request a deposit clearly so the project can start.

**When to use:** Immediately after a proposal is accepted.

**Inputs:**

- [DEPOSIT AMOUNT], [DUE DATE], [PAYMENT LINK]
- [START DATE]

**Prompt:**

```text
Write a short, upbeat email requesting the project deposit of [DEPOSIT AMOUNT] via [PAYMENT LINK], due [DUE DATE], so we can start on [START DATE]. Explain in one sentence what the deposit secures (e.g., reserved time in my schedule). Under 90 words.
```

**Output:** One short email.

**Tip:** Hold your start date only once the deposit arrives, and say so kindly.

**Pairs with:** ONB-01

## PAY-07 · Monthly money review

**Objective:** Get a quick picture of invoicing, collections and upcoming cash.

**When to use:** Monthly, during your weekly review nearest month-end.

**Inputs:**

- [INVOICE EXPORT]: number, client, issue date, due date, amount, paid, paid date (redacted)

**Prompt:**

```text
Analyze my invoices (redacted) """[INVOICE EXPORT]""". Report: total invoiced this month; total collected; outstanding and overdue totals; average days to payment for paid invoices; clients who paid late more than once; invoices due in the next 30 days. Suggest up to 3 practical changes (e.g., deposits, milestone billing). Use only the data provided and show your calculations.
```

**Output:** A short summary with a small table, calculations and up to 3 suggestions.

**Tip:** Check AI arithmetic against your spreadsheet totals.

**Pairs with:** OPS-06

## PAY-08 · Payment received thank-you

**Objective:** Confirm payment and strengthen the relationship.

**When to use:** When a payment arrives, especially after reminders.

**Inputs:**

- [INVOICE NUMBER], [AMOUNT]
- [NEXT STEP]

**Prompt:**

```text
Write a short thank-you confirming receipt of payment for invoice [INVOICE NUMBER] ([AMOUNT]). Mention the next step [NEXT STEP] if there is one. If this followed reminders, keep it gracious with no reference to lateness. Under 60 words.
```

**Output:** One brief message.

**Tip:** Mark the invoice as paid in your tracker the same day.

**Pairs with:** PAY-01

# Offboarding, Testimonials & Referrals

Finish well, earn honest testimonials and keep relationships warm.

## RET-01 · Project wrap-up & handover email

**Objective:** Close a project cleanly with everything the client needs.

**When to use:** When final deliverables are approved.

**Inputs:**

- [DELIVERABLES AND WHERE THEY ARE]
- [ACCESS CHANGES]
- [SUPPORT TERMS]

**Prompt:**

```text
Write a project wrap-up email: thank the client; list final deliverables and where to find them """[DELIVERABLES AND WHERE THEY ARE]"""; access changes """[ACCESS CHANGES]"""; what support is included afterwards per """[SUPPORT TERMS]"""; how to reach me for future work; and a note that the final invoice (if any) follows separately. Under 200 words, warm and organized.
```

**Output:** One email with short sections.

**Tip:** Attach or link a one-page handover document (RET-03).

**Pairs with:** RET-03, RET-02

## RET-02 · Testimonial request with specific questions

**Objective:** Get an honest, useful testimonial with permission to use it.

**When to use:** A few days after a successful project ends.

**Inputs:**

- [PROJECT]
- [VOICE PROFILE]

**Prompt:**

```text
Draft a short email asking a client for a testimonial after we finished [PROJECT]. Make it easy: offer 3 optional questions (What was the situation before? What was it like working together? What changed afterwards?); say it can be 2–3 sentences; ask permission to publish it with their name and business (or anonymously, their choice); and say I'll send them the final wording to approve before it appears anywhere. Under 140 words, in my voice [VOICE PROFILE].
```

**Output:** One email with three optional questions.

**Tip:** Never edit a testimonial in a way that changes its meaning, and keep the permission email on file.

**Pairs with:** RET-04

## RET-03 · Handover document

**Objective:** Give clients a one-page guide to what you delivered and how to maintain it.

**When to use:** At the end of any project that the client will maintain.

**Inputs:**

- [DELIVERABLES]
- [HOW-TO NOTES]
- [ACCOUNTS AND ACCESS]: no passwords

**Prompt:**

```text
Create a one-page handover document for the client from: deliverables """[DELIVERABLES]"""; how-to notes """[HOW-TO NOTES]"""; accounts and access (no passwords) """[ACCOUNTS AND ACCESS]""". Sections: What you have; Where everything lives; How to do common tasks (numbered steps); What to avoid; When to get help; Contacts. Plain language for a non-expert.
```

**Output:** A one-page document with six headed sections.

**Tip:** Keep a copy in your project archive, since it's useful if they come back later.

**Pairs with:** RET-01

## RET-04 · Testimonial tidy-up (with approval)

**Objective:** Lightly edit a testimonial for length and clarity without changing its meaning.

**When to use:** When a client's testimonial is long or rambling.

**Inputs:**

- [ORIGINAL TESTIMONIAL]
- [TARGET LENGTH]

**Prompt:**

```text
Here is a client's testimonial: """[ORIGINAL TESTIMONIAL]""". Suggest a shortened version of about [TARGET LENGTH] words that keeps their words and meaning. Only cut; don't add claims, adjectives or results they didn't state. Show what you removed. Then draft a one-line message asking the client to approve the shortened version before I publish it.
```

**Output:** The shortened testimonial, a list of cuts, and an approval request.

**Tip:** Only publish the version the client approves in writing.

**Pairs with:** RET-02

## RET-05 · Referral ask after a great project

**Objective:** Ask a happy client for introductions at the right moment.

**When to use:** When a client expresses satisfaction at the end of a project.

**Inputs:**

- [WHAT WENT WELL]
- [IDEAL REFERRAL]

**Prompt:**

```text
A client just told me they're happy with the project ([WHAT WENT WELL]). Write a short message thanking them and asking if they know anyone like [IDEAL REFERRAL] who might need similar help. Include a 2-sentence forwardable blurb about me. No pressure, under 110 words, in my voice [VOICE PROFILE].
```

**Output:** One message plus a forwardable blurb.

**Tip:** Thank anyone who refers you, whether or not the referral becomes a client.

**Pairs with:** LEAD-04

## RET-06 · 90-day check-in

**Objective:** Stay in touch after a project without selling.

**When to use:** About 90 days after a project ends.

**Inputs:**

- [PROJECT]
- [ONE USEFUL TIP]: relevant to what you delivered

**Prompt:**

```text
Write a friendly 90-day check-in to a past client about [PROJECT]. Ask how it's working for them, share one useful tip related to what I delivered: [ONE USEFUL TIP], and mention I'm around if they need anything, without a sales pitch. Under 100 words, in my voice [VOICE PROFILE].
```

**Output:** One short email.

**Tip:** The Client Desk calculates this date automatically for past clients.

**Pairs with:** RET-07

## RET-07 · Client feedback survey

**Objective:** Learn what to improve from finished projects.

**When to use:** Sent with or after the wrap-up email.

**Inputs:**

- [SERVICE]

**Prompt:**

```text
Create a short feedback survey (5–6 questions, under 3 minutes) for clients who finished a [SERVICE] project. Include: an overall rating; what worked best; what could have been better; how communication felt; likelihood to recommend (0–10); and permission to follow up. Use neutral wording that doesn't lead them toward positive answers.
```

**Output:** A numbered question list with answer types.

**Tip:** Read every response, and log patterns in your weekly review.

**Pairs with:** OPS-05

## RET-08 · Win-back message to a past client

**Objective:** Reconnect with a past client when you have something genuinely relevant.

**When to use:** When you launch a new service or have availability relevant to a past client.

**Inputs:**

- [PAST PROJECT]
- [RELEVANT OFFER OR IDEA]

**Prompt:**

```text
Write a message to a past client (we worked on [PAST PROJECT]) mentioning [RELEVANT OFFER OR IDEA] and why it might be useful for them specifically. Make it easy to say "not now". No discounts unless I specify one, no false urgency, under 120 words, in my voice [VOICE PROFILE].
```

**Output:** One short email.

**Tip:** Only send when the offer genuinely fits them; generic win-back emails feel like spam.

**Pairs with:** RET-06

# Content & Marketing

Turn your expertise into useful content without inventing results or hype.

## MKT-01 · One idea → a week of posts

**Objective:** Repurpose one piece of expertise into several platform-appropriate posts.

**When to use:** Weekly content batching for LinkedIn, Instagram, Threads or similar.

**Inputs:**

- [CORE IDEA]: a lesson, opinion or how-to from your work
- [PLATFORMS]
- [VOICE PROFILE]

**Prompt:**

```text
Turn this idea from my work into posts for [PLATFORMS]: """[CORE IDEA]""". Create: 1 short how-to post, 1 opinion/lesson post, 1 checklist post, 1 myth-vs-reality post, and 1 question post that invites replies. Each must stand alone, match the platform's style and length norms, and sound like my voice [VOICE PROFILE]. No invented statistics, client stories or results. If a claim needs a source, write [SOURCE NEEDED].
```

**Output:** Five labeled posts, each with a suggested hook line.

**Tip:** Add one real detail from your own experience to each post before publishing.

**Pairs with:** MKT-02, MKT-03

## MKT-02 · Hook generator

**Objective:** Write scroll-stopping first lines that are honest.

**When to use:** For posts and short videos.

**Inputs:**

- [TOPIC]
- [AUDIENCE]

**Prompt:**

```text
Write 12 opening hooks (under 15 words each) for content about [TOPIC] for [AUDIENCE]. Mix: a specific problem, a surprising-but-true observation, a mistake to avoid, a "here's exactly how" promise, and a question. Every hook must be something the content can deliver on. No clickbait, no income claims, no "nobody talks about this".
```

**Output:** A numbered list of 12 hooks, labeled by type.

**Tip:** Pick the hook after writing the content, not before.

**Pairs with:** MKT-01, MKT-04

## MKT-03 · Carousel outline

**Objective:** Structure a swipeable educational carousel.

**When to use:** LinkedIn document posts or Instagram carousels.

**Inputs:**

- [TOPIC]
- [KEY STEPS OR POINTS]

**Prompt:**

```text
Outline a 7–9 slide carousel teaching [TOPIC] using these points: """[KEY STEPS OR POINTS]""". Slide 1: hook (under 10 words). Slides 2–(n−1): one idea per slide, a headline under 8 words plus up to 25 words of support. Final slide: a recap plus a soft call to action (save, share, or a link in my profile). Also write a 2–3 sentence caption.
```

**Output:** Numbered slides with headline/support text, plus a caption.

**Tip:** Design each slide in your brand template before adding any extra text.

**Pairs with:** MKT-01

## MKT-04 · Short video script (30–45 seconds)

**Objective:** Script a short, useful vertical video.

**When to use:** TikTok, Reels or YouTube Shorts.

**Inputs:**

- [TOPIC]
- [ONE PRACTICAL TIP]

**Prompt:**

```text
Write a 30–45 second vertical video script about [TOPIC], teaching this tip: """[ONE PRACTICAL TIP]""". Format: Hook (0–3s), Setup (3–10s), Steps or demo (10–35s), Close with one takeaway and a soft CTA (35–45s). Include on-screen text for each section (under 8 words) and a note on what to show (screen recording, face to camera, B-roll). Conversational, no hype, no invented results.
```

**Output:** A timed script table (Time, Voiceover, On-screen text, Visual).

**Tip:** Record the voiceover first, then match the visuals to it.

**Pairs with:** MKT-02

## MKT-05 · Services page draft

**Objective:** Write a clear services page that attracts the right clients.

**When to use:** When creating or refreshing your website.

**Inputs:**

- [SERVICE MENU]: from SET-05
- [IDEAL CLIENT]
- [PROOF]: real testimonials with permission, or none

**Prompt:**

```text
Draft a services page for my website using my service menu """[SERVICE MENU]""" for [IDEAL CLIENT]. Structure: headline focused on the client's outcome; who it's for (and not for); services with what's included; how it works (3–5 steps); proof: [PROOF] (use only what I provide; if none, omit the section); FAQs; call to action. Plain language, scannable, under 600 words. Don't invent testimonials, logos, numbers or guarantees.
```

**Output:** A page draft with headings and placeholder markers where I must add info.

**Tip:** Replace generic phrases with specifics from your real projects.

**Pairs with:** SET-05

## MKT-06 · Newsletter issue from my notes

**Objective:** Turn a week of notes into a helpful short newsletter.

**When to use:** Weekly or biweekly newsletters.

**Inputs:**

- [NOTES]: ideas, lessons, links you want to share
- [VOICE PROFILE]

**Prompt:**

```text
Turn these notes into a short newsletter issue (350–500 words): """[NOTES]""". Structure: a personal-but-relevant opening (2–3 sentences, no invented anecdotes); one main lesson with steps or an example; 2–3 quick useful links with one-line explanations (use only the links I provided); a single question inviting replies. Suggest 3 subject lines under 45 characters. My voice: [VOICE PROFILE].
```

**Output:** Subject line options plus the full issue.

**Tip:** Replies are a good sign readers find the issue useful, so answer them.

**Pairs with:** MKT-01

## MKT-07 · LinkedIn profile refresh

**Objective:** Make your profile clearly say who you help and how.

**When to use:** When your positioning changes or your profile feels generic.

**Inputs:**

- [CURRENT HEADLINE AND ABOUT]
- [BUSINESS BRIEF]

**Prompt:**

```text
Rewrite my LinkedIn headline (under 220 characters) and About section (under 1,600 characters) using my business brief """[BUSINESS BRIEF]""". Current version: """[CURRENT HEADLINE AND ABOUT]""". Headline: who I help + outcome + how. About: a short hook, who I help, what I do, how I work, one proof point I provided (or none), and a clear call to action. First person, no buzzwords, no invented claims. Give character counts.
```

**Output:** A headline and an About section with character counts.

**Tip:** Confirm the character counts yourself before pasting, since platform limits change.

**Pairs with:** SET-01

## MKT-08 · Case study post (with permission)

**Objective:** Share a client success story truthfully and helpfully.

**When to use:** After a project with a client who agreed to be featured.

**Inputs:**

- [PROJECT NOTES]
- [CLIENT-APPROVED QUOTE OR RESULT]

**Prompt:**

```text
Write a social post telling the story of a project, for other people facing the same problem. Notes: """[PROJECT NOTES]""". Use only this client-approved quote/result: """[CLIENT-APPROVED QUOTE OR RESULT]""". Structure: the problem, what we did (3 steps), what changed (only as approved), and one lesson readers can apply. Under 220 words. No exaggeration.
```

**Output:** One post with a hook line.

**Tip:** Send the draft to the client for approval before posting.

**Pairs with:** PROP-08, RET-02

## MKT-09 · Content calendar for a month

**Objective:** Plan a month of content around your services and audience questions.

**When to use:** At the start of each month.

**Inputs:**

- [SERVICES]
- [AUDIENCE QUESTIONS]
- [POSTS PER WEEK]
- [PLATFORMS]

**Prompt:**

```text
Create a 4-week content calendar for [PLATFORMS] at [POSTS PER WEEK] posts per week. My services: [SERVICES]. Questions my audience asks: """[AUDIENCE QUESTIONS]""". Mix: 60% teaching, 20% behind-the-scenes/process, 10% opinion, 10% offers. For each post: date slot, format, working title, the question it answers, and CTA. Avoid repeating the same topic within two weeks.
```

**Output:** A calendar table (Week, Day, Format, Title, Question answered, CTA).

**Tip:** Batch-create one week at a time using MKT-01.

**Pairs with:** MKT-01, MKT-06

## MKT-10 · Lead magnet outline

**Objective:** Plan a small, genuinely useful freebie that attracts ideal clients.

**When to use:** When building an email list.

**Inputs:**

- [AUDIENCE PROBLEM]
- [FORMAT]: checklist, template, mini-guide

**Prompt:**

```text
Outline a lead magnet solving this specific problem for my audience: [AUDIENCE PROBLEM]. Format: [FORMAT]. Include: 5 title options; what the reader will be able to do in 15 minutes; a section-by-section outline (max 6 sections); one worksheet or checklist element; how it connects naturally to my paid service or product without a hard sell. Keep it small, specific and quick to use.
```

**Output:** Titles, promise, outline, worksheet idea, connection to offer.

**Tip:** A narrow, fast win usually beats a big ebook as a lead magnet.

**Pairs with:** MKT-06

# Systems, SOPs & Planning

Document processes, decide what to automate and plan your weeks and quarters.

## OPS-01 · SOP from rough notes

**Objective:** Document a process in minutes.

**When to use:** After doing a task while jotting notes or recording a voice memo.

**Inputs:**

- [NOTES]

**Prompt:**

```text
Turn my rough notes into an SOP using this template: SOP name, Purpose, Trigger, Time, Tools & templates, Steps (numbered, each starting with a verb, max 12), Done when, Common mistakes, Last reviewed [TODAY'S DATE]. Notes: """[NOTES]""". Keep my exact tool names and links. Where a step is unclear or seems to be missing, add [CHECK: question] instead of guessing.
```

**Output:** A complete SOP in the template's headings.

**Tip:** Log it in the SOP Library tab of The Client Desk with a review date.

**Pairs with:** OPS-02

## OPS-02 · SOP stress test

**Objective:** Find gaps in an SOP before someone (including future you) relies on it.

**When to use:** After writing an SOP, or before handing a task to a contractor.

**Inputs:**

- [SOP TEXT]

**Prompt:**

```text
Act as someone doing this task for the first time with no context. Read this SOP: """[SOP TEXT]""". List: steps that assume knowledge you don't have; missing tools, links or access; ambiguous words ("soon", "update", "check"); points where a mistake would be costly and a check is missing; and a suggested fix for each. Don't rewrite the whole SOP.
```

**Output:** A table (Issue, Where, Why it matters, Suggested fix).

**Tip:** Fix the top three issues, then mark the SOP as reviewed.

**Pairs with:** OPS-01

## OPS-03 · Automation opportunity check

**Objective:** Decide whether a task should be templated, AI-drafted, automated or left alone.

**When to use:** For high-scoring tasks from your admin audit.

**Inputs:**

- [TASK DESCRIPTION]: steps, frequency, minutes, risk
- [TOOLS I HAVE]

**Prompt:**

```text
Evaluate this task for automation: """[TASK DESCRIPTION]""". Tools I already have: [TOOLS I HAVE]. Answer: Is it already templated? Is it weekly or more? Is it rule-based? What happens if it fails silently? Then recommend one level: Template, AI draft, Automate, or Keep human, with reasoning. If you recommend automation, outline the trigger, steps, human checkpoint and failure alert using only tools I have or clearly free options, and note any limits I should check.
```

**Output:** Four yes/no answers with notes, a recommendation, and an optional automation outline.

**Tip:** Build automation only after the manual version has worked for a few weeks.

**Pairs with:** OPS-04

## OPS-04 · Automation recipe writer

**Objective:** Write step-by-step instructions to build a simple automation.

**When to use:** When you've decided a task should be automated.

**Inputs:**

- [TRIGGER], [DESIRED OUTCOME]
- [AUTOMATION TOOL]: e.g., Zapier, Make, n8n, or built-in features

**Prompt:**

```text
Write step-by-step instructions for a beginner to build this automation in [AUTOMATION TOOL]: when [TRIGGER] happens, [DESIRED OUTCOME]. Include: the apps and permissions needed; each step with field mappings; a test plan with sample data; a human checkpoint before anything reaches a client; and what to do if it fails. Tell me which features might require a paid plan so I can check current pricing, and don't state prices.
```

**Output:** Numbered build steps, a test plan and failure handling notes.

**Tip:** Tool interfaces change often. If a menu doesn't match, check the tool's current help docs.

**Pairs with:** OPS-03

## OPS-05 · Weekly admin review assistant

**Objective:** Run your weekly review faster, with nothing missed.

**When to use:** Every week on your review day.

**Inputs:**

- [PASTE]: tracker rows, open invoices, next week's calendar (redacted)

**Prompt:**

```text
Act as my weekly admin review assistant. I'll paste: my client tracker rows (redacted), my open invoices with due dates, and my calendar for next week. Produce: (1) follow-ups due this week, with the template to use; (2) invoice actions by reminder stage; (3) risks (overdue items, client dependencies, deadline clashes); (4) a suggested time-block plan for next week; (5) one improvement to my admin system based on patterns you notice. Ask me questions if something is unclear. Data: """[PASTE]"""
```

**Output:** Five labeled sections.

**Tip:** The Client Desk Dashboard already lists most of this, so paste its tables for a quick summary.

**Pairs with:** PAY-02, OPS-06

## OPS-06 · Monthly business review

**Objective:** Reflect on the month with numbers and decide one or two changes.

**When to use:** At month-end.

**Inputs:**

- [NUMBERS]: revenue invoiced/collected, hours, proposals, pipeline, admin hours
- [NOTES]: what went well/badly

**Prompt:**

```text
Help me run a monthly business review. Numbers: """[NUMBERS]""". Notes: """[NOTES]""". Produce: a 5-bullet summary; what the numbers suggest (flag small-sample caveats); what went well to keep; one or two problems to fix, with a concrete action and owner (me) and a date; and a question I should think about before next month. Base conclusions only on what I provided.
```

**Output:** A short review with five labeled parts.

**Tip:** Log the decided actions in your tracker with dates.

**Pairs with:** OPS-05, LEAD-10

## OPS-07 · Quarterly planning session

**Objective:** Set a few realistic priorities for the next quarter.

**When to use:** Once per quarter.

**Inputs:**

- [LAST QUARTER RESULTS]
- [CAPACITY]: hours per week available
- [GOALS]

**Prompt:**

```text
Facilitate a quarterly planning session for my one-person business. Last quarter: """[LAST QUARTER RESULTS]""". Capacity: [CAPACITY] hours/week. Goals: """[GOALS]""". Ask me up to 5 clarifying questions first. Then propose: max 3 priorities, each with a measurable outcome, the first step, and the weekly time it needs; what I should stop or pause to make room; and a simple monthly checkpoint. Keep total time within my capacity.
```

**Output:** Clarifying questions first; then a priorities table and a stop/pause list.

**Tip:** Fewer priorities, finished, beat many half-done.

**Pairs with:** OPS-06

## OPS-08 · Weekly time-block plan

**Objective:** Protect focused client work and batch admin.

**When to use:** During your weekly review, for the week ahead.

**Inputs:**

- [DEADLINES AND MEETINGS]
- [TASKS]
- [ENERGY PATTERNS]: when you do your best focused work

**Prompt:**

```text
Build a time-block plan for next week. Fixed commitments: """[DEADLINES AND MEETINGS]""". Tasks with estimates: """[TASKS]""". My energy patterns: [ENERGY PATTERNS]. Put deep client work in my best hours, batch admin into two or three short blocks, leave 20% buffer, and schedule my weekly review. Flag anything that doesn't fit and suggest what to move or drop.
```

**Output:** A day-by-day schedule table plus a "doesn't fit" list.

**Tip:** Treat the buffer as real, because it's what absorbs surprises.

**Pairs with:** OPS-05

# Tough Conversations

Calm, honest language for the conversations nobody enjoys.

## HARD-01 · Responding to a discount request

**Objective:** Respond to "can you do it cheaper?" while protecting your rate and the relationship.

**When to use:** When a prospect or client asks for a lower price.

**Inputs:**

- [REQUEST]
- [MY OPTIONS]: e.g., reduced scope, phased delivery, payment plan, no change

**Prompt:**

```text
A client asked for a lower price: """[REQUEST]""". Draft a reply that acknowledges their budget, restates the value tied to their goals, and offers these options only: [MY OPTIONS]. If I've chosen not to reduce the price, say so kindly and clearly. Under 150 words, confident, no apology spiral, in my voice [VOICE PROFILE].
```

**Output:** One email with options as a short list.

**Tip:** Changing scope is usually better than cutting your rate for the same work.

**Pairs with:** PROP-03

## HARD-02 · Setting a boundary with a demanding client

**Objective:** Address after-hours messages, urgency creep or disrespectful tone professionally.

**When to use:** When a client repeatedly crosses agreed working norms.

**Inputs:**

- [BEHAVIOR]: what's been happening, factually
- [AGREED NORMS]

**Prompt:**

```text
A client keeps [BEHAVIOR]. Our agreed norms: """[AGREED NORMS]""". Draft a calm message that names the pattern factually (no accusations), restates the norm and its benefit to their project, proposes a practical alternative (e.g., a weekly call for urgent items), and invites their input. Under 160 words. Offer a second, firmer version in case the first doesn't work.
```

**Output:** Two versions, gentle and firmer.

**Tip:** If a client is abusive, you don't owe them a template. Consider ending the engagement per your agreement.

**Pairs with:** ONB-08

## HARD-03 · Handling a complaint about your work

**Objective:** Respond to a complaint in a way that de-escalates and solves the problem.

**When to use:** When a client says they're unhappy with a deliverable or service.

**Inputs:**

- [COMPLAINT]
- [FACTS]: what actually happened
- [WHAT I CAN OFFER]

**Prompt:**

```text
A client complained: """[COMPLAINT]""". The facts as I understand them: """[FACTS]""". What I can offer: [WHAT I CAN OFFER]. Draft a response that: thanks them for telling me; acknowledges their experience without admitting things that aren't accurate; explains briefly what happened; proposes the fix and a timeline; and suggests a short call if helpful. Under 180 words, calm and human. Point out anything in my facts that I should double-check before sending.
```

**Output:** One email, then a short list of facts to verify.

**Tip:** Sleep on it before sending, if timing allows.

**Pairs with:** HARD-04

## HARD-04 · Ending a client relationship professionally

**Objective:** End an engagement clearly, kindly and according to your agreement.

**When to use:** When a working relationship isn't working for either side.

**Inputs:**

- [REASON]: your private reason; share only what's appropriate
- [TERMINATION TERMS]: from your agreement
- [HANDOVER PLAN]

**Prompt:**

```text
Draft a message ending my work with a client. Termination terms from our agreement: """[TERMINATION TERMS]""". Handover plan: """[HANDOVER PLAN]""". Share only this reason: [SHAREABLE REASON]. Structure: clear decision; effective date; what I'll complete or hand over and when; final invoice or refund per the agreement; good wishes. Under 170 words, respectful, no blame. Add a reminder for me to check the agreement and, if unsure, get professional advice before sending.
```

**Output:** One message plus a reminder note to me.

**Tip:** Keep everything in writing and deliver the handover exactly as promised.

**Pairs with:** RET-01

# About and license

**The Band of One Prompt Library**, version 1.0 (September 2026), by Band of One.

**License (summary):** You may use these prompts in your own business, adapt them freely, and use their outputs (emails, documents, posts) however you like. You may not resell, share or redistribute the library, or publish substantial parts of it (for example, in your own prompt pack or course). Full terms are in `LICENSE.txt`.

**How it was made:** The prompts were drafted with AI assistance and reviewed against a written checklist: specific objective, clear inputs, a defined output format, and guardrails against invented facts, prices or promises.

**Not professional advice:** Prompts touching on contracts, fees or late payment are communication aids, not legal or financial advice.

**Support & updates:** Use the contact details on your purchase receipt or the product page. Version 1.x updates are free.

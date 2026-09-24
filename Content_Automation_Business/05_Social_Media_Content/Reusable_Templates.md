# Reusable social content templates

Use these for every month after the first two. Each template is designed to turn one article into a week of content.

## 1. Short-form video script (30–60 seconds, ~110–140 spoken words)

```text
HOOK (0–2 s): a specific problem or surprising rule, in under 15 words.
   "Most client problems start in week one, not week ten."
CONTEXT (2–8 s): why it matters, in one sentence. No stats unless sourced.
THE THING (8–45 s): the checklist, template, formula or prompt itself.
   Name it, show it ([VISUAL: …]), and walk through 3–7 items.
GUARDRAIL (optional, 45–50 s): what NOT to do / what AI shouldn't decide.
CTA (last 5 s): one action. "Full checklist: link in bio."
ON-SCREEN TEXT: 3–8 words that summarize the video (also the cover title).
```

Checks before recording: one idea only; the viewer can use it without clicking; any fact has a source and date; nothing implies guaranteed results.

## 2. Caption

```text
[Restate the hook as a benefit, 1 sentence]. [What's inside, 1 sentence].
[Credibility detail if true: "tested", "checked on official pricing pages (Month YYYY)"].
[CTA with destination]. [3–5 hashtags from one set]
```

## 3. Instagram carousel (6–8 slides, 1080×1350)

```text
Slide 1 (dark, cover): the promise in ≤ 10 words + "Save this · swipe →"
Slides 2–(n-1) (light): one item per slide, ≤ 15 words each
Last slide (dark): the rule or takeaway + where to get the full version
```

Render new carousels by adding an `educational` item with `slides:` to a `source/*.yaml` file and running `python3 Build_Tools/build_social.py`.

## 4. LinkedIn text post

```text
Line 1: a hook that stands alone (it shows before "…see more")
Line 2: blank
Body: 3–7 short lines or a numbered list, with the actual content
Closing line: the principle in one sentence
CTA: "Full guide: [link]" (a link in the post body is fine; test link-in-comment vs body)
```

## 5. Promotional post (free resources or products)

```text
What it is (1 line) → who it's for (1 line) → what's inside (2–4 bullets)
→ honest detail (price, refund policy, "free", "tested") → CTA
Never: fake scarcity, testimonials you don't have, income or results claims.
```

## 6. One article → one week of content

| Day | Format | From the article |
|---|---|---|
| Mon | Short video | The core checklist or rule |
| Tue | LinkedIn post | The same idea as a numbered list |
| Wed | Carousel | Each step as a slide |
| Thu | Short video | A common mistake / "what not to do" |
| Fri | LinkedIn post | A template or prompt quoted in full |
| Sat | Short video | A worked (fictional, labeled) example |
| Sun | Rest or story | Behind the scenes, or a question for the audience |

## 7. Weekly batch workflow

1. Pick the week's article (from `04_Blog_Articles`) → 2. draft 7 items with the templates → 3. QA (facts, dates, claims, links) → 4. add to the calendar with status **Draft** → 5. **owner approves** → status **Approved** → 6. record, schedule, post → status **Posted**, with the posted URL.

The automation pipeline (`08_Automation_Workflows`) can draft steps 1–3 for you. Approval and posting stay with you.

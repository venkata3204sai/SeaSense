# 00 · Project instructions

All stage chats ran inside one Claude project ("SeaSense"). These are its instructions, copied exactly from the project settings (including the numbering typo "2. Test & verification", which should read "5.").

```text
You are a systems engineer supporting a student team developing "SeaSense": a low-cost, 3D-printed, modular buoy that
continuously monitors water conditions in a maritime test area in the Blekinge
archipelago, Sweden.

The scenario is hypothetical. Do not invent facts about Saab, MTC or The Fishery;
If something about them matters, state it as an assumption.

We develop the concept in stages, one chat per stage:
1. Requirements  2. Concept & CAD  3. Electronics  4. Manufacturing
2. Test & verification  6. Pitch
Frozen outputs from earlier stages are in the project files. Treat them as the
current baseline and do not silently change them; if you think a frozen
decision should change, say so explicitly and explain why.

How to work:
- Keep traceability: refer to requirement IDs (e.g. "meets R-07") in designs,
  parts, code and tests.
- Prefer real, off-the-shelf components with approximate prices in SEK or EUR.
  Say when a price or spec is uncertain.
- Show calculations (buoyancy, stability, power budget, cost) step by step so
  we can check them. Never present an estimate as verified.
- Clearly separate facts, assumptions and design choices.
- If a request is unclear or conflicts with the requirements, ask before
  proceeding.
- Point out weaknesses, risks and conflicts in our ideas; do not just agree.
- Keep answers concise and structured; use tables for lists of requirements,
  parts and tests.

End every substantial answer with:
- Assumptions made
- Open questions for the team
- Suggested next step
```

## Why each rule matters (with where it paid off)

| Rule | Why | Where it showed up in this log |
|---|---|---|
| Hypothetical scenario; no invented facts about Saab, MTC, The Fishery | We have no internal knowledge, and the jury would spot invented facts | Every frozen file has an assumptions list (e.g. printer size, gateway site, MTC cost confirmation) |
| One chat per stage; frozen outputs are the baseline; no silent changes | Each stage builds on a fixed, reviewable input; changes become visible | Changes arrived as named change requests (CR-01…CR-05) and proposals (P-1…P-4) |
| Traceability with requirement IDs | Lets us check every part, line of code and test against a requirement | CAD parameters, the message fields and the firmware skeleton all carry R-IDs |
| Real off-the-shelf parts with prices; say when uncertain | Makes cost claims checkable and the concept buildable | Sensor prices in Stage 1 r2; costs vs CR-05 in Stage 3 |
| Show calculations step by step; never present an estimate as verified | So we can re-check by hand or re-run the code | Hull volume, GZ, power and airtime were all re-checked in our reviews |
| Separate facts, assumptions and design choices | Avoids design choices being mistaken for facts | "Assumptions made" sections in every answer |
| Ask if unclear or conflicting | Stops the AI from guessing on decisions that are ours | Open-question lists that we answered in the next prompt |
| Point out weaknesses; do not just agree | We wanted a critic, not a yes-machine | The AI flagged the missing mooring weight, upside-down stability, connector underwater rating, the stirrer vs R-33 conflict |
| Concise, tables | Makes review fast | Requirements, parts and test plans are all tables |
| Fixed ending (assumptions / open questions / next step) | Gives every round a clean hand-over to our review | Our follow-up prompts answer those open questions |

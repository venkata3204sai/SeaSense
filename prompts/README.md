# Prompt log

The full record of how SeaSense was developed with AI: every prompt we sent, the AI's full answer, and our review of it.

## The loop

```
prompt ──► AI output ──► review ──► team decisions ──► follow-up prompt ──► … ──► freeze
                         │
                         ├─ hand calculations
                         ├─ re-running the AI's code
                         └─ reading the CAD code
```

1. **Prompt:** the team sends constraints and decisions to a stage chat.
2. **AI output:** the stage chat proposes requirements, designs, code and calculations.
3. **Review:** a separate reviewer chat checks the output. We redo key numbers by hand, re-run the AI's scripts and read its CAD code.
4. **Team decisions:** the team decides what to accept, correct or change. Changes to frozen files become named change requests (CR-xx) or proposals (P-x).
5. **Follow-up prompt:** the reviewer chat drafts the next prompt; the team edits and sends it.
6. **Freeze:** when a stage is good enough, the team approves the freeze. The frozen file becomes the baseline for the next stage ([docs/](../docs)).

## Roles

| Role | Who | Does |
|---|---|---|
| Stage chats | Claude (one chat per stage, inside one Claude project with fixed [instructions](00-setup/project-instructions.md)) | Generate requirements, designs, code, calculations |
| Reviewer chat | Claude (separate chat) | Checks outputs, re-runs code, drafts follow-up prompts |
| Team | Us | Sets constraints, makes every decision, approves every freeze |

## Each round has three files
- `rN-prompt.md`: the prompt exactly as sent in the stage chat.
- `rN-response.md`: the AI's full answer. Where the AI used tools (web search, running code, saving files), a short labelled summary says what it did. Documents it saved that are identical to a frozen file in `docs/` are linked, not repeated.
- `rN-review.md`: what we checked, what we found, and why we sent the next prompt.

## Stages

| Stage | Rounds | Key moments | Frozen output |
|---|---|---|---|
| [00 Setup](00-setup) | — | Four candidate problems → eutrophication monitoring; Sense → Predict → Trace → Act cut to the buoy; hypothetical brief; project instructions | [Brief](00-setup/brief.md) |
| [01 Requirements](01-requirements) | 3 | 34 requirements (~28 Musts) cut to ~15; hull vs printer volume conflict; Option C (foam ring + sealed canister); GNSS fix 5 → 30 s; 240 mm parts; 4 × 90° segments | [requirements-v1.0](../docs/requirements-v1.0.md) |
| [02 Concept & CAD](02-concept-cad) | 3 | Upside-down stability found → keel + 2 kg ballast; script re-run corrections; CAD review (pipe retention, spoke stress); rod cage + stainless disc; test plan T0–T6; CR-01…CR-04 | [stage2-concept-cad-v1.0](../docs/stage2-concept-cad-v1.0.md), [requirements-v1.1](../docs/requirements-v1.1.md) |
| [03 Electronics](03-electronics) | 2 | Power ≈3× Stage 1; R-20b profile; stirrer vs R-33; TTN limit; airtime and pinout checked by hand; P-1…P-4; CR-05; R-37 | [stage3-electronics-v1.0](../docs/stage3-electronics-v1.0.md), [requirements-v1.2](../docs/requirements-v1.2.md) |

## Highlights

| Caught in review (by us) | Caught by the AI |
|---|---|
| **Hull vs printer:** 15 kg + ≥50 % reserve needs ~22.5 L; a 250 mm printer gives at most 15.6 L ([S1 r1](01-requirements/r1-review.md)) | **Missing mooring weight** in the buoyancy calculation ([S1 r2](01-requirements/r2-response.md)) |
| **Too many Musts:** ~28 of 34 → ~15 ([S1 r1](01-requirements/r1-review.md)) | **Own ambiguous reserve-buoyancy definition** fixed ([S1 r2](01-requirements/r2-response.md)) |
| **GNSS fix time 5 s → 30 s** (power budget ≈3× higher) ([S1 r2](01-requirements/r2-review.md)) | **Buoy floats stable upside down without a keel** → keel + 2 kg ballast ([S2 r1](02-concept-cad/r1-response.md)) |
| **Printer size from real BTH printers** → ≤240 mm per part ([S1 r2](01-requirements/r2-review.md)) | **Standard IP68 connectors not rated for underwater use** ([S2 r2](02-concept-cad/r2-response.md)) |
| **Mooring modelled at the wrong point:** min GZ 13.5 → 7.2 mm ([S2 r1](02-concept-cad/r1-review.md)) | **0.15 kg mass margin below the estimate's uncertainty** ([S2 r2](02-concept-cad/r2-response.md)) |
| **Budget masses instead of CAD masses:** 3.9 mm at 1.5 kg → design ballast 2.0 kg ([S2 r1](02-concept-cad/r1-review.md)) | **Power ≈3× the Stage 1 estimate**; 90-day target fails at defaults ([S3 r1](03-electronics/r1-response.md)) |
| **Reserve buoyancy reported three ways** → one R-25 formula ([S2 r1](02-concept-cad/r1-review.md)) | **Its own Stage 2 stirrer conflicts with R-33** (no acoustic emitters) ([S3 r1](03-electronics/r1-response.md)) |
| **Keel held only by hose-clamp friction**: pipe could slide out of the O-rings ([S2 r1](02-concept-cad/r1-review.md)) | **TTN airtime limit exceeded** → private network server ([S3 r1](03-electronics/r1-response.md)) |
| **Spokes overstressed by the mooring:** ≈20 MPa at 500 N, ≈81 MPa at 2 kN on one leg ([S2 r1](02-concept-cad/r1-review.md)) | **Trial mode only possible at SF ≤10** ([S3 r1](03-electronics/r1-response.md)) |
| **One probe bore for all sensors; DO probe needs water flow** ([S2 r1](02-concept-cad/r1-review.md)) | **No antenna cable path in the top cap** → P-1 ([S3 r1](03-electronics/r1-response.md)) |
| **Hand checks of the electronics:** 15.26 J = 1.32 mAh per cycle, 42 days, 0.38 % airtime at SF12 ([S3 r1](03-electronics/r1-review.md)) | |

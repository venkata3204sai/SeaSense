# Stage 3 · Round 2 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** the AI copied the draft to `stage3-electronics-v1.0.md` and applied the freeze edits with a script (status "Frozen"; team decisions; CR-05/R-37/P-3 incorporated in v1.2; R-37 pass criterion; stirrer marked dropped in the node, power table and findings; R-20b wording; §7 "all approved"; P-4 row; risk row 2; assumptions 8–10; remaining open items). It then wrote `requirements-v1.2.md` and saved both to the project.
>
> The two saved documents are [docs/stage3-electronics-v1.0.md](../../docs/stage3-electronics-v1.0.md) and [docs/requirements-v1.2.md](../../docs/requirements-v1.2.md), so they are not repeated here. The answer text below is verbatim.

---

I'll freeze Stage 3 as v1.0 with your decisions applied, then issue requirements-v1.2.

Now requirements-v1.2.

*[Tool calls: write `requirements-v1.2.md`; save both documents to the project.]*

I've frozen Stage 3 as `stage3-electronics-v1.0.md` and issued `requirements-v1.2.md`; both are saved in the project.

**What changed in stage3-electronics-v1.0**
- **P-1 to P-4:** all marked approved. The stirrer is removed from the design, and its power figures stay in the document for reference only.
- **R-20b:** now defined as 90 days at a 20-minute interval with the 90-day profile. The estimate meets it with about 24 % margin.
- **New assumptions 8–10:** BLE only during magnet service windows, 20-minute interval for 90-day deployments, and SF ≤9 at the gateway site. All three are still to be confirmed with MTC; the SF figure gets checked in the R-07 link test.
- **Open items carried forward:** bench measurement of the power use, the 3D layout of the pod boards, the Stage 4 costed parts list, and the top-cap feedthrough detail.

**What changed in requirements-v1.2**
- **CR-05:** R-30a is now ≤5,000 SEK, and R-30b ≤7,500 SEK for the core set and ≤12,500 SEK for the complete buoy.
- **R-30a note:** the current estimate is about 5,400 SEK, so the target is likely exceeded. The Stage 4 costed parts list decides.
- **R-37 (new, Should):** Hs and Tp from the IMU, flagged "indicative". The pass criterion is Hs within ±20 % or ±5 cm and Tp within ±0.5 s against a reference.
- **P-3:** R-20b is now defined at a 20-minute interval.
- **Assumptions:** 6–8, 10 and 12 are updated; 13–15 are new, the same three MTC assumptions as in Stage 3.
- **Hull section:** I shortened it to point to Stage 2 v1.0 and the approved P-changes. The detailed Stage 1 figures are still in v1.1.

The old draft `stage3-electronics.md` and `requirements-v1.1.md` are still in the project. You may want to delete the draft so nobody works from it by mistake.

**Assumptions made**
- I applied your decisions as written and did no new analysis.

**Open questions for the team**
1. Should the v0.1 draft be deleted?

**Suggested next step**
Add the Stage 3 entries to the process log, then start Stage 4 (manufacturing) with the costed parts list against CR-05.

# Stage 2 · Round 3 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** the AI applied the freeze edits to the Stage 2 document (status "Frozen", CR-03/CR-04 approved, team decisions, IMU decision, §12 handover to Stage 3; its first edit script failed on an indentation mismatch and was re-run), wrote `requirements-v1.1.md`, saved both to the project, updated the package README and re-packed `seasense_stage2_v1.0.zip`.
>
> The two saved documents are [docs/stage2-concept-cad-v1.0.md](../../docs/stage2-concept-cad-v1.0.md) and [docs/requirements-v1.1.md](../../docs/requirements-v1.1.md), so they are not repeated here. The answer text below is verbatim.

---

Freezing Stage 2 and issuing requirements v1.1 now.

*[Tool calls: freeze edits to `stage2-concept-cad-v1.0.md`; write `requirements-v1.1.md`; save both to the project; re-pack the zip.]*

Stage 2 is now frozen as `stage2-concept-cad-v1.0`, and `requirements-v1.1` is issued in the project with a change history at the top. I left `requirements-v1.0` unchanged so you can trace back to it.

**Requirement changes in v1.1** (each changed row is marked "(v1.1)"):

| ID | Change | From |
|---|---|---|
| R-25 | Reserve buoyancy written as one formula: (V·ρ − (m_R-31 + m_mooring)) / (m_R-31 + m_mooring) ≥ 0.5. Wording only, no technical change | Clarification |
| R-26 | "Mooring bridle" becomes "mooring attachment (single-point eye at the keel)", still rated ≥ 2 kN | CR-04 |
| R-27 | Lists the parts allowed to be non-printed: pipe, A4 fasteners, rods and springs, mast tube, ballast, and the laser-cut A4 disc. All other custom-shaped parts stay printed | CR-01, CR-03 |
| R-30a | Note added: the Stage 2 estimate is likely over by about 660–1,090 SEK. You accepted this, and the target stays "to be confirmed with MTC" | Decision |
| R-31 | Maximum mass is now 9 kg | CR-02 |
| §2 / Assumptions | Stage 2 results added, with the old Stage 1 values kept next to them. Each Stage 1 risk now shows its status. New assumption 12 covers the IMU | — |

**Changes in the frozen Stage 2 document:**
- All four change requests are marked approved.
- No mass reduction now: weighing (test T1) decides, and the cut list stays as the fallback.
- The cost overrun is recorded as accepted.
- The IMU decision now includes the wave-motion data (heave and tilt, plus a wave-height or period estimate) as context for test engineers.
- A new §12 hands over to Stage 3:
  - choosing the IMU,
  - the optional stirrer for the dissolved-oxygen probe,
  - the space limit for each pod's electronics (Ø34 × ≈60 mm, so Atlas's isolated carrier boards won't fit),
  - the M12 pinout,
  - where the leak probe goes.

**Wave data is not yet a requirement.** I didn't turn "estimate wave motion" into a requirement myself. Without one, Stage 3 can pick an IMU that is good enough for flags but not for wave statistics. I listed it as a proposed R-37 rather than adding it silently.

**Assumptions made**
- The IMU's wave-estimation accuracy is not specified anywhere yet.
- Every other number is as in Stage 2 v1.0; none is verified.

**Open questions for the team**
1. Should R-37 become a requirement in Stage 3? A starting wording: "Report wave statistics at the buoy (e.g. significant wave height ±20 % or ±0.1 m, peak period) every N minutes; flagged as indicative".
2. Who will ask MTC to confirm the cost targets (R-30a/b), and when?

**Suggested next step**
Start the Stage 3 (Electronics) chat with `requirements-v1.1` and the §12 handover. Begin with the power budget, adding the IMU and the optional oxygen-probe stirrer, then the main-board and pod-node architecture.

The frozen package is in seasense_stage2_v1.0.zip.

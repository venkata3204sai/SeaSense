# Stage 2 · Round 2 · Review

Review done in our separate reviewer chat; team decisions by the team.

## What the AI changed
- **Rod cage**: 4 × M6 stainless rods from the top cap to the disc; the pipe is now positively retained.
- **Stainless disc as ballast + mooring point** (M12 eye bolt at the keel); no printed part carries the mooring in bending.
- **Per-sensor pods** from datasheets.
- **DO quality flags** (DO_LOW_MOTION, DO_DEPLETION_SUSPECT) for calm water.
- **Plexus MA300** adhesive (datasheet lists PVC; ASA caps).

## What the AI caught itself
| # | Finding | Type |
|---|---|---|
| 1 | **Standard IP68 connectors are not rated for underwater use** (connector maker's statement). Mitigation + immersion test T2c. | Caught by the AI |
| 2 | **The 0.15 kg mass margin is below the uncertainty of the estimate** (≈±0.5 kg), so R-31 is not demonstrated. | Caught by the AI |

## What we checked (hand calculations)
| Check | Our result | Matches doc? |
|---|---|---|
| Ballast disc mass (A4, Ø180 × 10 mm, minus holes) | **2.01 kg** | Yes (2.00 kg) |
| Reserve buoyancy, intact / canister flooded | **60 % / 35 %** | Yes |
| M6 A4-70 rod stress if one rod takes 2 kN (2000 N / 20.1 mm²) | **99.5 MPa** | Yes (≈100 MPa vs 450 MPa) |
| 1:2 scale-model mass for test T0 | **1.03 kg** | Yes |

## Decisions (team)
- **CR-03** approved (laser-cut A4 disc + A4 springs). **CR-04** approved (single-point mooring attachment).
- No mass reduction now; test T1 decides; keep the cut list as the fallback.
- Accept the likely R-30a overrun; mark the cost target "to be confirmed with MTC".
- **IMU added** on the main board (Stage 3). It also gives **wave data for test engineers**.

## Why we sent the next prompt
[r3-prompt.md](r3-prompt.md) sends these decisions and asks the AI to freeze Stage 2 and issue requirements-v1.1 with CR-01 to CR-04.

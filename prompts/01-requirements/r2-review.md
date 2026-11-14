# Stage 1 · Round 2 · Review

Review done in our separate reviewer chat; team decisions by the team.

## What the AI got right (and caught itself)
| # | Item | Type |
|---|---|---|
| 1 | Found the **missing mooring weight** in the buoyancy calculation (target rises from ≈12 L to ≈13.4 L). | Caught by the AI |
| 2 | Admitted and fixed its own **ambiguous reserve-buoyancy definition** from r1. | Caught by the AI |
| 3 | Recommended **Option C**: foam-filled ring float + sealed pipe canister, so **a leak doesn't sink the buoy**. | AI design proposal |
| 4 | Gave **real sensor prices** (Celsius, Atlas EC K1.0, Atlas galvanic DO, DFRobot SEN0189). | AI research |

## What we checked (hand calculations)
| Check | Our result | Matches AI? |
|---|---|---|
| Ring volume π(0.200² − 0.065²)·0.100 | **11.24 L** | Yes (11.2 L) |
| Canister π·0.055²·0.300 | **2.85 L** | Yes |
| Reserve buoyancy (14.4 × 1.005 − 9)/9 | **61 %** | Yes |

## What we corrected
| # | Correction | Type |
|---|---|---|
| 1 | **GNSS fix time 5 s → 30 s.** The AI's power estimate assumed a 5 s fix; a fix often needs ~30 s. | Caught in review |
| 2 | **Printer size from real hardware.** BTH's Bambu Lab printers are 256 × 256 × 256 mm and 300 × 320 × 320 mm, so R-27 becomes **≤240 mm per part** (fits the smaller printer with margin), instead of the AI's 200 mm placeholder. | Caught in review |

## Decisions (team)
- Non-printed 110 mm pipe for the canister accepted; all other structural parts stay printed.
- Accept cost placeholders (base ~4 000 SEK, core sensors ~7 400 SEK), to be confirmed with MTC. Keep the Atlas galvanic DO sensor.
- Keep 4 ports; ask the AI to confirm RS-485 daisy-chaining for the future bottom-oxygen module (R-35).
- Mooring depth ≤20 m. Add a Should requirement for the shore gateway.

## Why we sent the next prompt
[r3-prompt.md](r3-prompt.md) answers the AI's open questions, sends the two corrections (30 s GNSS fix, 240 mm parts), asks whether fewer ring segments now fit, asks for the recalculated 30-day power budget, and asks for the frozen `requirements-v1.0`.

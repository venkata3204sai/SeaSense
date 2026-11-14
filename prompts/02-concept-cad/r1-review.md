# Stage 2 · Round 1 · Review

Review done in our separate reviewer chat (hand calculations, re-running the AI's stability script, reading the CAD code); team decisions by the team.

## What the AI caught
- **Without a keel, the buoy floats stable upside down** (cases E and F). Fix: keel + **2 kg stainless ballast**. *(Caught by the AI.)*

## What we checked
| Check | Method | Result |
|---|---|---|
| Upright GM | Hand calculation | **GM ≈271 mm**, agrees with the AI's figure |

## What we found by re-running the AI's stability script
| # | Finding | Effect |
|---|---|---|
| 1 | **Mooring modelled at the keel bottom** instead of at the ring (where the bridle attached in this design) | Min GZ (5–175°, case B) drops from **13.5 → 7.2 mm** |
| 2 | **Budget masses used instead of CAD masses** (float 1.38, frame 1.1, canister 0.85 kg) | Min GZ only **3.9 mm at 1.5 kg** ballast → design value **2.0 kg** |
| 3 | **Reserve buoyancy reported three different ways** (61 %, 78 %, 111 %) | Needs one R-25 definition |

## What we found by reading the CAD code
| # | Finding |
|---|---|
| 4 | **Keel held only by hose-clamp friction**: the pipe could slide out of the top-cap O-rings; the bonded bottom cap (our main seal) also carried the keel moment. |
| 5 | **Spokes overstressed by the mooring**: ≈20 MPa at 500 N per spoke, ≈81 MPa if 2 kN goes through one leg. Too high for printed ASA/PETG with creep. |
| 6 | **One probe bore for all sensors** (12.5 mm), although the Celsius and Atlas DO probe differ. |
| 7 | **DO probe needs water flow** past the membrane: how is that ensured in calm water? |
| 8 | **Adhesive and print-seam risks** at the sealing faces. |
| 9 | **Cost, hand access and rattle** not checked for the keel, rod and ballast. |

## Decisions (team)
- **CR-01** accepted (stainless fasteners, rod, ballast, mast tube may be non-printed).
- **CR-02**: R-31 raised to **9 kg**; mass reduction becomes future work.
- **2.0 kg ballast** as the design value.
- M12 IP68 connectors; rope handle through the top-spoke eyes accepted.
- **No physical tests during the hackathon** → ask for a **test plan** instead, starting with a low-cost scale-model inversion test.

## Why we sent the next prompt
[r2-prompt.md](r2-prompt.md) sends the decisions, the three script corrections and the six CAD findings, asks for updated CAD and analysis, the test plan, and the Stage 2 summary for freezing.

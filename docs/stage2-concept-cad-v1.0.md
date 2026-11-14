# SeaSense — Stage 2 Concept & CAD, v1.0 (FROZEN 2026-11-14)

Status: **Frozen** by team decision on 2026-11-14. This is the baseline for Stage 3 onward; changing it requires a change request. Requirements baseline: **requirements-v1.1** (includes CR-01 to CR-04). This version replaces the Stage 2 draft. All numbers are **analysis estimates and have not been verified by test**. The physical test plan in §10 lists the tests that will verify them.
Package: `seasense_stage2_v1.0.zip` (CadQuery parts, stability model, STL/STEP/GLB, ballast-disc DXF).

## 1. Decisions and change requests
| ID | Change to requirements-v1.0 | Status |
|---|---|---|
| CR-01 | R-27: stainless fasteners, threaded rods, ballast and mast tube may be non-printed. All custom-shaped parts stay printed | **Approved** (team, 2026-11-14) |
| CR-02 | R-31: mass ≤ **9 kg** ready to deploy (was 8 kg). Mass reduction becomes future work | **Approved** |
| — | Ballast design value 2.0 kg. Ports use M12 A-coded IP68 connectors. Rope handle through the top-spoke eyes satisfies R-31 | **Approved** |
| CR-03 | R-27: allow **laser-cut A4 stainless plate** (the ballast/mooring disc) and **A4 compression springs** | **Approved** (team, 2026-11-14) |
| CR-04 | R-26 wording: "mooring bridle" becomes "**mooring attachment** (single-point eye at the keel), rated ≥ 2 kN" | **Approved** (team, 2026-11-14) |
| — | No mass reduction now: test T1 decides; the cut list in §4 is the fallback. R-30a overrun accepted and the target marked "to be confirmed with MTC". An accelerometer/IMU goes on the main board (Stage 3) | **Approved** |

CR-01 to CR-04 are incorporated in **requirements-v1.1**.

## 2. Architecture and load paths (what changed in v1.0)
- **Cage:** 4 × M6 A4 rods on r = 78 mm, positioned at the segment joints (0/90/180/270°). Each rod runs from a top-cap lug, through the top spoke, the ring joint (a half-boss in each segment) and the bottom spoke, then through the keel-head arm and the pod-carrier arm, and ends at the ballast disc.
  - Nuts above the top spoke and below the bottom spoke clamp the spoke–ring–spoke sandwich and lock the ring onto the rods. These rods replace 12 of the former 16 ring bolts; one M6 joint bolt per joint remains, at r = 170 mm.
- **Compression stack:** top cap → pipe → bonded bottom cap → keel head (4 legs on the cap floor, positioned under the pipe wall) → strut → pod carrier → spacer → disc. The stack is clamped by A4 springs under the top-cap lug nuts and the disc nuts.
  - The pipe is positively retained at both ends, so it cannot slide out of the top-cap O-rings (review finding 4).
  - The hose-clamped saddles now only centre the pipe.
- **Mooring (R-26):** an M12 A4 DIN 580 eye bolt in the centre of the disc. Load path: disc → 4 rods → nuts on the top spokes → ring.
  - No printed part carries the mooring load in bending.
  - The bottom-spoke eyes are not mooring points.
- **Lifting (R-31):** rope handle through the top-spoke eyes. Load path: ring → rods → disc → column (in compression).
- **Bonded bottom cap (R-24):** carries only stack compression, which flows straight from the pipe wall into the legs. It sees no keel moment and no peel. The keel moment (≈13 N·m lying on its side) is carried by the cage as a rod couple of ≈83 N, which is below the 150 N rod preload.
- **Vertical layout** (z measured from the ring underside):

| Item | z [mm] |
|---|---|
| Pipe | −120 … +180 |
| Keel head | −225 |
| Pod carrier | −460 … −335 |
| Pods | −452 … −342 |
| Disc | −535 … −525 |
| Eye bolt | down to ≈ −585 |

## 3. Stability (R-25, R-01) — CAD-derived masses, 2.0 kg ballast
Method: point-cloud hydrostatics, quasi-static, ρ = 1.005 kg/L, grid noise ≈ ±2 mm. A mooring pull is modelled as a vertical point weight at its attachment point. Code: `stability.py` / `report.py`.

| Case | Mass kg | WL above ring bottom mm | GM upright mm | GM inverted mm* | GZ90 mm | min GZ 5–175° mm | Upside-down stable? |
|---|---|---|---|---|---|---|---|
| A max config (4 × 0.3 kg pods) | 8.85 | 52 | 250 | −108 | 181 | 9.4 | no |
| B min config (3 × 0.2 kg pods) | 8.25 | 50 | 236 | −83 | 167 | **7.2** | no |
| C = B, canister flooded | 8.25 | 62 | 251 | −74 | 167 | 6.5 | no |
| D1 = B + 1 kg mooring at keel eye (**design**) | 9.25 | 56 | 280 | −142 | 218 | 12.4 | no |
| D2 = B + 1 kg mooring at ring, z = 0 (rejected) | 9.25 | 56 | 217 | −79 | 155 | 6.9 | no |
| D3 = A + 1 kg mooring at keel eye (deepest) | 9.85 | 62 | 290 | −160 | 224 | 13.9 | no |
| E = B without ballast (reference) | 6.25 | 34 | 153 | +76 | 42 | −20.3 | **yes** |

\*A negative GM inverted means the buoy is unstable when upside down, so it rights itself.

- The team's correction is reproduced: with the old geometry, moving the mooring from the keel to the ring drops min GZ from 13.5 to 7.2 mm. In v1.0 the mooring sits at the keel eye (D1).
- Ballast sensitivity (case B, min GZ): 1.0 kg → 1.3 mm, 1.5 kg → 4.5 mm, **2.0 kg → 7.2 mm**, 2.5 kg → 9.7 mm.
- **Weak spot:** near fully inverted (≈175°) the righting arm is only about 7 mm, so recovery from almost fully inverted will be slow. It is still positive in every case, and the mooring adds 5 mm.
- **R-25 reserve buoyancy, single definition:** (V·ρ − (R-31 max + mooring)) / (R-31 max + mooring) = (V·1.005 − 10 kg) / 10 kg.
  - Intact: V = 15.9 L → **60 %** (≥ 50 % ✓).
  - Canister flooded: V = 13.4 L → 35 %. This still floats (13.5 kg lift > 10 kg), which is what R-25 requires ✓.
  - The earlier figures (61 %, 78 %, 111 %) used other denominators and are withdrawn.
- **R-01:** pods sit on the carrier, and the Celsius tip is at z ≈ −477. That puts it 0.53–0.54 m below the waterline across cases A–D3 (0.5 ± 0.1 ✓).
- **Freeboard:** at the deepest case (D3) the ring top is 38 mm above the water.

## 4. Mass budget, max configuration (R-31 ≤ 9 kg)
| Item | kg | Source |
|---|---|---|
| Ring trays + lids | 1.25 | CAD v1.0 (smaller half-bosses than the 1.38 kg version) |
| Foam | 0.45 | Stage 1 |
| Spokes + 4 joint bolts + clamps | 0.82 | CAD ×0.7 infill + hardware |
| Pipe + caps | 0.85 | CAD |
| Electronics / battery | 0.25 / 0.30 | Stage 1 |
| Mast, GNSS, antenna / light, reflector | 0.40 / 0.30 | Stage 1 |
| Keel column, printed | 0.35 | CAD ×0.7 |
| Cage rods, nuts, springs | 0.55 | Catalogue estimate |
| Eye bolt + nut / rope handle | 0.10 / 0.03 | Estimate |
| Pods (R-31 allowance) | 1.20 | R-31 |
| Ballast disc | 2.00 | CAD (A4 Ø180 × 10) |
| **Total** | **8.85** | **Margin 0.15 kg (1.7 %)** |

**Top risk:** this margin is smaller than the uncertainty in the estimate (about ±0.5 kg), so R-31 compliance is not demonstrated. **Decision:** no mass reduction now; T1 decides. If T1 fails, this is the fallback cut list:
1. Lighter mast and light (−0.2 kg; this also improves stability).
2. Spokes at 30 % infill with 9 mm arms (−0.15 kg).
3. Ring walls at 1.8 mm (−0.1 kg).

## 5. Strength checks (R-26: 2 kN; hand calculations, static)
| Member | Calculation | Result | Verdict |
|---|---|---|---|
| Bottom-spoke eye (v0 path) | M = 500 N × 43 mm; Z = 44·12²/6 = 1056 mm³ | 20.4 MPa (500 N/leg), 81 MPa (2 kN on one leg) | **Rejected.** Agrees with the team's estimate. Too high for printed ASA/PETG with creep |
| M12 A4 DIN 580 eye bolt | Typical working load for an M12 DIN 580 eye bolt ≈ 340 kg (TBC on the purchased part) | ≈3.3 kN axial | OK |
| Ballast/mooring disc A4 10 mm | Simply supported circular plate a = 78, r₀ = 12: σ = 3P/(2πt²)·[(1+ν)ln(a/r₀)+1] | 33 MPa; ×1.5 for 4-point support ≈ 49 MPa vs Rp0.2 ≈ 200 MPa | OK (safety factor ≈ 4) |
| M6 A4-70 rods | A_s = 20.1 mm² | 25 MPa (shared), 100 MPa (one rod takes 2 kN) vs 450 MPa | OK |
| Washer bearing on top spoke (DIN 9021) | 500 N / 220 mm² | 2.3 MPa (9 MPa if one rod takes 2 kN, short term) | OK. Spoke is in compression on the ring, no bending |
| Top-cap lugs (preload only) | 150 N × 16.7 mm / (20·12²/6) | 5.2 MPa | **Watch for creep.** Limit preload to 150 N; check with test T3b |
| Thermal mismatch, stack vs rods | (300·70 + 413·95 − 723·16)·10⁻⁶ mm/K | ±1.0 mm at ±20 K → ±22 N with springs of 30 and 100 N/mm | OK only with springs. Without them the stack would loosen (rattle) or creep |

## 6. Sensor pods (R-01…R-04, R-15, R-16, R-19)
All four pods share the same interface: outer length 110 mm, the same dovetail and the same ball-lock pin. They sit at 45° between the cage rods. Above the potting, each pod is open and may flood.

| Pod | Sensor (datasheet) | Mount | Exposed | TBC |
|---|---|---|---|---|
| pod_temp | Blue Robotics Celsius: M10×1.5 bulkhead, 10.2 mm hole, AS568-013 face O-ring | 8 mm floor, Ø18 spot face | ≈25 mm | Protrusion and cage Ø from the BR drawing |
| pod_ec | Atlas ENV-40-EC-K1.0, Ø12 × 145.5 mm | Potted, O-ring on the probe body | 60 mm | Keep the cell ≥20 mm from walls; calibrate it fitted in the pod |
| pod_do | Atlas ENV-40-DOX, Ø16.5 × 105.3 mm | Potted, O-ring; membrane cap outside the pod so it can be serviced | 45 mm | Cap diameter |
| pod_turb | DFRobot SEN0189 (probe top not waterproof) | Fully potted in a pocket, 30 mm light-shield skirt with flow slots | ≈20 mm | Probe envelope (30 × 22 mm assumed) |

**DO water-flow requirement (review finding 7).** Atlas states that the galvanic probe needs a small water movement (≈60 ml/min); in stagnant water the reading falls.
- The pod leaves the membrane fully exposed, with no shroud. The buoy's heave and roll and the wave orbital motion at 0.45 m depth normally supply this flow.
- In flat calm the flow cannot be guaranteed, so flagging is handled as follows (R-09 quality flags):
  - **DO_LOW_MOTION** when the canister accelerometer RMS in the 60 s before the sample is below A_min (A_min to be set in a bench test, starting value 0.05 m/s²). This needs an IMU on the main board, which is a Stage 3 decision.
  - **DO_DEPLETION_SUSPECT** when a 30 s burst of 10 readings falls monotonically by more than 2 %.
  - Flagged values are still reported.
- **Decision:** an accelerometer/IMU will go on the main board (Stage 3). It also allows the buoy to estimate wave motion where it is moored (e.g. heave and tilt RMS, and a significant-wave-height or period estimate as a data product). Test engineers can use this as context for each trial. Its accuracy is not yet specified; see the handover in §12.
- Optional, for the Stage 3 trade-off: a coin vibration motor in pod_do, run 5 s before each reading. At 70 mA that adds ≈0.42 Ah per 30 days, about +21 % on the 2.0 Ah budget.

## 7. Sealing (R-24)
- **Bottom-cap bond (PVC to printed cap):** print the caps in **ASA**, not PETG, and bond with **Plexus MA300** (or MA310, which has a longer working time). Its datasheet lists rigid PVC, ABS and styrenics as substrates and gives 9.6 MPa lap shear on PVC with substrate failure. PETG is not listed, so it is not proven with this adhesive. Verify with lap-shear coupons (T2a).
  - Keep uncured MMA adhesive away from the O-rings.
- **Seams:** use slicer seam painting.
  - Top cap: seam on the outer skin at a lug, never on the bore or the groove walls.
  - Bottom cap: seam on the outside at a leg dimple.
  - Spot faces: ironed, with no seam on the face.
  - Print with 100 % infill and "inner wall first".
- **Coating:** thin penetrating epoxy (e.g. West 105/207 or XTC-3D type) on the O-ring grooves, the connector spot faces, the socket bond area of the bottom cap (before bonding, then scuffed) and the pod sealing faces.
  - Sand the grooves smooth afterwards and use silicone grease on the O-rings.
  - Optional: print the top cap 1 mm undersize in the bore and lathe-turn the grooves.
- **Connectors:** M12 A-coded 5-pole IP68 front-fastened panel sockets with a PG9 thread, Ø15.5 hole, e.g. Amphenol LTW M12A-05PFFP-SF8001 (≈25–30 PLN each).
  - **Risk:** binder states that IP67/IP68 plug connectors are not suitable for use under water. Mitigation: grease the mated pairs and wrap them in self-amalgamating tape (quick to remove, which keeps R-16 achievable), then run the 72 h immersion test (T2c).
  - If that test fails, alternatives are wet-mate or potted penetrator-style connectors, at higher cost.
  - The panel-thickness limit is unknown, so the floor is counterbored to 4 mm at each socket (TBC on the datasheet).

## 8. Access, rattle, cost
- **R-16 (hand access):** sockets at 45°, r = 30. A mated plug has:
  - 16 mm clearance to the nearest keel leg,
  - 22 mm to the next plug,
  - 48 mm to a rod,
  - 80 mm of vertical room under the cap.
  - Access is from the side, through the 110 mm gap between rods. This is tight but plausible; check it with a printed mock-up (T6).
- **R-33 (rattle):**
  - Single clamped disc instead of four loose discs.
  - Rods are spring-preloaded and never go slack (preload 150 N > 83 N moment couple).
  - Each pod is pushed up against its ball-lock pin by a 2 mm EPDM pad on its stop block.
  - Heat-shrink on the rods where they pass the printed brace holes.
  - Cables tied to the column every 100 mm.
  - Soft shackle or spliced rope at the eye bolt; no chain within 2 m of the buoy.
- **R-30a cost change vs the Stage-1 placeholder** (SEK, web retail estimates; get quotes):

| Item | Change (SEK) |
|---|---|
| Laser-cut A4 disc | +300 … 450 |
| 4 × M6 A4 rods | +160 … 280 |
| Nuts and washers | +60 … 100 |
| 8 springs | +120 … 240 |
| Eye bolt | +60 … 120 |
| Printed keel (≈0.5 kg ASA) | +150 |
| Rope | +20 |
| Removed: 12 bolts | −120 … −180 |
| Removed: M5 tie rods and inserts | −50 |
| Removed: M8 rod | −40 |
| **Net** | **+660 … 1,090** |

  - The 4 M12 sockets (≈65–80 SEK each at quantity) were assumed in the "ports" item of the placeholder.
  - **R-30a (≈4,000 SEK) is likely exceeded.** The team accepts this; the target is marked "to be confirmed with MTC" in requirements-v1.1. The costed BOM in Stage 4 must confirm the actual figure.

## 9. Parts (v1.0)
- **Printed (ASA, all ≤ 240 mm, R-27):**

| Part | Qty |
|---|---|
| ring_tray | 4 |
| ring_lid | 4 |
| spoke | 8 |
| top_cap | 1 |
| bottom_cap | 1 |
| keel_head | 1 |
| keel_strut | 1 |
| keel_spacer | 1 |
| pod_carrier | 1 |
| pod_temp / pod_ec / pod_do / pod_turb | 1 each |

- **Non-printed:** see the README in the package.

## 10. Physical test plan (later, e.g. at The Fishery; not during the hackathon)
| # | Test | Verifies | Equipment | Pass criteria |
|---|---|---|---|---|
| T0 | **1:2 scale-model inversion and inclining test** (first, cheap). Print the ring in one piece (OD 200 mm). Trim the mass to **1.03 kg** with the CG at **z = −64 mm**, using steel washers on an M3 keel rod and a mast-top weight. Check the CG on a knife edge first | GZ model; R-25 self-righting | ≈0.4 kg ASA, washers, kitchen scale ±1 g, box ≥ 0.45 m deep (fresh water; add 0.5 % mass), phone inclinometer | Rights from every release angle 30…170° (5 releases each). No resting equilibrium beyond 90°. Inclining test (50 g moved 80 mm → ≈1.9°) gives GM = 118 mm ± 25 % |
| T1 | Weigh and locate the CG of the full prototype, each subassembly and the total | R-31, CG used in §3 | Crane scale ±20 g, two-point suspension or knife edge | Max config ≤ 9.0 kg; z_G within ±25 mm of −148 mm. If it fails, re-run `report.py` with the measured values |
| T2a | Lap-shear coupons: PVC to ASA with MA300 (5 coupons), dry and after 7 days in salt water | Bond method (R-24) | Coupons, salt water 7 PSU, simple pull rig with a crane scale | Substrate or cohesive failure; ≥ 5 MPa after soaking |
| T2b | Canister pressure decay: both caps fitted, −0.3 bar for 30 min | R-24 seals | Hand vacuum pump with gauge | Decay ≤ 0.01 bar |
| T2c | Immersion at 1 m for 72 h: canister (with leak probe and humidity card), each potted pod, mated M12 pairs | R-24, R-10 | Tank or dock, rope | No water ingress; leak alarm silent; pod insulation resistance > 10 MΩ |
| T3a | Mooring proof load: ring supported on blocks, 2 kN on the eye bolt, held 5 min, 3 cycles | R-26 | Lever hoist + crane scale (≥ 300 kg) or 200 kg of weights; dial gauge on the disc | No cracks or crushing; permanent set at the disc ≤ 1 mm; nuts have not moved |
| T3b | Creep and preload retention: 500 N for 72 h; spring lengths measured before and after | R-26, R-33 | As T3a, plus a caliper | Change in deflection ≤ 0.5 mm; spring preload ≥ 120 N |
| T4 | Full-scale float and tilt in harbour or tank: waterline; release from 90°, 135° and 170°; inclining test | R-25, R-01 | Calm harbour, inclinometer, tape on the mast | WL 40–65 mm above the ring bottom; rights from every angle; GM 236–250 mm ± 30 %; temperature tip 0.4–0.6 m deep |
| T4f | Flooded canister: a dummy canister without electronics, filled with water | R-25 | As T4 | Floats; still rights from 90° |
| T5 | 7 days moored at a dock | R-24, R-33 | Dock, mooring | No leak alarm; no audible rattle; DO flag statistics logged |
| T6 | Connector swap with a mock-up of the bottom end, timed, gloves on | R-16 | Printed bottom cap + keel head mock-up, M12 cordsets | Each pod swapped in ≤ 10 min by one person |

**Order:** T0 and T2a run in parallel, before ordering hardware → build → T1 → T2b → T2c → T3a → T3b → T4 / T4f → T6 → T5. Stop and re-design if T0, T1 or T2a fails.

## 11. Open risks
1. R-31 mass margin is 0.15 kg.
2. Weak righting near 175° (min GZ ≈7 mm).
3. Underwater use of the M12 connectors.
4. Creep in the printed lugs and spokes.
5. R-30a cost likely exceeded.
6. DO readings in calm water (flagged, not solved).
7. The fill port and the bonded lid make up a large bonded perimeter. Failure only floods foam, so buoyancy is kept.
8. Ring freeboard is only 38 mm at the deepest case.

## 12. Handover to Stage 3 (Electronics)
- **IMU on the main board.** It supplies the DO_LOW_MOTION flag, capsize/inversion logging (useful in T0 and T4) and wave-motion estimates for test engineers. Choose the sensor, sampling rate and power cost in Stage 3. Also decide whether wave estimates become a formal requirement (proposed R-37, not yet in requirements-v1.1).
- **Optional DO stirrer** (vibration motor): a trade-off against the power budget.
- **Pod electronics** must fit a Ø34 × ≈60 mm potted volume. Atlas isolated carrier boards (56 × 32 mm) do not fit, so a smaller isolator is needed.
- **M12 A-coded 5-pole pinout** for R-15 (power, GND, RS-485 A/B, spare) to be defined.
- **Leak probe (R-10)** at the bottom of the canister, next to the connector nuts.

## Assumptions
- Masses not derived from CAD are the Stage-1 budget values; infill factors are 0.7.
- A4 Rp0.2 ≈ 200 MPa (plate) and 450 MPa (A4-70 rods). Eye-bolt rating as typical for DIN 580.
- Thermal range ±20 K; spring rates from catalogue-type springs (TBC).
- Probe dimensions marked TBC come from drawings that have not yet been checked.
- Prices are web retail, converted at ≈11 SEK/EUR and ≈2.6 SEK/PLN.

# SeaSense — Requirements v1.2 (FROZEN)

Status: Frozen 2026-11-14. Replaces requirements-v1.1 as the baseline for Stage 4 onward. Changes require an explicit change request.
Scope: the buoy and its data specification; shore gateway hardware (R-36). Shore data platform and analytics are another team's responsibility.

## Change history
| Version | Date | Change | Affected |
|---|---|---|---|
| v1.0 | 2026-11-14 | Stage 1 baseline frozen | — |
| v1.1 | 2026-11-14 | **CR-01:** stainless fasteners, threaded rods, ballast and mast tube may be non-printed; all other custom-shaped parts stay printed | R-27 |
| | | **CR-02:** maximum mass raised from 8 kg to **9 kg**. Mass reduction becomes future work; test T1 decides | R-31 (and R-25 through its reference to R-31) |
| | | **CR-03:** laser-cut A4 stainless plate (ballast/mooring disc) and A4 compression springs may be non-printed | R-27 |
| | | **CR-04:** "mooring bridle" becomes "mooring attachment (single-point eye at the keel)", still rated ≥ 2 kN | R-26 |
| | | Clarification (no technical change): reserve buoyancy given as one explicit formula | R-25 |
| | | Note: Stage 2 cost estimate indicates the R-30a target is likely exceeded (+≈660…1,090 SEK); accepted, target to be confirmed with MTC | R-30a, Assumption 10 |
| | | §2 hull summary: Stage 2 v1.0 results added; Stage 1 estimates retained for traceability | §2 |
| v1.2 | 2026-11-14 | **CR-05:** cost targets: base buoy ≤ **5,000 SEK**, core sensor set ≤ **7,500 SEK**, complete buoy (base + core) ≤ **12,500 SEK**. Benchmark: YSI EXO1 + CT + optical DO ≈86,000 SEK (team figure). Still to be confirmed with MTC | R-30a, R-30b |
| | | **R-37 added (Should):** indicative wave statistics (Hs, Tp) from the IMU | R-37 |
| | | **P-3:** R-20b defined at 20-min sampling with the 90-day profile (stage3-electronics-v1.0) | R-20b |
| | | Assumptions 12–15 updated/added from Stage 3 | §3 |

Priority: **M** = Must (core prototype) · **M-DR** = Must, design rule (met by component or material choice) · **S** = Should · **F** = Future work
Verification: **T** test · **A** analysis · **I** inspection · **D** demonstration
User needs: TE = test engineers, ENV = MTC environmental staff, MNT = maintenance, PRG = MTC programme / shore data team
Rows changed in v1.2 are marked **(v1.2)**; rows changed in v1.1 keep their **(v1.1)** mark.

## 1. Requirements

| ID | Requirement | Pri | Need | Verification |
|---|---|---|---|---|
| R-01 | Measure water temperature at 0.5 ± 0.1 m depth, range −2…+30 °C, accuracy ±0.5 °C | M | TE-1, ENV-1 | T: 3-point bath vs reference thermometer |
| R-02 | Measure conductivity and report practical salinity, range 0–20 PSU, accuracy ±0.5 PSU | M | TE-1, ENV-1 | T: standard solutions |
| R-03 | Measure dissolved oxygen, range 0–20 mg/L, accuracy ±0.5 mg/L maintained over a 30-day deployment | M | ENV-1, ENV-3 | T: 0 % / 100 % saturation checks; 30-day side-by-side vs reference sonde |
| R-04 | Turbidity module (optional; Must when fitted): indicative turbidity as a relative index, 2-point formazin calibration (≈0 and ≈100 NTU), repeatability ±10 % of reading, flagged "indicative" in data | M (module) | ENV-1, TE-1 | T: standards bath, repeated runs |
| R-05 | Sampling interval configurable 1–60 min; default 10 min; "trial mode" 1 min | S | TE-2, MNT-2 | D: remote change, check output rate |
| R-06 | Every sample carries UTC timestamp (±1 s) and position (±10 m CEP) | M | TE-3, TE-4 | T: comparison with GNSS reference |
| R-07 | ≥95 % of samples received at the shore gateway within 5 min of measurement, at ranges up to 3 km from one shore gateway supplied by the buoy team | M | TE-2 | T: 7-day field link test across the test area |
| R-08 | Store ≥30 days of samples on board; resend unsent data when the link returns | S | TE-4, ENV-1 | T: 48 h link blackout, verify complete back-fill |
| R-09 | Data follows a versioned, documented message specification: buoy ID, sensor/module IDs, units, quality flags, firmware and calibration IDs | M | PRG-4, ENV-2 | I: specification review signed off by shore team |
| R-10 | Every message reports battery level and a leak alarm | M | MNT-5 | T: wet leak probe; discharge battery |
| R-11 | Flag displacement > 50 m (configurable) from the deployed position | S | MNT-5, PRG-1 | T: move buoy, check flag |
| R-12 | Radio operates only in licence-exempt EU bands (868 MHz SRD) and complies with ETSI EN 300 220 incl. duty-cycle limits | M-DR | TE-5 | A + I: airtime calculation, module certificate |
| R-13 | Link design supports ≥50 buoys per gateway at the default interval | F | PRG-2 | A: airtime/collision analysis |
| R-14 | Sampling interval and trial mode changeable remotely; firmware updatable in the workshop without opening the sealed canister | S | MNT-2, PRG-3 | D |
| R-15 | ≥4 identical sensor ports on the canister bottom cap, each with: IP68 connector; switched power; RS-485 half-duplex multidrop bus with an addressed protocol (e.g. Modbus RTU); ≥2 devices per port via daisy-chain (in/out connector or T-splitter, terminated at the far end); operation over ≥30 m cable; printed pod mount. Must accommodate the mooring-line sensor (R-35) | M | TE-6, PRG-3 | I + D: each core module, plus two devices on one port at 30 m cable |
| R-16 | Swap a sensor module in ≤10 min by one person from a boat, without opening the canister | S | MNT-3 | D: timed by maintenance staff |
| R-17 | Each port supplies ≥0.5 W average / 2 W peak | F | PRG-3 | T |
| R-18 | Modules self-identify (type, serial, calibration coefficients and date) on connection | F | ENV-2, MNT-3 | D |
| R-19 | Adding a new sensor type requires only a firmware driver and a printed pod, no hull redesign | S | PRG-3 | D: integrate one non-baseline sensor |
| R-20a | Operate ≥30 days without service at 10-min sampling with the core sensor set | M | MNT-2 | A: power budget; T: 30-day endurance run |
| R-20b **(v1.2, P-3)** | Operate ≥90 days without service at **20-min sampling** with the core sensor set, using the 90-day profile (hourly DO depletion burst, flagged DO_BURST_SKIPPED otherwise) | S | MNT-2 | A: power budget; T: measured cycle energy extrapolated, plus endurance run |
| R-21 | Continue operating ≥7 days with no solar input (met by design if no solar fitted) | S | MNT-2, TE-2 | A |
| R-22 | Biofouling-induced drift stays within R-01…R-04 accuracy over the service interval | F | ENV-2, MNT-2 | T: pre/post deployment reference comparison |
| R-23 | Operate in Hs ≤ 1.0 m and wind ≤ 20 m/s; survive Hs ≤ 1.5 m and 25 m/s | S | All | A + T: tank or field test |
| R-24 | Electronics canister and sensor pods watertight to IP68 (1 m, 72 h). Buoyancy sections are foam-filled and need not be watertight | M | MNT-2 | T: immersion + pressure test |
| R-25 **(v1.1)** | Reserve buoyancy ≥50 % of (maximum mass per R-31 + design mooring weight-in-water ≤1 kg), i.e. (V_buoyant·ρ − (m_R-31 + m_mooring)) / (m_R-31 + m_mooring) ≥ 0.5, with ρ = 1.005 kg/L. Buoy remains afloat with the canister flooded. Self-rights from 90° heel; antenna stays clear of the water | M | MNT-1, PRG-1 | A: hydrostatics, GZ curve; T: flooded-canister and tilt tests |
| R-26 **(v1.1, CR-04)** | Mooring attachment (single-point eye at the keel) rated ≥2 kN; compatible with moorings in water depths ≤20 m | S | PRG-1 | T: proof load |
| R-27 **(v1.1, CR-01, CR-03)** | Every 3D-printed part fits within 240 × 240 × 240 mm and is printed in UV- and saltwater-resistant material (ASA or PETG). Permitted non-printed parts: the canister tube (110 mm pipe); A4 stainless fasteners, threaded rods and compression springs; the mast tube; ballast; laser-cut A4 stainless plate (ballast/mooring disc). All other custom-shaped parts are printed | M | MNT-4 | I + D: print a full part set |
| R-28 | All electronics and sensors available from ≥2 EU suppliers | S | MNT-4, PRG-2 | I: BOM review |
| R-29 | A damaged printed part can be reprinted and refitted within 24 h with common hand tools | F | MNT-4 | D |
| R-30a **(v1.2, CR-05)** | Base buoy (hull, electronics, battery, radio, GNSS, canister, ports) BOM ≤ **5,000 SEK** at quantity 20, independent of fitted modules (**to be confirmed with MTC**). Note: stage3-electronics-v1.0 central estimate ≈5,400 SEK (range 5,000–5,750); to be resolved by the Stage 4 costed BOM | M | PRG-1 | A: costed BOM |
| R-30b **(v1.2, CR-05)** | Sensor modules priced separately incl. node, pod and connector (to be confirmed with MTC): core set (temperature + salinity + DO) ≤ **7,500 SEK**; turbidity ≤ ~500 SEK. Complete buoy (base + core set) ≤ **12,500 SEK** | M | PRG-1 | A: costed BOM |
| R-31 **(v1.1, CR-02)** | Mass ≤**9 kg** ready to deploy with every port filled (allowance ≤0.3 kg per module); lifting handle fitted | M | MNT-1 | I: weigh in maximum configuration |
| R-32 | Yellow body, retroreflective tape, radar reflector, yellow flashing light, owner contact marking | M-DR | TE-5 | I |
| R-33 | No active acoustic emitters; mooring hardware designed against rattling | M-DR | TE-5 | I |
| R-34 | No biocidal antifouling; sealed LiFePO4 battery; no hazardous release if lost | M-DR | ENV-4 | I: material declaration |
| R-35 | Bottom-oxygen module on the mooring line, sharing an R-15 port by daisy-chain; its weight in water counts against the R-25 mooring allowance | F | ENV-1, ENV-3 | D |
| R-36 | Shore gateway: off-the-shelf outdoor 868 MHz LoRa(WAN) gateway, ≥IP65, powered from MTC mains or PoE; mast/wall mount with antenna ≥10 m above sea level and line of sight to the test area; internet via Ethernet (cellular backup optional); forwards data per R-09; buffers ≥24 h if internet is lost | S | TE-2, PRG-4 | I + D: installation check; 24 h internet-loss test |
| R-37 **(v1.2, new)** | Report indicative wave statistics, significant wave height (Hs) and peak period (Tp), derived from the on-board IMU, flagged "indicative" in the data (R-09) | S | TE-3, ENV-1 | T: comparison with a reference wave measurement; pass: Hs within ±20 % or ±5 cm (whichever is larger), Tp within ±0.5 s |

## 2. Hull concept summary — Option C (baseline)

Unchanged from v1.1 §2. The current design and analysis are in **stage2-concept-cad-v1.0** (frozen), with approved Stage 3 changes P-1 (top-cap RF feedthroughs), P-2 (hourly DO burst in the 90-day profile) and P-4 (DO stirrer dropped). Electronics baseline: **stage3-electronics-v1.0** (frozen).

## 3. Assumptions

1. Saab, MTC and The Fishery details are unknown. The Fishery is assumed to have printers at least as capable as the BTH lab's Bambu Lab printers (256³ and 300 × 320 × 320 mm).
2. Ice-free season of roughly April–November; sheltered archipelago; mooring depth ≤20 m; test area within 3 km of one gateway site.
3. Brackish water density ≈1.005 kg/L; salinity ≈7 PSU (≈12 mS/cm), not measured at site.
4. Mooring weight in water ≤1 kg, including the R-35 module and its cable when fitted.
5. Placing buoys may require permission from Swedish authorities (e.g. Sjöfartsverket or the county board), to be confirmed.
6. Core sensors: Blue Robotics Celsius (temperature), Atlas Scientific EC K1.0 (salinity), Atlas Scientific galvanic DO (oxygen) with EZO circuits on SeaSense isolated pod nodes (stage3-electronics-v1.0). Turbidity: DFRobot SEN0189 in a potted, light-shielded pod. Prices are web retail at about 10 SEK/USD and 11 SEK/EUR, not quotes.
7. Each module contains a small microcontroller acting as an addressed Modbus RTU node on RS-485.
8. *(v1.2: superseded)* Power: see stage3-electronics-v1.0 §3 (≈6.2 Ah per 30 days for the core set at 10 min; unmeasured). Battery: 2 × 6 Ah LiFePO4 in parallel (12 Ah), usable ≈8.64 Ah after 80 % depth of discharge and 90 % cold derating. No solar on the prototype.
9. Trial mode keeps GNSS fixes at 10-minute intervals. Only the sensors sample every minute.
10. Cost targets per CR-05 (base ≤5,000 SEK, core ≤7,500 SEK, complete ≤12,500 SEK), pending MTC confirmation.
11. Gateway site has mains or PoE power and Ethernet internet, provided by MTC.
12. *(v1.2)* An IMU (LSM6DSOX) is fitted on the main board; it provides DO low-motion flags, capsize logging and the R-37 wave statistics.
13. *(v1.2)* BLE is used only during magnet-activated service windows; assumed acceptable to MTC (to be confirmed).
14. *(v1.2)* A 20-minute interval is acceptable for 90-day deployments (to be confirmed with MTC).
15. *(v1.2)* The gateway site gives SF ≤9 across the 3 km area; to be verified in the R-07 link test.

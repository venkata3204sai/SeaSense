# SeaSense — Requirements v1.0 (FROZEN, Stage 1 baseline)

Status: Frozen 2026-11-14. Baseline for Stage 2 (Concept & CAD) onward. Changes require an explicit change request.
Scope: the buoy and its data specification; shore gateway hardware (R-36). Shore data platform and analytics are another team's responsibility.

Priority: **M** = Must (core prototype) · **M-DR** = Must, design rule (met by component or material choice) · **S** = Should · **F** = Future work
Verification: **T** test · **A** analysis · **I** inspection · **D** demonstration
User needs: TE = test engineers, ENV = MTC environmental staff, MNT = maintenance, PRG = MTC programme / shore data team

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
| R-20b | Operate ≥90 days without service | S | MNT-2 | A + T |
| R-21 | Continue operating ≥7 days with no solar input (met by design if no solar fitted) | S | MNT-2, TE-2 | A |
| R-22 | Biofouling-induced drift stays within R-01…R-04 accuracy over the service interval | F | ENV-2, MNT-2 | T: pre/post deployment reference comparison |
| R-23 | Operate in Hs ≤ 1.0 m and wind ≤ 20 m/s; survive Hs ≤ 1.5 m and 25 m/s | S | All | A + T: tank or field test |
| R-24 | Electronics canister and sensor pods watertight to IP68 (1 m, 72 h). Buoyancy sections are foam-filled and need not be watertight | M | MNT-2 | T: immersion + pressure test |
| R-25 | Reserve buoyancy ≥50 % of (maximum mass per R-31 + design mooring weight-in-water ≤1 kg). Buoy remains afloat with the canister flooded. Self-rights from 90° heel; antenna stays clear of the water | M | MNT-1, PRG-1 | A: hydrostatics, GZ curve; T: flooded-canister and tilt tests |
| R-26 | Mooring bridle rated ≥2 kN; compatible with moorings in water depths ≤20 m | S | PRG-1 | T: proof load |
| R-27 | Every 3D-printed part fits within 240 × 240 × 240 mm and is printed in UV- and saltwater-resistant material (ASA or PETG). The canister tube is a non-printed 110 mm pipe; all other structural parts are printed | M | MNT-4 | I + D: print a full part set |
| R-28 | All electronics and sensors available from ≥2 EU suppliers | S | MNT-4, PRG-2 | I: BOM review |
| R-29 | A damaged printed part can be reprinted and refitted within 24 h with common hand tools | F | MNT-4 | D |
| R-30a | Base buoy (hull, electronics, battery, radio, GNSS, canister, ports) BOM ≤ ~4 000 SEK at quantity 20, independent of fitted modules (to be confirmed with MTC) | M | PRG-1 | A: costed BOM |
| R-30b | Sensor modules priced separately incl. pod and connector (to be confirmed with MTC): core set (temperature + salinity + DO) ≤ ~7 400 SEK; turbidity ≤ ~500 SEK | M | PRG-1 | A: costed BOM |
| R-31 | Mass ≤8 kg ready to deploy with every port filled (allowance ≤0.3 kg per module); lifting handle fitted | M | MNT-1 | I: weigh in maximum configuration |
| R-32 | Yellow body, retroreflective tape, radar reflector, yellow flashing light, owner contact marking | M-DR | TE-5 | I |
| R-33 | No active acoustic emitters; mooring hardware designed against rattling | M-DR | TE-5 | I |
| R-34 | No biocidal antifouling; sealed LiFePO4 battery; no hazardous release if lost | M-DR | ENV-4 | I: material declaration |
| R-35 | Bottom-oxygen module on the mooring line, sharing an R-15 port by daisy-chain; its weight in water counts against the R-25 mooring allowance | F | ENV-1, ENV-3 | D |
| R-36 | Shore gateway: off-the-shelf outdoor 868 MHz LoRa(WAN) gateway, ≥IP65, powered from MTC mains or PoE; mast/wall mount with antenna ≥10 m above sea level and line of sight to the test area; internet via Ethernet (cellular backup optional); forwards data per R-09; buffers ≥24 h if internet is lost | S | TE-2, PRG-4 | I + D: installation check; 24 h internet-loss test |

## 2. Hull concept summary — Option C (baseline)

**Concept:** a foam-filled 3D-printed ring float around a sealed electronics canister made from 110 mm pipe. Sensor pods hang below the canister; ballast sits low; a short mast carries the antennas, light and radar reflector.

| Item | Value (estimate, not verified) |
|---|---|
| Ring float | OD 400 mm, ID 130 mm, height 100 mm → π(0.200² − 0.065²)·0.100 = 11.2 L |
| Ring segments | **4 × 90°**, each about 200 × 200 × 100 mm (fits 240³, R-27). 3 × 120° does not fit: outer chord 346 mm > 240 mm and > the 339 mm build-plate diagonal |
| Canister | 110 mm pipe × 300 mm → π·0.055²·0.300 = 2.85 L; printed top and bottom caps |
| Sensor pods | ≈0.3 L total (assumed) |
| Total buoyant volume | ≈14.4 L |
| Reserve (8 kg + 1 kg mooring) | (14.4 × 1.005 − 9)/9 ≈ 61 % ≥ 50 % (R-25) |
| Static draft | ≈50 mm into the 100 mm ring |
| Canister-flooded case | Ring + pods ≈11.5 L → ≈11.6 kg lift > 9 kg, so the buoy stays afloat (R-25) |
| Mass budget | Float ≈1.0 kg, foam 0.45, canister 0.65, electronics 0.25, battery 0.3, mast/GNSS/antenna 0.4, light/reflector 0.3, frame/fasteners 0.6, port allowance 1.2 → ≈5.2 kg; ≈2.8 kg left for ballast and margin (R-31) |

**Joining and sealing**
- Ring segments: tongue-and-groove ends, through-bolted to 4 printed spokes that clamp to a canister collar. The joints don't need to seal because the segments are foam-filled (closed-cell PU poured in stages, or cut closed-cell blocks).
- Canister top cap: double radial O-ring against the smooth outside of the pipe, epoxy-coated printed groove, tie-rod clamp. Sits above the waterline.
- Canister bottom cap: permanently bonded (epoxy or marine PU) with 4 IP68 bulkhead connectors. This is the main remaining leak path.
- Printed parts that keep water out: ≥4 perimeters, 100 % infill near seals, thin epoxy coat.

**Key risks carried into Stage 2**
- Wide ring may be stable upside down. Ballast must sit about 0.4 m below the waterline; check with a righting-arm (GZ) curve.
- Expanding foam may split thin printed walls.
- Bulkhead connector sealing on the bottom cap.
- Printed flanges and spokes may creep under load.

**Requirements driven by this concept:** R-15, R-24, R-25, R-26, R-27, R-30a, R-31, R-32.

## 3. Assumptions

1. Saab, MTC and The Fishery details are unknown. The Fishery is assumed to have printers at least as capable as the BTH lab's Bambu Lab printers (256³ and 300 × 320 × 320 mm).
2. Ice-free season of roughly April–November; sheltered archipelago; mooring depth ≤20 m; test area within 3 km of one gateway site.
3. Brackish water density ≈1.005 kg/L; salinity ≈7 PSU (≈12 mS/cm), not measured at site.
4. Mooring weight in water ≤1 kg, including the R-35 module and its cable when fitted.
5. Placing buoys may require permission from Swedish authorities (e.g. Sjöfartsverket or the county board), to be confirmed.
6. Core sensors: Blue Robotics Celsius (temperature), Atlas Scientific EC K1.0 kit (salinity), Atlas Scientific galvanic DO kit (oxygen, with isolated carrier boards). Turbidity: DFRobot SEN0189 in a potted, light-shielded pod. Prices are web retail at about 10 SEK/USD and 11 SEK/EUR, not quotes.
7. Atlas EZO circuits have no addressing in UART mode (to be confirmed against the datasheet). Each module therefore contains a small microcontroller acting as an addressed RS-485 node.
8. Power: GNSS fix 30 s at 30 mA every cycle; sensors 5 s at 50 mA; MCU 35 s at 5 mA; LoRa 0.1 s at 120 mA; sleep 0.1 mA; converter efficiency 85 %. That gives ≈2.0 Ah per 30 days. Battery: 2 × 6 Ah LiFePO4 cells in parallel (12 Ah), usable ≈8.6 Ah after 80 % depth of discharge and 90 % cold derating. No solar on the prototype.
9. Trial mode keeps GNSS fixes at 10-minute intervals. Only the sensors sample every minute.
10. Cost placeholders (base ≈4 000 SEK, core sensors ≈7 400 SEK) accepted by the team, pending MTC confirmation.
11. Gateway site has mains or PoE power and Ethernet internet, provided by MTC.

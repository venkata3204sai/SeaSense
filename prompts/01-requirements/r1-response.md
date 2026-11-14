# Stage 1 · Round 1 · AI response (verbatim)

---

Here's a first draft of the Stage 1 requirements. The numbers I proposed are starting points for the team to argue with. None of them are verified.

## 1. User needs

| ID | User group | Need |
|---|---|---|
| **TE-1** | Test engineers (e.g. Saab) | Know temperature, salinity, oxygen and turbidity at the trial site while the trial is running |
| **TE-2** | Test engineers | Receive data in near real time, during the trial |
| **TE-3** | Test engineers | Get data with timestamps and positions that can be lined up with their own trial logs |
| **TE-4** | Test engineers | Compare conditions between test runs |
| **TE-5** | Test engineers | Buoys must not disturb trials: no acoustic noise, no radio interference, no collision hazard for uncrewed vessels |
| **TE-6** | Test engineers | Add trial-specific sensors (e.g. sound speed, current) for a single campaign |
| **ENV-1** | MTC environmental staff | A long, continuous record of the parameters linked to eutrophication and low oxygen |
| **ENV-2** | MTC environmental staff | Data credible enough to show regulators and the public (calibration, quality flags) |
| **ENV-3** | MTC environmental staff | Early detection of low-oxygen or bloom events |
| **ENV-4** | MTC environmental staff | The buoy itself must not pollute: materials, biocides, batteries, lost units |
| **MNT-1** | Maintenance staff | Deploy and recover from a small boat with 1–2 people |
| **MNT-2** | Maintenance staff | Long intervals between service visits |
| **MNT-3** | Maintenance staff | Swap sensors and batteries quickly without special tools |
| **MNT-4** | Maintenance staff | Repair and reprint parts locally at The Fishery |
| **MNT-5** | Maintenance staff | See each buoy's health and position remotely, and find a buoy that has drifted |
| **PRG-1** | MTC programme | Low unit cost, so losing one is acceptable |
| **PRG-2** | MTC programme | Scale from 10–20 buoys to more |
| **PRG-3** | MTC programme | Room for future measurements and uses that aren't specified yet |
| **PRG-4** | Shore data team | A stable, documented data specification to build on |

## 2. Buoy requirements

Priority: **M** = must, **S** = should, **C** = could. Verification: **T** = test, **A** = analysis, **I** = inspection, **D** = demonstration.

### Measurement

| ID | Requirement | Reason | Need | Pri | Verif. |
|---|---|---|---|---|---|
| R-01 | Measure water temperature at 0.5 ± 0.1 m depth, range −2…+30 °C, accuracy ±0.2 °C | Core parameter; drives stratification and sonar conditions | TE-1, ENV-1 | M | T: compare against a reference thermometer in a bath at 3 points |
| R-02 | Measure conductivity and report practical salinity, range 0–20 PSU, accuracy ±0.5 PSU | Local Baltic salinity is low (assumed about 7–8 PSU), so the range is set for brackish water | TE-1, ENV-1 | M | T: check against standard solutions |
| R-03 | Measure dissolved oxygen, range 0–20 mg/L, accuracy ±0.3 mg/L or ±5 % (whichever is larger) | Low-oxygen zones are a key environmental concern | ENV-1, ENV-3 | M | T: 0 % and 100 % saturation checks; side-by-side with a reference sonde |
| R-04 | Measure turbidity, range 0–100 NTU, accuracy ±2 NTU or ±10 % | Indicates blooms and sediment stirred up by trials | ENV-1, TE-1 | M | T: formazin or other standards |
| R-05 | Sampling interval configurable from 1 to 60 min. Default 10 min; "trial mode" 1 min | Trials need fine time resolution; long-term monitoring needs to save power | TE-2, MNT-2 | M | D: change the setting remotely and check the output rate |
| R-06 | Each sample carries a UTC timestamp (±1 s, GNSS-disciplined) and position (±10 m CEP) | Lets data be lined up with trial logs | TE-3, TE-4 | M | T: compare against a GNSS reference |

### Data and communication

| ID | Requirement | Reason | Need | Pri | Verif. |
|---|---|---|---|---|---|
| R-07 | ≥95 % of samples reach the shore gateway within 5 min of measurement, at up to 5 km from the gateway | Defines "near real time" | TE-2 | M | T: field link test across the test area for at least 7 days |
| R-08 | Store at least 90 days of samples on board and resend missed data once the link returns | Prevents data gaps if the link drops | TE-4, ENV-1 | M | T: block the link for 48 h, then check that all missed data arrives |
| R-09 | Data follows a versioned, documented message specification: buoy ID, sensor IDs, units, quality flags, firmware and calibration IDs | Gives the shore team a stable interface | PRG-4, ENV-2 | M | I: spec review signed off by the shore team |
| R-10 | Every message includes health data: battery voltage and state of charge, internal humidity or leak flag, enclosure temperature, signal strength | Lets maintenance see buoy health remotely | MNT-5 | M | T: induce faults (e.g. moisture) and check they are reported |
| R-11 | Raise a flag if the buoy moves more than 50 m from its deployed position (configurable) | Detects a broken mooring | MNT-5, PRG-1 | M | T: move the buoy and check the alert |
| R-12 | Radio operates only in licence-exempt EU bands (e.g. 868 MHz SRD) and complies with ETSI EN 300 220, including duty-cycle limits | Legal operation, and avoids interfering with trial radio links | TE-5 | M | A + I: airtime calculation and module certification |
| R-13 | Link design supports at least 50 buoys per gateway at the default interval | Allows the fleet to grow | PRG-2 | S | A: airtime and collision analysis |
| R-14 | Sampling interval and trial mode can be changed remotely; firmware can be updated in the workshop without opening the sealed enclosure | Avoids opening the hull, which is a leak risk | MNT-2, PRG-3 | S | D |

### Modularity

| ID | Requirement | Reason | Need | Pri | Verif. |
|---|---|---|---|---|---|
| R-15 | At least 4 sensor ports with one standard mechanical and electrical interface (connector, supply voltage, digital bus) | Lets sensors be added, removed and swapped | TE-6, PRG-3 | M | I + D |
| R-16 | One person can swap a sensor module in ≤10 min on a boat, with no tools other than a single hand tool, and without opening the main electronics enclosure | Keeps field changes practical | MNT-3 | M | D: timed by a maintenance technician |
| R-17 | Each port supplies at least 0.5 W average and 2 W peak | Leaves headroom for future sensors | PRG-3 | S | T |
| R-18 | Modules identify themselves (type, serial number, calibration coefficients and date) when connected | Calibration traceability; plug-and-play | ENV-2, MNT-3 | S | D |
| R-19 | A new sensor type needs only a firmware driver and a printed adapter, with no hull redesign | Supports future, unspecified uses | PRG-3 | S | D: integrate one sensor not in the baseline |

### Autonomy and environment

| ID | Requirement | Reason | Need | Pri | Verif. |
|---|---|---|---|---|---|
| R-20 | Run at least 90 days without service at the default interval with the standard sensor set; stretch goal is the full season (about 180 days) | Long autonomous operation | MNT-2 | M | A: power budget; T: endurance run |
| R-21 | Keep operating for at least 7 days with no solar input | Overcast weather in autumn | MNT-2, TE-2 | M | A + T: run with the solar panel covered |
| R-22 | Sensor drift from biofouling stays within the R-01…R-04 accuracy over the service interval | Without this, the 90-day autonomy is meaningless | ENV-2, MNT-2 | M | T: comparison against a reference before and after deployment |
| R-23 | Operate at significant wave height up to 1.0 m and wind up to 20 m/s; survive up to 1.5 m waves and 25 m/s wind | Sheltered-archipelago conditions (assumed) | All | M | A + T: tank or field test |
| R-24 | Electronics enclosure is IP68 (1 m, 72 h); sensor modules rated to at least 2 m | Ingress is the dominant failure mode | MNT-2 | M | T: immersion and pressure test |
| R-25 | Self-rights from 90° heel; reserve buoyancy ≥50 % with the maximum module load; antenna stays above the waterline under R-23 conditions | Keeps the radio and solar panel working | TE-2 | M | A: hydrostatics; T: tilt test |
| R-26 | Mooring point rated to ≥2 kN; compatible with moorings at depths up to 30 m | Prevents loss of buoys | PRG-1 | M | T: proof load |

### Manufacturing, cost, safety

| ID | Requirement | Reason | Need | Pri | Verif. |
|---|---|---|---|---|---|
| R-27 | All structural parts printable on FDM printers with a build volume of 250 × 250 × 250 mm, in a UV- and saltwater-resistant material (e.g. ASA or PETG) | Local production (printer size to be confirmed) | MNT-4 | M | I + D: print a full set |
| R-28 | All electronics and sensors are off-the-shelf and available from at least 2 EU suppliers | Repairs and fleet scale-up | MNT-4, PRG-2 | M | I: BOM review |
| R-29 | A damaged printed part can be reprinted and refitted within 24 h using common hand tools | Fast repairs | MNT-4 | S | D |
| R-30 | Unit cost (BOM, quantity 20): base buoy ≤3 000 SEK; standard 4-sensor configuration ≤10 000 SEK | Losing one buoy is acceptable (target to be confirmed) | PRG-1 | M | A: costed BOM |
| R-31 | Mass ≤15 kg ready to deploy; fitted with a lifting handle | One- or two-person handling | MNT-1 | M | I: weigh |
| R-32 | Yellow body, retroreflective tape, radar reflector, optional flashing yellow light; owner contact details marked on the hull | Visible to boats and to uncrewed vessel sensors | TE-5 | M | I |
| R-33 | No active acoustic emitters; mooring hardware designed so it does not rattle | Avoids disturbing sonar trials | TE-5 | M | I; C: hydrophone check |
| R-34 | No biocidal antifouling; sealed LiFePO4 battery; no hazardous substances released if the buoy is lost | Environmental mandate | ENV-4 | M | I: material declaration |

## 3. Conflicts and risks

- **Autonomy vs biofouling (R-20 vs R-22).** In Baltic summers, unprotected optical sensors can foul within a few weeks. The 90-day target may only be reachable with a wiper or copper guard. That adds cost and power, and copper may conflict with R-34.
- **Cost vs accuracy (R-03, R-04 vs R-30).** Cheap galvanic oxygen probes drift, and hobby-grade turbidity sensors aren't marine-rated. An optical oxygen sensor alone could use most of the 10 000 SEK.
- **Real time vs geography (R-07).** Islands can block line of sight to a single gateway. We may need several gateways or relay buoys. The duty-cycle limit also caps how fast trial mode can be across the fleet.
- **Modularity vs sealing (R-15 vs R-24).** Every external connector is a potential leak path.
- **3D-printed hull vs longevity.** Layer lines let water in and print quality varies. Seams will probably need sealing or coating, and that needs testing.
- **"Future unspecified uses" (PRG-3)** can't be verified as written. I bounded it with R-17 and R-19.

**Assumptions made**
- I treated Saab, MTC and The Fishery details as unknown and used no facts about them.
- Test area is within about 5 km of one gateway, water depth ≤30 m, ice-free season roughly April–November.
- Local salinity is about 7–8 PSU (typical for the southern Baltic coast; not checked for this site).
- Measuring at a single depth (0.5 m) is enough for the baseline.
- Placing buoys may need permission from Swedish authorities (e.g. Sjöfartsverket or the county board). This needs to be confirmed.
- Cost targets and the printer build volume are my placeholders.

**Open questions for the team**
1. How big is the test area, and where would the gateway be? This determines R-07, R-13 and the radio choice.
2. Do the environmental staff need oxygen near the seabed? Low-oxygen zones are often at the bottom, not the surface. If so, we need a sensor on the mooring line, which is a big design change.
3. What loss cost does MTC actually find acceptable? R-30 is a guess.
4. Which printer and materials does The Fishery have?
5. Does "near real time" mean seconds or minutes for Saab-type trials?
6. Does the buoy team supply the gateway, or does MTC?
7. What service interval can maintenance realistically commit to? This decides how to handle the fouling conflict.

**Suggested next step**
Go through questions 1–3 with the team and fix the "M" numbers (especially R-03, R-07, R-20, R-30). Then freeze this as the Stage 1 baseline. Once you've agreed on it, I can save it to the project files as `requirements-v1.md` so Stage 2 (concept and CAD) can trace back to it.

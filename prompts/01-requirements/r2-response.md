# Stage 1 · Round 2 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** before answering, the AI ran 5 web searches: Atlas Scientific EC K1.0 kit price; Atlas Scientific DO kit / EZO-DO price and accuracy; Blue Robotics Celsius price; DFRobot SEN0189 price; Blue Robotics 3-inch enclosure price. The answer text below is verbatim.

---

I'll check current sensor and enclosure prices first, then do the hull analysis and the full revised table.

# SeaSense — Stage 1 Requirements, revision 2

Your 12 L figure is right. But it leaves out the weight the mooring hangs on the buoy, and including it raises the target to about 13.5 L. I recommend a foam-filled printed ring float with a separate sealed electronics canister. The core sensors cost more than the old placeholder allowed: about 7 400 SEK per buoy, mostly the oxygen sensor.

## 1. Checking your buoyancy numbers

**Definition.** "Reserve buoyancy ≥50 %" was ambiguous in my draft, and that's my mistake. I'm now defining it as: *extra lift ≥ 50 % of the floating weight*. (The other common definition, "50 % of total volume above water", would need about 16 L.)

**Your calculation**, using brackish water at ρ ≈ 1.005 kg/L (assumed for about 7 PSU):
- Volume displaced at rest: 8 kg ÷ 1.005 = 7.96 L
- Total buoyant volume needed: 1.5 × 7.96 = **11.9 L** ✔
- Sphere Ø250 mm: 4/3·π·0.125³ = **8.18 L** ✔. Cylinder Ø250 × 250 mm: π·0.125²·0.25 = **12.27 L** ✔

**Four corrections:**
1. **Wall thickness doesn't reduce buoyancy.** Buoyancy depends on the outside volume. Walls only add mass, and that mass is already inside the 8 kg. What matters is how much of the volume stays dry or foam-filled.
2. **Everything below the waterline counts toward the 12 L:** canister, sensor pods, frame. This helps us.
3. **Mooring weight is missing.** The rope and chain hanging from the buoy is a weight it has to carry. With a 1 kg mooring weight in water: 1.5 × 9 kg ÷ 1.005 = **13.4 L**. A future bottom-oxygen sensor on the mooring adds to this too.
4. **Printer size.** "250 mm" may be optimistic. Common printers range from about 250 × 210 × 220 mm to 256 mm cubed, and a Ø250 part leaves no margin anyway. I'm designing to **≤ 200 × 200 × 200 mm per part** until The Fishery confirms its printer.

## 2. Hull options

| | **A. Sealed vertical can** | **B. Flat disc, 4 sealed compartments** | **C. Foam-filled ring float + sealed canister** |
|---|---|---|---|
| Size | Ø230 × 300 mm | Ø400 × 100 mm | Ring Ø400/Ø130 × 100 mm; canister Ø110 × 300 mm |
| Volume | π·0.115²·0.30 = **12.5 L** | π·0.2²·0.1 = **12.6 L** | Ring π(0.2²−0.065²)·0.1 = 11.2 L + canister 2.85 L + pods ≈0.3 L = **14.4 L** |
| Reserve (8 kg + 1 kg mooring) | (12.5·1.005−9)/9 = **40 %** ✘ | **40 %** ✘ | (14.4·1.005−9)/9 = **61 %** ✔ |
| Static draft | 7.96 L ÷ 0.0415 m² ≈ 192 mm | 7.96 ÷ 0.1257 ≈ 63 mm | About 50 mm into the ring (estimate) |
| Printed sections | 2 shell parts + hatch | 4 quadrants (200 × 200 mm) + hatch | 6 ring segments (60° each, about 200 × 144 × 100 mm) + 2 canister caps + frame |
| Where the seams are | 1 seam around the hull, only about 30 mm above the waterline; hatch on top | 4 seams running down through the waterline; hatch | Float seams don't need to seal; canister: top cap above water, bottom cap under water |
| If it leaks | Any leak sinks the buoy and it's lost | One compartment flooded leaves 9.4 L, so it still floats | A cracked segment barely matters (foam). A flooded canister kills the electronics, but the buoy **still floats and can be recovered** |
| Leak risk | **High**: one compartment, printed walls, seam close to the waterline | **Medium**: many seams, but it survives one leak. Electronics still need their own box | **Low**: only a small canister has to stay dry |
| Motion and stability | Narrow, so less waterplane stiffness; needs low ballast | Very stiff, follows the waves; may be stable upside down | Stiff and stable. **Risk:** a wide ring can be stable upside down, so ballast must sit about 0.4 m down |

Option A would need to grow to about 13.4 L (Ø230 × 325 mm) to meet the target. Option B is the same story.

**Other options I considered:**
- **A lighter buoy** doesn't shrink the hull. R-25 is defined at the *maximum* mass with every port filled, so we size the volume for 8 kg no matter what. A lighter actual buoy just floats higher. My mass estimate (below) is about 5.3 kg before ballast, so there are about 2.7 kg left for ballast and growth.
- **Foam filling:** two-part closed-cell polyurethane flotation foam (about 30–50 kg/m³, so roughly 0.5 kg for 11 L) or cut closed-cell foam blocks. **Risk:** expanding pour-in foam can split thin prints, so pour in stages or use cut blocks.

### How the sections join and seal

| Joint | Method | Leak risk | Used in |
|---|---|---|---|
| Ring segment to segment | Through-bolts into a printed or stainless hoop, or bonded with marine PU adhesive (e.g. Sikaflex-291i type). **Doesn't need to seal** | Not relevant (foam-filled) | C |
| Canister top cap (opens for service) | Two radial O-rings on the *smooth outside of an extruded pipe*; printed cap with an epoxy-coated groove; tie-rod clamp | Low: above water, only spray | C |
| Canister bottom cap | Permanently bonded (epoxy or marine PU), with IP68 bulkhead connectors for the sensor ports | Medium: the connectors are the main leak path | C |
| Seam around the hull / compartment seams | Bolted flange with a flat EPDM gasket (tolerates rough printed surfaces better than an O-ring on printed plastic). Printed flanges creep under bolt load, so they need re-tightening | Medium–high | A, B |
| Every printed part that has to keep water out | ≥4 perimeters, 100 % infill near seals, thin epoxy coat to close the pores between print layers | Lowers risk; needs testing | All |

### Recommendation: Option C

It's the only option that meets the 50 % reserve including the mooring load, and the only one where a leak doesn't lose the buoy. It also puts the waterproofing work on one small part we can test on the bench.

**Requirements it affects:**
- **R-24:** the waterproof boundary is now the canister and sensor pods; the float is excluded.
- **R-25:** reserve now includes the mooring load, and the buoy must survive a flooded canister.
- **R-27:** maximum part size.
- **R-15:** ports sit on the bottom cap of the canister.
- **R-31:** mass budget.
- **R-30:** cost now includes the canister.
- **R-26, R-32:** mooring bridle on the frame; light and reflector on a mast on the canister.

**Interpretation to confirm:** the canister tube would be standard 110 mm drainage pipe, not printed. Is that within "the body must be 3D printed"? The float, caps, frame and pods would all still be printed.

**Mass budget for C (estimate, not verified):** printed float about 1.1 kg, foam 0.45, canister 0.65, electronics 0.25, battery 0.3, mast/GNSS/antenna 0.4, light and reflector 0.3, frame and fasteners 0.6, sensor-port allowance 4 × 0.3 = 1.2. **Total ≈ 5.3 kg**, leaving ≈2.7 kg for ballast and margin.

## 3. Off-the-shelf sensors versus the accuracy and cost targets

Prices are converted at about 10 SEK/USD and 11 SEK/EUR (assumed). They exclude VAT, shipping and volume discounts unless noted.

| Module | Proposed part | Spec / price | Meets target? |
|---|---|---|---|
| **Temperature (R-01)** | Blue Robotics Celsius | ±0.1 °C when used between −5 and 50 °C; $76.00. A new version that replaces the TSYS01 sensor with the TMP119 is $70.00 but out of stock. **About 950 SEK with pod** | ✔ Big margin. I'm keeping it because the salinity and oxygen readings both need temperature correction. The cheap fallback is a DFRobot Waterproof DS18B20 Temperature Sensor Kit at $7.50, which has about ±0.5 °C typical (my recollection, not checked) and so no margin |
| **Salinity (R-02)** | Atlas Scientific EC K 1.0 kit | $229.99 (US retail); probe Accuracy: ±2%. **About 2 550 SEK with pod** | ✔ ±2 % at about 12 mS/cm (my estimate for about 7 PSU) is roughly ±0.2 PSU. The target is ±0.5 PSU |
| **Dissolved oxygen (R-03)** | Atlas Scientific DO kit (galvanic) | $354.99 retail, or $319.50 each at 25+ units. **About 3 850 SEK with pod** | ⚠ Atlas quotes an accuracy of ±0.05 mg/L, but that's the electronics. Real-world accuracy is limited by probe drift and membrane fouling, and the probe needs water moving past it (approximately 60 ml/min). ±0.5 mg/L over 30 days is plausible but **unverified**, so it needs a side-by-side field test. An optical DO sensor would cost several times more, so galvanic stays |
| **Turbidity (R-04, optional)** | DFRobot SEN0189 in a potted, light-shielded pod | $9.90; gives Relative turbidity (no NTU value), and the top of the probe is not waterproof. A user reports you need to be mindful of light interference from the ambient environment. **About 350 SEK with pod** | ✔ Fine for "indicative" only. Upgrade path: DFRobot also lists a version rated IP68 fully waterproof, can be submerged long-term with a 0–1000 NTU range. I couldn't confirm its part number or price |

**Two electronics notes:**
- Atlas says when reading Dissolved Oxygen and Conductivity together, it is strongly recommended that the EZO™ Dissolved Oxygen circuit is electrically isolated. Both kits include isolated carrier boards.
- Each circuit draws 0.4mA at 3.3V even in sleep. Three of them is about 1.2 mA × 720 h ≈ 0.86 Ah per month, so they must be switched off completely between readings (R-20a).

**Cost check:**
- Core sensor set ≈ 950 + 2 550 + 3 850 = **≈7 350 SEK**. The oxygen sensor is about half of that.
- Base buoy estimate ≈ **3 800 SEK**: radio and microcontroller about 250, GNSS 200, LiFePO4 battery 350, power board 300, leak sensor 150, antennas 200, canister 200, 4 IP68 bulkhead connectors 480, filament and foam 500, frame and mooring hardware 300, light, reflector and tape 500. All approximate.
- Core-equipped buoy ≈ **11 000 SEK**, above the old 10 000 SEK placeholder. I've raised the placeholders (still to be confirmed with MTC) rather than loosening R-03, because oxygen is the parameter the environmental staff need most.

**Power check for 30 days (rough, Stage 3 will verify):** about 0.12 mAh per 10-minute cycle (sensors on 5 s at 50 mA, GNSS 5 s at 30 mA, LoRa 0.1 s at 120 mA) gives about 18 mAh/day, or about 0.55 Ah per 30 days. One 6 Ah cell is enough even with a 3× margin. So **solar is optional for the prototype**, which simplifies the design.

## 4. Revised requirements table

Pri: **M** = Must (core prototype) · **M-DR** = Must, design rule (met by component or material choice) · **S** = Should · **F** = Future work. Verif.: T test · A analysis · I inspection · D demonstration.

### Must: core prototype

| ID | Requirement | Reason | Need | Verif. |
|---|---|---|---|---|
| R-01 | Water temperature at 0.5 ± 0.1 m depth, −2…+30 °C, **±0.5 °C** | Core parameter; also corrects salinity and oxygen readings | TE-1, ENV-1 | T: 3-point bath test against a reference |
| R-02 | Conductivity, reported as practical salinity, 0–20 PSU, ±0.5 PSU | Brackish water | TE-1, ENV-1 | T: standard solutions |
| R-03 | Dissolved oxygen 0–20 mg/L, **±0.5 mg/L** over the 30-day deployment | Low-oxygen zones | ENV-1, ENV-3 | T: 0 % and 100 % saturation checks; 30-day side-by-side with a reference sonde |
| R-04 | *(Turbidity module, when fitted)* **Indicative** turbidity: relative index calibrated at 2 formazin points (0 and about 100 NTU); repeatability ±10 % of reading; flagged "indicative" in the data | Blooms and sediment; low cost | ENV-1, TE-1 | T: bath with standards; repeat runs |
| R-06 | Every sample has a UTC timestamp (±1 s) and position (±10 m) | Lining data up with trial logs | TE-3, TE-4 | T: compare against a GNSS reference |
| R-07 | ≥95 % of samples reach the shore gateway within 5 min, at up to **3 km** from **one gateway that we supply** (off-the-shelf LoRa gateway on MTC power and internet) | Near real time | TE-2 | T: 7-day field link test |
| R-09 | Versioned message specification: buoy ID, sensor and module IDs, units, quality flags, firmware and calibration IDs | Interface for the shore team | PRG-4, ENV-2 | I: shore team signs off |
| R-10 | Every message reports **battery level and a leak alarm** | Basic health monitoring | MNT-5 | T: wet the leak probe; drain the battery |
| R-15 | ≥4 sensor ports on the canister's bottom cap, all identical: IP68 connector, switched power, a digital bus that works over ≥30 m of cable (e.g. RS-485), and a printed pod mount. **The interface must also work for a sensor on the mooring line (R-35)** | Modularity; future bottom-oxygen sensor | TE-6, PRG-3 | I + D: plug in each core module and a dummy on 30 m of cable |
| R-20a | **≥30 days** without service at a 10-minute sampling interval with the core set fitted | Autonomy for the prototype | MNT-2 | A: power budget; T: 30-day endurance run |
| R-24 | **Electronics canister and sensor pods** watertight to IP68 (1 m, 72 h). Buoyancy sections must not need to be watertight (foam-filled) | Ingress is the main failure mode (changed by the hull choice) | MNT-2 | T: immersion test plus pressure test |
| R-25 | Reserve buoyancy ≥50 % of (max mass under R-31 + design mooring weight ≤1 kg). **Buoy stays afloat with the canister flooded.** Self-rights from 90°; antenna stays clear of the water | Room to add modules; buoy recoverable after a leak (changed by the hull choice) | MNT-1, PRG-1 | A: hydrostatics and righting curve; T: flooded-canister and tilt tests |
| R-27 | All printed parts ≤200 × 200 × 200 mm (to be confirmed against The Fishery's printer), in UV- and saltwater-resistant material (ASA or PETG) | Local production | MNT-4 | I + D: print a full set |
| R-30a | **Base buoy** (hull, electronics, battery, radio, GNSS, canister, ports) ≤4 000 SEK BOM at quantity 20, *to be confirmed with MTC*. Cost must not depend on which modules are fitted | Losing a buoy is acceptable | PRG-1 | A: costed BOM |
| R-30b | **Sensor modules** priced separately, each including its pod and connector: temperature ≤1 000, salinity ≤3 000, oxygen ≤4 000, turbidity ≤500 SEK, *to be confirmed with MTC* | Fleet cost scales with configuration | PRG-1 | A: costed BOM |
| R-31 | ≤**8 kg** ready to deploy with **every port filled** (allowance ≤0.3 kg per module); lifting handle | One-person handling; lets us size the hull | MNT-1 | I: weigh in the maximum configuration |

### Must: design rules

| ID | Requirement | Reason | Need | Verif. |
|---|---|---|---|---|
| R-12 | Licence-exempt EU band (868 MHz SRD) only; complies with ETSI EN 300 220, including duty-cycle limits | Legal operation; no interference with trial radio links | TE-5 | A + I: airtime calculation and module certificate |
| R-32 | Yellow body, retroreflective tape, radar reflector, yellow flashing light, owner contact details on the hull | Visible to boats and uncrewed vessels | TE-5 | I |
| R-33 | No active acoustic emitters; mooring hardware designed so it doesn't rattle | Avoids disturbing sonar trials | TE-5 | I |
| R-34 | No biocidal antifouling; sealed LiFePO4 battery; no hazardous materials released if the buoy is lost | Environmental mandate | ENV-4 | I: material declaration |

### Should

| ID | Requirement | Need | Verif. |
|---|---|---|---|
| R-05 | Sampling interval configurable 1–60 min; trial mode at 1 min | TE-2 | D |
| R-08 | ≥30 days of samples stored on board; missed data resent when the link returns | TE-4 | T: 48 h with the link blocked |
| R-11 | Alert if the buoy moves more than 50 m from its deployed position | MNT-5 | T |
| R-14 | Settings changeable remotely; firmware updated in the workshop without opening the canister | MNT-2 | D |
| R-16 | Sensor module swapped in ≤10 min on a boat, without opening the canister | MNT-3 | D: timed |
| R-19 | A new sensor type needs only a firmware driver and a printed pod | PRG-3 | D |
| R-20b | ≥90 days without service | MNT-2 | A + T |
| R-21 | ≥7 days of operation with no solar input (automatically met if the prototype has no solar) | MNT-2 | A |
| R-23 | Operate at waves ≤1.0 m and wind ≤20 m/s; survive ≤1.5 m and 25 m/s | All | A + T |
| R-26 | Mooring bridle rated ≥2 kN; moorings up to 30 m deep | PRG-1 | T: proof load |
| R-28 | All electronics and sensors available from ≥2 EU suppliers | MNT-4, PRG-2 | I: BOM review |

### Future work

| ID | Requirement |
|---|---|
| R-13 | ≥50 buoys per gateway |
| R-17 | Port power ≥0.5 W average / 2 W peak |
| R-18 | Modules identify themselves (type, serial, calibration) |
| R-22 | Biofouling: drift stays within accuracy over the service interval |
| R-29 | Reprint and refit a damaged part within 24 h |
| R-35 *(new)* | Bottom-oxygen module on the mooring line, using an R-15 port; its weight in water counts against the R-25 mooring allowance |

## 5. Change log

| ID | Old | New | Reason |
|---|---|---|---|
| R-01 | ±0.2 °C | ±0.5 °C | Team scope decision. The chosen part still gives ±0.1 °C |
| R-03 | ±0.3 mg/L or ±5 % | ±0.5 mg/L over 30 days | Team decision; matches what galvanic probes realistically achieve |
| R-04 | ±2 NTU, core sensor | Indicative, optional module | Team decision. A low-cost sensor gives only a relative value |
| R-07 | 5 km, gateway by MTC | 3 km, one gateway supplied by us | Team decision; gateway is now in our scope |
| R-08 | 90 days stored, Must | 30 days, Should | Matches R-20a |
| R-10 | Full health set | Battery level + leak alarm | Team decision |
| R-15 | ≥4 ports, generic bus | Bus must work over ≥30 m; on bottom cap; must support R-35 | Future bottom-oxygen sensor; hull choice |
| R-20 | 90 days, Must | R-20a 30 days (M); R-20b 90 days (S) | Team decision |
| R-24 | Electronics enclosure IP68 | Only canister and pods are watertight; float foam-filled | Hull recommendation (Option C) |
| R-25 | "≥50 % reserve", undefined | Defined as % of weight, including mooring load; must float with canister flooded | Ambiguity in my draft; mooring weight was missing |
| R-27 | 250 mm build volume | ≤200 mm per part, to be confirmed | Printer size unknown; a Ø250 part has no margin |
| R-30 | One combined cost | R-30a base ≤4 000 SEK + R-30b per-module prices | Team decision; real prices push the core set to about 7 400 SEK |
| R-31 | ≤15 kg | ≤8 kg with every port filled | Team decision |
| R-13, 17, 18, 22, 29 | Must or Should | Future | Team decision |
| R-35 | — | New: bottom-oxygen module | Team decision |

**Assumptions made**
- Brackish water density about 1.005 kg/L. Local salinity about 7 PSU, which corresponds to about 12 mS/cm (my estimate).
- Mooring weight in water ≤1 kg (rope with a short chain).
- Standard 110 mm drainage pipe for the canister counts as "off-the-shelf" alongside a printed body.
- Exchange rates about 10 SEK/USD and 11 SEK/EUR. Retail prices from web listings, not quotes.
- Prices for the radio, GNSS, battery and connectors are from my general knowledge, not looked up.
- Sensor pods displace about 0.3 L in total.
- The power estimate assumes the sensor circuits are fully switched off between readings.

**Open questions for the team**
1. Is a non-printed canister tube acceptable under "the body must be 3D printed"? If not, the canister has to be printed and coated, which raises leak risk.
2. What exact printer and build volume does The Fishery have?
3. Will MTC accept about 4 000 SEK for the base buoy and about 7 400 SEK for the core sensors? If not, oxygen is where the money goes. Do we drop oxygen to a cheaper probe or loosen R-03?
4. Is 4 ports enough? With turbidity fitted plus a future bottom-oxygen sensor, we'd need 5. Each extra port adds 0.3 kg to the 8 kg budget and one more leak path.
5. How deep will the moorings be? This sets the mooring weight and the R-35 cable length.
6. Does the gateway need its own requirement (power, mounting, internet connection)?

**Suggested next step**
Answer questions 1–3, then freeze this as Stage 1 baseline v2. Stage 2 should start with a quick model of Option C to check that it rights itself from upside down, since that's its main risk. Once you approve this version, I'll save it to the project as `requirements-v2.md`.

**Sources:**
- [Atlas Scientific EC K1.0 kit – RobotShop](https://www.robotshop.com/products/atlas-scientific-conductivity-sensor-k-10-kit)
- [Atlas Scientific K1.0 probe – RobotShop](https://www.robotshop.com/products/atlas-scientific-conductivity-probe)
- [Atlas Scientific DO kit – RobotShop](https://www.robotshop.com/products/atlas-scientific-dissolved-oxygen-sensor-kit)
- [Atlas Scientific DO kit – Atlas](https://atlas-scientific.com/kits/dissolved-oxygen-kit/)
- [EZO-DO datasheet](https://cdn.robotshop.com/media/a/atl/rb-atl-03/pdf/do_ezo_datasheet-1.pdf)
- [EZO-DO datasheet (legacy)](https://datasheet.chipsmall.com/SEN-11194/154710.pdf)
- [Blue Robotics Celsius](https://claude.wp.bluerobotics.com/?p=5015)
- [Blue Robotics Celsius R3](https://bluerobotics.com/?p=5015)
- [Celsius PCB specs](https://claude.wp.bluerobotics.com/?p=5133)
- [DFRobot SEN0189](https://www.dfrobot.com/product-1394.html)
- [SEN0189 – RobotShop](https://www.robotshop.com/products/gravity-analog-turbidity-sensor)
- [DFRobot turbidity search](https://www.dfrobot.com/search-turbidity%20sensor.html)

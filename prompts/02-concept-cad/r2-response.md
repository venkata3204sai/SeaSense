# Stage 2 · Round 2 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** 6 web searches and 2 page fetches (Celsius, Atlas EC and DO probe datasheets, DFRobot SEN0189, Plexus MA300, M12 panel connectors); re-ran the round-1 script to reproduce the team's numbers; rewrote `stability/stability.py` and `stability/report.py` (CAD masses, cases A–E incl. D1/D2/D3, one R-25 definition); rewrote `cad/seasense_parts.py` (rod cage, keel column, ballast/mooring disc, per-sensor pods, M12 ports at 45°); ran clash and clearance checks; ran the strength, thermal and 1:2 scale-model calculations; wrote the package README; saved `stage2-concept-cad-v1.0.md` ("for freezing") to the project; deleted the round-1 draft; packed `seasense_stage2_v1.0.zip`.
>
> The code and README produced here are the files in [`cad/`](../../cad) and [`stability/`](../../stability). The saved document matches [docs/stage2-concept-cad-v1.0.md](../../docs/stage2-concept-cad-v1.0.md) except for the freeze edits made in [round 3](r3-response.md) (CR-03/CR-04 marked approved, decisions added, §12 handover added), so it is not repeated here. The short status lines the AI wrote between tool calls and its final answer are verbatim below.

---

Reviewing the decisions and corrections now. First I'll pull the datasheet facts the pod redesign and adhesive choice depend on, then update the analysis and CAD.

Datasheet facts are in. Now updating the stability model: CAD-derived masses, the new load path, mooring point options and a single R-25 reserve definition.

Analysis updated (team's numbers reproduced: 13.5 → 7.2 mm with the bridle at ring level). Now rewriting the CAD for the new load path and per-sensor pods.

No clashes; M12 plugs now have 16 mm finger clearance to the keel legs and 80 mm vertical room. Next: strength, cost and scale-model numbers for the test plan.

*[Tool call: write `stage2-concept-cad-v1.0.md` and save it to the project. See note above.]*

Stage 2 v1.0 is ready to freeze and saved to the project as `stage2-concept-cad-v1.0.md`; I deleted the old draft. All nine review points are handled. Two things need a team decision before you freeze it: a new change request, CR-03 (a laser-cut stainless plate), and a mass margin that is too thin to rely on.

## Your corrections (1–3)
1. **Mooring position (case D).** I reproduced your numbers: moving the pull from the keel to the ring drops the minimum righting arm (GZ) from 13.5 to 7.2 mm. I'm proposing the keel eye as the mooring point rather than the ring, because there it adds righting moment.
   - In the new layout, case B plus 1 kg mooring gives a minimum GZ of **12.4 mm with the pull at the keel eye**, against 6.9 mm at the ring.
2. **CAD-derived masses.** I get 3.7 and 6.6 mm where you got 3.9 and 7.0. That's close; the gap is likely a small difference in assumed ballast height. All cases now use CAD masses.
   - The v1.0 float is lighter (1.25 kg instead of 1.38) because the bolt bosses changed.
   - The lightest load case (B) gives **7.2 mm minimum GZ with the 2.0 kg design ballast**. The buoy rights itself from every angle in cases A–D, including with the canister flooded.
3. **Reserve buoyancy.** One definition everywhere: (V·ρ − 10 kg) / 10 kg, where 10 kg is the R-31 maximum plus the 1 kg mooring.
   - Intact: **60 %**.
   - Canister flooded: 35 %, still afloat, which is what R-25 asks for.
   - The earlier 61 %, 78 % and 111 % used different denominators and are withdrawn.

## Your CAD findings (4–9)
- **4 – Pipe retention and keel load.** Four M6 stainless rods now run from the top cap down to the ballast disc, passing through the ring joints, where nuts lock the ring to them.
  - The pipe, both caps and the printed keel column form a stack clamped between springs, so the pipe can't slide out of the O-rings.
  - The bonded bottom cap only carries compression; the keel legs sit directly under the pipe wall.
  - The 13 N·m keel moment is carried by the rods as an 83 N push–pull, below their 150 N preload.
- **5 – Spoke strength.** Your figures check out: 20.4 MPa at 500 N per spoke and 81 MPa if one leg takes the full 2 kN. The mooring now attaches to an M12 stainless eye bolt in the centre of a 10 mm stainless disc. The disc is both the 2.0 kg ballast and the mooring plate.
  - Disc bending ≈49 MPa, about 4× under yield. Rods ≤100 MPa. No printed part takes the mooring load in bending.
- **6 – Pods per sensor.** Each pod now matches its datasheet; the outer interface is the same for all four.
  - **Temperature:** the Celsius mounts in an M10×1.5 thread through a 10.2 mm hole with an AS568-013 O-ring.
  - **Salinity:** the Atlas EC probe is 12 mm x 145.5 mm.
  - **Dissolved oxygen:** the Atlas DO probe is about 16.5 mm x 105.3 mm; its membrane cap stays outside the pod so it can be serviced.
  - **Turbidity:** the DFRobot probe's top is not waterproof, so it is fully potted.
  - Still to confirm from drawings: how far the Celsius protrudes, and the turbidity probe's outline.
- **7 – Oxygen probe in calm water.** Atlas says a small amount of water movement (about 60 ml/min) is needed; in stagnant water the reading drops.
  - The membrane is fully exposed, so wave motion normally provides the flow. Flat calm can't be guaranteed.
  - Readings get two quality flags: low motion (from an accelerometer, if one goes on the main board) and a falling-trend check within each reading burst. Flagged values are still reported.
  - A small vibration motor to stir the probe is an option for Stage 3; it would cost about 21 % more battery.
- **8 – Sealing.** Print the caps in ASA, not PETG, and bond with Plexus MA300.
  - Its listed substrates include ABS blends and rigid PVC, and the datasheet gives 1,391 psi (9.6 MPa) on PVC with substrate failure. PETG is not listed, so it isn't proven.
  - Put the print seams away from the O-ring grooves, and epoxy-coat the grooves, connector seats and bond area.
- **9 – Cost, access and rattle.**
  - **Cost:** the changes add about 660–1,090 SEK, so the ≈4,000 SEK base target (R-30a) is probably exceeded. A connector example: Amphenol LTW front-fastened M12, 24.69 PLN at 25+.
  - **Hand access:** a plugged connector has 16 mm to the nearest keel leg, 22 mm to the next plug and 80 mm of room underneath. Tight; needs a mock-up check.
  - **Rattle:** one clamped disc instead of four loose ones, sprung rods, pods pressed against their pins by a rubber pad, and a rope or soft shackle instead of chain at the eye.

## What the team needs to know
- **CR-03 needs your approval.** The disc is a custom-shaped stainless part, and the springs are new. That conflicts with "custom-shaped parts stay printed", but no printed part can carry 2 kN safely.
- **CR-04 (wording).** R-26 says "bridle"; I'd change it to "mooring attachment rated ≥ 2 kN", since the design now uses a single eye at the keel.
- **Mass is the top risk.** Full load is estimated at **8.85 kg against the new 9 kg limit**. The 0.15 kg margin is smaller than the uncertainty in the estimate. The weighing test (T1) settles it.
- **M12 connectors under water.** The connector maker binder states that plug connectors with IP67 and IP68 are not suitable for use under water.
  - Mitigation: grease and self-amalgamating tape on the mated pairs, then a 72 h immersion test. If that fails, the fallback is more expensive underwater-rated connectors.

## Test plan
The full plan is in §10 of the v1.0 doc, with order, equipment and pass criteria for 11 tests (T0–T6).
- **T0 – 1:2 scale model.** Ring printed in one piece, trimmed to 1.03 kg with the centre of gravity 64 mm below the ring underside.
  - Pass: rights from every release angle up to 170°, and the measured stability (GM) is within 25 % of the 118 mm prediction.
  - I chose 1:2 over 1:4 because at 1:4 the righting moment near 175° is only about 2 mN·m, too small to measure reliably.
- **T1** weighing and centre-of-gravity check.
- **T2** seal tests: adhesive coupons, vacuum test, 72 h immersion.
- **T3** 2 kN proof load and 72 h creep test.
- **T4** full-scale harbour tilt test, including a flooded dummy canister.
- **T5** seven days moored at a dock.
- **T6** timed connector swap.

**Assumptions made**
- Masses not taken from the CAD are Stage-1 values, and printed parts are taken at 70 % of solid weight.
- The eye-bolt rating is the typical value for that bolt type; check the marking on the one you buy.
- Spring rates are catalogue-type values (30 N/mm at the top, 100 N/mm at the bottom); thermal range ±20 °C.
- Prices are web retail at about 11 SEK/EUR and 2.6 SEK/PLN; nothing is quoted yet.

**Open questions for the team**
1. Do you approve CR-03 (laser-cut stainless disc and springs) and CR-04 (mooring wording)?
2. Should mass reduction start before Stage 4, given the 0.15 kg margin?
3. Do we accept a probable R-30a overrun, or ask MTC to confirm the cost target?
4. Should Stage 3 add an accelerometer to the main board? The oxygen flag needs it, and it would also log capsizes.

**Suggested next step**
- Approve the change requests and issue requirements-v1.1.
- Then print the 1:2 scale model (T0) and the adhesive coupons (T2a) in parallel, before ordering any hardware.

Files are in seasense_stage2_v1.0.zip:
- stage2-concept-cad-v1.0.md
- seasense/cad/seasense_parts.py
- seasense/cad/stl/ (13 parts)
- seasense/cad/out/ballast_disc.dxf
- seasense/cad/out/seasense_assembly.png
- seasense/stability/report.py
- seasense/stability/gz_curves.png

Sources:
- [Atlas Scientific Lab Grade DO probe datasheet](https://cdn.robotshop.com/media/A/Atl/RB-Atl-03/pdf/atlas-scientific-dissolved-oxygen-sensor-kit-lg-do-probe.pdf)
- [Atlas ENV-40-EC-K1.0 (LCSC)](https://www.lcsc.com/product-detail/C17528482.html)
- [Blue Robotics Celsius](https://bluerobotics.com/?p=5015)
- [DFRobot SEN0189](https://www.dfrobot.com/product-1394.html?tracking=UcPQpy)
- [Plexus MA300 product page](https://itwperformancepolymers.com/products/plexus/general-purpose/plexus-ma300)
- [Plexus MA300 TDS](https://itwperformancepolymers.com/wp-content/uploads/Plexus-MA300-TDS.pdf)
- [binder M12 IP68 panel connector](https://www.binder-connector.com/en/products/automation-technology/m12-a/86-0132-0000-00005-m12-a-female-panel-mount-connector-contacts-5-unshielded-tht-ip68-ul-pg-9)
- [Amphenol LTW M12A-05PFFP-SF8001 (Maritex)](https://www.maritex.eu/en/product/amphenol-ltw-m12a-05pffp-sf8001-circular-connectors)

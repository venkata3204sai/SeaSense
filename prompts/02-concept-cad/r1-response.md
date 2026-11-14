# Stage 2 · Round 1 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** in this round the AI worked in its own sandbox. It installed CadQuery, wrote and iterated a first version of `stability/stability.py` (point-cloud hydrostatics) and a ballast `sweep.py`, ran a ballast/foam-collar sweep, wrote `stability/report.py` (cases A–F), wrote a first version of `cad/seasense_parts.py` (9 printed parts incl. a proposed keel), thinned walls to save mass, added a clash check, wrote `render_assembly.py` and `render_parts.py`, packed `seasense_stage2.zip`, and saved a short draft summary `stage2-concept-cad-draft.md` to the project.
>
> This **round-1 code is not in this repo.** It was superseded in round 2; the code in [`cad/`](../../cad) and [`stability/`](../../stability) is the frozen v1.0 version. The draft summary was deleted by the AI in round 2 and is excluded here (drafts are not part of the repo). The answer text below is verbatim.

---

I'll read the frozen requirements baseline first, then do the stability calculation, write the CadQuery code, and export the STLs.

The buoy can float stable upside down unless the ballast hangs deep. Ballast inside or under the bottom cap doesn't fix it. With about 2 kg of stainless steel on a rigid keel about 0.58 m below the waterline, the GZ curve stays positive from 0° to 180°, so the buoy always rights itself. The keel also holds the pods at the 0.5 m depth R-01 needs. The CAD shows a second problem: the parts as drawn put the full-load mass over the 8 kg limit in R-31.

## 1. Stability (R-25)

**Method.** Each buoyant volume (ring, canister, mast, light, keel, pods, ballast) is filled with grid points. For each heel angle the script rotates the buoy and moves the waterline until the displaced volume × 1.005 kg/L equals the total mass. The centre of buoyancy (CB) is the middle of the submerged points. The righting arm is GZ = y_G − y_B, where positive means it turns back upright. Heights are measured from the underside of the ring.

**Centre of gravity, case B** (lightest load: 3 pods at 0.2 kg each, 2.0 kg ballast, Stage-1 mass budget):

| Item | m [kg] | z [mm] | m·z |
|---|---|---|---|
| Ring shell + foam | 1.45 | 50 | 72.5 |
| Spokes, frame, fasteners | 0.60 | 50 | 30.0 |
| Canister + caps | 0.65 | 30 | 19.5 |
| Electronics | 0.25 | 20 | 5.0 |
| Battery | 0.30 | −100 | −30.0 |
| Mast, GNSS, antenna | 0.40 | 450 | 180.0 |
| Light + radar reflector | 0.30 | 650 | 195.0 |
| Keel (printed parts + M8 rod) | 0.45 | −362 | −163.1 |
| 3 pods on keel | 0.60 | −450 | −270.0 |
| Stainless ballast | 2.00 | −538 | −1076.0 |
| **Total** | **7.00** | | **−1037** |

- **CG:** z_G = −1037 / 7.00 = −148 mm. The waterline is at +38 mm, so G is 186 mm below the waterline.
- **CB (upright):** displaced volume = 7.00 / 1.005 = 6.97 L.
  - Hand check: ring 4.27 L at 19 mm deep, canister 1.67 L, keel 0.31 L, pods 0.34 L, ballast 0.25 L. That puts B 96 mm below the waterline; the script gives 94 mm.
- **BM:** I = π/4·(0.2⁴ − 0.065⁴ + 0.056⁴) = 1.25×10⁻³ m⁴, so BM = I / V = 179 mm.
- **GM (upright):** 179 + (186 − 94) = 271 mm. The slope of the GZ curve gives 264 mm, which agrees.

**GZ [mm]:**

| φ | A: max load | B: min load | C: B, canister flooded | E: B, no ballast | F: B, 2 kg ballast in bottom cap, no keel |
|---|---|---|---|---|---|
| 30° | 118 | 108 | 120 | 34 | 57 |
| 60° | 150 | 133 | 146 | 11 | 37 |
| 90° | 203 | 189 | 184 | 40 | 28 |
| 120° | 198 | 178 | 171 | 44 | 31 |
| 150° | 82 | 68 | 63 | **−9** | **−18** |
| 165° | 30 | 21 | 19 | **−24** | **−25** |
| Upside down? | rights | rights | rights | **stable** | **stable** |

**Ballast:**
- **Recommended:** 2.0 kg as four removable 0.5 kg stainless discs (Ø76 mm) on the keel, so the team can trim after weighing the real build.
- **Minimum:** about 1.5 kg (case B). Below that, the light-load case stays stable upside down.
- **Weak spot:** with 2.0 kg, near 175° the arm is only about 7 mm, so the buoy rights itself slowly from almost fully inverted.
  - An optional 1 L foam collar on the mast adds about 3–4 mm there; I modelled it but did not include it in the CAD.
- **No lead** (R-34).

**Limits of the model:**
- It is static only: no waves, no dynamic rolling.
- The grid adds about ±2 mm of noise to GZ.
- The jump near 90° comes from the mast and keel crossing the waterline. It depends on my guesses for mast and light buoyancy.
- The mooring is treated as a 1 kg weight pulling straight down.

## 2. Parametric CAD

`cad/seasense_parts.py` has every key dimension at the top, each tagged with its requirement ID. All parts are valid solids, there are no clashes in the assembly, and every part is under 240 mm (R-27).

| Part | Qty | Bounding box [mm] | Requirements | Notes |
|---|---|---|---|---|
| ring_tray | 4 | 204×200×98 | R-25, R-27 | **Changed:** open tray instead of a closed shell (see below). Tongue-and-groove ends, bolt bosses |
| ring_lid | 4 | 200×200×2 | R-25 | Foam fill and vent ports |
| spoke | 8 | 193×81×30 | R-26, R-27, R-31 | Same part top and bottom, sitting over each segment joint. Saddle clamps the pipe with a hose clamp. The eye at the outer end is for the mooring bridle or lifting |
| top_cap | 1 | 172×172×78 | R-14, R-24 | Two 110×3.5 O-rings at 20 % squeeze, blind mast socket, 2 cable glands plus a service connector, tie-rod lugs |
| bottom_cap | 1 | 118×118×60 | R-15, R-24 | 0.25 mm bond gap, 4 × M16 connector holes with spot faces, 4 bosses for the keel |
| sensor_pod | 4 | 46×36×110 | R-01…R-04, R-16, R-19 | Potted cavity, probe bore sized by a parameter, slides onto a dovetail and is held by a pin |
| keel_flange / keel_strut / pod_carrier | 1 / 2 / 1 | ≤80×80×125 | R-25, R-01 (**proposed**) | Printed sleeves clamped in compression on an M8 stainless rod |

The ring segment is now an open tray with a bonded lid. A closed shell would need a 130 mm unsupported ceiling, which can't be printed. The open tray also lets the foam expand freely, which addresses the baseline risk of foam splitting the walls.

## 3. STL files and rendering

- **STL files:** `cad/stl/*.stl` (9 parts).
- **Assembly:** `cad/out/seasense_assembly.step` and `.glb`.
- **Rebuild everything:** `python seasense_parts.py`.
- **Quick preview image:** `python render_assembly.py 46`. It's rough; matplotlib draws some faces in the wrong order.
- **Better renders:**
  - FreeCAD: import the STEP file; part names and colours are kept.
  - CQ-editor: add `show_object(assembly())` to the script.
  - VS Code: `ocp_vscode.show(assembly())`.
  - Blender, for pitch images: import the GLB and add a water plane at z = 0.046 m.
- The README in the zip has the steps and print settings.

## Changes to the frozen baseline that need your decision

- **CR-01 (R-27):** the keel adds non-printed structural parts: a stainless rod and ballast. The mast tube is also not printed. R-27 currently says all structural parts except the pipe are printed. I propose wording that also allows stainless fasteners, rods, ballast and the mast tube.
- **CR-02 (R-31):** masses from the CAD are higher than the Stage-1 budget.
  - Float: ≈1.38 kg (budget 1.0). Frame and bolts: ≈1.1 kg (0.6). Canister and caps: ≈0.85 kg (0.65).
  - Full load then comes to **≈8.2 kg with 1.5 kg ballast, or 8.7 kg with 2.0 kg**, against the 8 kg limit.
  - Rerunning the stability with these masses still needs about 1.5 kg of ballast as the minimum.
  - Option 1: cut about 0.7 kg (8 bolts instead of 16, lighter spokes).
  - Option 2: raise the limit to 9 kg. Reserve buoyancy would then be 60 %, still above the 50 % required.

I also saved a short draft summary to the project as `claude/stage2-concept-cad-draft.md`. It is marked as not frozen.

**Assumptions made**
- Mass positions are estimates. The pipe is assumed to be PVC-U 110×3.2.
- Mast is 25 mm and 500 mm long, sealed. Light housing is 0.23 L.
- Ballast is stainless steel at 7.9 kg/L.
- Brackish water at 1.005 kg/L. Pods are 36 × 110 mm, about 0.11 L each.
- Part sizes are unconfirmed: O-ring 110×3.5, M16 panel connectors, a probe diameter of 12.5 mm.
- Print clearance is 0.3 mm per side; tune it on test prints.

**Open questions for the team**
1. Do you accept CR-01 (keel, rod and ballast as non-printed parts)?
2. For CR-02: cut mass, or raise R-31 to 9 kg?
3. Is a buoy about 1.35 m tall with the keel 0.6 m below the surface OK for launching from a boat and for the shallowest mooring sites?
4. Which IP68 connector family do we use? Its hole size and thread affect the bottom cap.
5. Is a rope handle through two top-spoke eyes acceptable as the R-31 lifting handle?

**Suggested next step**
- Print one ring tray, one spoke and the top cap, and check the fit on the real pipe and O-rings.
- Weigh the printed parts to firm up CR-02.
- Then do a tilt and inversion test in a tank or bucket with a scaled ballast stack, to check the GZ predictions against reality before Stage 3.

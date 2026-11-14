# Stage 1 · Round 2 · Prompt (verbatim)

```text
Team review of your draft. We want a smaller first prototype. Please revise the
requirements with these decisions:

SCOPE DECISIONS
- Core sensor set (always fitted): temperature (R-01), salinity (R-02),
  dissolved oxygen (R-03).
- Turbidity (R-04) becomes an optional sensor module, fitted only when needed.
- Cost (R-30): split into base buoy (hull, electronics, battery, radio, GPS) and
  sensor modules priced separately. Base buoy cost must not depend on which
  modules are fitted. Keep targets as placeholders "to be confirmed with MTC".
- Mass (R-31): ≤8 kg ready to deploy, INCLUDING all sensor ports filled. Reserve
  buoyancy must leave headroom so modules can be added without the buoy sinking.

MUST (core prototype, about 15):
R-01, R-02, R-03, R-06, R-07, R-09, R-10, R-15, R-20, R-24, R-25, R-27, R-30, R-31
plus R-04 as Must for the turbidity MODULE (when fitted).
Changes:
- R-01 accuracy ±0.5 °C; R-03 accuracy ±0.5 mg/L; R-04 "indicative" accuracy.
- R-07 range 3 km to one shore gateway (we supply the gateway).
- R-10 reduce to battery level + leak alarm.
- R-20 autonomy 30 days (90 days becomes a Should).

DESIGN RULES (keep as Must, met by component/material choice):
R-12, R-32, R-33, R-34

SHOULD: R-05, R-08, R-11, R-14, R-16, R-19, R-21, R-23, R-26, R-28

FUTURE WORK: R-13, R-17, R-18, R-22 (biofouling), R-29, and a bottom-oxygen
module on the mooring line (the modular interface R-15 must allow for it).

PROBLEM WE FOUND IN YOUR DRAFT
With 8 kg and ≥50% reserve buoyancy, the hull needs about 12 L of enclosed volume. But that is cube-equivalent: a 250 mm sphere is only ~8.2 L and a 250×250 mm cylinder ~12.3 L, before walls, lids and sensor ports. So the hull will most likely need to be printed in several sections. Please reason about this: 
- Check our numbers. 
- Propose 2–3 hull shapes suitable for a moored buoy in sheltered archipelago water, and for each one estimate the enclosed volume, how many printed sections it needs, and where the seams would be. 
- Explain how the sections would be joined and sealed (to meet R-24), and the leak risk of each option. 
- Consider alternatives too, e.g. a lighter buoy, foam-filled buoyancy sections that don't need to be watertight, or a separate printed float plus a sealed electronics canister. 
- Recommend one option and say which requirements it affects.

ALSO
- For the core sensors and the turbidity module, propose real off-the-shelf
  sensors with approximate prices. Check that the accuracy targets fit the cost
  targets; adjust and explain if not.
- Keep the same ID scheme. Give the full revised requirements table, then a
  short change log (old → new, reason).
```

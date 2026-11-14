# Stage 1 · Round 3 · Prompt (verbatim)

```text
Our answers to your open questions:
1. Non-printed 110 mm pipe for the canister is accepted (reduces leak risk);
   all other structural parts stay 3D printed.
2. Printer: the BTH Ericsson lab has two Bambu Lab printers with build volumes
   256×256×256 mm and 300×320×320 mm. We assume The Fishery has printers at least
   this capable. Set R-27 to ≤240×240×240 mm per part (fits the smaller printer
   with margin). Check whether the ring float can now use fewer segments than 6,
   and update the hull concept.
3. Accept the cost placeholders (base ~4 000 SEK, core sensors ~7 400 SEK),
   to be confirmed with MTC. Keep the Atlas galvanic DO sensor.
4. Keep 4 ports. Confirm that the RS-485 bus can daisy-chain more than one
   sensor on a port, so the future bottom-oxygen module (R-35) can share one.
5. Mooring depth ≤20 m.
6. Add one Should requirement for the shore gateway (power, mounting, internet).

We also checked your power estimate: GNSS often needs ~30 s for a fix, not 5 s.
Recalculate the 30-day budget with 30 s GNSS time and confirm the battery is
still enough.

Then give the final frozen requirements as "requirements-v1.0": one clean table
(ID, requirement, priority, need, verification), the hull concept summary
(Option C) and the assumptions list. No change log needed this time.
```

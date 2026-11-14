# Stage 3 · Round 1 · Prompt (verbatim)

Chat: "Stage 3 Electronics" (Claude project "SeaSense").

```text
Stage 3: Electronics. Baselines are requirements-v1.1 and stage2-concept-cad-v1.0
(see its §12 handover) in the project files.

Team decisions before you start:
- CR-05: R-30a base buoy ≤5,000 SEK, R-30b core sensor set ≤7,500 SEK (complete
  buoy ≤12,500 SEK), based on a YSI EXO1 + CT + optical DO costing ~86,000 SEK.
  Still "to be confirmed with MTC".
- Add R-37 as a Should: report indicative wave statistics (significant wave
  height and peak period) from the IMU, flagged "indicative".
- Time is limited: this is a single round. Be concise and concept-level.

Tasks:
1. Select the electronics: microcontroller, LoRa radio (868 MHz), GNSS, IMU,
   power system (2× LiFePO4), sensor interface per pod (note: Atlas isolated
   carrier boards don't fit the Ø34 × ~60 mm pod space), RS-485 per port, leak
   sensor. Parts list with approximate prices, linked to requirement IDs.
2. Block diagram (Mermaid) and M12 port pinout.
3. Power budget with the chosen parts, IMU and optional DO stirrer; confirm
   R-20a (30 days) and R-20b (90 days).
4. Data message format (R-09): fields, sizes, quality flags (incl.
   DO_LOW_MOTION, DO_DEPLETION_SUSPECT), and LoRa airtime vs the 1 % duty cycle
   (R-12), including trial mode.
5. Firmware structure (wake → read → flag → send → sleep) with a short code
   skeleton.
6. Update the cost estimate against CR-05.

End with the main risks and assumptions, then save everything as
stage3-electronics.md in the project.
```

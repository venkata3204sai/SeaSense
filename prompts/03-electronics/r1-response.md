# Stage 3 · Round 1 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** the AI read requirements-v1.1, stage2-concept-cad-v1.0 and the process log from the project; ran 3 web searches (Atlas ENV-40-EC-K1.0 price; Atlas ENV-40-DOX / EZO-DO price; RAK4630 price); wrote and ran a Python calculation script for LoRa airtime (Semtech formula) and the power budgets (configs A–E and trial mode); then wrote the Stage 3 document and saved it to the project as `stage3-electronics.md` (draft v0.1, "single-round concept, NOT frozen").
>
> The draft v0.1 is **not included** in this repo (drafts excluded). The frozen version is [docs/stage3-electronics-v1.0.md](../../docs/stage3-electronics-v1.0.md); it differs from the draft only by the freeze edits listed in [round 2](r2-response.md) (status, P-1…P-4 marked approved, stirrer marked dropped, R-20b wording, risk row 2, assumptions 8–10, remaining open items). The answer text below is verbatim.

---

I'll read the baselines first, then produce the Stage 3 electronics package and save it to the project.

I have the baselines and the numbers. Now I'll write the Stage 3 document.

*[Tool call: write and save `stage3-electronics.md` (draft v0.1). See note above.]*

The Stage 3 electronics package is saved to the project as `stage3-electronics.md`. On paper it meets the 30-day endurance target (R-20a) and the 7,500 SEK sensor limit (R-30b). It does not meet the 90-day target (R-20b) at the default settings, and the base buoy likely goes over 5,000 SEK. Nothing is measured yet; all figures are estimates.

**Main choices**
- **Main board:** RAK4630 module (nRF52840 microcontroller + SX1262 LoRa radio). Its BLE lets us update firmware without opening the canister (R-14), switched on only by a magnet so it costs no power when deployed. It is listed at about $15, and the datasheet gives about 4.2 µA in sleep and 67.8 mA when transmitting 15 bytes. I budgeted 90 mA for transmit to leave margin.
- **Other parts:** u-blox MAX-M10S for GNSS, LSM6DSOX for the IMU, BME280 for canister humidity and pressure, a comb-type leak probe, 16 MB flash, and two 6 Ah LiFePO4 cells in parallel with a MAX17260 fuel gauge.
- **Ports:** each of the four ports gets its own current-limited 12 V switch and its own fault-protected RS-485 chip, so one flooded port can't take down the others. Port power is 12 V because 5 V drops too much over 30 m of cable.
- **Sensor pods:** one common node board with an optional isolated section for the EC and DO pods. It is two Ø30 mm discs, which should fit the Ø34 × 60 mm pod space, but the fit still needs checking with a 3D layout.
- **M12 pinout:** follows the DeviceNet layout (1 shield, 2 +12 V, 3 GND, 4 D+, 5 D−), so we can buy standard cables, T-splitters and terminators.

**Results**
| Check | Result |
|---|---|
| R-20a (30 days at 10 min) | ✓ about 42 days for the core set; 36–38 days with turbidity and/or the stirrer |
| R-20b (90 days) | ✗ at the default settings. ✓ about 112 days with a 20-minute interval, faster GNSS fixes and an hourly DO burst |
| R-12 (1 % duty cycle) | ✓ at every spreading factor in normal mode. Trial mode only works at SF10 or lower, because SF10–12 limit messages to 51 bytes |
| R-30a (base ≤5,000 SEK) | ✗ likely: about 5,400 SEK (range 5,000–5,750) |
| R-30b (core sensors ≤7,500 SEK) | ✓ about 6,940 SEK |
| Complete buoy (≤12,500 SEK) | ✓ about 12,340 SEK, only about 160 SEK of margin |

Sensor prices behind R-30b: the EC probe is about €152 ex VAT at DigiKey, the DO probe $243.99, and the EZO-DO board €41.59.

**Things you should know**
- **Power is about 3× the Stage 1 estimate.** The DO depletion burst defined in Stage 2 (10 readings over 30 s) uses 52 % of each cycle's energy. GNSS uses 22 % and the isolated EC pod 20 %. The pod currents are guesses, so this is the biggest uncertainty.
- **The DO stirrer conflicts with R-33** (no active acoustic emitters). A vibration motor in the water is a noise source in an acoustic test area. I recommend not fitting it unless MTC approves.
- **Trial mode is costly:** one trial day uses as much battery as about 4.3 normal days. I made it switch itself off after 24 hours by default.
- **The Things Network won't work:** its 30 s per day airtime limit is exceeded (about 44 s per day at SF9), so we need our own network server on the shore gateway.
- **Proposed changes to frozen baselines (none applied):**
  - **P-1:** two antenna cable feedthroughs in the Stage 2 top cap, which has no path for them. This is a new leak path.
  - **P-2:** allow the DO burst to run hourly instead of every sample.
  - **P-3:** add CR-05 and R-37 to requirements-v1.2, and give R-20b a stated interval.
  - **P-4:** drop the stirrer option.

**Assumptions made**
- Prices are web retail at quantity 20, not quotes. The Celsius, EZO-EC, cell and gateway prices are not checked.
- Pod power, IMU and GNSS backup currents are estimates. GNSS is 30 mA × 30 s per cycle, as the team corrected in Stage 1.
- Usable battery is 8.64 Ah with 3 % self-discharge per month.
- MTC provides a gateway site where we can run a private network server.

**Open questions for the team**
1. Do you accept P-1 to P-4?
2. Does MTC allow BLE use and any vibration source in the test area?
3. Is a 20-minute interval acceptable for 90-day deployments?
4. Is "Hs within ±20 % or ±5 cm, Tp within ±0.5 s against a reference" the right pass criterion for R-37?
5. Will the gateway site give SF9 or lower across the whole 3 km area? Trial mode depends on it.

**Suggested next step**
Build a bench setup: RAK4631 WisBlock, MAX-M10S, LSM6DSOX and one isolated EC pod on 30 m of cable. Log the current over a full cycle to replace the estimated pod and GNSS figures, which decide R-20a.

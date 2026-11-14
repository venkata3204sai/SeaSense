# Stage 1 · Round 3 · AI response (verbatim)

> **Tool activity (summary, not verbatim):** the AI saved the full frozen requirements document to the project as `requirements-v1.0.md`. That document is identical to [docs/requirements-v1.0.md](../../docs/requirements-v1.0.md), so it is not repeated here. The answer text below is verbatim.

---

I'll check whether fewer segments now fit, rework the power budget, and save the frozen baseline to the project.

*[Tool call: project_write `requirements-v1.0.md`. Content = [docs/requirements-v1.0.md](../../docs/requirements-v1.0.md)]*

I've saved requirements v1.0 to the project as `claude/requirements-v1.0.md` and marked it frozen as the Stage 1 baseline. It contains the full requirements table, the Option C hull summary and the assumptions list. The checks you asked for:

## Ring segments: 6 → 4
- **4 × 90°:** each quarter-ring (OD 400, ID 130, height 100 mm) fits in a **200 × 200 × 100 mm** box, inside 240³. ✔
- **3 × 120°:** the outer edge is 2 · 200 · sin 60° = **346 mm** long. That's longer than 240 mm, and longer than the diagonal of the 240 mm build area (339 mm). ✘
- **Result:** 4 segments. That means a third fewer joints and foam pours, and about 0.1 kg less mass because there are fewer end walls. The total volume, reserve buoyancy (about 61 %) and draft are unchanged.

## Sharing a port on the RS-485 bus: yes, with three conditions
RS-485 is built for several devices on one cable. The standard allows up to 32 devices per bus and long cables, so 20–30 m is easy. Three conditions are now written into R-15:
1. **The protocol must address each device** (e.g. Modbus RTU). As far as I know, the Atlas circuits can't be addressed in UART mode, so each module needs a small microcontroller acting as its RS-485 node. This is assumption 7 in the document; check it against the datasheet in Stage 3.
2. **Wiring:** each module has a pass-through connector or uses a T-splitter, the far end gets a termination resistor, and branch cables stay short.
3. **Power:** the port's power budget has to cover both modules. Voltage drop over 20 m is small: with 0.25 mm² wire the round trip is about 2.8 Ω, so about 0.14 V at 50 mA.

## Power budget with a 30 s GNSS fix
Charge used per 10-minute cycle (estimate):

| Item | Current | Time | Charge |
|---|---|---|---|
| Sensors | 50 mA | 5 s | 250 mAs |
| **GNSS fix** | 30 mA | **30 s** | **900 mAs** |
| Microcontroller awake | 5 mA | 35 s | 175 mAs |
| LoRa transmit | 120 mA | 0.1 s | 12 mAs |
| **Per cycle** | | | **1 337 mAs = 0.371 mAh** |

- Per day: 144 cycles × 0.371 = 53.5 mAh, plus sleep 0.1 mA × 24 h = 2.4 mAh, giving **55.9 mAh/day**.
- Over 30 days: 1.68 Ah. Divided by 85 % converter efficiency, that's **≈2.0 Ah**. My earlier estimate was 0.55 Ah, so your correction roughly triples it.
- Battery: 2 × 6 Ah LiFePO4 cells in parallel. After allowing 80 % usable discharge and losses in cold water, about **8.6 Ah is usable**. That's **4.4× margin for 30 days** ✔. One cell alone would still give 2.2×.
- 90 days needs about 5.9 Ah, which is less than 8.6 Ah. So R-20b also looks reachable on battery alone (estimate).
- **Trial-mode warning:** if the GNSS fixed every minute, each trial day would use as much as about 10 normal days. So trial mode keeps GNSS fixes at 10-minute intervals and only the sensors sample every minute (assumption 9). Time stays within ±1 s between fixes on the real-time clock.
- The GNSS is about two-thirds of the energy per cycle, so it's the cheapest thing to improve. Keeping its backup supply on gives faster "hot" fixes and is worth testing in Stage 3.

## Gateway
I added **R-36 (Should)**:
- off-the-shelf outdoor 868 MHz gateway, at least IP65
- powered from MTC mains or PoE
- antenna at least 10 m above sea level, with line of sight to the test area
- Ethernet internet connection
- forwards data in the R-09 format
- stores at least 24 h of data if the internet drops

**Assumptions made** (the full list is in the document)
- The power figures are typical datasheet-style values, not measurements.
- The gateway antenna height of at least 10 m is my estimate for 3 km over water with islands in the way.

**Open questions for the team**
1. Who confirms the cost placeholders with MTC, and by when? R-30a and R-30b stay provisional until then.
2. Can MTC actually provide a gateway site at least 10 m above sea level? If not, R-07 coverage is at risk.

**Suggested next step**
Start Stage 2 (Concept & CAD) in a new chat using `requirements-v1.0.md` as the baseline. The first task should be a stability check of Option C: work out how much ballast is needed, how deep it sits, and whether the buoy rights itself from upside down, since that's the biggest unchecked risk.

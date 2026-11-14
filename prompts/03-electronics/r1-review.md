# Stage 3 · Round 1 · Review

Review done in our separate reviewer chat; team decisions by the team.

## What the AI caught
| # | Finding | Type |
|---|---|---|
| 1 | **Power ≈3× the Stage 1 estimate** (6.16 vs 2.0 Ah per 30 days). Drivers: DO burst 52 %, GNSS 22 %, isolated EC pod 20 %. | Caught by the AI |
| 2 | **The 90-day target (R-20b) fails at the default settings.** Only reachable with a 20-min interval, GNSS hot starts and an hourly DO burst. | Caught by the AI |
| 3 | **Its own Stage 2 DO stirrer conflicts with R-33** (no active acoustic emitters). The AI caught a gap in its earlier output. | Caught by the AI |
| 4 | **The Things Network fair-use airtime limit is exceeded** (≈44 s/day vs 30 s/day at SF9) → private network server on our gateway. | Caught by the AI |
| 5 | **Trial mode only possible at SF ≤10** (51-byte payload limit at SF10–12). | Caught by the AI |
| 6 | **No antenna cable path in the Stage 2 top cap** → P-1 (RF feedthroughs). | Caught by the AI |

## What we checked by hand
| Check | Our result | Matches doc? |
|---|---|---|
| Energy per 10-min cycle (core set) | **15.26 J = 1.32 mAh** | Yes |
| Endurance, core set at 10 min | **42 days** (8.64 Ah / 6.16 Ah per 30 d) | Yes |
| Airtime, default mode at SF12 | **0.38 %** of time = **38 % of the 1 % legal limit** | Yes |
| Payload limits (51 B at SF10–12, 115 B at SF9) vs message sizes | Consistent | Yes |
| M12 pinout | Consistent with R-15 | Yes |

## Decisions (team)
- **P-1 to P-4 accepted**: top-cap RF feedthroughs; hourly DO burst in the 90-day profile; R-20b at a 20-min interval; stirrer dropped.
- **MTC assumptions** (to be confirmed): BLE only during magnet-activated service windows is acceptable; a 20-min interval is acceptable for 90-day deployments; the gateway site gives SF ≤9 across the 3 km area (verify in the R-07 link test).
- **R-37 pass criterion**: Hs ±20 % or ±5 cm, Tp ±0.5 s against a reference.

## Why we sent the next prompt
[r2-prompt.md](r2-prompt.md) sends these decisions and asks for the freeze: stage3-electronics-v1.0 and requirements-v1.2 (CR-05, R-37, P-3), with no further analysis.

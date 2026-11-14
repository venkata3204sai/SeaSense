# Stage 1 · Round 1 · Review

Review done in our separate reviewer chat; team decisions by the team.

## What we checked
- Number and priority of the requirements.
- Whether the hull volume implied by R-25 (reserve buoyancy) and R-31 (mass) fits R-27 (printer size), by hand calculation.

## What we found
| # | Finding | Type |
|---|---|---|
| 1 | The AI gave **34 requirements**, of which **~28 were Musts**. Far too many for a first prototype. | Scope |
| 2 | **Hull vs printer conflict.** 15 kg (R-31) with ≥50 % reserve buoyancy (R-25) needs a hull of **~22.5 L**. A 250 mm printer (R-27) gives at most **15.6 L**, and that is a cube. A Ø250 mm sphere is only **8.2 L**, a Ø250 × 250 mm cylinder **12.3 L**. | Caught in review (hand calculation) |

## Decisions (team)
- Cut to **~15 Musts** (core prototype); the rest become design rules, Should or Future work.
- **Turbidity becomes an optional module.**
- **Cost split** into base buoy + separately priced modules.
- Mass **≤8 kg including all ports filled**.
- Ask the AI to **reason about hull shapes** instead of prescribing one, so we can review its reasoning.

## Why we sent the next prompt
[r2-prompt.md](r2-prompt.md) gives the scope decisions above, states the volume problem with our numbers (at 8 kg) and asks the AI to check them, propose 2–3 hull options with volumes, seams and leak risks, consider foam-filled sections or a separate sealed canister, and propose real sensors with prices.

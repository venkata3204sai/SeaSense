# 00 · How we arrived at the problem

## 1. Candidates we considered
| Candidate | Idea |
|---|---|
| Water-quality buoy | Low-cost buoy that measures water conditions in the archipelago |
| Ice-detection buoy | Buoy that detects and reports ice conditions |
| Hull-inspection USV | Small uncrewed surface vessel for hull inspection |
| Ghost-gear tag | Tag for finding lost fishing gear |

## 2. What we chose
**Eutrophication monitoring in the Blekinge archipelago.** The archipelago suffers from eutrophication, algal blooms and low-oxygen zones, and a test area for maritime trials needs to know its water conditions.

## 3. Scoping
1. We first sketched a 4-layer system: **Sense → Predict → Trace → Act**.
2. We then **cut the scope to the buoy only** (Sense). Predict, Trace and Act stay as the future vision.
3. We made the scenario **hypothetical**: an MTC test area with three user groups (test engineers, MTC environmental staff, maintenance staff). We used no internal Saab/MTC knowledge, and the project instructions tell the AI to state anything about Saab, MTC or The Fishery as an assumption.

## 4. How we wrote the brief
- Written in a **client-brief style** that we learned in a previous course (see [brief.md](brief.md)).
- We gave the AI **only the constraints it could not know** (users, location, 3D printing at a local workshop, gateway on shore, scope boundary towards the shore data team).
- We **left design choices to the AI** (hull shape, sensors, radio, numbers) so that we could review them. Every review round is logged in this folder's siblings.

Next: [project-instructions.md](project-instructions.md) · [brief.md](brief.md) · [Stage 1 round 1](../01-requirements/r1-prompt.md)

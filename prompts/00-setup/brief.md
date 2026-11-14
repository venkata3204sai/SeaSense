# 00 · The brief as sent

This is the brief exactly as it was sent: the first part of the Stage 1 round 1 prompt, everything above the `---` line (see [../01-requirements/r1-prompt.md](../01-requirements/r1-prompt.md) for the full prompt including the task instructions).

```text
PROJECT "SeaSense" (hypothetical brief)

The Marine Technology Center (MTC) in Karlskrona wants a system for continuous
water monitoring in its test area in the Blekinge archipelago: measuring water
conditions such as temperature, salinity, oxygen and turbidity, sending the data
to shore, and supporting future unspecified measurements and uses.

Users: test engineers from companies such as Saab, who run trials with uncrewed
vessels, underwater vehicles and sonar and need to know the water conditions
during each trial; MTC staff, who must show that trial activities do not harm
the environment (the archipelago suffers from eutrophication, algal blooms and
low-oxygen zones); and maintenance staff, who deploy and service the buoys. MTC
expects to deploy 10–20 buoys in the first season and scale up if successful.

Requirements:
- The system consists of floating buoys that are as autonomous as possible: once
  deployed, they should run for long periods without service.
- The buoys must be modular, so sensors can be added, removed or replaced
  depending on what a trial or environmental study needs.
- The buoy body must be 3D printed so it can be produced and repaired in MTC's
  local workshop (The Fishery), using off-the-shelf sensors and electronics.
- Data must be available to users on shore in near real time, and stored so that
  conditions can be compared between test runs and over time.
- Each buoy must be cheap enough that losing one is acceptable.
- It is assumed that MTC can place a receiver/gateway on land with power and
  internet access, and that the buoys operate in the sheltered archipelago during
  the ice-free season.
- The shore-side data platform and analytics will be handled by another team;
  your responsibility is the buoy itself and the specification of the data it
  sends, so that team can build on it.
```

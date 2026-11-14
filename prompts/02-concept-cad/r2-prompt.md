# Stage 2 · Round 2 · Prompt (verbatim)

```text
Team review of Stage 2.

DECISIONS
- CR-01 accepted: stainless fasteners, M8 rod, ballast discs and mast tube may be
  non-printed. All custom-shaped parts stay printed.
- CR-02: raise R-31 to ≤9 kg. Mass reduction becomes future work.
- 2.0 kg ballast is the design value (not 1.5 kg minimum).
- Use M12 IP68 circular connectors unless you see a better low-cost option.
- Rope handle through top-spoke eyes is accepted for R-31.

CORRECTIONS FROM RERUNNING YOUR STABILITY SCRIPT
1. Case D puts the mooring pull at the keel bottom (z_bridle = -585), but the
   bridle attaches to the bottom-spoke eyes at the ring (~z = 0). With z_bridle = 0
   the minimum GZ (5–175°) drops from 13.5 to 7.2 mm (case B). Update case D.
2. The GZ cases use Stage-1 budget masses. Rerun with the CAD-derived masses
   (float 1.38, frame 1.1, canister 0.85 kg). We get min GZ 3.9 mm at 1.5 kg
   ballast and 7.0 mm at 2.0 kg.
3. Reserve buoyancy is reported as 61 %, 78 % and 111 % in different places. Use
   one definition (R-25) consistently.

FINDINGS FROM OUR REVIEW OF THE CAD CODE
4. Load path / pipe retention: the keel, pods and ballast (~3.6 kg) hang from the
   bonded bottom cap, and the pipe is held to the spokes only by hose-clamp
   friction, while the top cap is tied to the spokes. If the pipe slips (e.g.
   lifting the buoy out of the water by the spoke eyes), it slides out of the top
   cap and the O-ring seal is lost (~25 mm margin). The bonded bottom cap is also
   our main seal but now carries ~13 N·m keel moment when the buoy lies on its
   side. Propose a positive axial stop for the pipe and a keel attachment that
   does not load the sealing joint.
5. Spoke strength (R-26): the bridle pulls down on the bottom-spoke eye 43 mm
   beyond the outer bolt; spoke section 44×12 mm. Our estimate: ~20 MPa bending at
   500 N per spoke (2 kN shared by 4 legs), ~80 MPa if one leg takes most of the
   load. Too high for printed PETG/ASA, especially with creep. Check this and
   propose a better mooring load path (e.g. a stainless bridle plate).
6. Pods: PROBE_D = 12.5 mm for every pod, but the Celsius sensor and the Atlas DO
   probe are different. Make pod dimensions per sensor from the datasheets.
7. DO probe flow: the galvanic probe needs water movement past the membrane. How
   does the pod ensure flow in calm water? If it cannot, say how readings are
   flagged.
8. Sealing: recommend an adhesive proven for PVC-to-PETG/ASA bonding, and specify
   seam placement away from O-ring grooves plus epoxy coating of sealing faces.
9. Update the R-30a cost with the keel, rod and ballast; check hand access to
   unplug connectors under the keel flange (R-16); and check for rattle from the
   ballast discs and pod pins (R-33).

THEN
- Update the CAD and analysis for the changes above.
- We will NOT do physical tests during the hackathon. Instead, write a short
  physical test plan for later (e.g. at The Fishery): which tests verify the
  stability, sealing, mooring-strength and mass claims, in what order, what
  equipment is needed, and the pass criteria. Include a low-cost scale-model
  inversion test as the first step.
- Give the final Stage 2 summary as "stage2-concept-cad-v1.0" for freezing.
```

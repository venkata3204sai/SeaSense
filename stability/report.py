"""Stage 2 v1.0 stability cases -> results.json, gz_curves.png, printed tables."""
import json, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from stability import gz_curve, summary, build, r25_reserve, BASE, Z_EYE, Z_RING_BRIDLE, MASS_V10

MAXC = dict(BASE)                                  # 4 pods x 0.3 kg (R-31 allowance)
MINC = dict(BASE, n_pods=3, m_pod=0.2)             # core set only, light modules: stability-critical
cases = {
    "A  max config (4 x 0.3 kg pods)": MAXC,
    "B  min config (3 x 0.2 kg pods)": MINC,
    "C  B, canister flooded": dict(MINC, canister_flooded=True),
    "D1 B + 1 kg mooring at keel eye (design)": dict(MINC, mooring_kg=1.0, z_bridle=Z_EYE),
    "D2 B + 1 kg mooring at ring (rejected)": dict(MINC, mooring_kg=1.0, z_bridle=Z_RING_BRIDLE),
    "D3 A + 1 kg mooring at keel eye (deepest draft)": dict(MAXC, mooring_kg=1.0, z_bridle=Z_EYE),
    "E  B, no ballast (reference)": dict(MINC, ballast_kg=0.0),
}
res = {}
fig, ax = plt.subplots(figsize=(9.5, 5.4))
for name, cfg in cases.items():
    r = gz_curve(cfg); s = summary(r)
    res[name] = dict(summary=s, mass_items=r["mass_items"], curve=[(p["deg"], round(p["gz"], 1)) for p in r["curve"]])
    ls = "--" if name.startswith(("D2", "E")) else "-"
    ax.plot([p["deg"] for p in r["curve"]], [p["gz"] for p in r["curve"]], ls, lw=1.8, label=name)
ax.axhline(0, color="k", lw=.8); ax.axvline(90, color="grey", ls=":", lw=1)
ax.set_xlim(0, 180); ax.grid(alpha=.3)
ax.set_xlabel("heel angle φ [deg]"); ax.set_ylabel("GZ [mm]  (+ = rights)")
ax.set_title("SeaSense v1.0 – GZ curves, CAD-derived masses, 2.0 kg ballast (analysis, not verified)")
ax.legend(fontsize=7.5, loc="upper right"); fig.tight_layout(); fig.savefig("gz_curves.png", dpi=150)

for k, v in res.items():
    print(f"{k:48s}", v["summary"])
print("\nGZ table [mm]")
ks = list(res)
print("deg  " + "  ".join(k.split()[0].rjust(4) for k in ks))
for i in range(0, 37, 3):
    print(f"{int(res[ks[0]]['curve'][i][0]):3d}  " + "  ".join(f"{res[k]['curve'][i][1]:4.0f}" for k in ks))

print("\nR-25 reserve buoyancy (one definition: (V*rho - (9 kg + 1 kg)) / 10 kg)")
for fl in (False, True):
    _, W, _ = build(dict(MAXC, canister_flooded=fl))
    print(f"  {'canister flooded' if fl else 'intact          '}: V = {W.sum():5.2f} L -> reserve {r25_reserve(W.sum())*100:4.0f} %"
          f"   (afloat: {W.sum()*1.005:.1f} kg lift vs 10 kg)")

print("\nBallast sensitivity, case B, min GZ 5-175 deg:")
for mb in (1.0, 1.5, 2.0, 2.5):
    print("  ", mb, "kg ->", summary(gz_curve(dict(MINC, ballast_kg=mb)))["min_gz_5_175"], "mm")

print("\nMass table, case A (max config):")
tot = mz = 0
for n, m, z in res[ks[0]]["mass_items"]:
    tot += m; mz += m * z
    print(f"  {n:40s} {m:5.2f} kg  z={z:7.1f}  m*z={m*z:8.1f}")
print(f"  {'TOTAL':40s} {tot:5.2f} kg  zG={mz/tot:7.1f}")
json.dump(res, open("results.json", "w"), indent=1)

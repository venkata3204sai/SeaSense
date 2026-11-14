"""
SeaSense Stage 2 (v1.0) - hydrostatics & righting-arm (GZ) curve, hull Option C + keel cage.
Traceability: R-25 (reserve buoyancy, flooded canister, self-righting), R-31 (mass <= 9 kg after CR-02),
R-01 (temperature at 0.5 +/- 0.1 m), R-26 (mooring attachment point).

Method (ANALYSIS - not verified by test):
  * Each buoyant part is a simple solid (annulus / cylinder) sampled on a 3-D point grid; weights are
    rescaled so every part has its exact analytic volume.
  * For each heel angle phi (rotation about x) the body is rotated, the points are sorted by height and the
    waterline is placed where submerged volume x rho = total mass (free-floating, quasi-static).
  * GZ = y_G' - y_B'  (positive = righting).  Grid noise is about +/- 2 mm on GZ.
  * A mooring pull is modelled as a vertical point weight at the attachment point (valid for a taut,
    vertical line; a 4-leg bridle is approximated by a point on the axis at ring level).
Coordinates: z = 0 at the underside of the ring float, mm / kg / L.
"""
import json
import numpy as np

RHO = 1.005                 # kg/L brackish water (requirements assumption 3)
R31_MAX_KG = 9.0            # R-31 after CR-02
MOORING_MAX_KG = 1.0        # R-25 design mooring weight in water

# ---------------------------------------------------------------- geometry (mm), matches cad v1.0
RING_RI, RING_RO, RING_H = 65.0, 200.0, 100.0
CAN_R, CAN_Z0, CAN_Z1 = 56.0, -130.0, 188.0                    # pipe + caps envelope
CAN_INNER_R, CAN_INNER_Z0, CAN_INNER_Z1 = 51.8, -120.0, 180.0   # floodable volume (pipe ID)
MAST_R, MAST_Z0, MAST_Z1 = 12.5, 190.0, 690.0
LIGHT_R, LIGHT_Z0, LIGHT_Z1 = 35.0, 690.0, 750.0
KEEL_R, KEEL_Z0, KEEL_Z1 = 15.0, -525.0, -130.0                # printed column (head..spacer)
POD_R, POD_L, POD_RING, POD_Z = 20.0, 110.0, 48.0, -400.0      # pods centred 0.45 m below ring bottom
DISC_R, DISC_Z0, DISC_Z1 = 90.0, -535.0, -525.0                # 10 mm A4 disc = ballast + mooring plate
STEEL = 7.95                                                   # kg/L stainless (R-34: no lead)
Z_EYE = -585.0                                                 # M12 DIN 580 eye bolt under the disc
Z_RING_BRIDLE = 0.0                                            # alternative: bridle at ring level


def grid_cyl(r_in, r_out, z0, z1, h, cx=0.0, cy=0.0):
    xs = np.arange(-r_out + h / 2, r_out, h)
    zs = np.arange(z0 + h / 2, z1, h)
    X, Y, Z = np.meshgrid(xs, xs, zs, indexing="ij")
    R = np.hypot(X, Y)
    m = (R <= r_out) & (R >= r_in)
    P = np.stack([X[m] + cx, Y[m] + cy, Z[m]], axis=1)
    v_exact = np.pi * (r_out**2 - r_in**2) * (z1 - z0) * 1e-6
    return P, np.full(len(P), v_exact / len(P))


# Mass items v1.0: (name, kg, z_mm). CAD-derived where marked; others Stage-1 budget (unverified).
MASS_V10 = [
    ("ring trays + lids (CAD v1.0)", 1.25, 50),
    ("ring foam", 0.45, 50),
    ("spokes 70% of solid + 4 bolts + clamps", 0.82, 50),
    ("canister pipe + caps (CAD)", 0.85, 30),
    ("electronics", 0.25, 20),
    ("battery 2x6 Ah LiFePO4", 0.30, -100),
    ("mast, GNSS, LoRa antenna", 0.40, 450),
    ("light + radar reflector", 0.30, 650),
    ("rope handle", 0.03, 120),
    ("keel column printed (CAD v1.0, 70%)", 0.35, -340),
    ("4 x M6 A4 cage rods 0.75 m + nuts", 0.55, -173),
    ("M12 A4 eye bolt + nut", 0.10, -560),
]


def build(cfg):
    parts = [grid_cyl(RING_RI, RING_RO, 0, RING_H, 3.0)]
    P, w = grid_cyl(0, CAN_R, CAN_Z0, CAN_Z1, 2.0)
    if cfg.get("canister_flooded"):
        r = np.hypot(P[:, 0], P[:, 1])
        keep = ~((r < CAN_INNER_R) & (P[:, 2] > CAN_INNER_Z0) & (P[:, 2] < CAN_INNER_Z1))
        v = np.pi * CAN_R**2 * (CAN_Z1 - CAN_Z0) * 1e-6 - np.pi * CAN_INNER_R**2 * (CAN_INNER_Z1 - CAN_INNER_Z0) * 1e-6
        P = P[keep]; w = np.full(len(P), v / len(P))
    parts.append((P, w))
    parts.append(grid_cyl(0, MAST_R, MAST_Z0, MAST_Z1, 2.0))
    parts.append(grid_cyl(0, LIGHT_R, LIGHT_Z0, LIGHT_Z1, 2.5))
    parts.append(grid_cyl(0, KEEL_R, KEEL_Z0, KEEL_Z1, 2.0))
    mass = [(n, cfg.get("mass_overrides", {}).get(n, m), z) for n, m, z in cfg.get("mass_items", MASS_V10)]
    for i in range(cfg["n_pods"]):
        a = np.pi / 4 + np.pi / 2 * i
        parts.append(grid_cyl(0, POD_R, POD_Z - POD_L / 2, POD_Z + POD_L / 2, 2.0,
                              POD_RING * np.cos(a), POD_RING * np.sin(a)))
    if cfg["n_pods"]:
        mass.append((f"{cfg['n_pods']} sensor pods", cfg["n_pods"] * cfg["m_pod"], POD_Z))
    mb = cfg["ballast_kg"]
    if mb > 0:
        t = mb / STEEL * 1e6 / (np.pi * DISC_R**2)
        zc = (DISC_Z0 + DISC_Z1) / 2
        parts.append(grid_cyl(0, DISC_R, zc - t / 2, zc + t / 2, 1.5))
        mass.append(("stainless ballast disc", mb, zc))
    if cfg.get("mooring_kg", 0):
        mass.append(("mooring pull (wt. in water)", cfg["mooring_kg"], cfg["z_bridle"]))
    P = np.concatenate([p for p, _ in parts]); W = np.concatenate([w for _, w in parts])
    return P, W, mass


def gz_curve(cfg, angles=np.arange(0, 181, 5)):
    P, W, mass = build(cfg)
    M = sum(m for _, m, _ in mass)
    zG = sum(m * z for _, m, z in mass) / M
    V_need = M / RHO
    out = []
    for deg in angles:
        a = np.radians(deg); c, s = np.cos(a), np.sin(a)
        y = P[:, 1] * c - P[:, 2] * s
        z = P[:, 1] * s + P[:, 2] * c
        order = np.argsort(z); cw = np.cumsum(W[order])
        k = np.searchsorted(cw, V_need)
        if k >= len(cw):
            raise RuntimeError("sinks")
        sub = order[: k + 1]
        yB = np.sum(y[sub] * W[sub]) / W[sub].sum()
        zB = np.sum(z[sub] * W[sub]) / W[sub].sum()
        out.append(dict(deg=float(deg), gz=float(-zG * s - yB), zWL=float(z[order[k]]), zB=float(zB)))
    return dict(mass_kg=M, zG=zG, V_need=V_need, V_tot=float(W.sum()), mass_items=mass, curve=out)


def r25_reserve(V_buoyant_L):
    """Single R-25 definition: (buoyancy - (R-31 max mass + design mooring)) / (R-31 max + mooring)."""
    load = R31_MAX_KG + MOORING_MAX_KG
    return (V_buoyant_L * RHO - load) / load


def summary(res):
    c = res["curve"]
    gz = np.array([p["gz"] for p in c]); deg = np.array([p["deg"] for p in c])
    band = (deg >= 5) & (deg <= 175)
    neg = deg[(deg > 0) & (deg < 180)][gz[(deg > 0) & (deg < 180)] <= 0]
    g = dict(zip(deg, gz))
    return dict(
        mass=round(res["mass_kg"], 2),
        WL_above_ring_bottom=round(c[0]["zWL"]),
        zG_below_WL=round(c[0]["zWL"] - res["zG"]),
        zB_below_WL=round(c[0]["zWL"] - c[0]["zB"]),
        GM_upright=round(g[5] / np.sin(np.radians(5))),
        GM_inverted=round(-g[175] / np.sin(np.radians(5))),     # > 0 would mean stable upside down
        gz90=round(g[90]), gz_max=round(gz.max()),
        min_gz_5_175=round(float(gz[band].min()), 1),
        stable_inverted=bool(len(neg)),
    )


BASE = dict(n_pods=4, m_pod=0.30, ballast_kg=2.0, mooring_kg=0.0, z_bridle=Z_EYE)

if __name__ == "__main__":
    print(json.dumps(summary(gz_curve(BASE)), indent=1))

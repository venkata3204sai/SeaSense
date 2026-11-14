"""Headless assembly render (matplotlib) -> out/seasense_assembly.png
Usage: python render_assembly.py [waterline_z_mm]
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from seasense_parts import assembly

WL = float(sys.argv[1]) if len(sys.argv) > 1 else 44.0   # waterline above ring bottom (stability case A)

tris, cols = [], []
light = np.array([0.4, -0.6, 0.7]); light /= np.linalg.norm(light)
for child in assembly().children:
    shape = child.obj.val().moved(child.loc)
    v, t = shape.tessellate(1.5, 0.4)
    V = np.array([p.toTuple() for p in v]); T = np.array(t)
    tri = V[T]
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    shade = 0.45 + 0.55 * np.abs(n @ light)
    rgb = np.array(child.color.toTuple()[:3]) if child.color else np.array([.7, .7, .7])
    tris.append(tri); cols.append(np.clip(rgb[None, :] * shade[:, None], 0, 1))
tris = np.concatenate(tris); cols = np.concatenate(cols)

fig = plt.figure(figsize=(13, 8))
for k, (elev, azim, title) in enumerate([(22, -55, "Isometric"), (0, -90, "Elevation")]):
    ax = fig.add_subplot(1, 2, k + 1, projection="3d")
    sel = tris
    c = cols
    if k == 1:   # cut-away: drop the front half (y < 0) so the canister & keel are visible
        keep = tris[:, :, 1].mean(axis=1) > 0
        sel, c = tris[keep], cols[keep]
    ax.add_collection3d(Poly3DCollection(sel, facecolors=c, edgecolors="none", linewidths=0))
    if k == 1:
        xs = np.array([-320, 320])
        ax.plot(xs, [0, 0], [WL, WL], color="tab:blue", lw=1.5)
        ax.text(220, 0, WL + 15, f"waterline ≈ {WL:.0f} mm\n(analysis, case A)", color="tab:blue", fontsize=8)
        ax.plot(xs, [0, 0], [WL - 500, WL - 500], color="tab:blue", lw=1, ls="--")
        ax.text(120, 0, WL - 490, "0.5 m depth (R-01)", color="tab:blue", fontsize=8)
    ax.set_xlim(-330, 330); ax.set_ylim(-330, 330); ax.set_zlim(-600, 780)
    ax.set_box_aspect((660, 660, 1380))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off(); ax.set_title(title + (" (half section)" if k else ""), fontsize=11)
fig.suptitle("SeaSense Option C – Stage 2 v1.0 assembly (cage load path, keel, ballast/mooring disc)", fontsize=12)
fig.tight_layout()
fig.savefig("out/seasense_assembly.png", dpi=140, bbox_inches="tight")
print("saved out/seasense_assembly.png", len(tris), "triangles")

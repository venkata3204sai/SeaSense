"""Parts sheet: each printed part rendered alone -> out/seasense_parts_sheet.png"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from seasense_parts import PRINTED

light = np.array([0.4, -0.6, 0.7]); light /= np.linalg.norm(light)
fig = plt.figure(figsize=(16, 14))
for i, (name, (fn, qty, req)) in enumerate(PRINTED.items()):
    s = fn().val()
    print(name, "valid solid:", s.isValid())
    v, t = s.tessellate(0.5, 0.3)
    V = np.array([p.toTuple() for p in v]); tri = V[np.array(t)]
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0]); n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    shade = 0.4 + 0.6 * np.abs(n @ light)
    ax = fig.add_subplot(4, 4, i + 1, projection="3d")
    ax.add_collection3d(Poly3DCollection(tri, facecolors=np.clip(np.array([1, .8, .1]) * shade[:, None], 0, 1), edgecolors="none"))
    lo, hi = V.min(0), V.max(0); c = (lo + hi) / 2; r = (hi - lo).max() / 2
    ax.set_xlim(c[0]-r, c[0]+r); ax.set_ylim(c[1]-r, c[1]+r); ax.set_zlim(c[2]-r, c[2]+r); ax.set_box_aspect((1, 1, 1))
    ax.view_init(28, -60 if name != "bottom_cap" else 60); ax.set_axis_off()
    if name == "bottom_cap": ax.view_init(-30, -60)
    d = hi - lo
    ax.set_title(f"{name}  ×{qty}\n{d[0]:.0f}×{d[1]:.0f}×{d[2]:.0f} mm · {req}", fontsize=9)
fig.suptitle("SeaSense v1.0 printed parts (all ≤ 240 mm, R-27)", fontsize=12)
fig.tight_layout(); fig.savefig("out/seasense_parts_sheet.png", dpi=130, bbox_inches="tight")

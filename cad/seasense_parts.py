"""
SeaSense - Stage 2 v1.0 parametric CAD (CadQuery 2.x)   baseline: requirements-v1.0 + CR-01, CR-02, CR-03
=============================================================================================================
Load path (v1.0): 4 x M6 A4 "cage" rods at r = 78 mm run from the top-cap lugs, through the top spokes, the
ring joints and the bottom spokes (nuts lock the ring), the keel head, the pod-carrier lip, down to the
stainless ballast disc.  Pipe + both caps + printed keel column form a compression stack clamped between the
top-cap lugs and the disc.  Mooring (M12 eye bolt) and lifting loads go disc <-> rods <-> ring; the bonded
bottom cap only carries stack compression (no peel, no keel moment).

Printed parts (ASA, R-27):                              Non-printed (CR-01/CR-03):
  ring_tray x4, ring_lid x4      R-25 R-27                 110x3.2 PVC-U pipe 300 mm            R-27
  spoke x8 (4 top, 4 bottom)     R-27 R-31 (handle)        4 x M6 A4 rod 750 mm, 4 x M6x130 bolts
  top_cap                        R-14 R-24                 ballast_disc 10 mm A4 (laser cut)    R-25 R-26 R-34
  bottom_cap                     R-15 R-24                 M12 A4 DIN 580 eye bolt              R-26
  keel_head, keel_strut, spacer  R-25 R-01                 25 mm mast tube, light               R-32
  pod_carrier                    R-01 R-15 R-16            4 x M12 A-coded IP68 panel sockets   R-15
  pod_temp / pod_ec / pod_do / pod_turb   R-01..R-04 R-15 R-16 R-19 R-24
Coordinates: z = 0 at the underside of the ring float (mm).  Numbers are design choices unless an R-ID or
datasheet is cited; "TBC" = confirm against the physical part / drawing before printing.
Run:  python seasense_parts.py   -> stl/*.stl, out/seasense_assembly.step|.glb, out/ballast_disc.dxf
"""
import math
from pathlib import Path
import cadquery as cq

# =========================================================================== PARAMETERS
BUILD_ENVELOPE = 240.0      # R-27
CLEAR = 0.3                 # sliding fit per side, tune on test prints

# ---- ring float (Option C baseline) ---------------------------------------- R-25 R-27
RING_OD, RING_ID, RING_H, N_SEG = 400.0, 130.0, 100.0, 4
SEG_WALL = 2.0              # ~4.4 perimeters @0.45 mm (baseline >= 4)
SEG_END_WALL = 3.0
LID_T = 2.0
TONGUE_DEPTH, TONGUE_R, TONGUE_Z = 4.5, (110.0, 155.0), (25.0, 70.0)
GROOVE_PAD = 2.0
FILL_PORT_D, VENT_D = 16.0, 4.0

# ---- cage / joints (v1.0 load path) --------------------------------------- R-25 R-26
CAGE_R = 78.0               # rod circle radius
CAGE_ANGLES = (0, 90, 180, 270)   # on the segment joints
ROD_HOLE = 6.6              # M6 A4-70 rods
JOINT_BOLT_R = 170.0        # one M6 through-bolt per joint, on the joint line
HALF_BOSS_D = 16.0          # boss split across the joint (half in each segment)

# ---- spokes ---------------------------------------------------------------- R-27 R-31
SPOKE_W, SPOKE_T, SPOKE_REACH = 44.0, 12.0, 235.0
EYE_D = 10.5                # top spokes: rope-handle eyes (R-31). NOT a mooring point (R-26 -> keel eye)
PIPE_OD, PIPE_WALL = 110.0, 3.2
SADDLE_T, SADDLE_H, SADDLE_HALF_ANGLE = 8.0, 30.0, 40.0
CLAMP_GROOVE = (14.0, 27.0, 1.5)

# ---- top cap --------------------------------------------------------------- R-14 R-24
TC_BORE = PIPE_OD + 0.4
ORING_GLAND_DEPTH, ORING_GROOVE_W, ORING_Z = 2.8, 4.8, (10.0, 24.0)   # 2 x O-ring 110 x 3.5 EPDM (TBC)
TC_SKIRT, TC_LID, TC_WALL_OUT = 40.0, 8.0, 3.5
MAST_D, SOCKET_H = 25.0, 30.0
GLAND_HOLE, GLAND_R = 16.2, 35.0            # M16 glands (antenna, light) + service connector
LUG_W, LUG_T = 20.0, 12.0                   # lugs carry the stack preload (see strength notes)

# ---- bottom cap ------------------------------------------------------------ R-15 R-24
BC_BOND_GAP, BC_SOCKET, BC_FLOOR, BC_WALL = 0.25, 40.0, 10.0, 4.0
N_PORTS, PORT_R, PORT_ANGLE0 = 4, 30.0, 45.0
PORT_HOLE = 15.5            # M12 A-coded panel socket, PG9 thread (e.g. Amphenol LTW M12A-05PFFP-SF8001)
PORT_PANEL_T = 4.0          # max panel thickness of the socket (TBC on datasheet) -> inside counterbore
PORT_CBORE_D = 26.0         # inside counterbore for the socket nut
PORT_SPOTFACE = (22.0, 0.5) # flat outer seat for the socket O-ring
LEG_R, LEG_D = 48.0, 16.0   # keel-head legs bear on the cap floor here (0/90/180/270 deg)
DIMPLE_DEPTH = 1.0

# ---- keel column (printed, compression only) ------------------------------- R-25 R-01
HEAD_T, HEAD_HUB_R, HEAD_ARM_W, LEG_H = 15.0, 18.0, 18.0, 80.0   # 80 mm: room for straight M12 plugs (R-16)
COL_OD, COL_ID = 30.0, 14.0
SPIGOT_D, SPIGOT_H = 20.0, 6.0
STRUT_L = 110.0
SPACER_L = 65.0
M12_NUT_AF, M12_NUT_H = 19.0, 11.0
HUB_R, CARRIER_L = 20.0, 125.0
LIP_T, STOP_W, STOP_R = 8.0, 16.0, 28.0   # rod-bracing arms + pod stop block under each rail
PIN_D = 4.2                 # A4 ball-lock pin (detent), R-16/R-33
RAIL_ROOT_W, RAIL_TIP_W, RAIL_H = 8.0, 12.0, 5.0
POD_RING = 48.0             # pod axis radius on the carrier
POD_ANGLES = (45, 135, 225, 315)   # between the cage rods

# ---- ballast / mooring plate (non-printed) ------------------------- R-25 R-26 R-34
DISC_D, DISC_T, DISC_CENTER_HOLE = 180.0, 10.0, 13.0   # A4: pi*0.9^2*0.1 dm3 * 7.95 = 2.02 kg - holes

# ---- sensor pods: per sensor, from datasheets ------------------- R-01..R-04 R-15 R-19
POD_L = 110.0               # identical outer length/interface for all pods (R-15, R-19)
POD_WALL = 3.0
BLOCK_W = 24.0
POD_SPECS = {
    # Blue Robotics Celsius (R3): M10x1.5 bulkhead, 10.2 mm hole, AS568-013 face O-ring (datasheet).
    # Probe protrusion / cage diameter: TBC from BR drawing (assumed 25 mm / 14 mm).
    "temp": dict(od=40.0, bottom=8.0, mount="bulkhead", hole=10.2, spotface=18.0, probe_d=14.0, protrude=25.0),
    # Atlas ENV-40-EC-K1.0: 12 x 145.5 mm (datasheet). Potted, O-ring on body. 60 mm exposed.
    "ec": dict(od=40.0, bottom=12.0, mount="potted", probe_d=12.0, oring_cs=1.5, protrude=60.0),
    # Atlas ENV-40-DOX: 16.5 x 105.3 mm (datasheet). Membrane cap outside the pod for service.
    "do": dict(od=40.0, bottom=12.0, mount="potted", probe_d=16.5, oring_cs=2.0, protrude=45.0),
    # DFRobot SEN0189: probe envelope NOT in text datasheet -> 30 x 22 mm assumed (TBC from drawing).
    # Top of probe not waterproof -> fully potted, light-shield skirt with flow slots.
    "turb": dict(od=46.0, bottom=6.0, mount="pocket", pocket=(30.0, 22.0), skirt=30.0, protrude=20.0),
}

# ---- vertical layout ---------------------------------------------------------------------------
PIPE_Z = (-120.0, 180.0)
TC_Z = PIPE_Z[1] - TC_SKIRT                 # top-cap skirt bottom (140)
BC_Z = PIPE_Z[0]                            # pipe end on bottom-cap floor (-120)
HEAD_Z = BC_Z - BC_FLOOR - LEG_H - HEAD_T   # keel-head arm underside (-195)
CARRIER_Z = HEAD_Z - STRUT_L - CARRIER_L    # carrier bottom (-460)
DISC_Z = CARRIER_Z - SPACER_L - DISC_T      # disc underside (-535)


# =========================================================================== HELPERS
def annulus(r_in, r_out, z0, z1):
    wp = cq.Workplane("XY").workplane(offset=z0).circle(r_out)
    if r_in > 0:
        wp = wp.circle(r_in)
    return wp.extrude(z1 - z0)


def cyl(r, z0, z1, x=0.0, y=0.0):
    return cq.Workplane("XY").workplane(offset=z0).center(x, y).circle(r).extrude(z1 - z0)


def box(x0, x1, y0, y1, z0, z1):
    return cq.Workplane("XY").box(x1 - x0, y1 - y0, z1 - z0, centered=False).translate((x0, y0, z0))


def wedge(a0, a1, z0, z1, R=1000.0, n=16):
    pts = [(0.0, 0.0)] + [(R * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
                           R * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    return cq.Workplane("XY").workplane(offset=z0).polyline(pts).close().extrude(z1 - z0)


def polar(r, deg):
    return r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg))


def rotz(wp, deg):
    return wp.rotate((0, 0, 0), (0, 0, 1), deg)


def hexagon(af, z0, z1):
    return cq.Workplane("XY").workplane(offset=z0).polygon(6, af / math.cos(math.pi / 6)).extrude(z1 - z0)


def joint_points():
    """Fastener positions on the two joints of the 0..90 deg segment."""
    return [(CAGE_R, 0.0), (JOINT_BOLT_R, 0.0), (0.0, CAGE_R), (0.0, JOINT_BOLT_R)]


def arms_x(r_hole, width, z0, z1, hub_r, angles=CAGE_ANGLES):
    """Hub + radial arms ending in a rod hole at r_hole (rods pass through, lateral bracing)."""
    s = cyl(hub_r, z0, z1)
    for a in angles:
        arm = box(0, r_hole, -width / 2, width / 2, z0, z1).union(cyl(width / 2, z0, z1, r_hole, 0)) \
            .cut(cyl(ROD_HOLE / 2, z0 - 1, z1 + 1, r_hole, 0))
        s = s.union(rotz(arm, a))
    return s


# =========================================================================== RING
def ring_tray():
    """90 deg open-top tray (foam poured, lid bonded). Half-bosses on both joints for rod + bolt. R-25 R-27"""
    ri, ro, h = RING_ID / 2, RING_OD / 2, RING_H - LID_T
    quad = box(0, ro + 1, 0, ro + 1, -1, h + 1)
    tray = annulus(ri, ro, 0, h).intersect(quad)
    cavity = annulus(ri + SEG_WALL, ro - SEG_WALL, SEG_WALL, h + 1) \
        .intersect(box(SEG_END_WALL, ro, SEG_END_WALL, ro, 0, h + 2))
    tray = tray.cut(cavity)
    for x, y in joint_points():
        tray = tray.union(cyl(HALF_BOSS_D / 2, 0, h, x, y).intersect(quad))
    c = CLEAR
    pad_t = TONGUE_DEPTH + c + GROOVE_PAD
    tray = tray.union(box(TONGUE_R[0] - c - 3, TONGUE_R[1] + c + 3, 0, pad_t, TONGUE_Z[0] - c - 3, TONGUE_Z[1] + c + 3))
    tray = tray.cut(box(TONGUE_R[0] - c, TONGUE_R[1] + c, -1, TONGUE_DEPTH + c, TONGUE_Z[0] - c, TONGUE_Z[1] + c))
    tray = tray.union(box(-TONGUE_DEPTH, 0.5, TONGUE_R[0], TONGUE_R[1], TONGUE_Z[0], TONGUE_Z[1]))
    for x, y in joint_points():
        tray = tray.cut(cyl(ROD_HOLE / 2, -1, h + 1, x, y))
    return tray


def ring_lid():
    ri, ro = RING_ID / 2, RING_OD / 2
    lid = annulus(ri, ro, 0, LID_T).intersect(box(0, ro + 1, 0, ro + 1, -1, LID_T + 1))
    for x, y in joint_points():
        lid = lid.cut(cyl(ROD_HOLE / 2, -1, LID_T + 1, x, y))
    fx, fy = polar((ri + ro) / 2, 45)
    vx, vy = polar((ri + ro) / 2, 70)
    return lid.cut(cyl(FILL_PORT_D / 2, -1, LID_T + 1, fx, fy)).cut(cyl(VENT_D / 2, -1, LID_T + 1, vx, vy))


# =========================================================================== SPOKE
def spoke():
    """Arm along +x over a joint. Cage rod at r=78 and joint bolt at r=170 clamp the ring sandwich."""
    r_in = PIPE_OD / 2 + 0.2
    r_out = r_in + SADDLE_T
    tip_c = SPOKE_REACH - SPOKE_W / 2
    s = box(r_out - 1, tip_c, -SPOKE_W / 2, SPOKE_W / 2, 0, SPOKE_T).union(cyl(SPOKE_W / 2, 0, SPOKE_T, tip_c, 0))
    s = s.union(annulus(r_in, r_out, 0, SADDLE_H).intersect(wedge(-SADDLE_HALF_ANGLE, SADDLE_HALF_ANGLE, -1, SADDLE_H + 1)))
    g0, g1, gd = CLAMP_GROOVE
    s = s.cut(annulus(r_out - gd, r_out + 5, g0, g1))
    for r in (CAGE_R, JOINT_BOLT_R):
        s = s.cut(cyl(ROD_HOLE / 2, -1, SPOKE_T + 1, r, 0))
    return s.cut(cyl(EYE_D / 2, -1, SPOKE_T + 1, tip_c, 0))


# =========================================================================== CAPS
def top_cap():
    """Skirt opens downwards (z = 0 at skirt bottom); pipe end bears on the lid underside."""
    r_groove = PIPE_OD / 2 + ORING_GLAND_DEPTH
    r_out = r_groove + TC_WALL_OUT
    top = TC_SKIRT + TC_LID
    cap = cyl(r_out, 0, top).cut(cyl(TC_BORE / 2, -1, TC_SKIRT))
    for z in ORING_Z:
        cap = cap.cut(annulus(TC_BORE / 2 - 0.1, r_groove, z, z + ORING_GROOVE_W))
    for a in CAGE_ANGLES:
        lug = box(r_out - 3, CAGE_R, -LUG_W / 2, LUG_W / 2, top - LUG_T, top) \
            .union(cyl(LUG_W / 2, top - LUG_T, top, CAGE_R, 0)) \
            .cut(cyl(ROD_HOLE / 2, top - LUG_T - 1, top + 1, CAGE_R, 0))
        cap = cap.union(rotz(lug, a))
    cap = cap.union(cyl(MAST_D / 2 + 5, top, top + SOCKET_H)).cut(cyl(MAST_D / 2 + 0.2, top + 2, top + SOCKET_H + 1))
    for a in (45, 135, 225):
        x, y = polar(GLAND_R, a)
        cap = cap.cut(cyl(GLAND_HOLE / 2, TC_SKIRT - 1, top + 1, x, y))
    return cap


def bottom_cap():
    """Socket opens upwards (z = 0: pipe end on floor). Floor carries only stack compression."""
    r_bore = PIPE_OD / 2 + BC_BOND_GAP
    cap = cyl(r_bore + BC_WALL, -BC_FLOOR, BC_SOCKET).cut(cyl(r_bore, 0, BC_SOCKET + 1))
    for i in range(N_PORTS):
        x, y = polar(PORT_R, PORT_ANGLE0 + 360 / N_PORTS * i)
        cap = cap.cut(cyl(PORT_HOLE / 2, -BC_FLOOR - 1, 1, x, y))
        cap = cap.cut(cyl(PORT_CBORE_D / 2, -BC_FLOOR + PORT_PANEL_T, 1, x, y))          # inside counterbore
        cap = cap.cut(cyl(PORT_SPOTFACE[0] / 2, -BC_FLOOR - 1, -BC_FLOOR + PORT_SPOTFACE[1], x, y))
    for a in CAGE_ANGLES:                                                             # leg locating dimples
        x, y = polar(LEG_R, a)
        cap = cap.cut(cyl(LEG_D / 2 + 0.3, -BC_FLOOR - 1, -BC_FLOOR + DIMPLE_DEPTH, x, y))
    return cap


# =========================================================================== KEEL COLUMN
def _socket_top(part, z_top):
    return part.cut(cyl(SPIGOT_D / 2 + CLEAR, z_top - SPIGOT_H - 0.5, z_top + 1))


def _spigot_bottom(part, z_bot):
    return part.union(annulus(COL_ID / 2, SPIGOT_D / 2, z_bot - SPIGOT_H, z_bot + 0.5))


def keel_head():
    """Legs up to the cap floor (clear of the M12 plugs at 45 deg); arms brace the 4 cage rods."""
    h = arms_x(CAGE_R, HEAD_ARM_W, 0, HEAD_T, HEAD_HUB_R)
    for a in CAGE_ANGLES:
        x, y = polar(LEG_R, a)
        h = h.union(cyl(LEG_D / 2, HEAD_T - 1, HEAD_T + LEG_H, x, y))
    h = _spigot_bottom(h, 0)
    return h.cut(cyl(COL_ID / 2, -SPIGOT_H - 1, HEAD_T - 3))


def keel_strut(length=STRUT_L):
    s = annulus(COL_ID / 2, COL_OD / 2, 0, length)
    return _socket_top(_spigot_bottom(s, 0), length)


def keel_spacer():
    """Bottom of the column; hex pocket holds the M12 nut of the mooring eye bolt (R-26)."""
    s = _socket_top(cyl(COL_OD / 2 + 4, 0, SPACER_L), SPACER_L)
    s = s.cut(hexagon(M12_NUT_AF + 0.4, -1, M12_NUT_H + 1))
    return s.cut(cyl(DISC_CENTER_HOLE / 2, -1, SPACER_L - SPIGOT_H - 2))


def _dovetail(root_w, tip_w, h, x_root, z0, z1):
    pts = [(x_root, -root_w / 2), (x_root + h, -tip_w / 2), (x_root + h, tip_w / 2), (x_root, root_w / 2)]
    return cq.Workplane("XY").workplane(offset=z0).polyline(pts).close().extrude(z1 - z0)


def pod_carrier():
    c = cyl(HUB_R, 0, CARRIER_L).union(arms_x(CAGE_R, HEAD_ARM_W, 0, LIP_T, HUB_R))
    for a in POD_ANGLES:
        c = c.union(rotz(box(HUB_R - 1, STOP_R, -STOP_W / 2, STOP_W / 2, 0, LIP_T), a))
        rail = _dovetail(RAIL_ROOT_W, RAIL_TIP_W, RAIL_H, HUB_R, LIP_T, CARRIER_L) \
            .union(box(HUB_R - 1.0, HUB_R + 0.01, -RAIL_ROOT_W / 2, RAIL_ROOT_W / 2, LIP_T, CARRIER_L))
        rail = rail.cut(cq.Workplane("XZ").center(HUB_R + RAIL_H / 2, CARRIER_L - 5).circle(PIN_D / 2).extrude(20, both=True))
        c = c.union(rotz(rail, a))
    c = _spigot_bottom(c, 0)
    c = _socket_top(c, CARRIER_L)
    return c.cut(cyl(COL_ID / 2, -SPIGOT_H - 1, CARRIER_L - SPIGOT_H - 1))


# =========================================================================== PODS
def sensor_pod(kind):
    """Pod axis at origin, keel axis at x = -POD_RING. Open top: pot electronics + cable, rest may flood."""
    sp = POD_SPECS[kind]
    r = sp["od"] / 2
    x_face = -(POD_RING - HUB_R - CLEAR)
    pod = cyl(r, 0, POD_L).union(box(x_face, -(r - 4), -BLOCK_W / 2, BLOCK_W / 2, 0, POD_L))
    pod = pod.cut(cyl(r - POD_WALL, sp["bottom"], POD_L + 1))
    c = CLEAR
    pod = pod.cut(_dovetail(RAIL_ROOT_W + 2 * c, RAIL_TIP_W + 2 * c, RAIL_H + c, x_face - 0.01, -1, POD_L + 1))
    b = sp["bottom"]
    if sp["mount"] == "bulkhead":                       # Celsius: threaded bulkhead + face O-ring
        pod = pod.cut(cyl(sp["hole"] / 2, -1, b + 1)).cut(cyl(sp["spotface"] / 2, -1, 0.5))
    elif sp["mount"] == "potted":                       # Atlas probes: bore + internal O-ring groove
        d = sp["probe_d"]
        pod = pod.cut(cyl(d / 2 + 0.2, -1, b + 1))
        gd = 0.8 * sp["oring_cs"]
        pod = pod.cut(cyl(d / 2 + gd, b / 2 - 0.7 * sp["oring_cs"], b / 2 + 0.7 * sp["oring_cs"]))
    elif sp["mount"] == "pocket":                       # turbidity: rectangular opening + light-shield skirt
        w, dd = sp["pocket"]
        pod = pod.cut(box(-w / 2, w / 2, -dd / 2, dd / 2, -1, b + 1))
        skirt = annulus(r - POD_WALL, r, -sp["skirt"], 0.5).intersect(wedge(-110, 110, -sp["skirt"] - 1, 1))
        for a in (0, 180):                              # flow slots, oriented away from the hub
            skirt = skirt.cut(rotz(box(r - 6, r + 1, -6, 6, -sp["skirt"] + 6, -6), a + 90))
        pod = pod.union(skirt)
    return pod


def probe_visual(kind):
    sp = POD_SPECS[kind]
    if kind == "turb":
        w, dd = sp["pocket"]
        return box(-w / 2 + 1, w / 2 - 1, -dd / 2 + 1, dd / 2 - 1, -sp["protrude"], 0)
    return cyl(sp["probe_d"] / 2, -sp["protrude"], 0)


# =========================================================================== NON-PRINTED
def pipe():
    return annulus(PIPE_OD / 2 - PIPE_WALL, PIPE_OD / 2, *PIPE_Z)


def ballast_disc():
    d = cyl(DISC_D / 2, 0, DISC_T).cut(cyl(DISC_CENTER_HOLE / 2, -1, DISC_T + 1))
    for a in CAGE_ANGLES:
        x, y = polar(CAGE_R, a)
        d = d.cut(cyl(ROD_HOLE / 2, -1, DISC_T + 1, x, y))
    return d


PRINTED = {   # name: (builder, qty, requirement IDs)
    "ring_tray": (ring_tray, 4, "R-25 R-27"),
    "ring_lid": (ring_lid, 4, "R-25 R-27"),
    "spoke": (spoke, 8, "R-27 R-31"),
    "top_cap": (top_cap, 1, "R-14 R-24"),
    "bottom_cap": (bottom_cap, 1, "R-15 R-24"),
    "keel_head": (keel_head, 1, "R-25"),
    "keel_strut": (keel_strut, 1, "R-25"),
    "keel_spacer": (keel_spacer, 1, "R-25 R-26"),
    "pod_carrier": (pod_carrier, 1, "R-01 R-15 R-16"),
    "pod_temp": (lambda: sensor_pod("temp"), 1, "R-01 R-15 R-19 R-24"),
    "pod_ec": (lambda: sensor_pod("ec"), 1, "R-02 R-15 R-19 R-24"),
    "pod_do": (lambda: sensor_pod("do"), 1, "R-03 R-15 R-19 R-24"),
    "pod_turb": (lambda: sensor_pod("turb"), 1, "R-04 R-15 R-19 R-24"),
}


# =========================================================================== ASSEMBLY
def assembly():
    A = cq.Assembly(name="SeaSense_v1_0")
    yellow, grey, white = cq.Color(1.0, 0.82, 0.0), cq.Color(0.55, 0.55, 0.58), cq.Color(0.92, 0.92, 0.92)
    dark, steel, blue = cq.Color(0.2, 0.2, 0.22), cq.Color(0.7, 0.72, 0.75), cq.Color(0.2, 0.45, 0.8)
    L = lambda x=0, y=0, z=0: cq.Location(cq.Vector(x, y, z))
    R = lambda a: cq.Location(cq.Vector(0, 0, 0), cq.Vector(0, 0, 1), a)
    tray, lid, sp = ring_tray(), ring_lid(), spoke()
    for i in range(N_SEG):
        a = 360 / N_SEG * i
        A.add(tray, name=f"ring_tray_{i}", color=yellow, loc=R(a))
        A.add(lid, name=f"ring_lid_{i}", color=yellow, loc=L(z=RING_H - LID_T) * R(a))
        A.add(sp, name=f"spoke_top_{i}", color=dark, loc=L(z=RING_H) * R(a))
        A.add(sp.mirror("XY"), name=f"spoke_bot_{i}", color=dark, loc=R(a))
    A.add(pipe(), name="pipe_110", color=grey)
    A.add(top_cap(), name="top_cap", color=white, loc=L(z=TC_Z))
    A.add(bottom_cap(), name="bottom_cap", color=white, loc=L(z=BC_Z))
    for i in range(N_PORTS):                                       # mated M12 plugs (envelope, TBC)
        x, y = polar(PORT_R, PORT_ANGLE0 + 90 * i)
        A.add(cyl(10, BC_Z - BC_FLOOR - 50, BC_Z - BC_FLOOR, x, y), name=f"m12_plug_{i}", color=dark)
    A.add(keel_head(), name="keel_head", color=white, loc=L(z=HEAD_Z))
    A.add(keel_strut(), name="keel_strut", color=white, loc=L(z=HEAD_Z - STRUT_L))
    A.add(pod_carrier(), name="pod_carrier", color=white, loc=L(z=CARRIER_Z))
    for kind, a in zip(("temp", "ec", "do", "turb"), POD_ANGLES):
        loc = R(a) * L(POD_RING, 0, CARRIER_Z + LIP_T)
        A.add(sensor_pod(kind), name=f"pod_{kind}", color=blue, loc=loc)
        A.add(probe_visual(kind), name=f"probe_{kind}", color=dark, loc=loc)
    A.add(keel_spacer(), name="keel_spacer", color=white, loc=L(z=DISC_Z + DISC_T))
    A.add(ballast_disc(), name="ballast_disc", color=steel, loc=L(z=DISC_Z))
    A.add(cyl(6, DISC_Z - 50, DISC_Z), name="eye_bolt_M12", color=steel)
    ztop = TC_Z + TC_SKIRT + TC_LID
    for a in CAGE_ANGLES:
        x, y = polar(CAGE_R, a)
        A.add(cyl(3.0, DISC_Z - 8, ztop + 8, x, y), name=f"cage_rod_{a}", color=steel)
    A.add(cyl(MAST_D / 2, ztop + 2, ztop + 502), name="mast", color=grey)
    A.add(cyl(35, ztop + 502, ztop + 562), name="light", color=yellow)
    return A


def check_and_export(out_dir="."):
    out = Path(out_dir)
    (out / "stl").mkdir(parents=True, exist_ok=True)
    (out / "out").mkdir(parents=True, exist_ok=True)
    for f in (out / "stl").glob("*.stl"):
        f.unlink()
    rows = []
    for name, (fn, qty, req) in PRINTED.items():
        part = fn()
        s = part.val()
        bb = s.BoundingBox()
        dims = (bb.xlen, bb.ylen, bb.zlen)
        cq.exporters.export(part, str(out / "stl" / f"{name}.stl"), tolerance=0.05, angularTolerance=0.1)
        rows.append((name, qty, req, dims, all(d <= BUILD_ENVELOPE for d in dims), s.Volume() / 1000, s.isValid()))
    print(f"{'part':12s} qty  {'bbox mm':22s} R-27 valid  cm3   g(ASA 1.07, solid)  reqs")
    for n, q, r, d, ok, v, val in rows:
        print(f"{n:12s} {q:2d}  {d[0]:6.1f}x{d[1]:6.1f}x{d[2]:6.1f}  {'OK ' if ok else 'NO!'}  {val!s:5s} {v:6.1f}  {v*1.07:6.0f}   {r}")
    disc = ballast_disc()
    print(f"ballast_disc  1  A4 {DISC_D:.0f}x{DISC_T:.0f} mm, {disc.val().Volume()/1e6*7.95:.2f} kg")
    cq.exporters.export(disc.section(DISC_T / 2), str(out / "out" / "ballast_disc.dxf"))
    A = assembly()
    A.export(str(out / "out" / "seasense_assembly.step"))
    A.export(str(out / "out" / "seasense_assembly.glb"))
    return rows


if __name__ == "__main__":
    print("layout z [mm]: head", HEAD_Z, "carrier", CARRIER_Z, "disc", DISC_Z)
    check_and_export(Path(__file__).parent)

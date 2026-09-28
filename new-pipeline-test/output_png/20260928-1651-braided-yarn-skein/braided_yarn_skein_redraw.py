"""braided-yarn-skein (redraw of the new-pipeline traced PNG).

Subject: an upright three-strand yarn plait with a loose tail.
Plan on VRECT_M (centerline box (10,4)-(38,44)); body axis x=20:
- body: one closed contour of staggered r5 lobes, the way a plait's strands
  alternate sides. Left notches (15,9/19/29), right notches 5 lower at
  (25,14/24/34). The left lobes own x=10; the top dome (20,9) r5 owns y=4.
  The bottom is a two-cubic cup with its apex at (20,41), tangent-horizontal
  there, sweeping straight up into the lowest left notch.
- strands: three parallel diagonals notch to notch (10 apart, 8.9 on
  centerlines), each sharing its end nodes with the body (connections).
- tail: one S cubic from the bottom apex that trails right and owns x=38 and
  y=44, so the plait itself can stay slim (the trace is 1:3); a 28-wide body
  read as a fat coil at 48 px.
Metric issues fixed: all seven clearance errors (e0..e5 strands 1.8-7.9
apart) -- the trace's doubled S-curves are rebuilt as single parallel strands
>= 8.9 apart; the redrawn tail root sits 8+ from the lowest strand.
keyshape-short-axis (x filled 47%) -- the tail reaches x=38, the lobes x=10.
stroke-width (2.65 -> 4) -- rebuilt at stroke 4. Holes: the six sub-2.5 slivers
are gone; four faces remain and pass the build gate's hole check, but by the
metrics script's stricter stroke-4 raster the two bands measure 5.46 and the
top/bottom caps 3.2/4.3 (need 6): a slim plait cannot give 10-wide centerline
faces inside a 20-wide body without losing its levels.
No useful Lucide match (no braid/yarn icon); construction is lobe arcs + slashes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5ab9f3b5-03e7-4655-9d6a-e84a5583b790"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1651-braided-yarn-skein/"
    "braided-yarn-skein_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 20                   # plait axis; the tail owns the right edge
NL, NR = 15, 25             # notch columns; r5 lobes bulge to x=10 / x=30
LOBE_R = 5
LEFT_Y = (9, 19, 29)        # left notches, one lobe (10) apart
DROP = 5                    # right notches sit half a lobe lower (stagger)
BOTTOM = (AXIS, 41)         # bottom apex and tail root
TAIL = (
    ((20.0, 43.0), (23.0, 44.0), (27.0, 43.0)),
    ((31.0, 42.0), (36.0, 41.0), (38, 44)),
)


class BraidedYarnSkeinRedraw(Solo48):
    icon_id = "braided-yarn-skein-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crafts"
    aliases = ("yarn braid", "plaited yarn", "braided skein", "wool plait")
    keywords = ("yarn", "skein", "braid", "plait", "wool", "knitting", "craft")

    def build(self) -> None:
        ls = [(NL, y) for y in LEFT_Y]
        rs = [(NR, y + DROP) for y in LEFT_Y]
        top_r = (NR, LEFT_Y[0])                     # dome end above R1
        # Body clockwise from the first left notch; every arc bulges outward.
        self.add_arc("dome-t", ls[0], top_r, radius_x=LOBE_R)
        self.add_line("wall-r", top_r, rs[0])
        self.add_arc("lobe-r1", rs[0], rs[1], radius_x=LOBE_R)
        self.add_arc("lobe-r2", rs[1], rs[2], radius_x=LOBE_R)
        # The bottom is deeper than the top dome (apex BOTTOM, not a mirrored
        # r5 dome): it keeps the tail root 8 clear of the lowest strand. It
        # sweeps straight up into L3, so that strand shares a node with it.
        bx, by = BOTTOM
        self.add_bezier("dome-b1", rs[2], ((NR, by - 3), (bx + 2.8, by), BOTTOM))
        self.add_bezier("dome-b2", BOTTOM, ((bx - 2.8, by), (NL, by - 4), ls[2]))
        self.add_arc("lobe-l2", ls[2], ls[1], radius_x=LOBE_R)
        self.add_arc("lobe-l1", ls[1], ls[0], radius_x=LOBE_R)
        self.add_contour(
            "body", "dome-t", "wall-r", "lobe-r1", "lobe-r2", "dome-b1",
            "dome-b2", "lobe-l2", "lobe-l1", closed=True,
        )
        # Plait crossings: parallel diagonals notch to notch.
        for i, (l, r) in enumerate(zip(ls, rs), 1):
            self.add_line(f"strand-{i}", l, r)
            self.relate("connect", f"strand-{i}", "body")

        self.add_bezier("tail", BOTTOM, *TAIL)
        self.relate("connect", "tail", "body")

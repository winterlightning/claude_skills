"""clustered-berry-with-branching-stem-batch-051 (redraw of the new-pipeline traced SVG).

Plan: three equal round berries in a triangle mirrored about x=24 -- two
upper berries left and right, one lower berry at the centre -- hung from one
stem that forks into three stalks, on CIRCLE (centerline radius 20).
- berries: circles of radius R=5 (centerline), so each hole is 6 wide.
  Upper centres (24-D, Y_UP) and (24+D, Y_UP) with D=15, Y_UP=24; their
  outer extremes (4,24)/(44,24) sit on the keyshape circle. Lower centre
  (24, Y_LOW) with Y_LOW=36 keeps the cluster compact: 9.2 between the
  lower and each upper berry on centerlines.
- stem: a line from the top (24,4) (on the keyshape circle) down to the
  fork (24, FORK_Y), continuing straight down to the lower berry's top
  (24, 31). It runs 10 from both upper berries.
- stalks: two mirrored cubics leave the fork at a wide angle and arch over
  to the top of each upper berry, arriving vertically, like the trace.

Keyshape: the metrics suggest SQUARE (x fills 86%). A SQUARE (36 wide on
centerlines) cannot hold two upper berries 9 from the middle stem with a
hole of 6 (needs 2*(R+9+R) = 38 at R=5); CIRCLE gives 40 across the
middle, and its radial fit lets the stem top and berry sides share the rim.

Metric issues fixed:
- stroke-width (info): drawn at stroke 4 and every gap sized for it.
- keyshape-short-axis (warn): CIRCLE is reached at (4,24), (44,24), (24,4).
- clearance e0/e1, e0/e2 (lower vs upper berries, 2.4-2.5): now 9.2.
- clearance e1/e2 (upper berries, 7.4): now 20 apart.
- clearance e1/e4, e2/e4 (stem vs upper berries, 3.7): now 10.
- clearance e3/e4 (stalks vs stem, 6.25) and narrow-join (28.5 deg): the
  stalks now leave the fork well away from the stem.
- hole x2 (3.1 wide, between stalks and stem): the stalks no longer run
  back along the stem, so those slivers are gone; the berry holes are 6.

Lucide: no berry-cluster match (lucide "cherry" has two berries on
converging stalks); the construction follows the trace.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ac0aabf7-0c09-4997-9ab6-af64655e476d"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1916-clustered-berry-with-branching-stem-batch-051/"
    "clustered-berry-with-branching-stem-batch-051_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
R = 5                 # berry radius (centerline)
D = 15                # upper berries sit AXIS +- D
Y_UP, Y_LOW = 24, 36  # berry centre rows
STEM_TOP = (AXIS, 4)
FORK = (AXIS, 10)
# Right stalk: fork -> top of the right berry, arriving vertically.
STALK = ((26, 15), (31, 14), (34, 15.5)), ((37, 17), (AXIS + D, 17), (AXIS + D, Y_UP - R))


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class ClusteredBerryWithBranchingStemBatch051Redraw(Solo48):
    icon_id = "clustered-berry-with-branching-stem-batch-051-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("berry cluster", "berries")
    keywords = ("berry", "berries", "cluster", "stem", "fruit", "food", "currant")

    def _berry(self, name, cx, cy):
        self.add_arc(f"{name}-top", (cx - R, cy), (cx + R, cy), radius_x=R)
        self.add_arc(f"{name}-bottom", (cx + R, cy), (cx - R, cy), radius_x=R)
        self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)

    def build(self) -> None:
        self._berry("berry-left", AXIS - D, Y_UP)
        self._berry("berry-right", AXIS + D, Y_UP)
        self._berry("berry-low", AXIS, Y_LOW)

        self.add_line("stem-top", STEM_TOP, FORK)
        self.add_line("stem-low", FORK, (AXIS, Y_LOW - R))
        self.add_contour("stem", "stem-top", "stem-low")
        self.add_bezier("stalk-right", FORK, *STALK)
        self.add_bezier("stalk-left", FORK, *(tuple(map(mirror, s)) for s in STALK))

        self.relate("connect", "stem", "berry-low")
        self.relate("connect", "stalk-right", "stem")
        self.relate("connect", "stalk-left", "stem")
        self.relate("connect", "stalk-right", "berry-right")
        self.relate("connect", "stalk-left", "berry-left")

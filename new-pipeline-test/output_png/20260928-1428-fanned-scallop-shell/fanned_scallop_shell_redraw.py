"""fanned-scallop-shell (redraw of the new-pipeline traced SVG).

Plan: wide scallop on HRECT_L (centerline box (4,8)-(44,40)), mirrored about x=24.
- rim: two r=5 crown lobes on cusps y=13 reach y=8; each wing is one smooth
  cubic run from its crown cusp out to a vertical tangent on x=4/x=44 and
  tapering down to the hinge; an r=5 hinge bump between (19,35)/(29,35)
  reaches y=40, so the four extremes sit exactly on the keyshape.
- ribs: three straight ribs from one fan node (24,28) to the three rim cusps,
  so every rib ends on the rim; the node sits 8.6 from the hinge corners.
Dropped from the trace: two of the five rim lobes (the shoulder lobes), and the
five free-floating ribs, which at 48 px sat 2-4 units from each other and the
walls (metrics clearance errors). Converging on a shared node keeps the fan
read and clears internal spacing. No useful Lucide match (Lucide `shell` is a
spiral whelk, not a scallop).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1428-fanned-scallop-shell/"
    "fanned-scallop-shell_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
CUSP_Y = 13                 # crown cusps; r=5 semicircle lobes reach y=8
CUSPS = ((14, CUSP_Y), (AXIS, CUSP_Y), (34, CUSP_Y))
LOBE_R = 5
HINGE = ((19, 35), (29, 35))  # hinge bump corners; r=5 bump reaches y=40
HINGE_R = 5
FAN = (AXIS, 28)            # ribs radiate from here, clear of the hinge
# Left wing: hinge corner -> widest point (4, WING_Y) -> side cusp, one smooth
# run with a vertical tangent at x=4.
WING_Y = 19
WING_LOW = ((13, 32), (4, 27), (4, WING_Y))
WING_HIGH = ((4, 14), (9, 10), CUSPS[0])


def mx(p):
    return (2 * AXIS - p[0], p[1])


class FannedScallopShellRedraw(Solo48):
    icon_id = "fanned-scallop-shell-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/sea-life"
    aliases = ("scallop shell", "seashell", "scallop", "clam shell")
    keywords = ("shell", "scallop", "seashell", "beach", "ocean", "sea", "mollusc", "seafood")

    def build(self) -> None:
        c1, c2, c3 = CUSPS
        hl, hr = HINGE
        # Rim clockwise from the left hinge corner.
        self.add_bezier("wing-l", hl, WING_LOW, WING_HIGH)
        self.add_arc("crown-l", c1, c2, radius_x=LOBE_R)
        self.add_arc("crown-r", c2, c3, radius_x=LOBE_R)
        self.add_bezier(
            "wing-r", c3,
            (mx(WING_HIGH[1]), mx(WING_HIGH[0]), mx(WING_LOW[2])),
            (mx(WING_LOW[1]), mx(WING_LOW[0]), hr),
        )
        self.add_arc("hinge", hr, hl, radius_x=HINGE_R)
        self.add_contour("rim", "wing-l", "crown-l", "crown-r", "wing-r", "hinge", closed=True)

        # Ribs fan from one node toward the hinge; each tip lands on a rim cusp.
        for name, cusp in (("rib-l", c1), ("rib-c", c2), ("rib-r", c3)):
            self.add_line(name, FAN, cusp)
            self.relate("connect", name, "rim")

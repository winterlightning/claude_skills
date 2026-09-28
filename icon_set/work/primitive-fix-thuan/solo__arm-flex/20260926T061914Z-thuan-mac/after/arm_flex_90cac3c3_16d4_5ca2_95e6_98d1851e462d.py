"""Arm flex: a flexed arm seen from the side - upper arm rising from the bottom, the
forearm bent up to a clenched fist at the top, and a bulging biceps.

Symbol plan: one open outline, read from the right end of the base. The base runs
along the bottom edge to a radius-4 corner, the outer arm edge climbs almost
vertically, a tangent shoulder cubic turns into the straight upper forearm, and
the fist is a radius-5 half disc on the right (two quarter arcs) ending at the
wrist. The inner forearm drops from the wrist to the biceps. The biceps is a
pronounced rounded arch (two tangent cubics, crest y=24), which falls into a deep
V dip and rises again in an upward curve to the right edge, where the arm leaves
the frame.
Deliberate asymmetry: a side view of one arm.
Revision (reviewer: "Raise the biceps into a pronounced rounded arch, followed by a
deep dip and an upward curve on the right"): the flat biceps line is replaced.
Human reference: icon_set/references/human_ref proportions for arm and fist.
Lucide construction: 'biceps-flexed' - arm with rounded biceps arch and dip.
Keyshape SQUARE: centerline x 6 (outer edge corner) .. 42 (base and curve ends),
y 6 (fist) .. 42 (base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "90cac3c3-16d4-5ca2-95e6-98d1851e462d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__arm-flex/20260926T061914Z-thuan-mac/reference/arm flex_90cac3c3-16d4-5ca2-95e6-98d1851e462d.svg"
AUTHOR = "claude-opus-5-5"


class ArmFlex(Solo48):
    icon_id = "arm-flex"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/body"
    aliases = ("flexed-biceps", "muscle")
    keywords = ("arm", "flex", "biceps", "muscle", "strength", "strong", "fitness", "gym")

    def build(self) -> None:
        self.add_bezier("rise", (42, 27), ((39, 27.5), (37, 29), (35, 33)))
        self.add_bezier("biceps", (35, 33),
                        ((33, 27), (30, 24), (26, 24)),
                        ((22, 24), (18, 27), (18, 34)))
        self.add_line("inner-forearm", (18, 34), (17, 17))
        self.add_line("wrist", (17, 17), (22, 16))
        self.add_arc("fist-lower", (22, 16), (27, 11), radius_x=5, sweep=False)
        self.add_arc("fist-upper", (27, 11), (22, 6), radius_x=5, sweep=False)
        self.add_line("upper-forearm", (22, 6), (11, 12))
        self.add_bezier("shoulder", (11, 12), ((9, 13.1), (8, 14.5), (8, 17)))
        self.add_line("outer-edge", (8, 17), (6, 38))
        self.add_arc("elbow-corner", (6, 38), (10, 42), radius_x=4, sweep=False)
        self.add_line("base", (10, 42), (42, 42))
        self.add_contour("arm", "rise", "biceps", "inner-forearm", "wrist", "fist-lower",
                         "fist-upper", "upper-forearm", "shoulder", "outer-edge",
                         "elbow-corner", "base")

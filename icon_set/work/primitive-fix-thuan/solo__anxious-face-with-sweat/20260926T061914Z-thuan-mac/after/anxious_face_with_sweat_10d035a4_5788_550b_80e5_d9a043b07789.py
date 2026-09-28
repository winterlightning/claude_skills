"""Anxious face with sweat: a frowning face with two dot eyes and a sweat drop at its
upper right, where the face outline opens.

Symbol plan: the face is a radius-20 circle about the canvas centre, drawn from the
top counterclockwise round to the right point, leaving the upper-right quadrant
open for the drop. The drop is a teardrop (two straight sides meeting at a point,
closed by a radius-4 lower arc) whose tip touches radius 20. The features share
one vertical axis x=24: two dot eyes at x = 24 +/- 5 and a shallow frown (rx 6, ry
1) centred under them.
Revision (reviewer: "align two eyes center with the mouth"): the eyes sat at x 16
and 26 (centre 21) over a mouth centred at 24; they are now centred at 24.
Lucide construction: 'frown' - circle face, dot eyes, frown arc.
Keyshape CIRCLE: face radius 20; the drop tip reaches radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "10d035a4-5788-550b-80e5-d9a043b07789"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__anxious-face-with-sweat/20260926T061914Z-thuan-mac/reference/in trouble_10d035a4-5788-550b-80e5-d9a043b07789.svg"
AUTHOR = "claude-opus-5-5"


class AnxiousFaceWithSweat(Solo48):
    icon_id = "anxious-face-with-sweat"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ("in-trouble", "nervous-face")
    keywords = ("anxious", "sweat", "worried", "nervous", "face", "emoji", "trouble")

    def build(self) -> None:
        axis, eye_dx, eye_y = 24, 5, 25
        self.add_arc("head-upper-left", (24, 4), (4, 24), radius_x=20, sweep=False)
        self.add_arc("head-lower", (4, 24), (44, 24), radius_x=20, sweep=False)
        self.add_contour("head", "head-upper-left", "head-lower")
        self.add_line("drop-left", (36, 8), (32, 15))
        self.add_arc("drop-bottom", (32, 15), (40, 15), radius_x=4, sweep=False)
        self.add_line("drop-right", (40, 15), (36, 8))
        self.add_contour("sweat", "drop-left", "drop-bottom", "drop-right", closed=True)
        self.add_dot("eye-left", (axis - eye_dx, eye_y))
        self.add_dot("eye-right", (axis + eye_dx, eye_y))
        self.add_arc("frown", (axis - 6, 34), (axis + 6, 34), radius_x=6, radius_y=1)

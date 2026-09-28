"""Bat: a flying bat seen from the front, wings spread, with two pointed ears and a
scalloped lower wing edge meeting at the body's tail point.

Symbol plan: one closed outline mirrored about x=24. The ears are a straight M on
top; each shoulder is a radius-8 quarter arc into the tall outer wing edge (an
rx 6 / ry 22 arc down to the wing tip). The lower edge of each wing is two gentle
radius-10 circular scallops, wing tip -> cusp (14,33) -> tail point (24,40),
both bowing upward, so the edge reads as smooth shallow curves meeting in points.
Revision (reviewer: "Make the lower edges of the wings curve more smoothly"): the
bulging elliptical scallops (ry 6-7) are replaced by shallow circular ones.
Lucide construction: no bat; 'bird' style open wing curves informed the scallops.
Keyshape HRECT_L: centerline x 4..44 (wing tips), y 8 (ears) .. 40 (tail point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d82ffd85-eb28-548b-b938-7a80b6c3090b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bat/20260926T061914Z-thuan-mac/reference/bat_d82ffd85-eb28-548b-b938-7a80b6c3090b.svg"
AUTHOR = "claude-opus-5-5"

SCALLOP_R = 10


class Bat(Solo48):
    icon_id = "bat"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("flying-bat",)
    keywords = ("bat", "wings", "flying", "halloween", "night", "animal", "nocturnal", "vampire")

    def build(self) -> None:
        self.add_line("ears-1", (18, 19), (17, 8))
        self.add_line("ears-2", (17, 8), (24, 12))
        self.add_line("ears-3", (24, 12), (31, 8))
        self.add_line("ears-4", (31, 8), (30, 19))
        self.add_arc("right-shoulder", (30, 19), (38, 11), radius_x=8, sweep=False)
        self.add_arc("right-wing", (38, 11), (44, 33), radius_x=6, radius_y=22, sweep=True)
        self.add_arc("right-scallop", (44, 33), (34, 33), radius_x=SCALLOP_R, sweep=False)
        self.add_arc("right-base", (34, 33), (24, 40), radius_x=SCALLOP_R, sweep=False)
        self.add_arc("left-base", (24, 40), (14, 33), radius_x=SCALLOP_R, sweep=False)
        self.add_arc("left-scallop", (14, 33), (4, 33), radius_x=SCALLOP_R, sweep=False)
        self.add_arc("left-wing", (4, 33), (10, 11), radius_x=6, radius_y=22, sweep=True)
        self.add_arc("left-shoulder", (10, 11), (18, 19), radius_x=8, sweep=False)
        self.add_contour("bat-outline", "ears-1", "ears-2", "ears-3", "ears-4", "right-shoulder",
                         "right-wing", "right-scallop", "right-base", "left-base", "left-scallop",
                         "left-wing", "left-shoulder", closed=True)

"""Grinning face with tongue out: two closed happy eyes (upward arcs) above
a wide smile from which a rounded tongue hangs, slightly right of centre.

Symbol plan: eyes are one radius-4 arc definition instanced at x = 13 and
35. The smile is one run - curve, straight lip, curve - mirrored about
x = 24. The tongue is a U (two sides and a radius-5 bottom) standing on two
lip nodes, so the lip closes it into a tongue shape. The reference's face
circle is omitted: inside a radius-20 rim the tongue could only be an
undersized hole or an open U that reads as a wavy mouth (attempts/ keeps
that ringed attempt).
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: laugh / smile (arc eyes, smile curve) - tongue added
as a U on the lip.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a2b16bc0-fda9-42be-8b90-0bef7d9dc58b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__happy-face-with-sideways-tongue/20260925T092530Z-thuan-mac/reference/face grin tongue_a2b16bc0-fda9-42be-8b90-0bef7d9dc58b.svg"
AUTHOR = "claude-opus-5-5"


class HappyFaceWithTongue(Solo48):
    icon_id = "happy-face-with-sideways-tongue"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emoji"
    aliases = ("face with tongue", "grin tongue", "playful face")
    keywords = ("face", "tongue", "grin", "playful", "silly", "emoji")

    def build(self) -> None:
        for index, cx in enumerate((13, 35), 1):
            self.add_arc(f"eye-{index}", (cx - 4, 10), (cx + 4, 10), radius_x=4)
        lip_y, tongue_left, tongue_right = 29, 20, 30
        self.add_bezier("smile-1", (6, 20), ((8, 25), (13, lip_y), (18, lip_y)))
        self.add_line("smile-2", (18, lip_y), (tongue_left, lip_y))
        self.add_line("smile-3", (tongue_left, lip_y), (tongue_right, lip_y))
        self.add_bezier("smile-4", (tongue_right, lip_y), ((35, lip_y), (40, 25), (42, 20)))
        self.add_contour("smile", "smile-1", "smile-2", "smile-3", "smile-4")
        self.add_line("tongue-1", (tongue_left, lip_y), (tongue_left, 37))
        self.add_arc("tongue-2", (tongue_left, 37), (tongue_right, 37), radius_x=5, sweep=False)
        self.add_line("tongue-3", (tongue_right, 37), (tongue_right, lip_y))
        self.add_contour("tongue", "tongue-1", "tongue-2", "tongue-3")
        self.relate("connect", "smile", "tongue")

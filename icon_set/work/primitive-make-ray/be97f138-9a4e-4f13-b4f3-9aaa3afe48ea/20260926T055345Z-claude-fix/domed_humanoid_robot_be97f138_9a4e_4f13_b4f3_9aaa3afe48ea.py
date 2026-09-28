"""A friendly humanoid robot: a domed head on a boxy body, arms curving down from the
shoulders and two straight legs with feet.

Symbol plan: symmetric about x = 24 (m(x) = 48 - x). The head is a dome - an r9
semicircle about (24, 15) whose sides flare slightly down to the body's top corners
(14, 24) and (34, 24) - with a single round eye (dot) at its centre, 9 from the dome and
the body top. The body is a closed rectangle x 14..34, y 24..34. Each arm leaves a
shoulder corner on an r8 quarter arc out to x 6 and drops straight to y 38 (round cap for
the hand), 8 from the body side. The legs drop from the body bottom at x 19 and 29 to
y 42 and turn outward into feet. A first version with a narrow dome and a chest dot
(attempts/v1-padlock-look.svg) read as a padlock with a keyhole.
Lucide construction: 'bot'-style rounded head on a rectangular body; arms as quarter arcs
into straight runs.
Keyshape SQUARE: centerline x 6..42 (arms), y 6..42 (dome top, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "be97f138-9a4e-4f13-b4f3-9aaa3afe48ea"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__domed-humanoid-robot/20260926T055140Z-thuan-mac/reference/fiction robot_be97f138-9a4e-4f13-b4f3-9aaa3afe48ea.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class DomedHumanoidRobot(Solo48):
    icon_id = "domed-humanoid-robot"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ("fiction robot", "robot", "android")
    keywords = ("robot", "android", "bot", "machine", "sci-fi", "fiction", "automaton", "ai", "toy")

    def build(self) -> None:
        top, bottom, bl, br = 24, 34, 14, 34
        self.add_polyline("body", (bl, top), (br, top), (br, bottom), (29, bottom), (19, bottom),
                          (bl, bottom), closed=True)
        # head
        self.add_line("head-left", (bl, top), (15, 15))
        self.add_arc("head-dome", (15, 15), (33, 15), radius_x=9)
        self.add_line("head-right", (33, 15), (br, top))
        self.add_contour("head", "head-left", "head-dome", "head-right")
        self.relate("connect", "body", "head")
        self.add_dot("eye", (24, 15))
        # arms
        for side, m in (("left", lambda p: p), ("right", _m)):
            self.add_arc(f"arm-{side}-shoulder", m((bl, top)), m((6, 32)), radius_x=8,
                         sweep=side == "right")
            self.add_line(f"arm-{side}-lower", m((6, 32)), m((6, 38)))
            self.add_contour(f"arm-{side}", f"arm-{side}-shoulder", f"arm-{side}-lower")
            self.relate("connect", "body", f"arm-{side}")
            self.add_polyline(f"leg-{side}", m((19, bottom)), m((19, 42)), m((15, 42)))
            self.relate("connect", "body", f"leg-{side}")

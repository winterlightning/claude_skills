"""Double-ball massage hammer: two balls flanking a rectangular head on a straight handle.

Revision of the disapproved drawing, which had no head block and read as scissors.
Plan (SQUARE, centerline (6,6)-(42,42)): r5 balls about (11,11) and (37,11), a head
block (16,6)-(32,16) whose side walls are tangent to the balls at (16,11)/(32,11), and a
single-stroke handle from the block's bottom centre (24,16) down to (24,42). Mirrored
about x=24. Lucide `hammer` informs the head-on-handle construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5faf9360-04f6-45b9-a0d4-f000e5846bb1"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__double-ball-massage-hammer/20260927T150749Z-thuan-mac-1/reference/massage stick ball_5faf9360-04f6-45b9-a0d4-f000e5846bb1.svg"
AUTHOR = "claude-fable-5-1"


class DoubleBallMassageHammer(Solo48):
    icon_id = "double-ball-massage-hammer"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("massage stick", "massage mallet")
    keywords = ("massage", "hammer", "ball", "stick", "spa", "therapy", "mallet")

    def build(self) -> None:
        for name, cx in (("ball-left", 11), ("ball-right", 37)):
            r, cy = 5, 11
            pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
            for j in range(4):
                self.add_arc(f"{name}-{j}", pts[j], pts[(j + 1) % 4], radius_x=r)
            self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)
        self.add_polyline("head", (16, 6), (32, 6), (32, 11), (32, 16), (24, 16), (16, 16), (16, 11), closed=True)
        self.relate("connect", "head", "ball-left")
        self.relate("connect", "head", "ball-right")
        self.add_line("handle", (24, 16), (24, 42))
        self.relate("connect", "handle", "head")

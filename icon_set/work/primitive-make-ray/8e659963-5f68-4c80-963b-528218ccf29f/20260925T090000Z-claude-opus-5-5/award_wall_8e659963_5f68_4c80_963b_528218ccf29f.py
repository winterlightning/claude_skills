"""Award wall: a shield-shaped pennant hanging from a rod on a triangular hanger.

Symbol plan: everything mirrored about x=24. The pennant is one closed
contour whose top edge is the rod between its two hang points; the rod's
short overhangs and the hanger's two roof lines leave from those same hang
points and are declared connected there. Sides are straight down to a
pointed base, with round joins standing in for the reference's softened
corners. Lucide: `badge`/`shield` single-outline construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8e659963-5f68-4c80-963b-528218ccf29f"
SOURCE_PATH = "icon_set/work/todo-references/award wall_8e659963-5f68-4c80-963b-528218ccf29f.svg"
AUTHOR = "claude-opus-5-5"

CX = 24
ROD_Y, ROD_HALF = 12, 16          # rod x 8..40
SIDE_HALF = 13                    # pennant sides x 11..37
SIDE_BOTTOM, TIP_Y, APEX_Y = 36, 44, 4


class AwardWall(Solo48):
    icon_id = "award-wall"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/award"
    aliases = ("pennant", "wall banner", "hanging award")
    keywords = ("award", "pennant", "banner", "flag", "wall", "trophy", "honor")

    def build(self) -> None:
        l, r = CX - SIDE_HALF, CX + SIDE_HALF
        self.add_polyline(
            "pennant",
            (l, ROD_Y), (r, ROD_Y), (r, SIDE_BOTTOM), (CX, TIP_Y), (l, SIDE_BOTTOM), closed=True,
        )
        self.add_line("rod-left", (CX - ROD_HALF, ROD_Y), (l, ROD_Y))
        self.add_line("rod-right", (r, ROD_Y), (CX + ROD_HALF, ROD_Y))
        self.add_polyline("hanger", (l, ROD_Y), (CX, APEX_Y), (r, ROD_Y))
        self.relate("connect", "rod-left", "pennant-1", "pennant-5", "hanger-1")
        self.relate("connect", "rod-right", "pennant-1", "pennant-2", "hanger-2")

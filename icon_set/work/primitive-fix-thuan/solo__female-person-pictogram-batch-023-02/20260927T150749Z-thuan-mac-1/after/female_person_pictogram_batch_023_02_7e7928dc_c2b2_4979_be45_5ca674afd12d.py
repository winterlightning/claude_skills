"""Female person pictogram: a round head above a flared dress with the legs below the hem.

Revision of the disapproved drawing, whose flat-topped dress and leg block read as an
arrow. Plan (VRECT_L, centerline (8,4)-(40,44)): head r6 at (24,10) built from four
cardinal quarter arcs; a standalone shoulder line (20,24)-(28,24) exactly 8 below the
head (4 visible units), with 45-degree sides flaring to the hem at y=36 and a tapered
leg block to y=44. Human reference: icon_set/references/human_ref/user.svg for the
head/shoulder proportion; Lucide `user` construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7e7928dc-c2b2-4979-be45-5ca674afd12d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__female-person-pictogram-batch-023-02/20260927T150749Z-thuan-mac-1/reference/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg"
AUTHOR = "claude-fable-5-1"


class FemalePersonPictogram(Solo48):
    icon_id = "female-person-pictogram-batch-023-02"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("woman pictogram", "female user", "full body woman")
    keywords = ("female", "woman", "person", "pictogram", "dress", "restroom", "user")

    def build(self) -> None:
        x, y, r = 24, 10, 6
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for j in range(4):
            self.add_arc(f"head-{j}", pts[j], pts[(j + 1) % 4], radius_x=r)
        self.add_contour("head", "head-0", "head-1", "head-2", "head-3", closed=True)
        self.add_line("shoulders", (20, 24), (28, 24))
        self.add_polyline("dress", (28, 24), (40, 36), (32, 36), (30, 44), (18, 44), (16, 36), (8, 36), (20, 24))
        self.relate("connect", "shoulders", "dress")
        self.mark_human_figure("woman", head="head", torso="shoulders", torso_junction="start")

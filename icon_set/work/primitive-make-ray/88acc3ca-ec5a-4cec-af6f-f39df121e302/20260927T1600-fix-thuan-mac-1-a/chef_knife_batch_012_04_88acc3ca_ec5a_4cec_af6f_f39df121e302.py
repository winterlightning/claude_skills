"""Chef knife: a broad curved blade pointing up-left with a long rounded handle down-right.

Revision of the disapproved drawing, whose handle was a tiny diamond so the knife read
as a spatula. Plan (SQUARE, centerline (6,6)-(42,42)): one outline contour on the
45-degree diagonal. Handle: 3-4-5 round cap r5 about (37,37) (hits right 42 and
bottom 42 at once) with sides on x-y=+-7; bolster (29,22)-(22,29) extended to the
dropped heel (20,31); spine straight to the tip (6,6); belly cubic back to the heel.
Lucide `utensils`/knife blade construction; the diagonal is deliberate.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "88acc3ca-ec5a-4cec-af6f-f39df121e302"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chef-knife-batch-012-04/20260927T150749Z-thuan-mac-1/reference/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg"
AUTHOR = "claude-fable-5-1"


class ChefKnife(Solo48):
    icon_id = "chef-knife-batch-012-04"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("kitchen knife", "cook's knife")
    keywords = ("knife", "chef", "blade", "handle", "cutlery", "kitchen", "cooking")

    def build(self) -> None:
        self.add_line("spine", (29, 22), (6, 6))
        self.add_bezier("belly", (6, 6), ((6, 18), (12, 31), (20, 31)))
        self.add_line("heel", (20, 31), (22, 29))
        self.add_line("handle-low", (22, 29), (34, 41))
        self.add_arc("cap", (34, 41), (41, 34), radius_x=5, sweep=False)
        self.add_line("handle-high", (41, 34), (29, 22))
        self.add_contour("knife", "spine", "belly", "heel", "handle-low", "cap", "handle-high", closed=True)
        self.add_line("bolster", (22, 29), (29, 22))
        self.relate("connect", "bolster", "knife")

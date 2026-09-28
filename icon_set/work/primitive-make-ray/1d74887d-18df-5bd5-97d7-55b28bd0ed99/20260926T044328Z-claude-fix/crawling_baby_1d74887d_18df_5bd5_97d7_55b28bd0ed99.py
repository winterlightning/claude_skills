"""A crawling baby: a big round head over a body on all fours - arm reaching to the floor in front, leg folded behind.

Symbol plan: the head is a ring (r5) straight above the flat back, exactly 8 on
centerlines (4 units of ink), per the shared human reference. The body is one closed
tube outline 8 thick: a flat back, the front arm as a 45-degree tube (sides x+y=41 and
x+y=55, 9.9 apart) ending in an r5 hand cap whose 3-4-5 ends keep the sides on the grid,
the belly, the thigh's front dropping to the floor, the shin along the floor ending in
an r5 foot cap, and an r8 curve from the shin's top back up into the back.
Lucide construction: 'baby' - large head over a crawling body silhouette.
Keyshape SQUARE: centerline x 6..42 (hand, foot), y 6..42 (head top, floor).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1d74887d-18df-5bd5-97d7-55b28bd0ed99"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crawling-baby/20260926T044250Z-thuan-mac/reference/crawling kid_1d74887d-18df-5bd5-97d7-55b28bd0ed99.svg"
AUTHOR = "claude-opus-5-5"


class CrawlingBaby(Solo48):
    icon_id = "crawling-baby"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ("crawling kid", "baby crawling", "toddler")
    keywords = ("baby", "crawling", "infant", "toddler", "child", "kid", "family", "nursery")

    def build(self) -> None:
        back, belly, floor = 24, 32, 42
        hx, hy, hr = 20, 11, 5
        pts = [(hx - hr, hy), (hx, hy - hr), (hx + hr, hy), (hx, hy + hr)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=hr)
        self.add_contour("head", *names, closed=True)
        # body: the flat back is its own line (joined at both ends) so the exact head gap is
        # measured against a straight run; the rest is one open outline
        cap_c = (11, 37)
        shoulder, hand_out, hand_in, armpit = (17, back), (cap_c[0] - 3, cap_c[1] - 4), (cap_c[0] + 4, cap_c[1] + 3), (23, belly)
        self.add_line("back", shoulder, (28, back))
        self.add_arc("hip", (28, back), (36, belly), radius_x=8)
        self.add_line("shin-top", (36, belly), (37, belly))
        self.add_arc("foot", (37, belly), (37, floor), radius_x=5)
        self.add_line("shin-bottom", (37, floor), (27, floor))
        self.add_line("thigh-front", (27, floor), (27, belly))
        self.add_line("belly", (27, belly), armpit)
        self.add_line("arm-inner", armpit, hand_in)
        self.add_arc("hand", hand_in, hand_out, radius_x=5, large_arc=True)
        self.add_line("arm-outer", hand_out, shoulder)
        self.add_contour("body", "hip", "shin-top", "foot", "shin-bottom",
                         "thigh-front", "belly", "arm-inner", "hand", "arm-outer")
        self.relate("connect", "body", "back")
        self.mark_human_figure("baby", head="head", torso="back", torso_junction="start")

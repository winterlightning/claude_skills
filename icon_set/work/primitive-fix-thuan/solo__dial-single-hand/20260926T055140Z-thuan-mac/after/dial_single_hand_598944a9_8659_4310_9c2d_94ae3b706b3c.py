"""A round dial with a single straight hand pointing from the centre up to the right.

Symbol plan: the rim is a full r20 circle about (24, 24) (four quarter arcs). The hand is
one straight line from the centre (24, 24) to (33, 17) - the reference's shallow up-right
angle (about 38 degrees, length 11.4, two thirds of the rim radius as in the reference) -
leaving 8.6 between its tip and the rim. The
reference's tiny tick at the pivot is dropped: at 48 px it would only thicken the round cap.
Lucide construction: 'circle' rim with a single 'clock'-style hand from the centre.
Keyshape CIRCLE: rim radius 20 about (24, 24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "598944a9-8659-4310-9c2d-94ae3b706b3c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dial-single-hand/20260926T055140Z-thuan-mac/reference/disc_598944a9-8659-4310-9c2d-94ae3b706b3c.svg"
AUTHOR = "claude-opus-5-5"


class DialSingleHand(Solo48):
    icon_id = "dial-single-hand"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("disc", "dial", "gauge", "meter")
    keywords = ("dial", "gauge", "meter", "clock", "needle", "hand", "disc", "knob", "indicator")

    def build(self) -> None:
        c, r = 24, 20
        pts = [(c - r, c), (c, c - r), (c + r, c), (c, c + r)]
        names = ("rim-nw", "rim-ne", "rim-se", "rim-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("rim", *names, closed=True)
        self.add_line("hand", (c, c), (c + 9, c - 7))

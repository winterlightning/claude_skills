"""A campaign bus: a van with a rounded front, a belt line and wheels, flying a swallowtail flag on a pole.

Symbol plan: the van body is one closed outline - r8 rounded front (tangent into the roof
and the front wall), flat roof, r3 rear corners, bottom split for two wheel arcs (r5
hanging from shared endpoints). A belt line crosses the body at mid height. The window
divider rises from the belt through the roof and continues as the flagpole; the flag is
a closed swallowtail whose left edge is the top of the pole. Vertical rhythm is 8:
flag 4..12, roof 20, belt 28, bottom 36, wheels to 44.
Lucide construction: 'bus'/'truck' body with wheel arcs; 'flag' swallowtail pennant.
Keyshape VRECT_L: centerline x 8..40 (front, rear / flag tip), y 4..44 (flag top, wheels).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "637f75de-1cc0-403f-8da8-3087fab11c86"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__campaign-bus/20260926T034135Z-thuan-mac/reference/election campaign 1_637f75de-1cc0-403f-8da8-3087fab11c86.svg"
AUTHOR = "claude-opus-5-5"


class CampaignBus(Solo48):
    icon_id = "campaign-bus"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "civic/election"
    aliases = ("election campaign", "campaign van", "election bus")
    keywords = ("election", "campaign", "bus", "van", "flag", "tour", "politics", "vote", "rally")

    def build(self) -> None:
        front, rear, rr = 8, 40, 3
        flag_top, flag_bot, roof, belt, bottom = 4, 12, 20, 28, 36
        pole = 22
        w1, w2, wr = 15, 33, 5
        nose = front + 8  # r8 front curve meets the roof here
        # body
        self.add_line("roof-front", (nose, roof), (pole, roof))
        self.add_line("roof-rear", (pole, roof), (rear - rr, roof))
        self.add_arc("corner-rt", (rear - rr, roof), (rear, roof + rr), radius_x=rr)
        self.add_line("rear-upper", (rear, roof + rr), (rear, belt))
        self.add_line("rear-lower", (rear, belt), (rear, bottom - rr))
        self.add_arc("corner-rb", (rear, bottom - rr), (rear - rr, bottom), radius_x=rr)
        self.add_line("bottom-w2", (w2 + 4, bottom), (w2 - 4, bottom))
        self.add_line("bottom-mid", (w2 - 4, bottom), (w1 + 4, bottom))
        self.add_line("bottom-w1", (w1 + 4, bottom), (w1 - 4, bottom))
        self.add_arc("corner-lb", (w1 - 4, bottom), (front, bottom - rr), radius_x=rr)
        self.add_line("front-lower", (front, bottom - rr), (front, belt))
        self.add_arc("front-curve", (front, belt), (nose, roof), radius_x=8)
        self.add_contour("body", "roof-front", "roof-rear", "corner-rt", "rear-upper", "rear-lower",
                         "corner-rb", "bottom-w2", "bottom-mid", "bottom-w1", "corner-lb",
                         "front-lower", "front-curve", closed=True)
        # belt line and divider
        self.add_line("belt-front", (front, belt), (pole, belt))
        self.add_line("belt-rear", (pole, belt), (rear, belt))
        self.add_line("divider", (pole, belt), (pole, roof))
        self.relate("connect", "body", "belt-front")
        self.relate("connect", "body", "belt-rear")
        self.relate("connect", "body", "divider")
        self.relate("connect", "belt-front", "divider")
        self.relate("connect", "belt-rear", "divider")
        # wheels
        for name, wx in (("wheel-front", w1), ("wheel-rear", w2)):
            self.add_arc(name, (wx - 4, bottom), (wx + 4, bottom), radius_x=wr, large_arc=True, sweep=False)
            self.relate("connect", "body", name)
        # pole and swallowtail flag
        self.add_line("pole", (pole, roof), (pole, flag_bot))
        self.add_polyline("flag", (pole, flag_bot), (pole, flag_top), (rear, flag_top), (rear - 5, 8),
                          (rear, flag_bot), closed=True)
        self.relate("connect", "body", "pole")
        self.relate("connect", "divider", "pole")
        self.relate("connect", "pole", "flag")

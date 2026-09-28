"""Broccoli and a carrot: a broccoli floret on the left and a carrot lying on the diagonal.

Symbol plan: the broccoli crown is one closed cloud (a cubic run over four florets: a round left lobe
at x=4, a crest at y=8, a small top-right floret and a right lobe, with inward cusps) on a straight
base at y=22; the stalk hangs from that base as a U 8 wide with an r4 foot reaching y=40,
so the crown overhangs it on both sides. The carrot's axis runs along a=(-3,4)/5 from the
cap centre T=(37,25): its top is an r5 cap whose side points are T+-(4,3), and its sides
are mirror-image cubic runs (in the axis frame (u,v): (0,+-5) -> (6,+-5) -> (12,+-2.5)
-> (15,0)) meeting at the pointed tip (28,37). Two leaf stalks leave the cap's crown point
(40,21): one straight up, one out to the right.
Lucide construction: 'carrot' - tapered body on a diagonal with straight leaf stalks;
'cloud' - bumps with inward cusps for the floret.
Keyshape HRECT_L: centerline x 4..44 (crown lobe, leaf), y 8..40 (crest and leaf, stalk foot).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1833535f-220e-490a-9e51-7058a14ac9db"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260926T030905Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg"
AUTHOR = "claude-opus-5-5"


class BroccoliAndCarrot(Solo48):
    icon_id = "broccoli-and-carrot"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vegetables"
    aliases = ("broccoli-carrot", "vegetables", "veggies")
    keywords = ("broccoli", "carrot", "vegetable", "vegetables", "veggie", "food", "healthy", "vegan", "produce")

    def build(self) -> None:
        # broccoli crown
        self.add_bezier("crown-top", (8, 22),
                        ((5.5, 22), (4, 20), (4, 17.5)),
                        ((4, 15), (6, 13), (8.5, 13)),
                        ((8, 10), (10.5, 8), (13.5, 8)),
                        ((15.5, 8), (17, 9), (17.5, 10.5)),
                        ((18.5, 9.5), (19.5, 9), (21, 9)),
                        ((23.5, 9), (25, 11.5), (25, 14)),
                        ((25, 16.5), (24, 18), (22.5, 18.5)),
                        ((23, 20.5), (22.5, 22), (21, 22)))
        self.add_line("crown-base-right", (21, 22), (18, 22))
        self.add_line("crown-base-mid", (18, 22), (10, 22))
        self.add_line("crown-base-left", (10, 22), (8, 22))
        self.add_contour("crown", "crown-top", "crown-base-right", "crown-base-mid", "crown-base-left",
                         closed=True)
        self.add_line("stalk-left", (10, 22), (10, 36))
        self.add_arc("stalk-foot", (10, 36), (18, 36), radius_x=4, sweep=False)
        self.add_line("stalk-right", (18, 36), (18, 22))
        self.add_contour("stalk", "stalk-left", "stalk-foot", "stalk-right")
        self.relate("connect", "crown", "stalk")
        # carrot, axis frame about T=(37,25)
        tx, ty = 37, 25
        frame = lambda u, v: (round(tx - 0.6 * u + 0.8 * v, 2), round(ty + 0.8 * u + 0.6 * v, 2))
        L, top, Rr, tip = (33, 22), (40, 21), (41, 28), (28, 37)
        self.add_arc("carrot-cap-left", L, top, radius_x=5, sweep=True)
        self.add_arc("carrot-cap-right", top, Rr, radius_x=5, sweep=True)
        self.add_bezier("carrot-side-right", Rr, (frame(6, 5), frame(12, 2.5), tip))
        self.add_bezier("carrot-side-left", tip, (frame(12, -2.5), frame(6, -5), L))
        self.add_contour("carrot", "carrot-cap-left", "carrot-cap-right", "carrot-side-right",
                         "carrot-side-left", closed=True)
        self.add_line("leaf-up", top, (40, 8))
        self.add_line("leaf-right", top, (44, 18))
        self.relate("connect", "carrot", "leaf-up")
        self.relate("connect", "carrot", "leaf-right")
        self.relate("connect", "leaf-up", "leaf-right")

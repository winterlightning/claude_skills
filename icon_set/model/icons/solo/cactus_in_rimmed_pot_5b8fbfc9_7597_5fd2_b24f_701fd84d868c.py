"""Round-topped cactus with unequal raised arms in a rimmed pot. No local Lucide cactus match; uses quarter-circle bends and semicircular tips. Source has no spines to retain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'


class CactusInRimmedPot(Solo48):
    icon_id = 'cactus-in-rimmed-pot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46); arm heights intentionally unequal.
        self.add_line("trunk-left-bottom", (18,30), (18,23))
        self.add_arc("left-arm-outer", (18,23), (5,10), radius_x=13)
        self.add_arc("left-arm-cap", (5,10), (11,10), radius_x=3)
        self.add_arc("left-arm-inner", (11,10), (18,17), radius_x=7, sweep=False)
        self.add_line("trunk-left-top", (18,17), (18,8))
        self.add_arc("head-left", (18,8), (24,2), radius_x=6)
        self.add_arc("head-right", (24,2), (30,8), radius_x=6)
        self.add_line("trunk-right-top", (30,8), (30,15))
        self.add_arc("right-arm-inner", (30,15), (37,8), radius_x=7, sweep=False)
        self.add_arc("right-arm-cap", (37,8), (43,8), radius_x=3)
        self.add_arc("right-arm-outer", (43,8), (30,21), radius_x=13)
        self.add_line("trunk-right-bottom", (30,21), (30,30))
        self.add_contour("cactus", "trunk-left-bottom", "left-arm-outer", "left-arm-cap", "left-arm-inner", "trunk-left-top", "head-left", "head-right", "trunk-right-top", "right-arm-inner", "right-arm-cap", "right-arm-outer", "trunk-right-bottom")
        self.add_polyline("rim", (10,30), (24,30), (38,30), (38,36), (34,36), (14,36), (10,36), closed=True)
        self.add_polyline("pot", (14,36), (16,46), (32,46), (34,36))
        self.relate("connect", "rim", "pot")
        self.relate("connect", "cactus", "rim")

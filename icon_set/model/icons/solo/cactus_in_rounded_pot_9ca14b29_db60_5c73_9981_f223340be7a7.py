"""Cactus with left arm higher in a plain rounded pot. No useful local Lucide cactus match; coherent circular bends retain the intentional asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ca14b29-db60-5c73-9981-f223340be7a7'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_9ca14b29-db60-5c73-9981-f223340be7a7.svg'
AUTHOR = 'gpt-6'


class CactusInRoundedPot(Solo48):
    icon_id = 'cactus-in-rounded-pot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46); arm heights intentionally unequal.
        self.add_line("trunk-left-bottom", (18,30), (18,21))
        self.add_arc("left-arm-outer", (18,21), (5,8), radius_x=13)
        self.add_arc("left-arm-cap", (5,8), (11,8), radius_x=3)
        self.add_arc("left-arm-inner", (11,8), (18,15), radius_x=7, sweep=False)
        self.add_line("trunk-left-top", (18,15), (18,8))
        self.add_arc("head-left", (18,8), (24,2), radius_x=6)
        self.add_arc("head-right", (24,2), (30,8), radius_x=6)
        self.add_line("trunk-right-top", (30,8), (30,18))
        self.add_arc("right-arm-inner", (30,18), (37,11), radius_x=7, sweep=False)
        self.add_arc("right-arm-cap", (37,11), (43,11), radius_x=3)
        self.add_arc("right-arm-outer", (43,11), (30,24), radius_x=13)
        self.add_line("trunk-right-bottom", (30,24), (30,30))
        self.add_contour("cactus", "trunk-left-bottom", "left-arm-outer", "left-arm-cap", "left-arm-inner", "trunk-left-top", "head-left", "head-right", "trunk-right-top", "right-arm-inner", "right-arm-cap", "right-arm-outer", "trunk-right-bottom")
        self.add_polyline("mouth", (12,30), (24,30), (36,30))
        self.add_line("pot-right", (36,30), (34,42))
        self.add_arc("bottom-right", (34,42), (30,46), radius_x=4)
        self.add_line("bottom", (30,46), (18,46))
        self.add_arc("bottom-left", (18,46), (14,42), radius_x=4)
        self.add_line("pot-left", (14,42), (12,30))
        self.add_contour("pot", "pot-right", "bottom-right", "bottom", "bottom-left", "pot-left")
        self.relate("connect", "mouth", "pot")
        self.relate("connect", "cactus", "mouth")

"""Five alternating pointed leaves on a hanging stem. Lucide sprout informs two-arc leaves; short side stalks are absorbed into the stem attachments. Unequal heights and rightward terminal leaf are intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73751da6-c4f7-4cdd-9167-eaaf2012de13'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/hanging plant_73751da6-c4f7-4cdd-9167-eaaf2012de13.svg'
AUTHOR = 'gpt-6'


class FiveLeafHangingVine(Solo48):
    icon_id = 'five-leaf-hanging-vine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_L extremes (8,2)-(40,46). Staggered leaves retain the hanging rhythm.
        self.add_polyline("stem", (24,2), (24,12), (24,16), (24,28), (24,34))
        self.add_arc("upper-left-a", (8, 4), (24, 16), radius_x=16, radius_y=12)
        self.add_arc("upper-left-b", (24, 16), (8, 4), radius_x=16, radius_y=12)
        self.add_contour("upper-left", "upper-left-a", "upper-left-b", closed=True)
        self.add_arc("upper-right-a", (24, 12), (40, 2), radius_x=16, radius_y=10)
        self.add_arc("upper-right-b", (40, 2), (24, 12), radius_x=16, radius_y=10)
        self.add_contour("upper-right", "upper-right-a", "upper-right-b", closed=True)
        self.add_arc("lower-left-a", (8, 22), (24, 34), radius_x=16, radius_y=12)
        self.add_arc("lower-left-b", (24, 34), (8, 22), radius_x=16, radius_y=12)
        self.add_contour("lower-left", "lower-left-a", "lower-left-b", closed=True)
        self.add_arc("lower-right-a", (24, 28), (40, 16), radius_x=16, radius_y=12)
        self.add_arc("lower-right-b", (40, 16), (24, 28), radius_x=16, radius_y=12)
        self.add_contour("lower-right", "lower-right-a", "lower-right-b", closed=True)
        self.add_arc("terminal-a", (24, 34), (36, 46), radius_x=12, radius_y=12)
        self.add_arc("terminal-b", (36, 46), (24, 34), radius_x=12, radius_y=12)
        self.add_contour("terminal", "terminal-a", "terminal-b", closed=True)
        for name in ("upper-left", "upper-right", "lower-left", "lower-right", "terminal"):
            self.relate("connect", name, "stem")
        self.relate("connect", "lower-left", "terminal")

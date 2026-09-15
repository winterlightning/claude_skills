"""A crescent and five-pointed star. HRECT_L extremes (4,8)-(44,40). Lucide moon-star informs paired celestial subjects and a coherent concave crescent; preserve the source five-pointed star rather than the Lucide cross. Widen the crescent band and clear its opening for the star."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7ea547a-6e38-4494-be1a-8e7ed00dd417'
SOURCE_PATH = 'pictographic-primitives/symbol/moon and star_b7ea547a-6e38-4494-be1a-8e7ed00dd417.svg'
AUTHOR = 'gpt-6'


class MoonAndStar(Solo48):
    icon_id = 'moon-and-star'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('moon', 'star', 'night', 'crescent', 'sky', 'islam', 'ramadan', 'sleep')

    def build(self) -> None:
        self.add_arc('outer-top',(20,8),(4,24),radius_x=16,sweep=False)
        self.add_arc('outer-bottom',(4,24),(20,40),radius_x=16,sweep=False)
        self.add_arc('inner',(20,40),(20,8),radius_x=6,radius_y=16)
        self.add_contour('moon','outer-top','outer-bottom','inner',closed=True)
        self.add_polyline('star',(35,12),(38,19),(44,20),(39,25),(40,32),(35,29),(29,32),(30,25),(25,20),(32,19),(35,12),closed=True)

"""Two broad pointed leaves on a stem in a rimmed pot. Lucide sprout informs paired arc leaves, with intentional stagger retained from source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2afcf43c-09b9-5de1-9777-49c4ecd3a602'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_2afcf43c-09b9-5de1-9777-49c4ecd3a602.svg'
AUTHOR = 'gpt-6'


class BroadLeafSeedlingInRimmedPot(Solo48):
    icon_id = 'broad-leaf-seedling-in-rimmed-pot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46); left leaf deliberately higher.
        self.add_arc("left-upper", (5,2), (24,20), radius_x=19, radius_y=18)
        self.add_arc("left-lower", (24,20), (5,2), radius_x=19, radius_y=18)
        self.add_contour("left-leaf", "left-upper", "left-lower", closed=True)
        self.add_arc("right-upper", (24,23), (43,5), radius_x=19, radius_y=18)
        self.add_arc("right-lower", (43,5), (24,23), radius_x=19, radius_y=18)
        self.add_contour("right-leaf", "right-upper", "right-lower", closed=True)
        self.add_polyline("stem", (24,20), (24,23), (24,30))
        self.relate("connect", "left-leaf", "stem")
        self.relate("connect", "right-leaf", "stem")
        self.add_polyline("rim", (10,30), (24,30), (38,30), (38,36), (34,36), (14,36), (10,36), closed=True)
        self.add_polyline("pot", (14,36), (16,46), (32,46), (34,36))
        self.relate("connect", "rim", "pot")
        self.relate("connect", "stem", "rim")

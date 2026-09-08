"""Crystal sphere on a tapered stand. VRECT_XL (5,2)-(43,46). Retained orb and widening stand; removed extra plinth seam. Mirrored construction; no useful direct Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9acd961d-254b-46da-a4e6-47bf2a234155'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/sphere_9acd961d-254b-46da-a4e6-47bf2a234155.svg'
AUTHOR = 'astra-chatgpt'


class CrystalBallOnStand(Solo48):
    icon_id = 'crystal-ball-on-stand'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('crystal ball', 'sphere', 'fortune', 'divination', 'psychic', 'mystic', 'orb', 'future')

    def build(self) -> None:
        self.add_arc('orb-top', (7,19), (41,19), radius_x=17)
        self.add_arc('orb-bottom', (41,19), (7,19), radius_x=17)
        self.add_contour('orb', 'orb-top', 'orb-bottom', closed=True)
        self.add_polyline('stand', (5,46), (9,36), (39,36), (43,46), closed=True)
        self.relate('connect','orb','stand')

"""Rating half star (rating), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cdd85cc2-8ad0-55be-b0b7-722399ebd6d6'
SOURCE_PATH = 'icons-json/rating/rating half star_cdd85cc2-8ad0-55be-b0b7-722399ebd6d6.json'
AUTHOR = 'json_to_solo'

class RatingHalfStar(Solo48):
    icon_id = 'rating-half-star'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    aliases = ()
    keywords = ('rating', 'half', 'star')

    def build(self):
        self.add_line('e0', (40, 4), (40, 32))
        self.add_line('e1', (39, 34), (20, 44))
        self.add_line('e2', (20, 44), (26, 27))
        self.add_line('e3', (26, 27), (8, 16))
        self.add_line('e4', (8, 16), (31, 16))
        self.add_line('e5', (31, 16), (40, 4))
        self.add_line('e6', (40, 32), (39, 34))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e3', 'e4', 'e5')

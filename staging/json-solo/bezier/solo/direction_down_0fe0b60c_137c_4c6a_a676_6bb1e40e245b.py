"""Direction down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fe0b60c-137c-4c6a-a676-6bb1e40e245b'
SOURCE_PATH = 'icons-json/arrows/direction down_0fe0b60c-137c-4c6a-a676-6bb1e40e245b.json'
AUTHOR = 'json_to_solo'

class DirectionDownArrows(Solo48):
    icon_id = 'direction-down-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('direction', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 33), (24, 44))
        self.add_line('e2', (40, 33), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

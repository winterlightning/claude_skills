"""Circle arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3aff8073-22e1-56e9-acc2-deec5055c179'
SOURCE_PATH = 'icons-json/arrows/circle arrow left_3aff8073-22e1-56e9-acc2-deec5055c179.json'
AUTHOR = 'json_to_solo'

class CircleArrowLeftArrows(Solo48):
    icon_id = 'circle-arrow-left-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('circle', 'arrow', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (22, 15), (14, 24))
        self.add_line('e1', (22, 32), (14, 24))
        self.add_line('e2', (14, 24), (34, 24))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')

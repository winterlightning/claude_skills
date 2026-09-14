"""Circle arrow right (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90afee1d-c8d3-4450-9484-ad9b41908249'
SOURCE_PATH = 'icons-json/state/circle arrow right_90afee1d-c8d3-4450-9484-ad9b41908249.json'
AUTHOR = 'json_to_solo'

class CircleArrowRight(Solo48):
    icon_id = 'circle-arrow-right'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'arrow', 'right', 'state')

    def build(self):
        self.add_line('e0', (26, 15), (35, 24))
        self.add_line('e1', (13, 24), (35, 24))
        self.add_line('e2', (26, 33), (35, 24))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

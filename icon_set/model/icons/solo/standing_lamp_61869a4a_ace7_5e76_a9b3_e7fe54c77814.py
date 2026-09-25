"""Standing lamp (lamps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61869a4a-ace7-5e76-a9b3-e7fe54c77814'
SOURCE_PATH = 'pictographic-primitives/lamps/standing lamp_61869a4a-ace7-5e76-a9b3-e7fe54c77814.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class StandingLamp(Solo48):
    icon_id = 'standing-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    categories = ('lamps', 'primitives')
    aliases = ()
    keywords = ('standing', 'lamp', 'lamps')

    def build(self):
        self.add_line('e0', (24, 44), (24, 19))
        self.add_line('e1', (14, 44), (34, 44))
        self.add_line('e2', (34, 4), (14, 4))
        self.add_line('e3', (14, 4), (8, 19))
        self.add_line('e4', (8, 19), (40, 19))
        self.add_line('e5', (40, 19), (34, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')

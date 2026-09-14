"""Topic organize (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9931aa1d-bb1a-511f-85d1-eb3c53f683a0'
SOURCE_PATH = 'icons-json/interface-essential/topic organize_9931aa1d-bb1a-511f-85d1-eb3c53f683a0.json'
AUTHOR = 'json_to_solo'

class TopicOrganize(Solo48):
    icon_id = 'topic-organize'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('topic', 'organize', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 34), (9, 34))
        self.add_line('e1', (4, 29), (4, 19))
        self.add_line('e2', (9, 14), (16, 14))
        self.add_line('e3', (44, 28), (18, 28))
        self.add_line('e4', (18, 28), (18, 40))
        self.add_line('e5', (18, 40), (44, 40))
        self.add_line('e6', (44, 40), (44, 28))
        self.add_arc('e7-top', (16, 14), (26, 14), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (26, 14), (16, 14), radius_x=5, radius_y=6)
        self.add_arc('e8', (9, 34), (4, 29), radius_x=5)
        self.add_arc('e9', (4, 19), (9, 14), radius_x=5)
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e7')

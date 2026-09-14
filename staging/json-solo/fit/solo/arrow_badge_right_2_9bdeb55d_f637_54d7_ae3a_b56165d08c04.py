"""Arrow badge right 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bdeb55d-f637-54d7-ae3a-b56165d08c04'
SOURCE_PATH = 'icons-json/arrows/arrow badge right 2_9bdeb55d-f637-54d7-ae3a-b56165d08c04.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeRight2Arrows(Solo48):
    icon_id = 'arrow-badge-right-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 32), (31, 24))
        self.add_line('sym-e1', (31, 24), (24, 16))
        self.add_arc('sym-e3', (44, 24), (42, 20), radius_x=5, sweep=False)
        self.add_line('sym-e4', (42, 20), (31, 9))
        self.add_line('sym-e5', (31, 9), (29, 8))
        self.add_line('sym-e6', (29, 8), (6, 8))
        self.add_line('sym-e7', (6, 8), (4, 9))
        self.add_line('sym-e8', (4, 9), (4, 10))
        self.add_line('sym-e9', (4, 10), (4, 24))
        self.add_line('sym-e10', (4, 24), (4, 38))
        self.add_line('sym-e11', (4, 38), (4, 39))
        self.add_line('sym-e12', (4, 39), (6, 40))
        self.add_line('sym-e13', (6, 40), (29, 40))
        self.add_line('sym-e14', (29, 40), (31, 39))
        self.add_line('sym-e15', (31, 39), (42, 28))
        self.add_arc('sym-e16', (42, 28), (44, 24), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)

"""Arrow badge x left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '594d976c-4682-5989-80ec-2d26cb7a3aef'
SOURCE_PATH = 'icons-json/arrows/arrow badge x left_594d976c-4682-5989-80ec-2d26cb7a3aef.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeXLeft(Solo48):
    icon_id = 'arrow-badge-x-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'x', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (23, 32), (37, 16))
        self.add_line('e1', (23, 17), (37, 32))
        self.add_line('e2', (6, 27), (17, 39))
        self.add_line('e3', (20, 40), (41, 40))
        self.add_line('e4', (44, 37), (44, 10))
        self.add_line('e5', (40, 8), (19, 8))
        self.add_line('e6', (19, 8), (5, 22))
        self.add_arc('e7', (17, 39), (20, 40), radius_x=5, sweep=False)
        self.add_arc('e8', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_arc('e9-1', (44, 10), (42, 8), radius_x=2, sweep=False)
        self.add_line('e9-2', (42, 8), (40, 8))
        self.add_arc('e10-1', (5, 22), (4, 24), radius_x=3, sweep=False)
        self.add_arc('e10-2', (4, 24), (6, 27), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e5', 'e6', 'e10-1', 'e10-2', closed=True)

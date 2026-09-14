"""911 (text) (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53668ec4-a104-4d57-8154-81e216c068e3'
SOURCE_PATH = 'icons-json/state/911 (text)_53668ec4-a104-4d57-8154-81e216c068e3.json'
AUTHOR = 'json_to_solo'

class Icon911TextState(Solo48):
    icon_id = 'icon-911-text-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('text', 'state')

    def build(self):
        self.add_line('e0', (30, 8), (30, 40))
        self.add_line('e1', (44, 8), (44, 40))
        self.add_line('e2-1', (16, 17), (16, 31))
        self.add_arc('e2-2', (16, 31), (10, 40), radius_x=8)
        self.add_arc('e2-3', (10, 40), (7, 39), radius_x=5)
        self.add_arc('e2-4', (7, 39), (5, 36), radius_x=6)
        self.add_arc('e3', (25, 14), (30, 8), radius_x=18, sweep=False)
        self.add_arc('e4', (39, 14), (44, 8), radius_x=18, sweep=False)
        self.add_arc('e5-1', (16, 18), (10, 8), radius_x=9, sweep=False)
        self.add_line('e5-2', (10, 8), (7, 9))
        self.add_arc('e5-3', (7, 9), (5, 13), radius_x=9, sweep=False)
        self.add_arc('e5-4', (5, 13), (4, 18), radius_x=14, sweep=False)
        self.add_arc('e5-5', (4, 18), (5, 23), radius_x=15, sweep=False)
        self.add_arc('e5-6', (5, 23), (10, 28), radius_x=6, sweep=False)
        self.add_arc('e5-7', (10, 28), (16, 18), radius_x=9, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
        self.add_contour('c1', 'e3', 'e0')
        self.add_contour('c2', 'e4', 'e1')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c3', 'c0')

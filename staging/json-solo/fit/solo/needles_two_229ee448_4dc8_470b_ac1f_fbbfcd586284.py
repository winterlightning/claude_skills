"""Needles two (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '229ee448-4dc8-470b-ac1f-fbbfcd586284'
SOURCE_PATH = 'icons-json/state/needles two_229ee448-4dc8-470b-ac1f-fbbfcd586284.json'
AUTHOR = 'json_to_solo'

class NeedlesTwoState(Solo48):
    icon_id = 'needles-two-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('needles', 'two', 'state')

    def build(self):
        self.add_line('e0', (32, 37), (6, 37))
        self.add_line('e1', (17, 15), (6, 27))
        self.add_arc('e2-top', (32, 37), (42, 37), radius_x=5)
        self.add_arc('e2-bottom', (42, 37), (32, 37), radius_x=5)
        self.add_arc('e3-top', (16, 12), (28, 12), radius_x=6)
        self.add_arc('e3-bottom', (28, 12), (16, 12), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
        self.relate('connect', 'c1', 'e3')

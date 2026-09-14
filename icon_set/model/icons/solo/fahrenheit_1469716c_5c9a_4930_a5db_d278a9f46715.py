"""Fahrenheit (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1469716c-5c9a-4930-a5db-d278a9f46715'
SOURCE_PATH = 'icons-json/state/fahrenheit_1469716c-5c9a-4930-a5db-d278a9f46715.json'
AUTHOR = 'json_to_solo'

class Fahrenheit(Solo48):
    icon_id = 'fahrenheit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('fahrenheit', 'state')

    def build(self):
        self.add_line('e0', (40, 9), (19, 9))
        self.add_line('e1', (19, 9), (19, 44))
        self.add_line('e2', (35, 27), (19, 27))
        self.add_arc('e3', (8, 4), (8, 5), radius_x=5)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c1', 'c0')

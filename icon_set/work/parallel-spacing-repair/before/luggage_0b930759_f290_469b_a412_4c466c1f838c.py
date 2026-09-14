"""Luggage (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = 'icons-json/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.json'
AUTHOR = 'json_to_solo'

class Luggage(Solo48):
    icon_id = 'luggage'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('luggage', 'state')

    def build(self):
        self.add_line('e0', (19, 10), (19, 5))
        self.add_line('e1', (21, 4), (28, 4))
        self.add_line('e2', (29, 5), (29, 10))
        self.add_line('e3', (11, 40), (11, 44))
        self.add_line('e4', (37, 40), (37, 44))
        self.add_line('e5', (37, 40), (11, 40))
        self.add_line('e6', (8, 38), (8, 13))
        self.add_line('e7', (12, 10), (36, 10))
        self.add_line('e8', (40, 13), (40, 38))
        self.add_arc('e9', (19, 5), (21, 4), radius_x=3)
        self.add_arc('e10', (28, 4), (29, 5), radius_x=1)
        self.add_arc('e11', (11, 40), (8, 38), radius_x=3)
        self.add_arc('e12', (8, 13), (12, 10), radius_x=4)
        self.add_arc('e13', (36, 10), (40, 13), radius_x=4)
        self.add_arc('e14', (40, 38), (37, 40), radius_x=3)
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e11', 'e6', 'e12', 'e7', 'e13', 'e8', 'e14', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')

"""Acorn (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba175ed8-1c20-536e-bdbc-2223ac1856fa'
SOURCE_PATH = 'icons-json/food/acorn_ba175ed8-1c20-536e-bdbc-2223ac1856fa.json'
AUTHOR = 'json_to_solo'

class AcornFood(Solo48):
    icon_id = 'acorn-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('acorn', 'food')

    def build(self):
        self.add_line('e0', (11, 22), (37, 22))
        self.add_arc('e1', (27, 4), (24, 9), radius_x=5, sweep=False)
        self.add_arc('e2-1', (37, 22), (37, 33), radius_x=22)
        self.add_arc('e2-2', (37, 33), (24, 44), radius_x=26)
        self.add_arc('e2-3', (24, 44), (11, 33), radius_x=25)
        self.add_arc('e2-4', (11, 33), (11, 23), radius_x=20)
        self.add_line('e2-5', (11, 23), (8, 19))
        self.add_arc('e2-6', (8, 19), (14, 11), radius_x=10)
        self.add_line('e2-7', (14, 11), (24, 9))
        self.add_arc('e3-1', (37, 22), (40, 19), radius_x=3, sweep=False)
        self.add_arc('e3-2', (40, 19), (38, 14), radius_x=8, sweep=False)
        self.add_arc('e3-3', (38, 14), (24, 9), radius_x=17, sweep=False)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7')
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')

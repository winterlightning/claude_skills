"""Batch-07/bag carry (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80985b68-e4c6-544f-91e4-19b090803024'
SOURCE_PATH = 'icons-json/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.json'
AUTHOR = 'json_to_solo'

class Batch07BagCarry(Solo48):
    icon_id = 'batch-07-bag-carry'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'bag', 'carry', 'accessories')

    def build(self):
        self.add_line('e0', (37, 44), (12, 44))
        self.add_line('e1', (8, 40), (10, 13))
        self.add_line('e2', (10, 13), (38, 13))
        self.add_line('e3', (38, 13), (40, 37))
        self.add_arc('e4-1', (32, 13), (24, 4), radius_x=9, sweep=False)
        self.add_arc('e4-2', (24, 4), (18, 7), radius_x=8, sweep=False)
        self.add_line('e4-3', (18, 7), (16, 13))
        self.add_line('e5-1', (40, 37), (40, 41))
        self.add_arc('e5-2', (40, 41), (37, 44), radius_x=3)
        self.add_arc('e6', (12, 44), (8, 40), radius_x=4)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e0', 'e6', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')

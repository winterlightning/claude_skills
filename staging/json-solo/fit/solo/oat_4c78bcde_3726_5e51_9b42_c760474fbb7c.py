"""Oat (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c78bcde-3726-5e51-9b42-c760474fbb7c'
SOURCE_PATH = 'icons-json/food/oat_4c78bcde-3726-5e51-9b42-c760474fbb7c.json'
AUTHOR = 'json_to_solo'

class OatFood(Solo48):
    icon_id = 'oat-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('oat', 'food')

    def build(self):
        self.add_line('e0', (11, 42), (37, 6))
        self.add_arc('e1-1', (37, 6), (40, 13), radius_x=10)
        self.add_line('e1-2', (40, 13), (39, 21))
        self.add_arc('e1-3', (39, 21), (33, 33), radius_x=41)
        self.add_arc('e1-4', (33, 33), (16, 44), radius_x=22)
        self.add_line('e1-5', (16, 44), (11, 42))
        self.add_arc('e2-1', (37, 6), (32, 4), radius_x=9, sweep=False)
        self.add_arc('e2-2', (32, 4), (14, 16), radius_x=23, sweep=False)
        self.add_arc('e2-3', (14, 16), (8, 34), radius_x=32, sweep=False)
        self.add_arc('e2-4', (8, 34), (11, 42), radius_x=13, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0', closed=True)
        self.relate('connect', 'c0', 'c1')

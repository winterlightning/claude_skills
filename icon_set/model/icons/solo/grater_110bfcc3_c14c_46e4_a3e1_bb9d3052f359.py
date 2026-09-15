"""Grater (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '110bfcc3-c14c-46e4-a3e1-bb9d3052f359'
SOURCE_PATH = 'icons-json/food/grater_110bfcc3-c14c-46e4-a3e1-bb9d3052f359.json'
AUTHOR = 'gpt-6'

class Grater(Solo48):
    icon_id = 'grater'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('grater', 'food')

    def build(self):
        self.add_line('sym-e0', (9, 12), (39, 12))
        self.add_line('sym-e2', (39, 12), (40, 41))
        self.add_arc('sym-e3', (40, 41), (40, 42), radius_x=41, radius_y=41, large_arc=False, sweep=False)
        self.add_line('sym-e4', (40, 42), (38, 44))
        self.add_line('sym-e5', (38, 44), (10, 44))
        self.add_line('sym-e7', (10, 44), (8, 42))
        self.add_line('sym-e8', (8, 42), (8, 41))
        self.add_line('sym-e9', (8, 41), (9, 12))
        self.add_arc('sym-e10', (9, 12), (13, 5), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (13, 5), (15, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e12', (15, 4), (33, 4))
        self.add_arc('sym-e14', (33, 4), (35, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e15', (35, 5), (39, 12), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=False)

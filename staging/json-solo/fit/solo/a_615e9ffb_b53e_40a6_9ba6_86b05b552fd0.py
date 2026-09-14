"""A (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '615e9ffb-b53e-40a6-9ba6-86b05b552fd0'
SOURCE_PATH = 'icons-json/typeface/a_615e9ffb-b53e-40a6-9ba6-86b05b552fd0.json'
AUTHOR = 'json_to_solo'

class A615e9ffb(Solo48):
    icon_id = 'a-615e9ffb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('a', 'typeface')

    def build(self):
        self.add_line('e0', (40, 44), (40, 34))
        self.add_arc('e1-1', (40, 34), (25, 44), radius_x=18)
        self.add_line('e1-2', (25, 44), (19, 43))
        self.add_arc('e1-3', (19, 43), (11, 37), radius_x=15)
        self.add_line('e1-4', (11, 37), (9, 33))
        self.add_line('e1-5', (9, 33), (8, 25))
        self.add_line('e1-6', (8, 25), (9, 18))
        self.add_arc('e1-7', (9, 18), (12, 12), radius_x=21)
        self.add_arc('e1-8', (12, 12), (25, 4), radius_x=16)
        self.add_arc('e1-9', (25, 4), (39, 13), radius_x=16)
        self.add_line('e1-10', (39, 13), (40, 27))
        self.add_arc('e1-11', (40, 27), (40, 34), radius_x=31, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', closed=True)

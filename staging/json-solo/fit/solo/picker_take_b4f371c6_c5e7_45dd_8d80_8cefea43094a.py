"""Picker take (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4f371c6-c5e7-45dd-8d80-8cefea43094a'
SOURCE_PATH = 'icons-json/design/picker take_b4f371c6-c5e7-45dd-8d80-8cefea43094a.json'
AUTHOR = 'json_to_solo'

class PickerTakeDesign(Solo48):
    icon_id = 'picker-take-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'take', 'design')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (40, 16), (33, 16))
        self.add_line('e2', (15, 16), (33, 16))
        self.add_line('e3', (15, 16), (15, 28))
        self.add_line('e4', (20, 31), (20, 33))
        self.add_line('e5', (28, 33), (28, 31))
        self.add_line('e6', (33, 28), (33, 16))
        self.add_line('e7', (15, 16), (15, 8))
        self.add_line('e8', (33, 9), (33, 16))
        self.add_line('e9', (15, 28), (20, 31))
        self.add_arc('e10', (20, 33), (28, 33), radius_x=6, sweep=False)
        self.add_line('e11', (28, 31), (33, 28))
        self.add_arc('e12-1', (15, 8), (18, 5), radius_x=4)
        self.add_line('e12-2', (18, 5), (23, 4))
        self.add_line('e12-3', (23, 4), (29, 5))
        self.add_arc('e12-4', (29, 5), (33, 9), radius_x=5)
        self.add_arc('e13-1', (22, 39), (20, 43), radius_x=3, sweep=False)
        self.add_line('e13-2', (20, 43), (24, 44))
        self.add_line('e13-3', (24, 44), (27, 43))
        self.add_arc('e13-4', (27, 43), (24, 38), radius_x=4, sweep=False)
        self.add_arc('e13-5', (24, 38), (22, 39), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6')
        self.add_contour('c4', 'e7', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e8')
        self.add_contour('c5', 'e13-1', 'e13-2', 'e13-3', 'e13-4', 'e13-5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')

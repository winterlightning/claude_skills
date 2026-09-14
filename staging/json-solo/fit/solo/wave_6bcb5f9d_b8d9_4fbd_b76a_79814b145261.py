"""Wave (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bcb5f9d-b8d9-4fbd-b76a-79814b145261'
SOURCE_PATH = 'icons-json/wayfinding/wave_6bcb5f9d-b8d9-4fbd-b76a-79814b145261.json'
AUTHOR = 'json_to_solo'

class Wave6bcb5f9d(Solo48):
    icon_id = 'wave-6bcb5f9d'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('wave', 'wayfinding')

    def build(self):
        self.add_line('e0', (12, 28), (8, 21))
        self.add_line('e1', (40, 26), (36, 21))
        self.add_line('e2', (26, 37), (23, 42))
        self.add_arc('e3', (8, 42), (12, 28), radius_x=13, sweep=False)
        self.add_line('e4-1', (8, 21), (6, 16))
        self.add_arc('e4-2', (6, 16), (11, 6), radius_x=14)
        self.add_arc('e5-1', (38, 42), (42, 33), radius_x=13, sweep=False)
        self.add_line('e5-2', (42, 33), (40, 26))
        self.add_arc('e6', (36, 21), (40, 6), radius_x=12)
        self.add_arc('e7-1', (26, 6), (21, 13), radius_x=16, sweep=False)
        self.add_arc('e7-2', (21, 13), (21, 18), radius_x=9, sweep=False)
        self.add_line('e7-3', (21, 18), (27, 29))
        self.add_arc('e7-4', (27, 29), (26, 37), radius_x=10)
        self.add_contour('c0', 'e3', 'e0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e1', 'e6')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2')

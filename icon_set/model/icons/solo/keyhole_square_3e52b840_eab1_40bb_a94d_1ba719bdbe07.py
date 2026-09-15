"""Keyhole square (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e52b840-eab1-40bb-a94d-1ba719bdbe07'
SOURCE_PATH = 'icons-json/interface-essential/keyhole square_3e52b840-eab1-40bb-a94d-1ba719bdbe07.json'
AUTHOR = 'gpt-6'

class KeyholeSquare(Solo48):
    icon_id = 'keyhole-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyhole', 'square', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 22), (30, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (30, 22), (24, 27), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (24, 27), (18, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e3', (24, 27), (24, 33))
        self.add_line('sym-e4', (6, 38), (6, 10))
        self.add_arc('sym-e6', (6, 10), (10, 6), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e7', (10, 6), (38, 6))
        self.add_arc('sym-e9', (38, 6), (42, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e11', (42, 10), (42, 38))
        self.add_arc('sym-e12', (42, 38), (38, 42), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e14', (38, 42), (10, 42))
        self.add_arc('sym-e17', (10, 42), (6, 38), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', closed=False)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e17', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')

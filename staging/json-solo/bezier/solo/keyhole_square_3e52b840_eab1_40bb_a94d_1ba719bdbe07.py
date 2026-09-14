"""Keyhole square (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e52b840-eab1-40bb-a94d-1ba719bdbe07'
SOURCE_PATH = 'icons-json/interface-essential/keyhole square_3e52b840-eab1-40bb-a94d-1ba719bdbe07.json'
AUTHOR = 'json_to_solo'

class KeyholeSquareInterfaceEssential(Solo48):
    icon_id = 'keyhole-square-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyhole', 'square', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 22), (30, 22), radius_x=6)
        self.add_arc('sym-e1', (30, 22), (24, 27), radius_x=6)
        self.add_arc('sym-e2', (24, 27), (18, 22), radius_x=6)
        self.add_line('sym-e3', (24, 27), (24, 33))
        self.add_line('sym-e4', (6, 38), (6, 10))
        self.add_bezier('sym-e5', (6, 10), ((6.008, 9.967), (6, 10.033), (6, 10)))
        self.add_bezier('sym-e6', (6, 10), ((6, 8.331), (8.323, 6), (10, 6)))
        self.add_line('sym-e7', (10, 6), (24, 6))
        self.add_line('sym-e8', (24, 6), (38, 6))
        self.add_bezier('sym-e9', (38, 6), ((39.677, 6), (42, 8.331), (42, 10)))
        self.add_bezier('sym-e10', (42, 10), ((42, 10.033), (41.992, 9.967), (42, 10)))
        self.add_line('sym-e11', (42, 10), (42, 38))
        self.add_bezier('sym-e12', (42, 38), ((42, 39.685), (39.702, 42), (38, 42)))
        self.add_bezier('sym-e13', (38, 42), ((37.975, 42), (38.025, 41.992), (38, 42)))
        self.add_line('sym-e14', (38, 42), (24, 42))
        self.add_line('sym-e15', (24, 42), (10, 42))
        self.add_bezier('sym-e16', (10, 42), ((9.975, 41.992), (10.025, 42), (10, 42)))
        self.add_bezier('sym-e17', (10, 42), ((8.298, 42), (6, 39.685), (6, 38)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')

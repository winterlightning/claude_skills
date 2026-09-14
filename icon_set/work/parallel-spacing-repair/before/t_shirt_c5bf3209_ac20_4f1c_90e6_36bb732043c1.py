"""T shirt (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5bf3209-ac20-4f1c-90e6-36bb732043c1'
SOURCE_PATH = 'icons-json/clothes/t shirt_c5bf3209-ac20-4f1c-90e6-36bb732043c1.json'
AUTHOR = 'json_to_solo'

class TShirtC5bf3209(Solo48):
    icon_id = 't-shirt-c5bf3209'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        self.add_arc('sym-e0', (24, 11), (18, 6), radius_x=6)
        self.add_line('sym-e1', (18, 6), (13, 6))
        self.add_arc('sym-e3', (13, 6), (6, 11), radius_x=8, sweep=False)
        self.add_line('sym-e4', (6, 11), (6, 13))
        self.add_line('sym-e5', (6, 13), (6, 24))
        self.add_arc('sym-e6', (6, 24), (13, 25), radius_x=32, sweep=False)
        self.add_line('sym-e7', (13, 25), (13, 40))
        self.add_line('sym-e8', (13, 40), (15, 42))
        self.add_line('sym-e9', (15, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (33, 42))
        self.add_line('sym-e11', (33, 42), (35, 40))
        self.add_line('sym-e12', (35, 40), (35, 25))
        self.add_arc('sym-e13', (35, 25), (42, 24), radius_x=32, sweep=False)
        self.add_line('sym-e14', (42, 24), (42, 13))
        self.add_line('sym-e15', (42, 13), (42, 11))
        self.add_arc('sym-e16', (42, 11), (35, 6), radius_x=8, sweep=False)
        self.add_line('sym-e18', (35, 6), (30, 6))
        self.add_arc('sym-e19', (30, 6), (24, 11), radius_x=6)
        self.add_line('sym-e20', (13, 25), (13, 19))
        self.add_line('sym-e21', (35, 25), (35, 19))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c1', 'sym-e20')
        self.add_contour('sym-c2', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')

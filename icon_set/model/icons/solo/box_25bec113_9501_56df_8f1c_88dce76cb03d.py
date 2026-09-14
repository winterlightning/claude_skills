"""Box (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25bec113-9501-56df-8f1c-88dce76cb03d'
SOURCE_PATH = 'icons-json/shipping/box_25bec113-9501-56df-8f1c-88dce76cb03d.json'
AUTHOR = 'json_to_solo'

class Box25bec113(Solo48):
    icon_id = 'box-25bec113'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping')

    def build(self):
        self.add_line('sym-e0', (29, 6), (29, 16))
        self.add_line('sym-e1', (29, 16), (19, 16))
        self.add_line('sym-e2', (19, 16), (19, 6))
        self.add_line('sym-e3', (19, 6), (11, 6))
        self.add_line('sym-e5', (11, 6), (10, 6))
        self.add_arc('sym-e6', (10, 6), (6, 10), radius_x=4, sweep=False)
        self.add_line('sym-e8', (6, 10), (6, 37))
        self.add_line('sym-e9', (6, 37), (6, 38))
        self.add_line('sym-e10', (6, 38), (6, 39))
        self.add_arc('sym-e11', (6, 39), (9, 42), radius_x=3, sweep=False)
        self.add_arc('sym-e12', (9, 42), (10, 42), radius_x=1)
        self.add_line('sym-e13', (10, 42), (24, 42))
        self.add_line('sym-e14', (24, 42), (38, 42))
        self.add_line('sym-e15', (38, 42), (39, 42))
        self.add_arc('sym-e16', (39, 42), (42, 39), radius_x=3, sweep=False)
        self.add_line('sym-e17', (42, 39), (42, 38))
        self.add_arc('sym-e18', (42, 38), (42, 37), radius_x=38)
        self.add_line('sym-e19', (42, 37), (42, 10))
        self.add_arc('sym-e21', (42, 10), (38, 6), radius_x=4, sweep=False)
        self.add_line('sym-e22', (38, 6), (37, 6))
        self.add_line('sym-e24', (37, 6), (29, 6))
        self.add_line('sym-e25', (29, 6), (24, 6))
        self.add_line('sym-e26', (24, 6), (19, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e26')

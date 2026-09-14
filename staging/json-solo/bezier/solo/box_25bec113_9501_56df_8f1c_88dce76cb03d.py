"""Box (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25bec113-9501-56df-8f1c-88dce76cb03d'
SOURCE_PATH = 'icons-json/shipping/box_25bec113-9501-56df-8f1c-88dce76cb03d.json'
AUTHOR = 'json_to_solo'

class Box(Solo48):
    icon_id = 'box'
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
        self.add_bezier('sym-e4', (11, 6), ((10.918, 6), (11.082, 6), (11, 6)))
        self.add_bezier('sym-e5', (11, 6), ((10.779, 6), (10.221, 6), (10, 6)))
        self.add_bezier('sym-e6', (10, 6), ((8.028, 6), (6, 7.889), (6, 10)))
        self.add_bezier('sym-e7', (6, 10), ((6, 10.147), (6, 9.853), (6, 10)))
        self.add_line('sym-e8', (6, 10), (6, 37))
        self.add_bezier('sym-e9', (6, 37), ((6, 37.221), (6, 37.779), (6, 38)))
        self.add_bezier('sym-e10', (6, 38), ((6, 38.295), (6, 38.705), (6, 39)))
        self.add_bezier('sym-e11', (6, 39), ((6, 40.833), (7.184, 42), (9, 42)))
        self.add_bezier('sym-e12', (9, 42), ((9.229, 42), (9.779, 42), (10, 42)))
        self.add_line('sym-e13', (10, 42), (24, 42))
        self.add_line('sym-e14', (24, 42), (38, 42))
        self.add_bezier('sym-e15', (38, 42), ((38.221, 42), (38.771, 42), (39, 42)))
        self.add_bezier('sym-e16', (39, 42), ((40.816, 42), (42, 40.833), (42, 39)))
        self.add_bezier('sym-e17', (42, 39), ((42, 38.705), (42, 38.295), (42, 38)))
        self.add_bezier('sym-e18', (42, 38), ((42, 37.779), (42, 37.221), (42, 37)))
        self.add_line('sym-e19', (42, 37), (42, 10))
        self.add_bezier('sym-e20', (42, 10), ((42, 9.853), (42, 10.147), (42, 10)))
        self.add_bezier('sym-e21', (42, 10), ((42, 7.889), (39.972, 6), (38, 6)))
        self.add_bezier('sym-e22', (38, 6), ((37.779, 6), (37.221, 6), (37, 6)))
        self.add_bezier('sym-e23', (37, 6), ((36.918, 6), (37.082, 6), (37, 6)))
        self.add_line('sym-e24', (37, 6), (29, 6))
        self.add_line('sym-e25', (29, 6), (24, 6))
        self.add_line('sym-e26', (24, 6), (19, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')

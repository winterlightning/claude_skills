"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1fb9650-ac29-44c4-bc7c-62fe2b8946d1'
SOURCE_PATH = 'icons-json/entertainment/dice_b1fb9650-ac29-44c4-bc7c-62fe2b8946d1.json'
AUTHOR = 'json_to_solo'

class Dice(Solo48):
    icon_id = 'dice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_line('sym-e1', (6, 24), (6, 11))
        self.add_bezier('sym-e2', (6, 11), ((6, 10.869), (6, 11.123), (6, 11)))
        self.add_bezier('sym-e3', (6, 11), ((6, 8.717), (8.717, 6), (11, 6)))
        self.add_bezier('sym-e4', (11, 6), ((11.123, 6), (10.869, 6), (11, 6)))
        self.add_line('sym-e5', (11, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (37, 6))
        self.add_bezier('sym-e7', (37, 6), ((37.131, 6), (36.877, 6), (37, 6)))
        self.add_bezier('sym-e8', (37, 6), ((39.283, 6), (42, 8.717), (42, 11)))
        self.add_bezier('sym-e9', (42, 11), ((42, 11.123), (42, 10.869), (42, 11)))
        self.add_line('sym-e10', (42, 11), (42, 24))
        self.add_line('sym-e11', (42, 24), (42, 37))
        self.add_bezier('sym-e12', (42, 37), ((42, 37.131), (42, 36.877), (42, 37)))
        self.add_bezier('sym-e13', (42, 37), ((42, 39.283), (39.283, 42), (37, 42)))
        self.add_bezier('sym-e14', (37, 42), ((36.877, 42), (37.131, 42), (37, 42)))
        self.add_line('sym-e15', (37, 42), (24, 42))
        self.add_line('sym-e16', (24, 42), (11, 42))
        self.add_bezier('sym-e17', (11, 42), ((10.869, 42), (11.123, 42), (11, 42)))
        self.add_bezier('sym-e18', (11, 42), ((8.717, 42), (6, 39.283), (6, 37)))
        self.add_bezier('sym-e19', (6, 37), ((6, 36.877), (6, 37.131), (6, 37)))
        self.add_line('sym-e20', (6, 37), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', closed=True)

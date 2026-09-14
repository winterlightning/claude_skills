"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a9164c0-da9e-5daf-ab67-2a9588ba7d68'
SOURCE_PATH = 'icons-json/entertainment/dice_2a9164c0-da9e-5daf-ab67-2a9588ba7d68.json'
AUTHOR = 'json_to_solo'

class Dice2a9164c0(Solo48):
    icon_id = 'dice-2a9164c0'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self):
        self.add_arc('sym-e0', (20, 24), (28, 24), radius_x=4)
        self.add_arc('sym-e1', (28, 24), (20, 24), radius_x=4)
        self.add_bezier('sym-e2', (12, 6), ((11.935, 6), (12.065, 6), (12, 6)))
        self.add_bezier('sym-e3', (12, 6), ((9.3, 6), (6.573, 8.48), (6, 11)))
        self.add_bezier('sym-e4', (6, 11), ((6, 11.365), (6, 11.601), (6, 12)))
        self.add_bezier('sym-e5', (6, 12), ((6, 12.281), (6, 12.739), (6, 13)))
        self.add_bezier('sym-e6', (6, 13), ((6, 13.344), (6, 13.648), (6, 14)))
        self.add_bezier('sym-e7', (6, 14), ((6, 14.131), (6, 13.861), (6, 14)))
        self.add_line('sym-e8', (6, 14), (6, 35))
        self.add_bezier('sym-e9', (6, 35), ((6, 35.164), (6, 35.836), (6, 36)))
        self.add_bezier('sym-e10', (6, 36), ((6, 38.635), (7.374, 41.215), (10, 42)))
        self.add_bezier('sym-e11', (10, 42), ((10.671, 42), (11.313, 42), (12, 42)))
        self.add_bezier('sym-e12', (12, 42), ((12.245, 42), (12.763, 42), (13, 42)))
        self.add_bezier('sym-e13', (13, 42), ((13.139, 42), (12.861, 42), (13, 42)))
        self.add_line('sym-e14', (13, 42), (24, 42))
        self.add_line('sym-e15', (24, 42), (35, 42))
        self.add_bezier('sym-e16', (35, 42), ((35.139, 42), (34.861, 42), (35, 42)))
        self.add_bezier('sym-e17', (35, 42), ((35.237, 42), (35.755, 42), (36, 42)))
        self.add_bezier('sym-e18', (36, 42), ((36.687, 42), (37.329, 42), (38, 42)))
        self.add_bezier('sym-e19', (38, 42), ((40.626, 41.215), (42, 38.635), (42, 36)))
        self.add_bezier('sym-e20', (42, 36), ((42, 35.836), (42, 35.164), (42, 35)))
        self.add_line('sym-e21', (42, 35), (42, 14))
        self.add_bezier('sym-e22', (42, 14), ((42, 13.861), (42, 14.131), (42, 14)))
        self.add_bezier('sym-e23', (42, 14), ((42, 13.648), (42, 13.344), (42, 13)))
        self.add_bezier('sym-e24', (42, 13), ((42, 12.739), (42, 12.281), (42, 12)))
        self.add_bezier('sym-e25', (42, 12), ((42, 11.601), (42, 11.365), (42, 11)))
        self.add_bezier('sym-e26', (42, 11), ((41.427, 8.48), (38.7, 6), (36, 6)))
        self.add_bezier('sym-e27', (36, 6), ((35.935, 6), (36.065, 6), (36, 6)))
        self.add_line('sym-e28', (36, 6), (24, 6))
        self.add_line('sym-e29', (24, 6), (12, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', closed=True)

"""Fork (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0d4755a-cca4-5ee7-aa11-660d6df57a19'
SOURCE_PATH = 'icons-json/food/fork_a0d4755a-cca4-5ee7-aa11-660d6df57a19.json'
AUTHOR = 'json_to_solo'

class ForkFood(Solo48):
    icon_id = 'fork-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('fork', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 21))
        self.add_line('sym-e1', (24, 21), (24, 44))
        self.add_bezier('sym-e2', (24, 21), ((22.744, 21), (21.35, 21), (20, 21)))
        self.add_bezier('sym-e3', (20, 21), ((19.007, 21), (17.907, 21.096), (17, 21)))
        self.add_bezier('sym-e4', (17, 21), ((12.14, 20.5), (8, 18.382), (8, 16)))
        self.add_bezier('sym-e5', (8, 16), ((8, 15.782), (8, 16.218), (8, 16)))
        self.add_line('sym-e6', (8, 16), (8, 4))
        self.add_bezier('sym-e7', (24, 21), ((25.256, 21), (26.65, 21), (28, 21)))
        self.add_bezier('sym-e8', (28, 21), ((28.993, 21), (30.093, 21.096), (31, 21)))
        self.add_bezier('sym-e9', (31, 21), ((35.86, 20.5), (40, 18.382), (40, 16)))
        self.add_bezier('sym-e10', (40, 16), ((40, 15.782), (40, 16.218), (40, 16)))
        self.add_line('sym-e11', (40, 16), (40, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')

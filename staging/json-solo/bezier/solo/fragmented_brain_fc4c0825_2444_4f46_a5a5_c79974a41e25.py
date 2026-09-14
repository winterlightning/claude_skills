"""Fragmented brain (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc4c0825-2444-4f46-a5a5-c79974a41e25'
SOURCE_PATH = 'icons-json/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.json'
AUTHOR = 'json_to_solo'

class FragmentedBrainSymbol(Solo48):
    icon_id = 'fragmented-brain-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fragmented', 'brain', 'symbol')

    def build(self):
        self.add_line('e0', (13, 39), (26, 22))
        self.add_line('e1', (13, 39), (36, 26))
        self.add_line('e2', (9, 19), (26, 22))
        self.add_line('e3', (26, 22), (38, 10))
        self.add_line('e4', (26, 22), (36, 26))
        self.add_line('e5', (36, 26), (40, 24))
        self.add_bezier('e6', (13, 39), ((12.4, 39.32), (9.845, 39.975), (9.236, 39.975)), ((9.111, 39.988), (8.986, 40), (8.852, 40)), ((8.85, 40), (8.848, 40), (8.845, 40)), ((8.727, 39.988), (8.6, 39.988), (8.473, 39.975)), ((6.409, 39.975), (4.009, 37.551), (4.009, 34.622)), ((4.009, 34.464), (4, 34.318), (4, 34.161)), ((4, 34.159), (4, 34.156), (4, 34.154)), ((4, 33.982), (4.009, 33.822), (4.009, 33.662)), ((4.009, 28.542), (6.445, 22.52), (9, 19)))
        self.add_bezier('e7', (9, 19), ((13.909, 12.797), (21.336, 8.012), (28.191, 8.012)), ((28.397, 8.012), (28.611, 8), (28.826, 8)), ((28.83, 8), (28.833, 8), (28.836, 8)), ((29.191, 8), (29.555, 8.025), (29.909, 8.025)), ((32.564, 8.025), (35.582, 8.609), (38, 10)))
        self.add_bezier('e8', (40, 24), ((41.664, 23.102), (43.982, 21.502), (43.982, 18.708)), ((43.982, 18.56), (44, 18.412), (44, 18.265)), ((44, 18.262), (44, 18.26), (44, 18.258)), ((44, 18.112), (43.982, 17.967), (43.982, 17.809)), ((43.982, 13.92), (40.073, 11.292), (38, 10)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e2')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e4')
        self.add_contour('c7', 'e5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c5', 'c7')

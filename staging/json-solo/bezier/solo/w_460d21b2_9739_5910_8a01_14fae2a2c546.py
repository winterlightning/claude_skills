"""W (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '460d21b2-9739-5910-8a01-14fae2a2c546'
SOURCE_PATH = 'icons-json/typeface/W_460d21b2-9739-5910-8a01-14fae2a2c546.json'
AUTHOR = 'json_to_solo'

class W460d21b2(Solo48):
    icon_id = 'w-460d21b2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('w', 'typeface')

    def build(self):
        self.add_line('sym-e0', (42, 6), (35, 39))
        self.add_bezier('sym-e1', (35, 39), ((34.812, 39.925), (34.26, 42), (33, 42)))
        self.add_bezier('sym-e2', (33, 42), ((32.935, 42), (33.057, 42), (33, 42)))
        self.add_bezier('sym-e3', (33, 42), ((32.943, 41.992), (33.057, 42), (33, 42)))
        self.add_bezier('sym-e4', (33, 42), ((31.167, 42), (31.262, 38.203), (31, 37)))
        self.add_line('sym-e5', (31, 37), (26, 14))
        self.add_bezier('sym-e6', (26, 14), ((25.894, 13.845), (25.123, 14.155), (25, 14)))
        self.add_bezier('sym-e7', (25, 14), ((24.663, 13.59), (24.482, 12.847), (24, 13)))
        self.add_bezier('sym-e8', (24, 13), ((23.518, 12.847), (23.337, 13.59), (23, 14)))
        self.add_bezier('sym-e9', (23, 14), ((22.877, 14.155), (22.106, 13.845), (22, 14)))
        self.add_line('sym-e10', (22, 14), (17, 37))
        self.add_bezier('sym-e11', (17, 37), ((16.738, 38.203), (16.833, 42), (15, 42)))
        self.add_bezier('sym-e12', (15, 42), ((14.943, 42), (15.057, 41.992), (15, 42)))
        self.add_bezier('sym-e13', (15, 42), ((14.943, 42), (15.065, 42), (15, 42)))
        self.add_bezier('sym-e14', (15, 42), ((13.74, 42), (13.188, 39.925), (13, 39)))
        self.add_line('sym-e15', (13, 39), (6, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')

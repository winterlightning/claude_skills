"""Batch-02/hat sombrero (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c8abf37-4cc4-54b0-8d99-9072a76c457d'
SOURCE_PATH = 'icons-json/accessories/batch-02/hat sombrero_1c8abf37-4cc4-54b0-8d99-9072a76c457d.json'
AUTHOR = 'json_to_solo'

class Batch02HatSombrero(Solo48):
    icon_id = 'batch-02-hat-sombrero'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'sombrero', 'accessories')

    def build(self):
        self.add_bezier('sym-e0', (24, 8), ((23.991, 8), (24.009, 8), (24, 8)))
        self.add_bezier('sym-e1', (24, 8), ((20.2, 8), (18.673, 14.877), (18, 19)))
        self.add_line('sym-e2', (18, 19), (16, 30))
        self.add_line('sym-e3', (16, 30), (6, 30))
        self.add_bezier('sym-e4', (6, 30), ((5.427, 30.332), (4, 30.905), (4, 32)))
        self.add_bezier('sym-e5', (4, 32), ((4, 33.009), (4.627, 34.249), (5, 35)))
        self.add_bezier('sym-e6', (5, 35), ((5.191, 35.369), (5.809, 35.643), (6, 36)))
        self.add_bezier('sym-e7', (6, 36), ((7.745, 39.298), (11.173, 40), (14, 40)))
        self.add_bezier('sym-e8', (14, 40), ((14.109, 40), (13.882, 40), (14, 40)))
        self.add_line('sym-e9', (14, 40), (24, 40))
        self.add_line('sym-e10', (24, 40), (34, 40))
        self.add_bezier('sym-e11', (34, 40), ((34.118, 40), (33.891, 40), (34, 40)))
        self.add_bezier('sym-e12', (34, 40), ((36.827, 40), (40.255, 39.298), (42, 36)))
        self.add_bezier('sym-e13', (42, 36), ((42.191, 35.643), (42.809, 35.369), (43, 35)))
        self.add_bezier('sym-e14', (43, 35), ((43.373, 34.249), (44, 33.009), (44, 32)))
        self.add_bezier('sym-e15', (44, 32), ((44, 30.905), (42.573, 30.332), (42, 30)))
        self.add_line('sym-e16', (42, 30), (32, 30))
        self.add_line('sym-e17', (32, 30), (30, 19))
        self.add_bezier('sym-e18', (30, 19), ((29.327, 14.877), (27.8, 8), (24, 8)))
        self.add_bezier('sym-e19', (24, 8), ((23.991, 8), (24.009, 8), (24, 8)))
        self.add_line('sym-e20', (16, 30), (24, 30))
        self.add_line('sym-e21', (24, 30), (32, 30))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c1', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')

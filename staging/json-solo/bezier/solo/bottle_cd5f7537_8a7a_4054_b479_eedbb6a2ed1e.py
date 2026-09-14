"""Batch-01/bottle (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd5f7537-8a7a-4054-b479-eedbb6a2ed1e'
SOURCE_PATH = 'icons-json/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.json'
AUTHOR = 'json_to_solo'

class Batch01BottleDecoration(Solo48):
    icon_id = 'batch-01-bottle-decoration'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'bottle', 'decoration')

    def build(self):
        self.add_line('sym-e0', (35, 5), (35, 7))
        self.add_bezier('sym-e1', (35, 7), ((33.97, 7.873), (32.92, 8.018), (32, 9)))
        self.add_bezier('sym-e2', (32, 9), ((29.97, 11.155), (28.98, 15.555), (31, 18)))
        self.add_line('sym-e3', (31, 18), (37, 25))
        self.add_bezier('sym-e4', (37, 25), ((38.5, 26.818), (40, 29.7), (40, 32)))
        self.add_bezier('sym-e5', (40, 32), ((40, 32.182), (40, 32.818), (40, 33)))
        self.add_bezier('sym-e6', (40, 33), ((40, 33.327), (40, 33.673), (40, 34)))
        self.add_bezier('sym-e7', (40, 34), ((40, 38.264), (36.4, 42.636), (32, 44)))
        self.add_bezier('sym-e8', (32, 44), ((31.29, 44), (30.75, 44), (30, 44)))
        self.add_line('sym-e9', (30, 44), (24, 44))
        self.add_line('sym-e10', (24, 44), (18, 44))
        self.add_bezier('sym-e11', (18, 44), ((17.25, 44), (16.71, 44), (16, 44)))
        self.add_bezier('sym-e12', (16, 44), ((11.6, 42.636), (8, 38.264), (8, 34)))
        self.add_bezier('sym-e13', (8, 34), ((8, 33.673), (8, 33.327), (8, 33)))
        self.add_bezier('sym-e14', (8, 33), ((8, 32.818), (8, 32.182), (8, 32)))
        self.add_bezier('sym-e15', (8, 32), ((8, 29.7), (9.5, 26.818), (11, 25)))
        self.add_line('sym-e16', (11, 25), (17, 18))
        self.add_bezier('sym-e17', (17, 18), ((19.02, 15.555), (18.03, 11.155), (16, 9)))
        self.add_bezier('sym-e18', (16, 9), ((15.08, 8.018), (14.03, 7.873), (13, 7)))
        self.add_line('sym-e19', (13, 7), (13, 5))
        self.add_bezier('sym-e20', (13, 5), ((13.45, 4.555), (13.64, 4.327), (14, 4)))
        self.add_line('sym-e21', (14, 4), (24, 4))
        self.add_line('sym-e22', (24, 4), (34, 4))
        self.add_bezier('sym-e23', (34, 4), ((34.36, 4.327), (34.55, 4.555), (35, 5)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)

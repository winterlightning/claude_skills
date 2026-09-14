"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '489f79de-538e-42b6-b17b-4132665a5a1b'
SOURCE_PATH = 'icons-json/shopping/barcode_489f79de-538e-42b6-b17b-4132665a5a1b.json'
AUTHOR = 'json_to_solo'

class Barcode489f79de(Solo48):
    icon_id = 'barcode-489f79de'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self):
        self.add_line('sym-e0', (29, 32), (29, 16))
        self.add_line('sym-e1', (36, 32), (36, 16))
        self.add_line('sym-e2', (44, 13), (44, 35))
        self.add_bezier('sym-e3', (44, 35), ((44, 35.126), (44, 34.874), (44, 35)))
        self.add_bezier('sym-e4', (44, 35), ((44, 37.324), (41.509, 40), (39, 40)))
        self.add_bezier('sym-e5', (39, 40), ((38.855, 40), (39.145, 40), (39, 40)))
        self.add_line('sym-e6', (39, 40), (24, 40))
        self.add_line('sym-e7', (24, 40), (9, 40))
        self.add_bezier('sym-e8', (9, 40), ((8.855, 40), (9.145, 40), (9, 40)))
        self.add_bezier('sym-e9', (9, 40), ((6.491, 40), (4, 37.324), (4, 35)))
        self.add_bezier('sym-e10', (4, 35), ((4, 34.874), (4, 35.126), (4, 35)))
        self.add_line('sym-e11', (4, 35), (4, 13))
        self.add_bezier('sym-e12', (4, 13), ((4, 12.874), (4, 13.126), (4, 13)))
        self.add_bezier('sym-e13', (4, 13), ((4, 10.676), (6.491, 8), (9, 8)))
        self.add_bezier('sym-e14', (9, 8), ((9.145, 8), (8.855, 8), (9, 8)))
        self.add_line('sym-e15', (9, 8), (24, 8))
        self.add_line('sym-e16', (24, 8), (39, 8))
        self.add_bezier('sym-e17', (39, 8), ((39.145, 8), (38.855, 8), (39, 8)))
        self.add_bezier('sym-e18', (39, 8), ((41.509, 8), (44, 10.676), (44, 13)))
        self.add_bezier('sym-e19', (44, 13), ((44, 13.126), (44, 12.874), (44, 13)))
        self.add_line('sym-e20', (19, 32), (19, 16))
        self.add_line('sym-e21', (12, 32), (12, 16))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c3', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e21')

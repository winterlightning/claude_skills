"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e4', (44, 35), (39, 40), radius_x=5)
        self.add_line('sym-e6', (39, 40), (24, 40))
        self.add_line('sym-e7', (24, 40), (9, 40))
        self.add_arc('sym-e9', (9, 40), (4, 35), radius_x=5)
        self.add_line('sym-e11', (4, 35), (4, 13))
        self.add_arc('sym-e13', (4, 13), (9, 8), radius_x=5)
        self.add_line('sym-e15', (9, 8), (24, 8))
        self.add_line('sym-e16', (24, 8), (39, 8))
        self.add_arc('sym-e18', (39, 8), (44, 13), radius_x=5)
        self.add_line('sym-e20', (19, 32), (19, 16))
        self.add_line('sym-e21', (12, 32), (12, 16))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e11', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', closed=True)
        self.add_contour('sym-c3', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e21')

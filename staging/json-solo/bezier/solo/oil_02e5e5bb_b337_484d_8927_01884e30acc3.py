"""Oil (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02e5e5bb-b337-484d-8927-01884e30acc3'
SOURCE_PATH = 'icons-json/_uncategorized_29/oil_02e5e5bb-b337-484d-8927-01884e30acc3.json'
AUTHOR = 'json_to_solo'

class OilUncategorized(Solo48):
    icon_id = 'oil-uncategorized'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('oil', '_uncategorized')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.214, 43.997), (24.789, 44), (25, 44)))
        self.add_bezier('sym-e1', (25, 44), ((32.97, 44), (40, 37.255), (40, 30)))
        self.add_bezier('sym-e2', (40, 30), ((40, 29.918), (40, 30.082), (40, 30)))
        self.add_bezier('sym-e3', (40, 30), ((40, 29.691), (40, 29.309), (40, 29)))
        self.add_bezier('sym-e4', (40, 29), ((40, 25.955), (38.67, 22.555), (37, 20)))
        self.add_bezier('sym-e5', (37, 20), ((34.48, 16.136), (31.03, 12.545), (28, 9)))
        self.add_bezier('sym-e6', (28, 9), ((26.87, 7.682), (26.16, 6.3), (25, 5)))
        self.add_bezier('sym-e7', (25, 5), ((24.786, 4.76), (24.272, 4.306), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((23.728, 4.306), (23.214, 4.76), (23, 5)))
        self.add_bezier('sym-e9', (23, 5), ((21.84, 6.3), (21.13, 7.682), (20, 9)))
        self.add_bezier('sym-e10', (20, 9), ((16.97, 12.545), (13.52, 16.136), (11, 20)))
        self.add_bezier('sym-e11', (11, 20), ((9.33, 22.555), (8, 25.955), (8, 29)))
        self.add_bezier('sym-e12', (8, 29), ((8, 29.309), (8, 29.691), (8, 30)))
        self.add_bezier('sym-e13', (8, 30), ((8, 30.082), (8, 29.918), (8, 30)))
        self.add_bezier('sym-e14', (8, 30), ((8, 37.255), (15.03, 44), (23, 44)))
        self.add_bezier('sym-e15', (23, 44), ((23.211, 44), (23.786, 43.997), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)

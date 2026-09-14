"""Metal sheet (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a05feef9-d6c1-4050-8014-feb049ba4197'
SOURCE_PATH = 'icons-json/construction/metal sheet_a05feef9-d6c1-4050-8014-feb049ba4197.json'
AUTHOR = 'json_to_solo'

class MetalSheetConstruction(Solo48):
    icon_id = 'metal-sheet-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('metal', 'sheet', 'construction')

    def build(self):
        self.add_line('e0', (4, 12), (4, 37))
        self.add_line('e1', (7, 40), (25, 40))
        self.add_line('e2', (29, 37), (29, 32))
        self.add_line('e3', (12, 8), (13, 10))
        self.add_line('e4', (15, 12), (15, 29))
        self.add_line('e5', (18, 32), (29, 32))
        self.add_line('e6', (12, 8), (41, 8))
        self.add_line('e7', (44, 11), (44, 31))
        self.add_line('e8', (42, 32), (29, 32))
        self.add_bezier('e9', (12, 8), ((11.409, 8), (10.991, 8.017), (10.4, 8.017)), ((10.227, 8.017), (10.045, 8), (9.873, 8)), ((9.591, 8), (9.3, 8.008), (9.009, 8.008)), ((6.818, 8.008), (4.009, 9.844), (4.009, 12.025)), ((4.009, 12.084), (4, 11.941), (4, 12)))
        self.add_bezier('e10', (4, 37), ((4.609, 38.659), (5.245, 39.427), (7, 40)))
        self.add_bezier('e11', (25, 40), ((25.073, 39.992), (25.045, 39.992), (25.118, 39.983)), ((26.591, 39.983), (29, 38.322), (29, 37)))
        self.add_bezier('e12', (13, 10), ((13.436, 10.413), (15, 11.402), (15, 12)))
        self.add_bezier('e13', (15, 29), ((15, 30.154), (16.509, 32), (18, 32)))
        self.add_bezier('e14', (41, 8), ((41.073, 8), (41.409, 8), (41.482, 8)), ((42.427, 8), (43.982, 9.465), (43.982, 10.333)), ((43.991, 10.4), (43.991, 10.933), (44, 11)))
        self.add_bezier('e15', (44, 31), ((43.927, 31.143), (43.964, 31.048), (43.891, 31.2)), ((43.591, 31.882), (42.655, 31.714), (42, 32)))
        self.add_contour('c0', 'e9', 'e0', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c1', 'e3', 'e12', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

"""Warp arch (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdc7edeb-0efe-4644-960d-7671381627e9'
SOURCE_PATH = 'icons-json/design/warp arch_bdc7edeb-0efe-4644-960d-7671381627e9.json'
AUTHOR = 'json_to_solo'

class WarpArchDesign(Solo48):
    icon_id = 'warp-arch-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arch', 'design')

    def build(self):
        self.add_bezier('sym-e0', (4, 29), ((6.445, 26.69), (9.045, 24.51), (12, 23)))
        self.add_bezier('sym-e1', (12, 23), ((15.8, 21.064), (19.823, 20), (24, 20)))
        self.add_bezier('sym-e2', (24, 20), ((28.177, 20), (32.2, 21.064), (36, 23)))
        self.add_bezier('sym-e3', (36, 23), ((38.955, 24.51), (41.555, 26.69), (44, 29)))
        self.add_line('sym-e4', (44, 29), (44, 40))
        self.add_bezier('sym-e5', (44, 40), ((41.145, 37.65), (38.318, 35.49), (35, 34)))
        self.add_bezier('sym-e6', (35, 34), ((31.479, 32.416), (27.79, 32), (24, 32)))
        self.add_bezier('sym-e7', (24, 32), ((20.21, 32), (16.521, 32.416), (13, 34)))
        self.add_bezier('sym-e8', (13, 34), ((9.682, 35.49), (6.855, 37.65), (4, 40)))
        self.add_line('sym-e9', (4, 40), (4, 29))
        self.add_line('sym-e10', (4, 29), (4, 16))
        self.add_bezier('sym-e11', (4, 16), ((4.155, 15.84), (4, 16.14), (4, 16)))
        self.add_bezier('sym-e12', (4, 16), ((4.291, 15.7), (4.673, 15.28), (5, 15)))
        self.add_bezier('sym-e13', (5, 15), ((9.727, 10.93), (16.973, 8), (23, 8)))
        self.add_bezier('sym-e14', (23, 8), ((23.282, 8), (23.718, 8), (24, 8)))
        self.add_bezier('sym-e15', (24, 8), ((24.094, 8), (23.906, 8), (24, 8)))
        self.add_bezier('sym-e16', (24, 8), ((24.094, 8), (23.906, 8), (24, 8)))
        self.add_bezier('sym-e17', (24, 8), ((24.282, 8), (24.718, 8), (25, 8)))
        self.add_bezier('sym-e18', (25, 8), ((31.027, 8), (38.273, 10.93), (43, 15)))
        self.add_bezier('sym-e19', (43, 15), ((43.327, 15.28), (43.709, 15.7), (44, 16)))
        self.add_bezier('sym-e20', (44, 16), ((44, 16.14), (43.845, 15.84), (44, 16)))
        self.add_line('sym-e21', (44, 16), (44, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')

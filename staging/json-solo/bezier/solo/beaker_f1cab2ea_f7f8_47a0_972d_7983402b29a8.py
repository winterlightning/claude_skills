"""Beaker (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1cab2ea-f7f8-47a0-972d-7983402b29a8'
SOURCE_PATH = 'icons-json/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.json'
AUTHOR = 'json_to_solo'

class BeakerSymbol(Solo48):
    icon_id = 'beaker-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('beaker', 'symbol')

    def build(self):
        self.add_line('sym-e0', (15, 4), (19, 4))
        self.add_line('sym-e1', (19, 4), (29, 4))
        self.add_line('sym-e2', (29, 4), (33, 4))
        self.add_line('sym-e3', (19, 4), (19, 12))
        self.add_bezier('sym-e4', (19, 12), ((18.966, 12.073), (19.034, 11.927), (19, 12)))
        self.add_bezier('sym-e5', (19, 12), ((18.545, 12.309), (17.505, 12.791), (17, 13)))
        self.add_bezier('sym-e6', (17, 13), ((15.998, 13.418), (14.876, 14.345), (14, 15)))
        self.add_bezier('sym-e7', (14, 15), ((10.497, 17.627), (8, 22.282), (8, 27)))
        self.add_bezier('sym-e8', (8, 27), ((8, 27.173), (8, 26.827), (8, 27)))
        self.add_bezier('sym-e9', (8, 27), ((8, 27.409), (8, 27.591), (8, 28)))
        self.add_bezier('sym-e10', (8, 28), ((8, 29.282), (8.638, 30.791), (9, 32)))
        self.add_bezier('sym-e11', (9, 32), ((11.021, 38.727), (16.373, 44), (23, 44)))
        self.add_bezier('sym-e12', (23, 44), ((23.067, 44), (23.933, 44), (24, 44)))
        self.add_bezier('sym-e13', (24, 44), ((24.089, 44), (23.91, 44), (24, 44)))
        self.add_bezier('sym-e14', (24, 44), ((24.045, 44), (23.955, 44), (24, 44)))
        self.add_bezier('sym-e15', (24, 44), ((24.045, 44), (23.955, 44), (24, 44)))
        self.add_bezier('sym-e16', (24, 44), ((24.09, 44), (23.911, 44), (24, 44)))
        self.add_bezier('sym-e17', (24, 44), ((24.067, 44), (24.933, 44), (25, 44)))
        self.add_bezier('sym-e18', (25, 44), ((31.627, 44), (36.979, 38.727), (39, 32)))
        self.add_bezier('sym-e19', (39, 32), ((39.362, 30.791), (40, 29.282), (40, 28)))
        self.add_bezier('sym-e20', (40, 28), ((40, 27.591), (40, 27.409), (40, 27)))
        self.add_bezier('sym-e21', (40, 27), ((40, 26.827), (40, 27.173), (40, 27)))
        self.add_bezier('sym-e22', (40, 27), ((40, 22.282), (37.503, 17.627), (34, 15)))
        self.add_bezier('sym-e23', (34, 15), ((33.124, 14.345), (32.002, 13.418), (31, 13)))
        self.add_bezier('sym-e24', (31, 13), ((30.495, 12.791), (29.455, 12.309), (29, 12)))
        self.add_bezier('sym-e25', (29, 12), ((28.966, 11.927), (29.034, 12.073), (29, 12)))
        self.add_line('sym-e26', (29, 12), (29, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')

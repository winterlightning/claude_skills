"""Warp shell lower (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f312c0ee-793a-5fce-9b43-3724f5d94d76'
SOURCE_PATH = 'icons-json/design/warp shell lower_f312c0ee-793a-5fce-9b43-3724f5d94d76.json'
AUTHOR = 'json_to_solo'

class WarpShellLowerDesign(Solo48):
    icon_id = 'warp-shell-lower-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'shell', 'lower', 'design')

    def build(self):
        self.add_bezier('sym-e0', (44, 21), ((39.882, 20.84), (36.227, 20.587), (34, 17)))
        self.add_bezier('sym-e1', (34, 17), ((33.491, 16.183), (33, 14.943), (33, 14)))
        self.add_line('sym-e2', (33, 14), (33, 8))
        self.add_line('sym-e3', (33, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (15, 8))
        self.add_line('sym-e5', (15, 8), (15, 14))
        self.add_bezier('sym-e6', (15, 14), ((15, 14.943), (14.509, 16.183), (14, 17)))
        self.add_bezier('sym-e7', (14, 17), ((11.773, 20.587), (8.118, 20.84), (4, 21)))
        self.add_bezier('sym-e8', (4, 21), ((4, 21.733), (4, 23.267), (4, 24)))
        self.add_bezier('sym-e9', (4, 24), ((4, 25.322), (4.573, 26.745), (5, 28)))
        self.add_bezier('sym-e10', (5, 28), ((7.418, 35.091), (14.927, 40), (23, 40)))
        self.add_bezier('sym-e11', (23, 40), ((23.282, 40), (23.718, 40), (24, 40)))
        self.add_bezier('sym-e12', (24, 40), ((24.006, 40), (23.994, 40), (24, 40)))
        self.add_bezier('sym-e13', (24, 40), ((24.006, 40), (23.994, 40), (24, 40)))
        self.add_bezier('sym-e14', (24, 40), ((24.282, 40), (24.718, 40), (25, 40)))
        self.add_bezier('sym-e15', (25, 40), ((33.073, 40), (40.582, 35.091), (43, 28)))
        self.add_bezier('sym-e16', (43, 28), ((43.427, 26.745), (44, 25.322), (44, 24)))
        self.add_bezier('sym-e17', (44, 24), ((44, 23.267), (44, 21.733), (44, 21)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)

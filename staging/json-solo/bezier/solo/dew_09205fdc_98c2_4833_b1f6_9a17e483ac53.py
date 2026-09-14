"""Dew (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09205fdc-98c2-4833-b1f6-9a17e483ac53'
SOURCE_PATH = 'icons-json/_uncategorized_14/dew_09205fdc-98c2-4833-b1f6-9a17e483ac53.json'
AUTHOR = 'json_to_solo'

class DewUncategorized(Solo48):
    icon_id = 'dew-uncategorized'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('dew', '_uncategorized')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.247, 43.997), (24.756, 44), (25, 44)))
        self.add_bezier('sym-e1', (25, 44), ((32.69, 44), (40, 38.182), (40, 31)))
        self.add_bezier('sym-e2', (40, 31), ((40, 30.927), (40, 31.073), (40, 31)))
        self.add_bezier('sym-e3', (40, 31), ((40, 30.736), (40, 30.264), (40, 30)))
        self.add_bezier('sym-e4', (40, 30), ((40, 23.809), (32.89, 14.809), (29, 10)))
        self.add_bezier('sym-e5', (29, 10), ((27.79, 8.509), (26.12, 6.545), (25, 5)))
        self.add_bezier('sym-e6', (25, 5), ((24.779, 4.692), (24.268, 4.284), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((23.732, 4.284), (23.221, 4.692), (23, 5)))
        self.add_bezier('sym-e8', (23, 5), ((21.88, 6.545), (20.21, 8.509), (19, 10)))
        self.add_bezier('sym-e9', (19, 10), ((15.11, 14.809), (8, 23.809), (8, 30)))
        self.add_bezier('sym-e10', (8, 30), ((8, 30.264), (8, 30.736), (8, 31)))
        self.add_bezier('sym-e11', (8, 31), ((8, 31.073), (8, 30.927), (8, 31)))
        self.add_bezier('sym-e12', (8, 31), ((8, 38.182), (15.31, 44), (23, 44)))
        self.add_bezier('sym-e13', (23, 44), ((23.244, 44), (23.753, 43.997), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)

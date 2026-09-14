"""Crossed arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbeb6dcd-ae52-4f65-a738-3e8d379b4665'
SOURCE_PATH = 'icons-json/symbol/crossed arrow_fbeb6dcd-ae52-4f65-a738-3e8d379b4665.json'
AUTHOR = 'json_to_solo'

class CrossedArrowSymbol(Solo48):
    icon_id = 'crossed-arrow-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('crossed', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (15, 33), (34, 13))
        self.add_line('e1', (33, 33), (14, 13))
        self.add_line('e2', (37, 32), (33, 33))
        self.add_line('e3', (29, 8), (42, 6))
        self.add_line('e4', (42, 6), (40, 18))
        self.add_line('e5', (40, 18), (29, 8))
        self.add_line('e6', (19, 8), (6, 6))
        self.add_line('e7', (6, 6), (8, 18))
        self.add_line('e8', (19, 8), (8, 18))
        self.add_bezier('e9', (6, 37), ((6.016, 36.869), (6.033, 36.829), (6.049, 36.698)), ((6.205, 36.346), (6.802, 35.823), (7.072, 35.405)), ((7.489, 34.743), (7.923, 33.72), (8.561, 33.213)), ((8.839, 32.992), (9.175, 32.787), (9.51, 32.697)), ((9.935, 32.583), (10.516, 32.697), (10.942, 32.722)), ((12.3, 32.795), (13.65, 32.902), (15, 33)))
        self.add_bezier('e10', (11, 42), ((11.082, 41.975), (11.065, 41.951), (11.146, 41.918)), ((11.228, 41.902), (11.302, 41.885), (11.375, 41.861)), ((11.449, 41.828), (11.744, 41.534), (11.809, 41.485)), ((12.881, 40.666), (14.615, 40.094), (15.262, 38.809)), ((15.908, 37.525), (15.164, 34.358), (15, 33)))
        self.add_bezier('e11', (36, 42), ((34.454, 40.977), (32.583, 39.807), (32.231, 37.803)), ((32.051, 36.764), (32.804, 34.031), (33, 33)))
        self.add_bezier('e12', (42, 36), ((41.935, 35.894), (41.902, 35.847), (41.82, 35.749)), ((41.673, 35.569), (41.444, 35.463), (41.296, 35.283)), ((39.848, 33.605), (39.315, 32.442), (37, 32)))
        self.add_contour('c0', 'e9', 'e0')
        self.add_contour('c1', 'e10')
        self.add_contour('c2', 'e11', 'e1')
        self.add_contour('c3', 'e12', 'e2')
        self.add_contour('c4', 'e3', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e7')
        self.add_contour('c7', 'e8')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c2', 'c7')

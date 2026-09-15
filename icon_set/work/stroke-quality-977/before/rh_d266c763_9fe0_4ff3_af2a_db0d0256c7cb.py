"""Rh (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd266c763-9fe0-4ff3-af2a-db0d0256c7cb'
SOURCE_PATH = 'pictographic-primitives/state/Rh_d266c763-9fe0-4ff3-af2a-db0d0256c7cb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Rh(Solo48):
    icon_id = 'rh'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rh', 'state')

    def build(self):
        self.add_line('e0', (4, 25), (14, 25))
        self.add_line('e1', (15, 8), (5, 8))
        self.add_line('e2', (4, 9), (4, 40))
        self.add_line('e3', (21, 40), (14, 25))
        self.add_line('e4', (31, 8), (31, 40))
        self.add_line('e5', (44, 29), (44, 40))
        self.add_bezier('e6', (14, 25), ((14.691, 25), (15.482, 24.73), (16.127, 24.46)), ((19.955, 22.88), (21.4, 17.64), (20.564, 13.5)), ((20.018, 10.81), (17.818, 8.02), (15.127, 8.02)), ((15.055, 8.01), (15.073, 8.01), (15, 8)))
        self.add_bezier('e7', (5, 8), ((4.936, 8), (4.773, 8.01), (4.709, 8.01)), ((4.127, 8.01), (4.191, 8.66), (4, 9)))
        self.add_bezier('e8', (31, 24), ((32.209, 20.73), (34.664, 18.77), (38.045, 19.04)), ((39.3, 19.14), (40.536, 19.58), (41.509, 20.49)), ((43.155, 22.03), (43.991, 24.88), (43.991, 27.21)), ((43.991, 27.29), (44, 27.38), (44, 27.46)), ((44, 27.97), (44, 28.49), (44, 29)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e8', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')

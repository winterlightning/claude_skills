"""Warp fish (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf262ac0-6a03-43ea-a2f5-d9b248545818'
SOURCE_PATH = 'icons-json/design/warp fish_cf262ac0-6a03-43ea-a2f5-d9b248545818.json'
AUTHOR = 'json_to_solo'

class WarpFishDesign(Solo48):
    icon_id = 'warp-fish-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'fish', 'design')

    def build(self):
        self.add_line('e0', (44, 36), (41, 32))
        self.add_line('e1', (31, 31), (28, 36))
        self.add_line('e2', (27, 12), (31, 17))
        self.add_line('e3', (42, 15), (44, 12))
        self.add_line('e4', (44, 12), (44, 36))
        self.add_bezier('e5', (41, 32), ((38.518, 28.36), (33.855, 27.08), (31, 31)))
        self.add_bezier('e6', (28, 36), ((26.182, 38.51), (22.4, 39.98), (19.527, 39.98)), ((19.318, 39.98), (19.109, 40), (18.9, 40)), ((18.896, 40), (18.891, 40), (18.887, 40)), ((18.619, 40), (18.35, 39.98), (18.082, 39.98)), ((11.4, 39.98), (4.009, 31.59), (4.009, 24.28)), ((4.009, 24.211), (4, 24.142), (4, 24.073)), ((4, 24.072), (4, 24.071), (4, 24.07)), ((4, 23.86), (4.009, 23.65), (4.009, 23.44)), ((4.009, 16.14), (11.418, 8.02), (18.055, 8.02)), ((18.191, 8.02), (18.327, 8), (18.464, 8)), ((18.468, 8), (18.472, 8), (18.476, 8)), ((18.745, 8), (19.004, 8.01), (19.264, 8.01)), ((22.2, 8.01), (24.991, 9.79), (27, 12)))
        self.add_bezier('e7', (31, 17), ((34.891, 21.28), (39.173, 19.67), (42, 15)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4', closed=True)

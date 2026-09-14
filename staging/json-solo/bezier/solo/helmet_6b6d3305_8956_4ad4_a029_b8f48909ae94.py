"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b6d3305-8956-4ad4-a029-b8f48909ae94'
SOURCE_PATH = 'icons-json/protection/helmet_6b6d3305-8956-4ad4-a029-b8f48909ae94.json'
AUTHOR = 'json_to_solo'

class Helmet(Solo48):
    icon_id = 'helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_line('e0', (29, 29), (29, 13))
        self.add_line('e1', (19, 29), (19, 10))
        self.add_line('e2', (29, 10), (29, 13))
        self.add_line('e3', (6, 29), (43, 29))
        self.add_line('e4', (44, 31), (44, 37))
        self.add_line('e5', (42, 40), (6, 40))
        self.add_bezier('e6', (40, 29), ((40.055, 23.33), (37.709, 18.39), (33.4, 15.37)), ((31.909, 14.32), (30.627, 13.7), (29, 13)))
        self.add_bezier('e7', (19, 10), ((19.364, 9.51), (20.136, 9), (20.645, 8.66)), ((21.745, 8), (24.245, 8.02), (25.545, 8.02)), ((25.745, 8.02), (25.945, 8), (26.145, 8)), ((26.146, 8), (26.147, 8), (26.148, 8)), ((26.211, 8), (26.283, 8), (26.345, 8.01)), ((27.691, 8.01), (28.536, 8.84), (29, 10)))
        self.add_bezier('e8', (8, 29), ((7.945, 23.32), (10.445, 18.12), (14.9, 15.26)), ((16.336, 14.34), (17.473, 13.71), (19, 13)))
        self.add_bezier('e9', (43, 29), ((43.509, 29.68), (43.809, 30.11), (44, 31)))
        self.add_bezier('e10', (44, 37), ((44, 37.56), (43.136, 39.51), (42.736, 39.88)), ((42.627, 39.98), (42.055, 39.96), (42, 40)))
        self.add_bezier('e11', (6, 40), ((5.964, 40), (5.745, 40), (5.709, 40)), ((4.818, 40), (4.018, 38.72), (4.018, 37.83)), ((4.018, 37.77), (4.009, 37.71), (4.009, 37.65)), ((4.009, 37.6), (4.009, 37.55), (4.009, 37.5)), ((4.009, 37.41), (4.018, 37.29), (4.018, 37.17)), ((4.009, 37.12), (4, 37.06), (4, 37.01)), ((4, 36.11), (4.009, 35.21), (4.009, 34.31)), ((4.009, 33.82), (4.018, 33.32), (4.018, 32.83)), ((4.018, 32.61), (4, 32.39), (4, 32.17)), ((4, 32.169), (4, 32.167), (4, 32.166)), ((4, 32.077), (4, 31.999), (4.009, 31.91)), ((4.009, 30.92), (4.364, 29.64), (5.282, 29.17)), ((5.455, 29.08), (5.836, 29.08), (6, 29)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e7', 'e2')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c2')

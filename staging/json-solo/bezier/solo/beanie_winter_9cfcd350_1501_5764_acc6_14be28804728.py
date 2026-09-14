"""Batch-03/beanie winter (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cfcd350-1501-5764-acc6-14be28804728'
SOURCE_PATH = 'icons-json/accessories/batch-03/beanie winter_9cfcd350-1501-5764-acc6-14be28804728.json'
AUTHOR = 'json_to_solo'

class Batch03BeanieWinter(Solo48):
    icon_id = 'batch-03-beanie-winter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'beanie', 'winter', 'accessories')

    def build(self):
        self.add_line('e0', (30, 31), (8, 31))
        self.add_line('e1', (6, 35), (6, 40))
        self.add_line('e2', (9, 42), (38, 42))
        self.add_line('e3', (42, 39), (42, 35))
        self.add_line('e4', (38, 31), (30, 31))
        self.add_line('e5', (30, 31), (30, 42))
        self.add_line('e6', (17, 31), (17, 42))
        self.add_bezier('e7', (40, 32), ((39.787, 23.573), (35.561, 15.638), (26.455, 14.182)), ((24.826, 13.92), (23.182, 13.985), (21.545, 14.182)), ((14.869, 15), (10.664, 20.22), (9.068, 26.438)), ((8.651, 28.034), (8.09, 29.364), (8, 31)))
        self.add_bezier('e8', (26, 14), ((26.515, 13.19), (27.715, 12.472), (27.96, 11.515)), ((28.639, 8.855), (26.79, 6), (23.926, 6)), ((23.886, 6), (23.847, 6), (23.807, 6)), ((21.318, 6), (19.571, 8.582), (19.942, 10.966)), ((20.122, 12.136), (21.427, 13.067), (22, 14)))
        self.add_bezier('e9', (8, 31), ((6.585, 31), (6.016, 33.196), (6.016, 34.456)), ((6.008, 34.514), (6.008, 34.943), (6, 35)))
        self.add_bezier('e10', (6, 40), ((6, 41.546), (7.71, 41.992), (9.076, 41.992)), ((9.142, 41.992), (8.935, 42), (9, 42)))
        self.add_bezier('e11', (38, 42), ((38.164, 42), (38.228, 41.992), (38.392, 41.992)), ((40.102, 41.992), (42, 40.849), (42, 39)))
        self.add_bezier('e12', (42, 35), ((42, 34.804), (42, 34.235), (42, 34.039)), ((42, 33.81), (41.779, 33.556), (41.673, 33.376)), ((41.067, 32.354), (40.568, 32.427), (39.545, 32.182)), ((38.965, 32.043), (38.605, 31), (38, 31)))
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e12', 'e4', 'e5')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c2')

"""Synchronize arrows three (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92f7fa78-def1-430b-a511-f011591c78a6'
SOURCE_PATH = 'icons-json/interface-essential/synchronize arrows three_92f7fa78-def1-430b-a511-f011591c78a6.json'
AUTHOR = 'json_to_solo'

class SynchronizeArrowsThreeInterfaceEssential(Solo48):
    icon_id = 'synchronize-arrows-three-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'arrows', 'three', 'interface-essential')

    def build(self):
        self.add_line('e0', (15, 6), (13, 12))
        self.add_line('e1', (19, 13), (14, 13))
        self.add_line('e2', (13, 39), (14, 40))
        self.add_line('e3', (8, 41), (14, 40))
        self.add_line('e4', (13, 34), (14, 40))
        self.add_line('e5', (35, 26), (39, 22))
        self.add_line('e6', (42, 26), (39, 22))
        self.add_bezier('e7', (14, 13), ((13.624, 12.935), (13.27, 12.27), (13, 12)))
        self.add_bezier('e8', (35, 14), ((31.105, 10.048), (25.031, 7.98), (19.467, 9.15)), ((17.25, 9.616), (14.988, 10.961), (13, 12)))
        self.add_bezier('e9', (8, 18), ((7.035, 20.242), (6.016, 22.994), (6.016, 25.456)), ((6.016, 25.609), (6, 25.762), (6, 25.915)), ((6, 25.918), (6, 25.92), (6, 25.923)), ((6, 26.144), (6.016, 26.365), (6.016, 26.585)), ((6.016, 27.518), (6.213, 28.492), (6.425, 29.4)), ((7.342, 33.254), (9.842, 36.595), (13, 39)))
        self.add_bezier('e10', (14, 40), ((14.041, 40.27), (14, 39.73), (14, 40)))
        self.add_bezier('e11', (23, 42), ((23.074, 42), (23.337, 41.992), (23.411, 41.992)), ((25.514, 41.992), (27.715, 41.264), (29.588, 40.331)), ((35.029, 37.615), (38.261, 31.699), (38.793, 25.759)), ((38.915, 24.352), (39.065, 23.424), (39, 22)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e9', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e4', 'e10')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e11')
        self.add_contour('c8', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')

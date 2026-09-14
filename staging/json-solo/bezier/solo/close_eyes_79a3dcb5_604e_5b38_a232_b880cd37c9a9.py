"""Close eyes (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79a3dcb5-604e-5b38-a232-b880cd37c9a9'
SOURCE_PATH = 'icons-json/interface-essential/close eyes_79a3dcb5-604e-5b38-a232-b880cd37c9a9.json'
AUTHOR = 'json_to_solo'

class CloseEyesInterfaceEssential(Solo48):
    icon_id = 'close-eyes-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('close', 'eyes', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 34), (11, 28))
        self.add_line('e1', (16, 39), (18, 31))
        self.add_line('e2', (24, 40), (24, 32))
        self.add_line('e3', (31, 31), (33, 39))
        self.add_line('e4', (41, 34), (37, 28))
        self.add_bezier('e5', (44, 20), ((39.8, 14.55), (34.691, 9.8), (28.127, 8.45)), ((27.236, 8.27), (26.264, 8.02), (25.355, 8.02)), ((25.05, 8.02), (24.746, 8), (24.433, 8)), ((24.428, 8), (24.423, 8), (24.418, 8)), ((24.036, 8), (23.645, 8.02), (23.255, 8.02)), ((17.318, 8.02), (11.691, 11.42), (7.527, 15.89)), ((6.573, 16.91), (5.682, 17.98), (4.855, 19.13)), ((4.756, 19.268), (4, 20.22), (4, 20.354)), ((4, 20.356), (4, 20.358), (4, 20.36)), ((4, 20.71), (5.064, 22.2), (5.3, 22.54)), ((6.9, 24.82), (9.082, 26.47), (11.273, 28)), ((13.209, 29.35), (15.445, 30.29), (17.636, 31)), ((19.764, 31.69), (21.791, 31.93), (24, 32)), ((26.427, 32.07), (28.945, 31.76), (31.273, 31)), ((33.236, 30.36), (35.036, 29.25), (36.727, 28)), ((38.782, 26.48), (40.827, 24.81), (42.491, 22.78)), ((42.736, 22.48), (44, 20.96), (44, 20.65)), ((44, 20.43), (44, 20.22), (44, 20)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')

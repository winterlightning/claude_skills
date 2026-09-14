"""Arrange number (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '774a187b-a625-438b-9b84-1427193ca713'
SOURCE_PATH = 'icons-json/_uncategorized_04/arrange number_774a187b-a625-438b-9b84-1427193ca713.json'
AUTHOR = 'json_to_solo'

class ArrangeNumberUncategorized04(Solo48):
    icon_id = 'arrange-number-uncategorized-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('arrange', 'number', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (32, 7), (36, 4))
        self.add_line('e1', (36, 4), (36, 19))
        self.add_line('e2', (32, 19), (36, 19))
        self.add_line('e3', (39, 19), (36, 19))
        self.add_line('e4', (13, 9), (13, 34))
        self.add_line('e5', (8, 29), (13, 34))
        self.add_line('e6', (19, 29), (13, 34))
        self.add_line('e7', (40, 35), (38, 37))
        self.add_bezier('e8', (32, 43), ((32.783, 43.391), (33.263, 43.991), (34.156, 43.991)), ((34.223, 43.991), (34.291, 44), (34.358, 44)), ((34.359, 44), (34.36, 44), (34.361, 44)), ((34.427, 44), (34.494, 44), (34.552, 44)), ((37.154, 44), (39.983, 40.891), (39.983, 38.082)), ((39.992, 38.018), (39.992, 37.955), (40, 37.882)), ((40, 37.673), (39.983, 37.455), (39.983, 37.245)), ((39.983, 37.045), (39.983, 36.845), (39.983, 36.645)), ((39.992, 36.064), (39.992, 35.573), (40, 35)))
        self.add_bezier('e9', (38, 37), ((33.124, 40.464), (28.766, 33.764), (32.278, 29.4)), ((34.198, 27.018), (38.013, 27.5), (39.453, 30.209)), ((39.731, 30.745), (39.983, 31.373), (39.983, 32)), ((39.992, 32.082), (39.992, 32.173), (40, 32.255)), ((40, 33.145), (40, 34.118), (40, 35)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e7', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c7')

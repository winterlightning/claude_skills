"""Bh (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5635291-9570-40c9-ba89-ef57fb091088'
SOURCE_PATH = 'icons-json/symbol/bh (text u)_d5635291-9570-40c9-ba89-ef57fb091088.json'
AUTHOR = 'json_to_solo'

class BhTextUSymbol(Solo48):
    icon_id = 'bh-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bh', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (15, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (13, 27))
        self.add_line('e3', (16, 15), (8, 15))
        self.add_line('e4', (30, 4), (30, 27))
        self.add_line('e5', (40, 19), (40, 27))
        self.add_line('e6', (8, 44), (40, 44))
        self.add_bezier('e7', (13, 27), ((14.246, 27), (15.655, 26.8), (16.884, 26.482)), ((19.629, 25.764), (21.423, 23.409), (21.305, 20.318)), ((21.221, 18.2), (19.916, 16.591), (18.198, 15.727)), ((17.659, 15.455), (17.053, 15.309), (16.472, 15.155)), ((16.345, 15.118), (16.059, 15.045), (15.933, 15.018)), ((15.815, 14.982), (15.697, 14.945), (15.579, 14.909)), ((15.975, 14.745), (16.413, 14.691), (16.808, 14.536)), ((17.853, 14.118), (18.947, 13.264), (19.545, 12.245)), ((21.971, 8.091), (19.143, 4), (15, 4)))
        self.add_bezier('e8', (30, 15), ((30.354, 14.227), (30.585, 13.445), (31.183, 12.845)), ((32.118, 11.927), (33.339, 11.473), (34.585, 11.455)), ((37.743, 11.391), (39.983, 13.764), (39.983, 17.209)), ((39.992, 17.282), (39.992, 17.355), (40, 17.427)), ((40, 17.8), (40, 18.627), (40, 19)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e7', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e8', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')

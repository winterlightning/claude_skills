"""Curly brackets (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9944ea4-e25f-57dc-a6ca-a168c1412bdb'
SOURCE_PATH = 'icons-json/programing/curly brackets_c9944ea4-e25f-57dc-a6ca-a168c1412bdb.json'
AUTHOR = 'json_to_solo'

class CurlyBracketsC9944ea4(Solo48):
    icon_id = 'curly-brackets-c9944ea4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('curly', 'brackets', 'programing')

    def build(self):
        self.add_line('e0', (40, 27), (40, 36))
        self.add_line('e1', (9, 21), (9, 11))
        self.add_line('e2', (9, 29), (9, 36))
        self.add_bezier('e3', (35, 8), ((35.236, 8), (35.382, 8.008), (35.609, 8.008)), ((37.836, 8.008), (39.973, 9.179), (40.427, 11.326)), ((40.545, 11.882), (40.527, 12.488), (40.527, 13.053)), ((40.555, 15.394), (39.973, 19.528), (40.864, 21.642)), ((41.373, 22.88), (42.782, 23.545), (44, 24)))
        self.add_bezier('e4', (44, 24), ((42.573, 24.665), (40, 25.147), (40, 27)))
        self.add_bezier('e5', (40, 36), ((40, 37.827), (38.8, 40), (36.582, 40)), ((36.373, 40), (36.173, 40), (35.964, 40)), ((35.827, 40), (35.682, 39.992), (35.545, 39.992)), ((35.473, 39.992), (35.4, 40), (35.336, 40)), ((35.191, 40), (35.145, 40), (35, 40)))
        self.add_bezier('e6', (6, 24), ((7.436, 23.301), (9, 22.659), (9, 21)))
        self.add_bezier('e7', (9, 11), ((9.7, 9.568), (10.8, 8.008), (12.727, 8.008)), ((13.009, 8.008), (13.291, 8), (13.573, 8)), ((13.718, 8), (13.855, 8), (14, 8)))
        self.add_bezier('e8', (4, 24), ((4.609, 24), (5.209, 24), (5.818, 24)), ((6.155, 24.008), (6.655, 24.345), (6.927, 24.522)), ((8.145, 25.331), (8.691, 26.737), (8.655, 28.084)), ((8.645, 28.413), (9, 28.68), (9, 29)))
        self.add_bezier('e9', (9, 36), ((9, 37.735), (10.155, 40), (12.264, 40)), ((12.482, 40), (12.691, 40), (12.909, 40)), ((13.055, 40), (13.2, 39.992), (13.345, 39.992)), ((13.418, 39.992), (13.491, 40), (13.564, 40)), ((13.709, 40), (13.855, 40), (14, 40)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4', 'e0', 'e5')
        self.add_contour('c2', 'e6', 'e1', 'e7')
        self.add_contour('c3', 'e8', 'e2', 'e9')
        self.relate('connect', 'c2', 'c3')

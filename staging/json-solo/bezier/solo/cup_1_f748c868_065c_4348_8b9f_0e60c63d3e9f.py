"""Cup 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f748c868-065c-4348-8b9f-0e60c63d3e9f'
SOURCE_PATH = 'icons-json/symbol/cup 1_f748c868-065c-4348-8b9f-0e60c63d3e9f.json'
AUTHOR = 'json_to_solo'

class Cup1Symbol(Solo48):
    icon_id = 'cup-1-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cup', 'symbol')

    def build(self):
        self.add_line('e0', (34, 13), (37, 13))
        self.add_line('e1', (34, 13), (34, 30))
        self.add_line('e2', (34, 13), (34, 8))
        self.add_line('e3', (34, 8), (4, 8))
        self.add_line('e4', (4, 8), (4, 31))
        self.add_line('e5', (15, 40), (24, 40))
        self.add_bezier('e6', (37, 13), ((40.191, 13.185), (43.045, 14.602), (43.773, 17.794)), ((44, 18.846), (43.991, 20), (43.991, 21.069)), ((43.991, 21.227), (44, 21.376), (44, 21.534)), ((44, 21.536), (44, 21.539), (44, 21.541)), ((44, 21.853), (43.991, 22.164), (43.991, 22.476)), ((43.991, 26.248), (41.809, 28.968), (37.7, 29.667)), ((36.5, 29.869), (35.191, 29.949), (34, 30)))
        self.add_bezier('e7', (4, 31), ((4, 31.152), (4, 31.04), (4, 31.192)), ((4, 31.958), (4.382, 32.867), (4.691, 33.566)), ((6.236, 37.027), (10.209, 40), (14.4, 40)), ((14.573, 40), (14.827, 40), (15, 40)))
        self.add_bezier('e8', (24, 40), ((24.173, 40), (24.355, 40), (24.527, 40)), ((25.355, 40), (26.345, 39.705), (27.118, 39.461)), ((31.773, 37.987), (34, 34.362), (34, 30)))
        self.add_contour('c0', 'e0', 'e6')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e7', 'e5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

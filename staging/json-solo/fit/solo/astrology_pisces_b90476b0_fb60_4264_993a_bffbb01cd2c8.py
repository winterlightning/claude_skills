"""Astrology pisces (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b90476b0-fb60-4264-993a-bffbb01cd2c8'
SOURCE_PATH = 'icons-json/_uncategorized_04/astrology pisces_b90476b0-fb60-4264-993a-bffbb01cd2c8.json'
AUTHOR = 'json_to_solo'

class AstrologyPiscesUncategorized04(Solo48):
    icon_id = 'astrology-pisces-uncategorized-04'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('astrology', 'pisces', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (44, 8), (15, 8))
        self.add_line('e1', (17, 10), (15, 8))
        self.add_line('e2', (30, 38), (32, 40))
        self.add_line('e3', (34, 40), (5, 40))
        self.add_line('e4-1', (15, 8), (8, 9))
        self.add_arc('e4-2', (8, 9), (4, 15), radius_x=7, sweep=False)
        self.add_arc('e4-3', (4, 15), (12, 23), radius_x=8, sweep=False)
        self.add_arc('e4-4', (12, 23), (18, 20), radius_x=8, sweep=False)
        self.add_arc('e4-5', (18, 20), (17, 10), radius_x=7, sweep=False)
        self.add_line('e5-1', (32, 40), (40, 39))
        self.add_arc('e5-2', (40, 39), (44, 33), radius_x=7, sweep=False)
        self.add_line('e5-3', (44, 33), (43, 29))
        self.add_arc('e5-4', (43, 29), (40, 26), radius_x=8, sweep=False)
        self.add_arc('e5-5', (40, 26), (32, 26), radius_x=9, sweep=False)
        self.add_arc('e5-6', (32, 26), (30, 38), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', closed=True)
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e2', closed=True)
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c2')

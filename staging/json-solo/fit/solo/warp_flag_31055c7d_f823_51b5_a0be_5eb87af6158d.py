"""Warp flag (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31055c7d-f823-51b5-a0be-5eb87af6158d'
SOURCE_PATH = 'icons-json/design/warp flag_31055c7d-f823-51b5-a0be-5eb87af6158d.json'
AUTHOR = 'json_to_solo'

class WarpFlagDesign(Solo48):
    icon_id = 'warp-flag-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'flag', 'design')

    def build(self):
        self.add_line('e0', (26, 26), (20, 22))
        self.add_line('e1', (44, 10), (44, 34))
        self.add_line('e2', (26, 38), (20, 35))
        self.add_line('e3', (4, 37), (4, 13))
        self.add_line('e4', (22, 11), (26, 13))
        self.add_arc('e5', (44, 22), (26, 26), radius_x=15)
        self.add_arc('e6', (20, 22), (4, 25), radius_x=13, sweep=False)
        self.add_arc('e7-1', (44, 34), (34, 40), radius_x=13)
        self.add_line('e7-2', (34, 40), (30, 40))
        self.add_arc('e7-3', (30, 40), (26, 38), radius_x=11)
        self.add_arc('e8', (20, 35), (4, 37), radius_x=14, sweep=False)
        self.add_arc('e9-1', (4, 13), (14, 8), radius_x=16)
        self.add_arc('e9-2', (14, 8), (22, 11), radius_x=13)
        self.add_arc('e10', (26, 13), (44, 10), radius_x=15, sweep=False)
        self.add_contour('c0', 'e5', 'e0', 'e6')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e4', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')

"""Adobe cloud logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a854686-429a-4caa-b2bb-aa9186cfd668'
SOURCE_PATH = 'icons-json/_uncategorized_01/adobe cloud logo_1a854686-429a-4caa-b2bb-aa9186cfd668.json'
AUTHOR = 'json_to_solo'

class AdobeCloudLogoUncategorized01(Solo48):
    icon_id = 'adobe-cloud-logo-uncategorized-01'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('adobe', 'cloud', 'logo', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (27, 24), (19, 15))
        self.add_line('e1', (20, 40), (11, 29))
        self.add_line('e2', (16, 23), (30, 40))
        self.add_line('e3', (20, 40), (30, 40))
        self.add_arc('e4', (11, 29), (16, 23), radius_x=4)
        self.add_line('e5-1', (20, 40), (14, 40))
        self.add_arc('e5-2', (14, 40), (9, 38), radius_x=9)
        self.add_arc('e5-3', (9, 38), (4, 27), radius_x=15)
        self.add_line('e5-4', (4, 27), (5, 21))
        self.add_arc('e5-5', (5, 21), (10, 15), radius_x=12)
        self.add_arc('e5-6', (10, 15), (19, 15), radius_x=9)
        self.add_line('e6-1', (30, 40), (33, 40))
        self.add_arc('e6-2', (33, 40), (39, 37), radius_x=10, sweep=False)
        self.add_arc('e6-3', (39, 37), (44, 25), radius_x=17, sweep=False)
        self.add_arc('e6-4', (44, 25), (44, 22), radius_x=32)
        self.add_arc('e6-5', (44, 22), (41, 14), radius_x=18, sweep=False)
        self.add_arc('e6-6', (41, 14), (31, 8), radius_x=12, sweep=False)
        self.add_line('e6-7', (31, 8), (26, 9))
        self.add_line('e6-8', (26, 9), (19, 15))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6')
        self.add_contour('c4', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')

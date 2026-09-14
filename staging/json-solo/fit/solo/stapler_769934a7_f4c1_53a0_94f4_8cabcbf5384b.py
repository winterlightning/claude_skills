"""Stapler (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '769934a7-f4c1-53a0-94f4-8cabcbf5384b'
SOURCE_PATH = 'icons-json/office/stapler_769934a7-f4c1-53a0-94f4-8cabcbf5384b.json'
AUTHOR = 'json_to_solo'

class StaplerOffice(Solo48):
    icon_id = 'stapler-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('stapler', 'office')

    def build(self):
        self.add_line('e0', (37, 40), (7, 40))
        self.add_line('e1', (39, 34), (12, 12))
        self.add_line('e2', (12, 12), (16, 9))
        self.add_line('e3', (22, 10), (43, 27))
        self.add_line('e4', (43, 31), (39, 34))
        self.add_line('e5', (26, 33), (6, 33))
        self.add_line('e6', (6, 33), (6, 29))
        self.add_line('e7', (8, 20), (14, 14))
        self.add_arc('e8', (39, 34), (37, 40), radius_x=4)
        self.add_line('e9-1', (7, 40), (4, 38))
        self.add_line('e9-2', (4, 38), (5, 34))
        self.add_arc('e9-3', (5, 34), (6, 33), radius_x=13, sweep=False)
        self.add_arc('e10-1', (16, 9), (19, 8), radius_x=5)
        self.add_arc('e10-2', (19, 8), (22, 10), radius_x=5)
        self.add_line('e11-1', (43, 27), (44, 29))
        self.add_arc('e11-2', (44, 29), (43, 31), radius_x=3)
        self.add_arc('e12', (29, 27), (26, 33), radius_x=7, sweep=False)
        self.add_contour('c0', 'e8', 'e0', 'e9-1', 'e9-2', 'e9-3')
        self.add_contour('c1', 'e1', 'e2', 'e10-1', 'e10-2', 'e3', 'e11-1', 'e11-2', 'e4', closed=True)
        self.add_contour('c2', 'e12', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c4', 'c1')

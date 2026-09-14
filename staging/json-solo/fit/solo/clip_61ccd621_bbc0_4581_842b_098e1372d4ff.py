"""Clip (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61ccd621-bbc0-4581-842b-098e1372d4ff'
SOURCE_PATH = 'icons-json/office/clip_61ccd621-bbc0-4581-842b-098e1372d4ff.json'
AUTHOR = 'json_to_solo'

class ClipOffice(Solo48):
    icon_id = 'clip-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('clip', 'office')

    def build(self):
        self.add_line('e0', (19, 19), (7, 19))
        self.add_line('e1', (4, 21), (4, 37))
        self.add_line('e2', (7, 40), (13, 40))
        self.add_line('e3', (15, 38), (19, 20))
        self.add_line('e4', (17, 8), (31, 8))
        self.add_line('e5', (29, 17), (29, 19))
        self.add_line('e6', (19, 19), (29, 19))
        self.add_line('e7', (29, 19), (41, 19))
        self.add_line('e8', (44, 21), (44, 37))
        self.add_line('e9', (41, 40), (35, 40))
        self.add_line('e10', (33, 38), (29, 20))
        self.add_line('e11', (19, 40), (29, 40))
        self.add_arc('e12', (7, 19), (4, 21), radius_x=3, sweep=False)
        self.add_arc('e13', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_arc('e14', (13, 40), (15, 38), radius_x=2, sweep=False)
        self.add_arc('e15', (19, 20), (19, 19), radius_x=13)
        self.add_line('e16-1', (19, 19), (14, 13))
        self.add_arc('e16-2', (14, 13), (17, 8), radius_x=4)
        self.add_arc('e17-1', (31, 8), (34, 12), radius_x=4)
        self.add_arc('e17-2', (34, 12), (29, 17), radius_x=7)
        self.add_arc('e18', (41, 19), (44, 21), radius_x=3)
        self.add_arc('e19', (44, 37), (41, 40), radius_x=3)
        self.add_arc('e20', (35, 40), (33, 38), radius_x=2)
        self.add_line('e21', (29, 20), (29, 19))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e13', 'e2', 'e14', 'e3', 'e15', closed=True)
        self.add_contour('c1', 'e16-1', 'e16-2', 'e4', 'e17-1', 'e17-2', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', 'e21', closed=True)
        self.add_contour('c4', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')

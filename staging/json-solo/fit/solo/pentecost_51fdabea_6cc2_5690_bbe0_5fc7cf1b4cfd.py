"""Pentecost (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51fdabea-6cc2-5690-bbe0-5fc7cf1b4cfd'
SOURCE_PATH = 'icons-json/holidays/pentecost_51fdabea-6cc2-5690-bbe0-5fc7cf1b4cfd.json'
AUTHOR = 'json_to_solo'

class PentecostHolidays(Solo48):
    icon_id = 'pentecost-holidays'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('pentecost', 'holidays')

    def build(self):
        self.add_line('e0', (16, 28), (12, 26))
        self.add_line('e1', (4, 15), (19, 15))
        self.add_line('e2', (19, 15), (17, 8))
        self.add_line('e3', (17, 8), (31, 8))
        self.add_line('e4', (29, 15), (44, 15))
        self.add_line('e5', (26, 35), (24, 40))
        self.add_arc('e6', (24, 40), (16, 28), radius_x=16, sweep=False)
        self.add_arc('e7', (12, 26), (4, 15), radius_x=14)
        self.add_line('e8', (31, 8), (29, 15))
        self.add_line('e9-1', (44, 15), (42, 21))
        self.add_line('e9-2', (42, 21), (39, 25))
        self.add_line('e9-3', (39, 25), (30, 28))
        self.add_arc('e9-4', (30, 28), (26, 35), radius_x=16, sweep=False)
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e2', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e5', closed=True)

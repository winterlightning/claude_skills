"""Meeting headphone wireless (office), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b320b4e-ed89-4f2f-be89-6e9fdbbeecce'
SOURCE_PATH = 'icons-json/office/meeting headphone wireless_5b320b4e-ed89-4f2f-be89-6e9fdbbeecce.json'
AUTHOR = 'json_to_solo'

class MeetingHeadphoneWirelessOffice(Solo48):
    icon_id = 'meeting-headphone-wireless-office'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('meeting', 'headphone', 'wireless', 'office')

    def build(self):
        self.add_line('e0', (27, 42), (27, 43))
        self.add_line('e1', (26, 44), (22, 44))
        self.add_line('e2', (22, 40), (26, 40))
        self.add_line('e3', (27, 40), (27, 42))
        self.add_line('e4', (34, 39), (34, 29))
        self.add_line('e5', (14, 39), (14, 29))
        self.add_arc('e6-1', (14, 8), (24, 4), radius_x=15)
        self.add_arc('e6-2', (24, 4), (34, 8), radius_x=15)
        self.add_arc('e7', (17, 12), (31, 12), radius_x=11)
        self.add_line('e8', (27, 43), (26, 44))
        self.add_arc('e9-1', (22, 44), (21, 42), radius_x=2)
        self.add_line('e9-2', (21, 42), (22, 40))
        self.add_arc('e10', (26, 40), (27, 40), radius_x=28)
        self.add_arc('e11', (27, 42), (34, 39), radius_x=6, sweep=False)
        self.add_arc('e12-1', (34, 39), (40, 35), radius_x=5, sweep=False)
        self.add_arc('e12-2', (40, 35), (34, 29), radius_x=6, sweep=False)
        self.add_arc('e13-1', (34, 29), (27, 18), radius_x=10, sweep=False)
        self.add_arc('e13-2', (27, 18), (14, 29), radius_x=10, sweep=False)
        self.add_arc('e14-1', (14, 29), (8, 34), radius_x=6, sweep=False)
        self.add_arc('e14-2', (8, 34), (14, 39), radius_x=6, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e0', 'e8', 'e1', 'e9-1', 'e9-2', 'e2', 'e10', 'e3', closed=True)
        self.add_contour('c3', 'e11')
        self.add_contour('c4', 'e12-1', 'e12-2')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e13-1', 'e13-2')
        self.add_contour('c7', 'e14-1', 'e14-2', 'e5', closed=True)
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c6', 'c7')

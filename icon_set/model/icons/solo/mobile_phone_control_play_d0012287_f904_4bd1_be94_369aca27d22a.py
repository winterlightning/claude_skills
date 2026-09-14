"""Mobile phone control play (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0012287-f904-4bd1-be94-369aca27d22a'
SOURCE_PATH = 'icons-json/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.json'
AUTHOR = 'json_to_solo'

class MobilePhoneControlPlay(Solo48):
    icon_id = 'mobile-phone-control-play'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('mobile', 'phone', 'control', 'play', 'state')

    def build(self):
        self.add_line('e0', (40, 36), (8, 36))
        self.add_line('e1', (18, 14), (31, 19))
        self.add_line('e2', (31, 21), (18, 27))
        self.add_line('e3', (17, 27), (17, 14))
        self.add_line('e4', (14, 44), (34, 44))
        self.add_line('e5', (40, 40), (40, 8))
        self.add_line('e6', (35, 4), (13, 4))
        self.add_line('e7', (8, 8), (8, 37))
        self.add_line('e8', (31, 19), (31, 21))
        self.add_line('e9', (18, 27), (17, 27))
        self.add_line('e10', (17, 14), (18, 14))
        self.add_line('e11-1', (8, 37), (9, 41))
        self.add_arc('e11-2', (9, 41), (11, 43), radius_x=5, sweep=False)
        self.add_arc('e11-3', (11, 43), (14, 44), radius_x=6, sweep=False)
        self.add_line('e12-1', (34, 44), (38, 43))
        self.add_arc('e12-2', (38, 43), (40, 40), radius_x=4, sweep=False)
        self.add_arc('e13-1', (40, 8), (38, 5), radius_x=4, sweep=False)
        self.add_arc('e13-2', (38, 5), (35, 4), radius_x=5, sweep=False)
        self.add_line('e14-1', (13, 4), (10, 5))
        self.add_arc('e14-2', (10, 5), (8, 8), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', closed=True)
        self.add_contour('c2', 'e11-1', 'e11-2', 'e11-3', 'e4', 'e12-1', 'e12-2', 'e5', 'e13-1', 'e13-2', 'e6', 'e14-1', 'e14-2', 'e7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')

"""Standing lamp (lamps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6f7fecc-a175-5b95-8265-1575fd4ba319'
SOURCE_PATH = 'icons-json/lamps/standing lamp_e6f7fecc-a175-5b95-8265-1575fd4ba319.json'
AUTHOR = 'json_to_solo'

class StandingLampLamps(Solo48):
    icon_id = 'standing-lamp-lamps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('standing', 'lamp', 'lamps')

    def build(self):
        self.add_line('e0', (24, 44), (24, 21))
        self.add_line('e1', (14, 44), (34, 44))
        self.add_line('e2', (34, 4), (28, 4))
        self.add_line('e3', (28, 4), (15, 4))
        self.add_line('e4', (14, 5), (8, 20))
        self.add_line('e5', (12, 21), (40, 21))
        self.add_line('e6', (39, 17), (34, 4))
        self.add_line('e7', (15, 4), (14, 5))
        self.add_arc('e8', (8, 20), (12, 21), radius_x=3, sweep=False)
        self.add_line('e9', (40, 21), (39, 17))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')

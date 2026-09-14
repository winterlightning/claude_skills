"""Pop up alert (apps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f2d1b12-2c74-4b57-91be-a4a84e1da748'
SOURCE_PATH = 'icons-json/apps/pop up alert_1f2d1b12-2c74-4b57-91be-a4a84e1da748.json'
AUTHOR = 'json_to_solo'

class PopUpAlertApps(Solo48):
    icon_id = 'pop-up-alert-apps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('pop', 'up', 'alert', 'apps')

    def build(self):
        self.add_line('e0', (24, 4), (24, 9))
        self.add_line('e1', (8, 9), (11, 13))
        self.add_line('e2', (37, 13), (40, 9))
        self.add_line('e3', (33, 44), (15, 44))
        self.add_line('e4', (13, 42), (13, 19))
        self.add_line('e5', (15, 18), (33, 18))
        self.add_line('e6', (35, 19), (35, 42))
        self.add_arc('e7-1', (21, 28), (23, 25), radius_x=3)
        self.add_arc('e7-2', (23, 25), (27, 26), radius_x=3)
        self.add_arc('e7-3', (27, 26), (27, 29), radius_x=3)
        self.add_line('e7-4', (27, 29), (24, 33))
        self.add_line('e8', (24, 38), (24, 37))
        self.add_arc('e9', (15, 44), (13, 42), radius_x=2)
        self.add_arc('e10', (13, 19), (15, 18), radius_x=2)
        self.add_arc('e11', (33, 18), (35, 19), radius_x=2)
        self.add_arc('e12', (35, 42), (33, 44), radius_x=2)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3', 'e7-4')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', closed=True)

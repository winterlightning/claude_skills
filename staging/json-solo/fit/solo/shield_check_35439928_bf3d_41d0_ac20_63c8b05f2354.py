"""Shield check (apps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35439928-bf3d-41d0-ac20-63c8b05f2354'
SOURCE_PATH = 'icons-json/apps/shield check_35439928-bf3d-41d0-ac20-63c8b05f2354.json'
AUTHOR = 'json_to_solo'

class ShieldCheckApps(Solo48):
    icon_id = 'shield-check-apps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('shield', 'check', 'apps')

    def build(self):
        self.add_line('e0', (32, 18), (21, 30))
        self.add_line('e1', (21, 30), (16, 25))
        self.add_line('e2', (40, 11), (40, 24))
        self.add_line('e3', (8, 25), (8, 10))
        self.add_arc('e4-1', (8, 10), (24, 4), radius_x=69, sweep=False)
        self.add_line('e4-2', (24, 4), (40, 11))
        self.add_arc('e5-1', (40, 24), (24, 44), radius_x=23)
        self.add_arc('e5-2', (24, 44), (8, 25), radius_x=24)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e2', 'e5-1', 'e5-2', 'e3', closed=True)

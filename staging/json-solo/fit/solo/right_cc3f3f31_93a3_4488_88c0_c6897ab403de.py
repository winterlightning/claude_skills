"""Right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc3f3f31-93a3-4488-88c0-c6897ab403de'
SOURCE_PATH = 'icons-json/arrows/right_cc3f3f31-93a3-4488-88c0-c6897ab403de.json'
AUTHOR = 'json_to_solo'

class RightArrows(Solo48):
    icon_id = 'right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('right', 'arrows')

    def build(self):
        self.add_line('e0', (26, 17), (26, 11))
        self.add_line('e1', (30, 8), (43, 22))
        self.add_line('e2', (44, 26), (30, 39))
        self.add_line('e3', (26, 37), (26, 30))
        self.add_line('e4', (26, 30), (7, 30))
        self.add_line('e5', (4, 27), (4, 20))
        self.add_line('e6', (7, 18), (26, 18))
        self.add_arc('e7-1', (26, 11), (28, 8), radius_x=4)
        self.add_arc('e7-2', (28, 8), (30, 8), radius_x=20, sweep=False)
        self.add_arc('e8-1', (43, 22), (44, 24), radius_x=3)
        self.add_arc('e8-2', (44, 24), (44, 26), radius_x=30, sweep=False)
        self.add_arc('e9-1', (30, 39), (29, 40), radius_x=4, sweep=False)
        self.add_arc('e9-2', (29, 40), (26, 37), radius_x=3)
        self.add_arc('e10', (7, 30), (4, 27), radius_x=3)
        self.add_arc('e11', (4, 20), (7, 18), radius_x=3)
        self.add_arc('e12', (26, 18), (26, 17), radius_x=1)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1', 'e8-1', 'e8-2', 'e2', 'e9-1', 'e9-2', 'e3', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', closed=True)

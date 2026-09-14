"""Safety helmet (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '990d7f69-ffaf-5940-bacc-e3c7ad205e17'
SOURCE_PATH = 'icons-json/construction/safety helmet_990d7f69-ffaf-5940-bacc-e3c7ad205e17.json'
AUTHOR = 'json_to_solo'

class SafetyHelmet990d7f69(Solo48):
    icon_id = 'safety-helmet-990d7f69'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'construction')

    def build(self):
        self.add_line('e0', (30, 11), (29, 23))
        self.add_line('e1', (21, 8), (27, 8))
        self.add_line('e2', (18, 11), (19, 23))
        self.add_arc('e3-1', (18, 11), (10, 17), radius_x=20, sweep=False)
        self.add_arc('e3-2', (10, 17), (6, 29), radius_x=20, sweep=False)
        self.add_line('e3-3', (6, 29), (4, 33))
        self.add_arc('e3-4', (4, 33), (8, 37), radius_x=4, sweep=False)
        self.add_arc('e3-5', (8, 37), (23, 40), radius_x=39, sweep=False)
        self.add_line('e3-6', (23, 40), (33, 39))
        self.add_arc('e3-7', (33, 39), (40, 37), radius_x=45, sweep=False)
        self.add_arc('e3-8', (40, 37), (44, 33), radius_x=4, sweep=False)
        self.add_line('e3-9', (44, 33), (42, 29))
        self.add_arc('e3-10', (42, 29), (38, 17), radius_x=21, sweep=False)
        self.add_arc('e3-11', (38, 17), (30, 11), radius_x=19, sweep=False)
        self.add_arc('e4', (18, 11), (21, 8), radius_x=3)
        self.add_arc('e5', (27, 8), (30, 11), radius_x=3)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e0')
        self.add_contour('c1', 'e4', 'e1', 'e5')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

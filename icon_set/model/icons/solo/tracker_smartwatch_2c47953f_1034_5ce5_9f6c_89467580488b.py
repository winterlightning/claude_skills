"""Tracker smartwatch (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c47953f-1034-5ce5-9f6c-89467580488b'
SOURCE_PATH = 'icons-json/health/tracker smartwatch_2c47953f-1034-5ce5-9f6c-89467580488b.json'
AUTHOR = 'json_to_solo'

class TrackerSmartwatch(Solo48):
    icon_id = 'tracker-smartwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tracker', 'smartwatch', 'health')

    def build(self):
        self.add_line('e0', (34, 35), (34, 41))
        self.add_line('e1', (29, 44), (19, 44))
        self.add_line('e2', (15, 40), (15, 35))
        self.add_line('e3', (40, 24), (33, 24))
        self.add_line('e4', (33, 24), (28, 29))
        self.add_line('e5', (28, 29), (22, 20))
        self.add_line('e6', (22, 20), (18, 25))
        self.add_line('e7', (18, 25), (8, 25))
        self.add_line('e8', (34, 13), (34, 7))
        self.add_line('e9', (29, 4), (19, 4))
        self.add_line('e10', (15, 7), (15, 13))
        self.add_line('e11', (40, 32), (40, 17))
        self.add_line('e12', (33, 13), (13, 13))
        self.add_line('e13', (8, 18), (8, 31))
        self.add_line('e14', (15, 35), (35, 35))
        self.add_line('e15-1', (34, 41), (33, 43))
        self.add_line('e15-2', (33, 43), (29, 44))
        self.add_arc('e16', (19, 44), (15, 40), radius_x=4)
        self.add_line('e17-1', (34, 7), (33, 5))
        self.add_line('e17-2', (33, 5), (29, 4))
        self.add_line('e18-1', (19, 4), (16, 5))
        self.add_arc('e18-2', (16, 5), (15, 7), radius_x=2, sweep=False)
        self.add_arc('e19', (40, 17), (33, 13), radius_x=5, sweep=False)
        self.add_arc('e20-1', (13, 13), (9, 14), radius_x=7, sweep=False)
        self.add_line('e20-2', (9, 14), (8, 18))
        self.add_arc('e21', (8, 31), (15, 35), radius_x=6, sweep=False)
        self.add_arc('e22', (35, 35), (40, 32), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e15-1', 'e15-2', 'e1', 'e16', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8', 'e17-1', 'e17-2', 'e9', 'e18-1', 'e18-2', 'e10')
        self.add_contour('c3', 'e11', 'e19', 'e12', 'e20-1', 'e20-2', 'e13', 'e21', 'e14', 'e22', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')

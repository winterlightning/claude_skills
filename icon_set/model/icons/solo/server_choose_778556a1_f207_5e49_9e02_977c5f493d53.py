"""Server choose (servers), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '778556a1-f207-5e49-9e02-977c5f493d53'
SOURCE_PATH = 'icons-json/servers/server choose_778556a1-f207-5e49-9e02-977c5f493d53.json'
AUTHOR = 'json_to_solo'

class ServerChoose(Solo48):
    icon_id = 'server-choose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('server', 'choose', 'servers')

    def build(self):
        self.add_line('e0', (39, 40), (10, 40))
        self.add_line('e1', (40, 29), (8, 29))
        self.add_line('e2', (39, 8), (10, 8))
        self.add_line('e3', (40, 19), (8, 19))
        self.add_arc('e4-1', (40, 29), (44, 34), radius_x=6)
        self.add_arc('e4-2', (44, 34), (43, 37), radius_x=5)
        self.add_arc('e4-3', (43, 37), (39, 40), radius_x=5)
        self.add_line('e5-1', (10, 40), (6, 39))
        self.add_arc('e5-2', (6, 39), (4, 35), radius_x=5)
        self.add_line('e5-3', (4, 35), (5, 31))
        self.add_arc('e5-4', (5, 31), (8, 29), radius_x=16, sweep=False)
        self.add_arc('e6-1', (40, 29), (44, 24), radius_x=6, sweep=False)
        self.add_arc('e6-2', (44, 24), (40, 19), radius_x=6, sweep=False)
        self.add_arc('e7-1', (40, 19), (44, 14), radius_x=6, sweep=False)
        self.add_arc('e7-2', (44, 14), (39, 8), radius_x=7, sweep=False)
        self.add_arc('e8-1', (10, 8), (4, 14), radius_x=6, sweep=False)
        self.add_arc('e8-2', (4, 14), (8, 19), radius_x=6, sweep=False)
        self.add_arc('e9-1', (8, 19), (4, 24), radius_x=6, sweep=False)
        self.add_arc('e9-2', (4, 24), (8, 29), radius_x=6, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4')
        self.add_contour('c1', 'e6-1', 'e6-2')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e9-1', 'e9-2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')

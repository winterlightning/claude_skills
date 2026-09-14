"""Playstation vr (technology), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7ccf92a-afad-5337-b90a-b52d403c4d46'
SOURCE_PATH = 'icons-json/technology/playstation vr_e7ccf92a-afad-5337-b90a-b52d403c4d46.json'
AUTHOR = 'json_to_solo'

class PlaystationVrTechnology(Solo48):
    icon_id = 'playstation-vr-technology'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('playstation', 'vr', 'technology')

    def build(self):
        self.add_line('e0', (7, 18), (6, 22))
        self.add_line('e1', (21, 38), (26, 38))
        self.add_arc('e2-1', (43, 27), (35, 11), radius_x=18, sweep=False)
        self.add_arc('e2-2', (35, 11), (31, 9), radius_x=19, sweep=False)
        self.add_line('e2-3', (31, 9), (24, 8))
        self.add_arc('e2-4', (24, 8), (7, 18), radius_x=20, sweep=False)
        self.add_arc('e3', (6, 22), (5, 27), radius_x=23, sweep=False)
        self.add_line('e4-1', (26, 38), (39, 40))
        self.add_arc('e4-2', (39, 40), (42, 39), radius_x=5, sweep=False)
        self.add_line('e4-3', (42, 39), (44, 34))
        self.add_line('e4-4', (44, 34), (43, 27))
        self.add_line('e4-5', (43, 27), (41, 25))
        self.add_arc('e4-6', (41, 25), (26, 21), radius_x=24, sweep=False)
        self.add_arc('e4-7', (26, 21), (8, 24), radius_x=39, sweep=False)
        self.add_arc('e4-8', (8, 24), (5, 27), radius_x=8, sweep=False)
        self.add_line('e4-9', (5, 27), (4, 34))
        self.add_arc('e4-10', (4, 34), (8, 40), radius_x=7, sweep=False)
        self.add_line('e4-11', (8, 40), (21, 38))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0', 'e3')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', closed=True)
        self.relate('connect', 'c0', 'c1')

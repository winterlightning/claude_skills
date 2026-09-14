"""Rhythmic ribbon (sports), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18afe439-cb6c-56c8-a073-523d474849db'
SOURCE_PATH = 'icons-json/sports/rhythmic ribbon_18afe439-cb6c-56c8-a073-523d474849db.json'
AUTHOR = 'json_to_solo'

class RhythmicRibbonSports(Solo48):
    icon_id = 'rhythmic-ribbon-sports'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('rhythmic', 'ribbon', 'sports')

    def build(self):
        self.add_line('e0', (29, 22), (26, 20))
        self.add_line('e1', (23, 29), (8, 44))
        self.add_arc('e2-1', (40, 10), (28, 4), radius_x=15, sweep=False)
        self.add_arc('e2-2', (28, 4), (22, 8), radius_x=7, sweep=False)
        self.add_arc('e2-3', (22, 8), (23, 12), radius_x=3, sweep=False)
        self.add_arc('e2-4', (23, 12), (34, 18), radius_x=13)
        self.add_arc('e2-5', (34, 18), (33, 23), radius_x=4)
        self.add_arc('e2-6', (33, 23), (29, 22), radius_x=4)
        self.add_line('e3-1', (26, 20), (21, 19))
        self.add_arc('e3-2', (21, 19), (18, 21), radius_x=3, sweep=False)
        self.add_arc('e3-3', (18, 21), (23, 29), radius_x=8, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e1')

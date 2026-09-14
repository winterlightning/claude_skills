"""Brain head (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01418f39-dca2-44e9-bb44-904b3b62f519'
SOURCE_PATH = 'icons-json/health/brain head_01418f39-dca2-44e9-bb44-904b3b62f519.json'
AUTHOR = 'json_to_solo'

class BrainHeadHealth(Solo48):
    icon_id = 'brain-head-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('brain', 'head', 'health')

    def build(self):
        self.add_line('e0', (36, 44), (36, 32))
        self.add_line('e1', (12, 14), (8, 27))
        self.add_line('e2', (11, 28), (11, 33))
        self.add_line('e3', (16, 38), (19, 38))
        self.add_line('e4', (19, 38), (19, 44))
        self.add_line('e5-1', (36, 32), (39, 26))
        self.add_arc('e5-2', (39, 26), (40, 20), radius_x=19, sweep=False)
        self.add_line('e5-3', (40, 20), (39, 14))
        self.add_arc('e5-4', (39, 14), (34, 7), radius_x=15, sweep=False)
        self.add_arc('e5-5', (34, 7), (27, 4), radius_x=14, sweep=False)
        self.add_line('e5-6', (27, 4), (25, 4))
        self.add_arc('e5-7', (25, 4), (12, 14), radius_x=14, sweep=False)
        self.add_line('e6', (8, 27), (11, 28))
        self.add_arc('e7', (11, 33), (16, 38), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4')

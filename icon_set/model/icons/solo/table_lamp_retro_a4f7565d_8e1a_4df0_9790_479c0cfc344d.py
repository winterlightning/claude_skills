"""Table lamp retro (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4f7565d-8e1a-4df0-9790-479c0cfc344d'
SOURCE_PATH = 'icons-json/outdoors/table lamp retro_a4f7565d-8e1a-4df0-9790-479c0cfc344d.json'
AUTHOR = 'json_to_solo'

class TableLampRetro(Solo48):
    icon_id = 'table-lamp-retro'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('table', 'lamp', 'retro', 'outdoors')

    def build(self):
        self.add_line('e0', (17, 44), (24, 44))
        self.add_line('e1', (31, 44), (24, 44))
        self.add_line('e2', (26, 21), (28, 24))
        self.add_line('e3', (36, 22), (40, 25))
        self.add_line('e4', (22, 21), (20, 24))
        self.add_line('e5', (24, 20), (24, 44))
        self.add_arc('e6', (24, 4), (24, 6), radius_x=13, sweep=False)
        self.add_line('e7', (24, 20), (26, 21))
        self.add_arc('e8-1', (28, 24), (32, 22), radius_x=4, sweep=False)
        self.add_arc('e8-2', (32, 22), (36, 22), radius_x=4)
        self.add_line('e9-1', (40, 25), (40, 20))
        self.add_arc('e9-2', (40, 20), (37, 13), radius_x=19, sweep=False)
        self.add_arc('e9-3', (37, 13), (30, 7), radius_x=14, sweep=False)
        self.add_arc('e9-4', (30, 7), (24, 6), radius_x=17, sweep=False)
        self.add_line('e10', (24, 20), (22, 21))
        self.add_line('e11-1', (20, 24), (14, 21))
        self.add_line('e11-2', (14, 21), (8, 25))
        self.add_arc('e11-3', (8, 25), (8, 23), radius_x=36, sweep=False)
        self.add_line('e11-4', (8, 23), (9, 17))
        self.add_arc('e11-5', (9, 17), (11, 13), radius_x=19)
        self.add_arc('e11-6', (11, 13), (18, 7), radius_x=14)
        self.add_arc('e11-7', (18, 7), (24, 6), radius_x=17)
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e7', 'e2', 'e8-1', 'e8-2', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4')
        self.add_contour('c4', 'e10', 'e4', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e11-6', 'e11-7')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')

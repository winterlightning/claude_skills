"""Batch-02/umbrella (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb6872fb-7ad7-4948-9e90-e03cf896cf9a'
SOURCE_PATH = 'icons-json/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.json'
AUTHOR = 'json_to_solo'

class Batch02Umbrella(Solo48):
    icon_id = 'batch-02-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'umbrella', 'accessories')

    def build(self):
        self.add_line('e0', (24, 37), (24, 24))
        self.add_line('e1', (8, 24), (40, 24))
        self.add_line('e2', (24, 4), (24, 8))
        self.add_arc('e3-1', (16, 40), (20, 44), radius_x=4, sweep=False)
        self.add_arc('e3-2', (20, 44), (24, 37), radius_x=5, sweep=False)
        self.add_arc('e4', (40, 24), (8, 24), radius_x=16, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e0')
        self.add_contour('c1', 'e1', 'e4')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')

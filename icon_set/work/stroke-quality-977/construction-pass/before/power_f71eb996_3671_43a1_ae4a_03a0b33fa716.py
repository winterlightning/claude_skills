"""Power (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f71eb996-3671-43a1-ae4a-03a0b33fa716'
SOURCE_PATH = 'pictographic-primitives/symbol/power_f71eb996-3671-43a1-ae4a-03a0b33fa716.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PowerF71eb996(Solo48):
    icon_id = 'power-f71eb996'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('power', 'symbol')

    def build(self):
        self.add_line('e0', (24, 23), (24, 4))
        self.add_arc('e1-1', (15, 14), (8, 27), radius_x=16, sweep=False)
        self.add_line('e1-2', (8, 27), (9, 33))
        self.add_arc('e1-3', (9, 33), (12, 38), radius_x=17, sweep=False)
        self.add_arc('e1-4', (12, 38), (23, 44), radius_x=14, sweep=False)
        self.add_arc('e1-5', (23, 44), (40, 27), radius_x=17, sweep=False)
        self.add_arc('e1-6', (40, 27), (33, 13), radius_x=18, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6')
        self.add_contour('c1', 'e0')

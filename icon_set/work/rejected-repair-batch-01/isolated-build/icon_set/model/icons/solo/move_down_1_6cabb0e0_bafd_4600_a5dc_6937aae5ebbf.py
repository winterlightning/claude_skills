"""Move down 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cabb0e0-bafd-4600-a5dc-6937aae5ebbf'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move down 1_6cabb0e0-bafd-4600-a5dc-6937aae5ebbf.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveDown1(Solo48):
    icon_id = 'move-down-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'down', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 4), (24, 35))
        self.add_line('e1', (16, 27), (24, 35))
        self.add_line('e2', (32, 27), (24, 35))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

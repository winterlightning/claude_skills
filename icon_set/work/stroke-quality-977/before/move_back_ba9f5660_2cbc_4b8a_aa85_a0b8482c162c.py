"""Move back (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba9f5660-2cbc-4b8a-aa85-a0b8482c162c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move back_ba9f5660-2cbc-4b8a-aa85-a0b8482c162c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveBack(Solo48):
    icon_id = 'move-back'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'back', 'interface-essential')

    def build(self):
        self.add_line('e0', (12, 8), (4, 16))
        self.add_line('e1', (12, 25), (4, 16))
        self.add_line('e2', (44, 40), (44, 16))
        self.add_line('e3', (44, 16), (4, 16))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')

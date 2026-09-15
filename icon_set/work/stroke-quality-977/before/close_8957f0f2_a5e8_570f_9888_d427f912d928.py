"""Close (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8957f0f2-a5e8-570f-9888-d427f912d928'
SOURCE_PATH = 'pictographic-primitives/interface-essential/close_8957f0f2-a5e8-570f-9888-d427f912d928.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Close(Solo48):
    icon_id = 'close-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('close', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (24, 24))
        self.add_line('e1', (24, 24), (6, 42))
        self.add_line('e2', (42, 42), (24, 24))
        self.add_line('e3', (24, 24), (42, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.relate('connect', 'c0', 'c1')

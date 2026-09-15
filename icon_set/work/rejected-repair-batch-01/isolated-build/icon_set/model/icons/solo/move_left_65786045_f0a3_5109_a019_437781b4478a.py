"""Move left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65786045-f0a3-5109-a019-437781b4478a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move left_65786045-f0a3-5109-a019-437781b4478a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoveLeftInterfaceEssential(Solo48):
    icon_id = 'move-left-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'left', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (8, 44), (8, 4))
        self.add_line('sym-e1', (19, 24), (40, 24))
        self.add_line('sym-e2', (27, 33), (19, 24))
        self.add_line('sym-e3', (19, 24), (27, 15))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')

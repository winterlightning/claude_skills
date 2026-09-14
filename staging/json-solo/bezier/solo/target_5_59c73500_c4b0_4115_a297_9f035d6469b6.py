"""Target 5 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59c73500-c4b0-4115-a297-9f035d6469b6'
SOURCE_PATH = 'icons-json/state/target 5_59c73500-c4b0-4115-a297-9f035d6469b6.json'
AUTHOR = 'json_to_solo'

class Target5State(Solo48):
    icon_id = 'target-5-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('target', 'state')

    def build(self):
        self.add_line('e0', (6, 24), (42, 24))
        self.add_line('e1', (24, 6), (24, 42))
        self.add_arc('e2-top', (10, 24), (38, 24), radius_x=14)
        self.add_arc('e2-bottom', (38, 24), (10, 24), radius_x=14)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)

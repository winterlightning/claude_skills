"""Move bottom left (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6742b6f0-e815-4e2d-8ec1-12df0b549f2c'
SOURCE_PATH = 'icons-json/_uncategorized_27/move bottom left_6742b6f0-e815-4e2d-8ec1-12df0b549f2c.json'
AUTHOR = 'json_to_solo'

class MoveBottomLeftUncategorized(Solo48):
    icon_id = 'move-bottom-left-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('move', 'bottom', 'left', '_uncategorized')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (6, 42), (42, 42))
        self.add_contour('c0', 'e0', 'e1')

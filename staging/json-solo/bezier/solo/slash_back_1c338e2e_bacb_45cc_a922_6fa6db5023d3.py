"""Slash back (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c338e2e-bacb-45cc-a922-6fa6db5023d3'
SOURCE_PATH = 'icons-json/_uncategorized_34/slash back_1c338e2e-bacb-45cc-a922-6fa6db5023d3.json'
AUTHOR = 'json_to_solo'

class SlashBackUncategorized(Solo48):
    icon_id = 'slash-back-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('slash', 'back', '_uncategorized')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_contour('c0', 'e0')

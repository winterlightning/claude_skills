"""A cursor arrow with a continuous outer outline and an attached diagonal tail."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1d7d06ed-e8d1-45e5-bf6a-390fe16ad950'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cursor/20260927T032022Z-thuan-mac-1/reference/cursor_1d7d06ed-e8d1-45e5-bf6a-390fe16ad950.svg'
AUTHOR = "gpt-6"

class Cursor(Solo48):
    icon_id = 'cursor'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('cursor', 'interface-essential')

    def build(self):
        # A single outline keeps the pointer's corners coherent at native size.
        self.add_polyline('pointer', (8, 4), (40, 21), (23, 25), (11, 44), closed=True)
        self.add_line('tail', (23, 25), (31, 40))
        self.relate('connect', 'pointer', 'tail')

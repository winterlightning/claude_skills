"""4 (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b2e9958-1a24-4980-b7ee-0e7fca211f6f'
SOURCE_PATH = 'icons-json/text/4 (text)_1b2e9958-1a24-4980-b7ee-0e7fca211f6f.json'
AUTHOR = 'json_to_solo'

class Icon4TextText(Solo48):
    icon_id = 'icon-4-text-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (40, 35), (8, 35))
        self.add_line('e1', (8, 35), (35, 4))
        self.add_line('e2', (35, 4), (35, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')

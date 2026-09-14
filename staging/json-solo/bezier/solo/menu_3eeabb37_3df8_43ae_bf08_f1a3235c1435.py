"""Menu (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3eeabb37-3df8-43ae-bf08-f1a3235c1435'
SOURCE_PATH = 'icons-json/state/menu_3eeabb37-3df8-43ae-bf08-f1a3235c1435.json'
AUTHOR = 'json_to_solo'

class Menu(Solo48):
    icon_id = 'menu'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('menu', 'state')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')

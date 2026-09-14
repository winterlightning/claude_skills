"""Button refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71b16598-965c-53a3-a647-8340109fb044'
SOURCE_PATH = 'icons-json/interface-essential/button refresh arrow_71b16598-965c-53a3-a647-8340109fb044.json'
AUTHOR = 'json_to_solo'

class ButtonRefreshArrowInterfaceEssential(Solo48):
    icon_id = 'button-refresh-arrow-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('button', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 40), (17, 35))
        self.add_line('e1', (13, 42), (18, 40))
        self.add_arc('e2-1', (24, 41), (42, 24), radius_x=18, sweep=False)
        self.add_line('e2-2', (42, 24), (40, 15))
        self.add_arc('e2-3', (40, 15), (25, 6), radius_x=18, sweep=False)
        self.add_line('e2-4', (25, 6), (16, 8))
        self.add_arc('e2-5', (16, 8), (8, 15), radius_x=18, sweep=False)
        self.add_line('e2-6', (8, 15), (6, 24))
        self.add_arc('e2-7', (6, 24), (18, 40), radius_x=18, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e0')
        self.add_contour('c1', 'e1')

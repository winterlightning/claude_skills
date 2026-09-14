"""Navigation arrows left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b205973-2afe-5242-bbc5-3aeb127a60ff'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows left_2b205973-2afe-5242-bbc5-3aeb127a60ff.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsLeft2b205973(Solo48):
    icon_id = 'navigation-arrows-left-2b205973'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (25, 24))
        self.add_line('e1', (25, 24), (42, 6))
        self.add_line('e2', (42, 6), (42, 42))
        self.add_line('e3', (23, 42), (6, 24))
        self.add_line('e4', (6, 24), (23, 6))
        self.add_line('e5', (23, 6), (23, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4', 'e5', closed=True)

"""Navigation arrows right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1132aadf-1937-51f7-8ebb-05344c566e12'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows right_1132aadf-1937-51f7-8ebb-05344c566e12.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsRight(Solo48):
    icon_id = 'navigation-arrows-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (23, 24))
        self.add_line('e1', (23, 24), (6, 42))
        self.add_line('e2', (6, 42), (6, 6))
        self.add_line('e3', (25, 6), (42, 24))
        self.add_line('e4', (42, 24), (25, 42))
        self.add_line('e5', (25, 42), (25, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4', 'e5', closed=True)

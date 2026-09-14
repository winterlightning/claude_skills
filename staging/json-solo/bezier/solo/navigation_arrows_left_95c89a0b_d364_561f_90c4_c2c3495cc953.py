"""Navigation arrows left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95c89a0b-d364-561f-90c4-c2c3495cc953'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows left_95c89a0b-d364-561f-90c4-c2c3495cc953.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsLeft(Solo48):
    icon_id = 'navigation-arrows-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (27, 36), (27, 42))
        self.add_line('e1', (27, 42), (6, 24))
        self.add_line('e2', (6, 24), (27, 6))
        self.add_line('e3', (27, 6), (27, 11))
        self.add_line('e4', (42, 6), (21, 24))
        self.add_line('e5', (21, 24), (42, 42))
        self.add_line('e6', (42, 42), (42, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6', closed=True)

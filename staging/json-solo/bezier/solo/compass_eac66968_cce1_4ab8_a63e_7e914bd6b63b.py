"""Compass (navigation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eac66968-cce1-4ab8-a63e-7e914bd6b63b'
SOURCE_PATH = 'icons-json/navigation/compass_eac66968-cce1-4ab8-a63e-7e914bd6b63b.json'
AUTHOR = 'json_to_solo'

class CompassNavigation(Solo48):
    icon_id = 'compass-navigation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'navigation'
    aliases = ()
    keywords = ('compass', 'navigation')

    def build(self):
        self.add_line('e0', (31, 31), (32, 29))
        self.add_line('e1', (32, 29), (42, 6))
        self.add_line('e2', (42, 6), (17, 17))
        self.add_line('e3', (17, 17), (31, 31))
        self.add_line('e4', (31, 31), (6, 42))
        self.add_line('e5', (6, 42), (17, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5')

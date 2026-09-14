"""Navigation arrows bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59435844-0c5c-54b6-bb0f-84fe2edb677c'
SOURCE_PATH = 'icons-json/arrows/navigation arrows bottom_59435844-0c5c-54b6-bb0f-84fe2edb677c.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsBottomArrows(Solo48):
    icon_id = 'navigation-arrows-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'arrows', 'bottom')

    def build(self):
        self.add_line('e0', (6, 6), (42, 6))
        self.add_line('e1', (42, 6), (24, 23))
        self.add_line('e2', (24, 23), (6, 6))
        self.add_line('e3', (6, 25), (42, 25))
        self.add_line('e4', (42, 25), (24, 42))
        self.add_line('e5', (24, 42), (6, 25))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4', 'e5', closed=True)

"""Navigation arrows top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac746243-876c-506b-a8bf-2ba1fcd15a42'
SOURCE_PATH = 'icons-json/arrows/navigation arrows top_ac746243-876c-506b-a8bf-2ba1fcd15a42.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsTopArrows(Solo48):
    icon_id = 'navigation-arrows-top-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'arrows', 'top')

    def build(self):
        self.add_line('e0', (42, 42), (6, 42))
        self.add_line('e1', (6, 42), (24, 25))
        self.add_line('e2', (24, 25), (42, 42))
        self.add_line('e3', (42, 23), (6, 23))
        self.add_line('e4', (6, 23), (24, 6))
        self.add_line('e5', (24, 6), (42, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4', 'e5', closed=True)

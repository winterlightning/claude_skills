'Double navigation: two equal open chevrons replace crowded enclosed triangles, preserving direction and repetition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac746243-876c-506b-a8bf-2ba1fcd15a42'
SOURCE_PATH = 'icons-json/arrows/navigation arrows top_ac746243-876c-506b-a8bf-2ba1fcd15a42.json'
AUTHOR = 'gpt-6'

class NavigationArrowsTop(Solo48):
    icon_id = 'navigation-arrows-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'arrows', 'top')

    def build(self) -> None:
        def p(x,y): return (48-x,48-y)
        # Equal open chevrons keep the double-navigation symbol readable at 48.
        self.add_polyline('first',p(6,6),p(24,20),p(42,6))
        self.add_polyline('second',p(6,28),p(24,42),p(42,28))

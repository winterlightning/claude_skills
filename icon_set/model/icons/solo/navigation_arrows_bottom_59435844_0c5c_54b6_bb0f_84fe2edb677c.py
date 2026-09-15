'Double navigation: two equal open chevrons replace crowded enclosed triangles, preserving direction and repetition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59435844-0c5c-54b6-bb0f-84fe2edb677c'
SOURCE_PATH = 'pictographic-primitives/arrows/navigation arrows bottom_59435844-0c5c-54b6-bb0f-84fe2edb677c.svg'
AUTHOR = 'gpt-6'

class NavigationArrowsBottom(Solo48):
    icon_id = 'navigation-arrows-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'arrows', 'bottom')

    def build(self) -> None:
        def p(x,y): return (x,y)
        # Equal open chevrons keep the double-navigation symbol readable at 48.
        self.add_polyline('first',p(6,6),p(24,20),p(42,6))
        self.add_polyline('second',p(6,28),p(24,42),p(42,28))

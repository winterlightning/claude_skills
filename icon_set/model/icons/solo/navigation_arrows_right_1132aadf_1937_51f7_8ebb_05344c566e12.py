'Double navigation: two equal open chevrons replace crowded enclosed triangles, preserving direction and repetition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1132aadf-1937-51f7-8ebb-05344c566e12'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation arrows right_1132aadf-1937-51f7-8ebb-05344c566e12.svg'
AUTHOR = 'gpt-6'

class NavigationArrowsRight(Solo48):
    icon_id = 'navigation-arrows-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'arrows', 'right', 'interface-essential')

    def build(self) -> None:
        def p(x,y): return (y,48-x)
        # Equal open chevrons keep the double-navigation symbol readable at 48.
        self.add_polyline('first',p(6,6),p(24,20),p(42,6))
        self.add_polyline('second',p(6,28),p(24,42),p(42,28))

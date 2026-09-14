'Double navigation: two equal open chevrons replace crowded enclosed triangles, preserving direction and repetition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b205973-2afe-5242-bbc5-3aeb127a60ff'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows left_2b205973-2afe-5242-bbc5-3aeb127a60ff.json'
AUTHOR = 'gpt-6'

class NavigationArrowsLeft(Solo48):
    icon_id = 'navigation-arrows-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'left', 'interface-essential')

    def build(self) -> None:
        def p(x,y): return (48-y,x)
        # Equal open chevrons keep the double-navigation symbol readable at 48.
        self.add_polyline('first',p(6,6),p(24,20),p(42,6))
        self.add_polyline('second',p(6,28),p(24,42),p(42,28))

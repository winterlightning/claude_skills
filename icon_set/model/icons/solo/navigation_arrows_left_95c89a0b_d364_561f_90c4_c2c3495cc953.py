'Double navigation: two equal open chevrons replace crowded enclosed triangles, preserving direction and repetition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95c89a0b-d364-561f-90c4-c2c3495cc953'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows left_95c89a0b-d364-561f-90c4-c2c3495cc953.json'
AUTHOR = 'gpt-6'

class NavigationArrowsLeft95c89a0b(Solo48):
    icon_id = 'navigation-arrows-left-95c89a0b'
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

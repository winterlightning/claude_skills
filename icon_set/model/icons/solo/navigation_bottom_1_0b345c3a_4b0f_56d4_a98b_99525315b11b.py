'Navigation arrow: straight shaft reaches the shared arrow tip; mirrored arms retain the exact keyshape envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b345c3a-4b0f-56d4-a98b-99525315b11b'
SOURCE_PATH = 'icons-json/arrows/navigation bottom 1_0b345c3a-4b0f-56d4-a98b-99525315b11b.json'
AUTHOR = 'gpt-6'

class NavigationBottom1(Solo48):
    icon_id = 'navigation-bottom-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'bottom', 'arrows')

    def build(self) -> None:
        def point(x,y): return (x,y)
        self.add_polyline('head',point(8,28),point(24,44),point(40,28))
        self.add_line('shaft',point(24,4),point(24,44))
        self.relate('connect','head','shaft')

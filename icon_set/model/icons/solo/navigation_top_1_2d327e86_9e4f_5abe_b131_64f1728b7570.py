'Navigation arrow: straight shaft reaches the shared arrow tip; mirrored arms retain the exact keyshape envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d327e86-9e4f-5abe-b131-64f1728b7570'
SOURCE_PATH = 'icons-json/arrows/navigation top 1_2d327e86-9e4f-5abe-b131-64f1728b7570.json'
AUTHOR = 'gpt-6'

class NavigationTop1(Solo48):
    icon_id = 'navigation-top-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'top', 'arrows')

    def build(self) -> None:
        def point(x,y): return (48-x,48-y)
        self.add_polyline('head',point(8,28),point(24,44),point(40,28))
        self.add_line('shaft',point(24,4),point(24,44))
        self.relate('connect','head','shaft')

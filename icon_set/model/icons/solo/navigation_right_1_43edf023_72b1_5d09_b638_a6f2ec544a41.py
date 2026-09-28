'Navigation arrow: straight shaft reaches the shared arrow tip; mirrored arms retain the exact keyshape envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43edf023-72b1-5d09-b638-a6f2ec544a41'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation right 1_43edf023-72b1-5d09-b638-a6f2ec544a41.svg'
AUTHOR = 'gpt-6'

class NavigationRight1(Solo48):
    icon_id = 'navigation-right-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'right', 'interface-essential')

    def build(self) -> None:
        def point(x,y): return (y,48-x)
        self.add_polyline('head',point(8,28),point(24,44),point(40,28))
        self.add_line('shaft',point(24,4),point(24,44))
        self.relate('connect','head','shaft')

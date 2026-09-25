'Navigation arrow: straight shaft reaches the shared arrow tip; mirrored arms retain the exact keyshape envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49892f36-8933-5254-828d-32374149c076'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation left 1_49892f36-8933-5254-828d-32374149c076.svg'
AUTHOR = 'gpt-6'

class NavigationLeft1(Solo48):
    icon_id = 'navigation-left-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self) -> None:
        def point(x,y): return (48-y,x)
        self.add_polyline('head',point(8,28),point(24,44),point(40,28))
        self.add_line('shaft',point(24,4),point(24,44))
        self.relate('connect','head','shaft')

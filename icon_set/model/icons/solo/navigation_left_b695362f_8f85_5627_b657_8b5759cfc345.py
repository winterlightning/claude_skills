'Curved navigation arrow: preserve the directional sweep with one coherent cubic curve attached to a balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b695362f-8f85-5627-b657-8b5759cfc345'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation left_b695362f-8f85-5627-b657-8b5759cfc345.svg'
AUTHOR = 'gpt-6'

class NavigationLeftB695362f(Solo48):
    icon_id = 'navigation-left-b695362f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self) -> None:
        def point(x,y): return (48-y,x)
        self.add_polyline('head',point(8,32),point(20,44),point(32,32))
        self.add_bezier('shaft',point(40,4),(point(20,4),point(20,18),point(20,44)))
        self.relate('connect','head','shaft')

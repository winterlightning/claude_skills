'Curved navigation arrow: preserve the directional sweep with one coherent cubic curve attached to a balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24bc3247-3213-54c7-9085-304a4536c87a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation right_24bc3247-3213-54c7-9085-304a4536c87a.svg'
AUTHOR = 'gpt-6'

class NavigationRight(Solo48):
    icon_id = 'navigation-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'right', 'interface-essential')

    def build(self) -> None:
        def point(x,y): return (y,48-x)
        self.add_polyline('head',point(8,32),point(20,44),point(32,32))
        self.add_bezier('shaft',point(40,4),(point(20,4),point(20,18),point(20,44)))
        self.relate('connect','head','shaft')

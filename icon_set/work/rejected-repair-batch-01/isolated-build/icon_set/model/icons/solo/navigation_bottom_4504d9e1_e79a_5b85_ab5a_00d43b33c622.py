'Curved navigation arrow: preserve the directional sweep with one coherent cubic curve attached to a balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4504d9e1-e79a-5b85-ab5a-00d43b33c622'
SOURCE_PATH = 'pictographic-primitives/arrows/navigation bottom_4504d9e1-e79a-5b85-ab5a-00d43b33c622.svg'
AUTHOR = 'gpt-6'

class NavigationBottom(Solo48):
    icon_id = 'navigation-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'bottom', 'arrows')

    def build(self) -> None:
        def point(x,y): return (x,y)
        self.add_polyline('head',point(8,32),point(20,44),point(32,32))
        self.add_bezier('shaft',point(40,4),(point(20,4),point(20,18),point(20,44)))
        self.relate('connect','head','shaft')

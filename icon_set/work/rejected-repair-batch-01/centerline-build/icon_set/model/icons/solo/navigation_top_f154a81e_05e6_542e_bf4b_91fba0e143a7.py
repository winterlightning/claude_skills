'Curved navigation arrow: preserve the directional sweep with one coherent cubic curve attached to a balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f154a81e-05e6-542e-bf4b-91fba0e143a7'
SOURCE_PATH = 'pictographic-primitives/arrows/navigation top_f154a81e-05e6-542e-bf4b-91fba0e143a7.svg'
AUTHOR = 'gpt-6'

class NavigationTop(Solo48):
    icon_id = 'navigation-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'top', 'arrows')

    def build(self) -> None:
        def point(x,y): return (48-x,48-y)
        self.add_polyline('head',point(8,32),point(20,44),point(32,32))
        self.add_bezier('shaft',point(40,4),(point(20,4),point(20,18),point(20,44)))
        self.relate('connect','head','shaft')

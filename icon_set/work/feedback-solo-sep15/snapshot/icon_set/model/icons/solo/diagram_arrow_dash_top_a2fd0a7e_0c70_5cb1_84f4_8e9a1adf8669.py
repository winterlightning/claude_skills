'Dashed directional arrow: remove a redundant tiny dash, preserving the dashed shaft and full balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2fd0a7e-0c70-5cb1-84f4-8e9a1adf8669'
SOURCE_PATH = 'pictographic-primitives/arrows/diagram arrow dash top_a2fd0a7e-0c70-5cb1-84f4-8e9a1adf8669.svg'
AUTHOR = 'gpt-6'

class DiagramArrowDashTop(Solo48):
    icon_id = 'diagram-arrow-dash-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'top', 'arrows')

    def build(self) -> None:
        def p(x,y): return (48-x,48-y)
        self.add_line('dash',p(24,4),p(24,10))
        self.add_line('shaft',p(24,18),p(24,44))
        self.add_polyline('head',p(8,30),p(24,44),p(40,30))
        self.relate('connect','head','shaft')

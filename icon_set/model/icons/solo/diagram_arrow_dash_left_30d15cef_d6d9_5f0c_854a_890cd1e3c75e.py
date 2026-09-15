'Dashed directional arrow: remove a redundant tiny dash, preserving the dashed shaft and full balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30d15cef-d6d9-5f0c-854a-890cd1e3c75e'
SOURCE_PATH = 'pictographic-primitives/arrows/diagram arrow dash left_30d15cef-d6d9-5f0c-854a-890cd1e3c75e.svg'
AUTHOR = 'gpt-6'

class DiagramArrowDashLeft(Solo48):
    icon_id = 'diagram-arrow-dash-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'left', 'arrows')

    def build(self) -> None:
        def p(x,y): return (48-y,x)
        self.add_line('dash',p(24,4),p(24,10))
        self.add_line('shaft',p(24,18),p(24,44))
        self.add_polyline('head',p(8,30),p(24,44),p(40,30))
        self.relate('connect','head','shaft')

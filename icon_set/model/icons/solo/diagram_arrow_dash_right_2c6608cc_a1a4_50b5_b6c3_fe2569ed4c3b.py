'Dashed directional arrow: remove a redundant tiny dash, preserving the dashed shaft and full balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c6608cc-a1a4-50b5-b6c3-fe2569ed4c3b'
SOURCE_PATH = 'pictographic-primitives/arrows/diagram arrow dash right_2c6608cc-a1a4-50b5-b6c3-fe2569ed4c3b.svg'
AUTHOR = 'gpt-6'

class DiagramArrowDashRight(Solo48):
    icon_id = 'diagram-arrow-dash-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'right', 'arrows')

    def build(self) -> None:
        def p(x,y): return (y,48-x)
        self.add_line('dash',p(24,4),p(24,10))
        self.add_line('shaft',p(24,18),p(24,44))
        self.add_polyline('head',p(8,30),p(24,44),p(40,30))
        self.relate('connect','head','shaft')

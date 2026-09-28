'Dashed directional arrow: remove a redundant tiny dash, preserving the dashed shaft and full balanced arrowhead.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbde1963-5027-5077-ab03-2eb4f5db0a27'
SOURCE_PATH = 'pictographic-primitives/arrows/diagram arrow dash bottom_dbde1963-5027-5077-ab03-2eb4f5db0a27.svg'
AUTHOR = 'gpt-6'

class DiagramArrowDashBottom(Solo48):
    icon_id = 'diagram-arrow-dash-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'bottom', 'arrows')

    def build(self) -> None:
        def p(x,y): return (x,y)
        self.add_line('dash',p(24,4),p(24,10))
        self.add_line('shaft',p(24,18),p(24,44))
        self.add_polyline('head',p(8,30),p(24,44),p(40,30))
        self.relate('connect','head','shaft')

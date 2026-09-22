'A long horizontal shaft ends in a broad right-facing open point. HRECT_M extremes (4,10)-(44,38) fit the wide reference. Lucide arrow-right contributes the shared tip and single chevron contour. Arms mirror about y=24; one true shaft-tip contact. No details omitted.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'b5fa2798-49f6-407b-a04a-a6f57dfb705c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/right from line_b5fa2798-49f6-407b-a04a-a6f57dfb705c.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'arrow-right-with-open-point'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Arrow Pointing Right']
    keywords = ['arrow', 'right', 'with', 'open', 'point']
    def build(self):
        tip=(44,24)
        self.add_line('shaft',(4,24),tip)
        self.add_polyline('point',(30,10),tip,(30,38))
        self.relate('connect','shaft','point')

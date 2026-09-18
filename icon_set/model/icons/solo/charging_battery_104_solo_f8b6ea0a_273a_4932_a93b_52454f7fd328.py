"""Battery with Charging Flash Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = 'pictographic-primitives/other/battery 1_f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'charging-battery-104-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'battery with charging flash symbol')
    def build(self):
        rounded_rect(self,'battery',6,6,34,42,4)
        self.add_polyline('terminal',(34,18),(42,18),(42,30),(34,30))
        self.relate('connect','terminal','battery')
        self.add_polyline('bolt',(25,15),(15,25),(25,23),(18,33))

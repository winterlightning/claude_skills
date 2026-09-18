"""Fork and Knife Dining Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = 'pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fork-and-knife-dining-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'fork and knife dining symbol')
    def build(self):
        circle(self,'outline',24,24,20)
        self.add_polyline('fork',(16,16),(16,23),(20,27),(24,23),(24,16))
        self.add_line('stem',(20,27),(20,34))
        self.relate('connect','fork','stem')
        self.add_line('knife',(33,17),(33,31))

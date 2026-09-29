"""Mobile and Tablet Devices. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3'
SOURCE_PATH = 'pictographic-primitives/state/responsive_5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mobile-and-tablet-devices-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('sub icon', 'mobile and tablet devices')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'phone',6,22,20,42,3)
        self.add_polyline('tablet',(15,13),(15,6),(42,6),(42,34),(29,34))
        self.add_line('phone-rule',(6,34),(20,34))
        self.relate('connect','phone','phone-rule')

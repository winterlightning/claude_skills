"""Mobile and Tablet Devices. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-and-tablet-devices-solo/20260927T153322Z-thuan-mac-1/reference/responsive_5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3.svg'
AUTHOR = "gpt-6"

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
        # Rear tablet is open where the front handset overlaps it.
        rounded_rect(self, 'phone', 6, 22, 20, 42, 3)
        self.add_polyline('tablet', (22, 14), (22, 6), (42, 6), (42, 34), (32, 34))
        self.add_line('phone-rule', (6, 34), (20, 34))
        self.relate('connect', 'phone', 'phone-rule')

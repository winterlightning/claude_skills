"""Desktop Computer Monitor. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '09fbfc2b-65a0-4684-b8ee-0ad753b3dbf9'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/monitor_09fbfc2b-65a0-4684-b8ee-0ad753b3dbf9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'desktop-computer-monitor-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    tags = ('sub icon',)
    keywords = ('sub icon', 'desktop computer monitor')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'screen',4,8,44,31,4)
        self.add_line('divider',(4,23),(44,23))
        self.relate('connect','screen','divider')
        self.add_polyline('stand',(20,31),(18,40),(30,40),(28,31))
        self.relate('connect','screen','stand')

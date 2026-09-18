"""Bluetooth Wireless Connectivity Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '809bf53d-f979-4aa8-bf75-748eb9b9dacd'
SOURCE_PATH = 'pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bluetooth-wireless-connectivity-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'bluetooth wireless connectivity symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_polyline('bluetooth',(17,18),(30,30),(23,34),(23,14),(30,18),(17,30))

"""Wifi Connection Error Warning. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '6b92f4d5-2f2c-4908-98d5-ef4a8b8d7abf'
SOURCE_PATH = 'pictographic-primitives/state/wifi exclamation_6b92f4d5-2f2c-4908-98d5-ef4a8b8d7abf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wifi-connection-error-warning-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'wifi connection error warning')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('left-outer',(4,15),((8,11),(13,9),(16,8)))
        self.add_bezier('right-outer',(32,8),((35,9),(40,11),(44,15)))
        self.add_line('left-inner',(10,25),(15,22))
        self.add_line('right-inner',(33,22),(38,25))
        self.add_line('stem',(24,10),(24,30))
        self.add_dot('dot',(24,40))

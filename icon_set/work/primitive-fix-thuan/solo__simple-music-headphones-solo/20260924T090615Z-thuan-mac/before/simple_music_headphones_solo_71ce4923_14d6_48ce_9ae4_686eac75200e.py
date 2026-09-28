"""Simple Music Headphones. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '71ce4923-14d6-48ce-9ae4-686eac75200e'
SOURCE_PATH = 'pictographic-primitives/other/headphone_71ce4923-14d6-48ce-9ae4-686eac75200e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-music-headphones-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'simple music headphones')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('band',(6,24),(42,24),radius_x=18)
        rounded_rect(self,'left-pad',6,24,16,42,5)
        rounded_rect(self,'right-pad',32,24,42,42,5)
        self.relate('connect','band','left-pad','right-pad')

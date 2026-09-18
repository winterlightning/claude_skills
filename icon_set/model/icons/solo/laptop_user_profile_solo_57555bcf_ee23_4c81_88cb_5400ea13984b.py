"""Laptop User Profile. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '57555bcf-ee23-4c81-88cb-5400ea13984b'
SOURCE_PATH = 'pictographic-primitives/symbol/laptop person_57555bcf-ee23-4c81-88cb-5400ea13984b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laptop-user-profile-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'laptop user profile')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('screen',(8,30),(8,8),(40,8),(40,30))
        self.add_polyline('base',(8,30),(4,40),(44,40),(40,30),(8,30))
        self.relate('connect','screen','base')
        circle(self,'head',24,16,3)
        self.add_arc('shoulders',(17,28),(31,28),radius_x=7,radius_y=2)

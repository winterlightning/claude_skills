"""Heart Gift Box. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '15e4830e-dce1-452c-9f05-87646ea11df9'
SOURCE_PATH = 'pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-gift-box-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    tags = ('sub icon',)
    keywords = ('sub icon', 'heart gift box')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('box',(6,18),(42,18),(42,42),(6,42),closed=True)
        self.add_bezier('bow',(24,18),((9,18),(10,6),(15,6)),((19,6),(22,12),(24,18)),((26,12),(29,6),(33,6)),((38,6),(39,18),(24,18)))
        self.relate('connect','box','bow')
        self.add_bezier('heart',(24,33),((18,30),(16,28),(19,27)),((21,27),(23,28),(24,29)),((25,28),(27,27),(29,27)),((32,27),(30,30),(24,33)))
        self.add_contour('heart-shape','heart',closed=True)

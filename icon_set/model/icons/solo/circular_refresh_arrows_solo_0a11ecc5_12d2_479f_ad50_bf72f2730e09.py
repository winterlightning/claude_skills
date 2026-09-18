"""Circular Refresh Arrows. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH = 'pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-refresh-arrows-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular refresh arrows')
    def build(self):
        self.add_arc('upper-a',(6,24),(24,6),radius_x=18)
        self.add_arc('upper-b',(24,6),(38,13),radius_x=18)
        self.add_contour('upper','upper-a','upper-b')
        self.add_polyline('head-left',(7,16),(6,24),(15,24))
        self.add_arc('lower-a',(42,24),(24,42),radius_x=18)
        self.add_arc('lower-b',(24,42),(10,35),radius_x=18)
        self.add_contour('lower','lower-a','lower-b')
        self.add_polyline('head-right',(33,24),(42,24),(41,32))
        self.relate('connect','upper','head-left')
        self.relate('connect','lower','head-right')

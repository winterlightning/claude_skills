"""Hand Pointing Upwards. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
One open hand contour with rounded raised fingertip; thumb folds left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'eab3080c-0a62-4d7b-b2b0-750ba686504c'
SOURCE_PATH = 'pictographic-primitives/other/hand point 1_eab3080c-0a62-4d7b-b2b0-750ba686504c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pointing-upwards-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'hand pointing upwards')
    def build(self):
        # Plan: One open hand contour with rounded raised fingertip; thumb folds left.
        self.add_bezier('hand',(20,44),((16,40),(12,35),(9,31)),((8,30),(8,30),(8,28)),((8,24),(11,22),(14,25)),((15,26),(16,28),(17,29)))
        self.add_line('finger-left',(17,29),(17,9))
        self.add_arc('fingertip',(17,9),(27,9),radius_x=5)
        self.add_line('finger-right-a',(27,9),(27,20))
        self.add_line('finger-right-b',(27,20),(32,20))
        self.add_arc('palm',(32,20),(40,28),radius_x=8)
        self.add_line('wrist',(40,28),(40,44))
        self.add_contour('outline','hand','finger-left','fingertip','finger-right-a','finger-right-b','palm','wrist')

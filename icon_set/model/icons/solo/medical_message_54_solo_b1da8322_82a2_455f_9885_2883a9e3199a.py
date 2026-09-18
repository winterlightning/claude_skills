"""Medical Consultation Chat Bubble. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'b1da8322-82a2-455f-9885-2883a9e3199a'
SOURCE_PATH = 'pictographic-primitives/other/chat medical cross 1_b1da8322-82a2-455f-9885-2883a9e3199a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'medical-message-54-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'medical consultation chat bubble')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_line('top',(12,6),(36,6))
        self.add_arc('tr',(36,6),(42,12),radius_x=6)
        self.add_line('right',(42,12),(42,28))
        self.add_arc('br',(42,28),(36,34),radius_x=6)
        self.add_line('tail-1',(36,34),(24,34))
        self.add_line('tail-2',(24,34),(14,42))
        self.add_line('tail-3',(14,42),(14,34))
        self.add_line('tail-4',(14,34),(12,34))
        self.add_arc('bl',(12,34),(6,28),radius_x=6)
        self.add_line('left',(6,28),(6,12))
        self.add_arc('tl',(6,12),(12,6),radius_x=6)
        self.add_contour('outline','top','tr','right','br','tail-1','tail-2','tail-3','tail-4','bl','left','tl',closed=True)
        self.add_polyline('cross-h',(17,20),(24,20),(31,20))
        self.add_polyline('cross-v',(24,15),(24,20),(24,25))
        self.relate('connect','cross-h','cross-v')

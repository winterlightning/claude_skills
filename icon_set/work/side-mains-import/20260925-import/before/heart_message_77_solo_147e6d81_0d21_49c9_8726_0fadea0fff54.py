"""Message Bubble with Heart. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Rounded speech enclosure with its complete heart symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '147e6d81-0d21-49c9-8726-0fadea0fff54'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble with heart_147e6d81-0d21-49c9-8726-0fadea0fff54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-message-77-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'message bubble with heart')
    def build(self):
        # Plan: Rounded speech enclosure with its complete heart symbol.
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
        self.add_bezier('heart',(24,25),((20,22),(15,21),(15,17)),((15,15),(21,14),(24,18)),((27,14),(33,15),(33,17)),((33,21),(28,22),(24,25)))
        self.add_contour('heart-shape','heart',closed=True)

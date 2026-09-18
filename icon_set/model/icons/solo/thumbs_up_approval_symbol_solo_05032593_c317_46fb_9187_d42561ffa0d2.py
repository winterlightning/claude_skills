"""Thumbs Up Approval Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '05032593-c317-46fb-9187-d42561ffa0d2'
SOURCE_PATH = 'pictographic-primitives/state/circle thumbs up_05032593-c317-46fb-9187-d42561ffa0d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'thumbs-up-approval-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'thumbs up approval symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_bezier('thumb',(15,31),((19,31),(20,29),(22,25)),((24,23),(26,18),(27,15)),((28,13),(31,15),(30,19)),((30,22),(29,24),(29,24)),((32,24),(33,24),(33,28)),((32,31),(32,34),(30,33)),((23,34),(21,34),(18,32)),((16,32),(15,32),(15,31)))
        self.add_contour('hand','thumb',closed=True)

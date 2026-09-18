"""Location Pin With Check Mark. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '4435680b-318b-4218-8cd9-57af301bba08'
SOURCE_PATH = 'pictographic-primitives/symbol/pin check mark_4435680b-318b-4218-8cd9-57af301bba08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'location-pin-with-check-mark-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'location pin with check mark')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('pin-top',(8,20),(40,20),radius_x=16)
        self.add_bezier('pin-bottom',(40,20),((40,29),(29,40),(24,44)),((19,40),(8,29),(8,20)))
        self.add_contour('outline','pin-top','pin-bottom',closed=True)
        self.add_polyline('check',(17,20),(22,25),(30,18))

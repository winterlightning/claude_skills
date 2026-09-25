"""Completed Task Checklist. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7cfb0a8d-3a06-46ff-b6d2-3ff796fbca84'
SOURCE_PATH = 'pictographic-primitives/content/list_7cfb0a8d-3a06-46ff-b6d2-3ff796fbca84.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'completed-task-checklist-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    tags = ('sub icon',)
    keywords = ('sub icon', 'completed task checklist')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        for y in (16,30):
         self.add_polyline('check-'+str(y),(15,y),(19,y+3),(24,y-1))
         self.add_line('text-'+str(y),(33,y),(33,y))

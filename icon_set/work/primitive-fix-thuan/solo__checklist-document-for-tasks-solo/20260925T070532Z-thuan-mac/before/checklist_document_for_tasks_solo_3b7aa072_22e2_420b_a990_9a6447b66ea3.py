"""Checklist Document for Tasks. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '3b7aa072-22e2-420b-a990-9a6447b66ea3'
SOURCE_PATH = 'pictographic-primitives/symbol/task list_3b7aa072-22e2-420b-a990-9a6447b66ea3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'checklist-document-for-tasks-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'checklist document for tasks')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('page',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        for y in (17,33):
         circle(self,'box-'+str(y),20,y,3)
         self.add_line('text-'+str(y),(31,y+1),(31,y+1))

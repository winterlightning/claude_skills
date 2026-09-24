"""Open Hand Palm. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '92d8dd38-d4cf-4c21-a6ee-c09f59061b77'
SOURCE_PATH = 'pictographic-primitives/other/hand 1_92d8dd38-d4cf-4c21-a6ee-c09f59061b77.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-hand-palm-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'open hand palm')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('hand',(18,44),((13,40),(8,34),(8,30)),((8,26),(12,25),(15,29)))
        self.add_line('index',(15,29),(15,10))
        self.add_arc('finger-a',(15,10),(23,10),radius_x=4)
        self.add_line('joint-a',(23,10),(23,8))
        self.add_arc('finger-b',(23,8),(31,8),radius_x=4)
        self.add_line('joint-b',(31,8),(31,12))
        self.add_arc('finger-c',(31,12),(39,12),radius_x=4)
        self.add_bezier('outer',(39,12),((40,20),(40,27),(40,32)),((40,40),(34,44),(27,44)))
        self.add_line('wrist',(27,44),(18,44))
        self.add_contour('outline','hand','index','finger-a','joint-a','finger-b','joint-b','finger-c','outer','wrist',closed=True)

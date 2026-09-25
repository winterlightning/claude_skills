"""Minimalist Pig Face. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '2878cc5b-7eb0-476d-b3f7-1ad79cba16a4'
SOURCE_PATH = 'pictographic-primitives/state/pig_2878cc5b-7eb0-476d-b3f7-1ad79cba16a4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'minimalist-pig-face-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'minimalist pig face')
    def build(self):
        self.add_bezier('pig',(14,10),((11,8),(8,6),(6,6)),((6,14),(8,18),(10,21)),((8,31),(14,42),(24,42)),((34,42),(40,31),(38,21)),((40,18),(42,14),(42,6)),((40,6),(37,8),(34,10)),((28,6),(20,6),(14,10)))
        self.add_contour('head','pig',closed=True)
        circle(self,'snout',24,30,3)
        self.add_dot('eye-left',(18,20))
        self.add_dot('eye-right',(30,20))

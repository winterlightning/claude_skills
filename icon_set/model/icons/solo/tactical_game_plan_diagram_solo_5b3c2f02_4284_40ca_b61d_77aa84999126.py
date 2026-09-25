"""Tactical Game Plan Diagram. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '5b3c2f02-4284-40ca-b61d-77aa84999126'
SOURCE_PATH = 'pictographic-primitives/state/strategy_5b3c2f02-4284-40ca-b61d-77aa84999126.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tactical-game-plan-diagram-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    tags = ('sub icon',)
    keywords = ('sub icon', 'tactical game plan diagram')
    def build(self):
        rounded_rect(self,'outline',6,6,42,42,5)
        circle(self,'start',18,30,3)
        self.add_bezier('route',(18,27),((18,27),(31,28),(31,18)))
        self.add_polyline('head',(27,22),(31,18),(33,21))
        self.relate('connect','start','route')
        self.relate('connect','route','head')
        self.add_line('cross-a',(15,15),(19,19))
        self.add_line('cross-b',(15,19),(19,15))
        self.relate('connect','cross-a','cross-b')

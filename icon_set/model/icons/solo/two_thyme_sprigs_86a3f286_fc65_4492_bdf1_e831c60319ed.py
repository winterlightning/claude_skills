"""Fresh Thyme Sprigs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86a3f286-fc65-4492-bdf1-e831c60319ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/thyme_86a3f286-fc65-4492-bdf1-e831c60319ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-thyme-sprigs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('thyme', 'herb', 'sprig', 'stem', 'branch', 'seasoning', 'plant')

    def build(self):
        # Plan: Two thyme sprigs with staggered upward branches. Lucide sprout shared attachment nodes. Fine subordinate branch omitted; differing stem heights retained. Envelope (6,6)-(42,42).
        self.add_polyline('stem-left',(14,6),(14,16),(14,30),(14,42))
        self.add_polyline('stem-right',(34,12),(34,24),(34,38),(34,42))
        for i,y in enumerate((16,30)):
         self.add_bezier(f'left-branch-{i}',(6,y-8),((6,y-4),(10,y),(14,y)),((18,y),(20,y-4),(20,y-8)));self.relate('connect',f'left-branch-{i}','stem-left')
        for i,y in enumerate((24,38)):
         self.add_bezier(f'right-branch-{i}',(28,y-8),((28,y-4),(30,y),(34,y)),((38,y),(42,y-4),(42,y-8)));self.relate('connect',f'right-branch-{i}','stem-right')

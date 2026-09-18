"""Hand Facing Down. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'acc6f9a7-f1e5-46cf-961e-ce00f3dd0639'
SOURCE_PATH = 'pictographic-primitives/other/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-facing-down-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'hand facing down')
    def build(self):
        self.add_bezier('palm',(4,18),((9,18),(14,20),(19,16)),((24,12),(29,8),(32,8)),((34,8),(39,13),(44,18)),((44,22),(42,25),(38,23)),((34,20),(31,20),(28,23)),((22,28),(16,29),(4,27)))
        self.add_line('wrist',(4,27),(4,18))
        self.add_contour('outline','palm','wrist',closed=True)
        self.add_bezier('crease',(17,40),((23,40),(31,34),(38,31)))

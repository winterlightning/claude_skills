"""Verified Scalloped Seal Badge. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '728427d6-1a96-46e6-afb1-88fabe63ca21'
SOURCE_PATH = 'pictographic-primitives/interface-essential/check badge_728427d6-1a96-46e6-afb1-88fabe63ca21.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'verified-scalloped-seal-badge-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    tags = ('sub icon',)
    keywords = ('sub icon', 'verified scalloped seal badge')
    def build(self):
        self.add_bezier('seal',(24,4),((29,4),(29,10),(34,10)),((39,10),(38,17),(42,20)),((44,24),(40,27),(39,32)),((39,38),(32,38),(29,42)),((24,44),(21,40),(16,39)),((10,39),(10,32),(6,29)),((4,24),(8,21),(9,16)),((9,10),(16,10),(19,6)),((21,5),(23,4),(24,4)))
        self.add_contour('outline','seal',closed=True)
        self.add_polyline('check',(16,24),(22,29),(31,20))

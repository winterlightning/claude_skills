"""Access Key Card. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'db1da222-3377-4c97-b61f-22ec2ef4ed83'
SOURCE_PATH = 'pictographic-primitives/other/key vertical rectangcle_db1da222-3377-4c97-b61f-22ec2ef4ed83.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'access-key-card-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'access key card')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'card',10,4,38,44,4)
        circle(self,'key-bow',24,17,4)
        self.add_polyline('key-stem',(24,21),(24,32),(28,32))
        self.relate('connect','key-bow','key-stem')

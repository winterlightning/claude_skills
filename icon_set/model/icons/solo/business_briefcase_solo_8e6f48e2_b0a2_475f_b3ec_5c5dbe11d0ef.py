"""Business briefcase.

Construction reference: briefcase.
Blank front and raised handle; no badges or latch.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '8e6f48e2-b0a2-475f-b3ec-5c5dbe11d0ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/case_8e6f48e2-b0a2-475f-b3ec-5c5dbe11d0ef.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'business-briefcase-solo-8e6f48e2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('business-briefcase',)
    keywords = ('business', 'briefcase')

    def build(self):
        # Body owns the centered handle; 8-unit handle opening above its top.
        box(self,'body',4,16,44,40,4,nodes=((16,16),(32,16)))
        path(self,'handle',(16,16),[('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,16))])
        self.relate('connect','body','handle')

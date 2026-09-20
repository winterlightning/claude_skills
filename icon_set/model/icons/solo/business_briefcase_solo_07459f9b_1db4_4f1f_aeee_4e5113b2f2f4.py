"""Business briefcase.

Construction reference: briefcase.
Blank front and raised handle; no badges or latch.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '07459f9b-1db4-4f1f-aeee-4e5113b2f2f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/pg_app_cdn/all_icons/07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'business-briefcase-solo-07459f9b'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('business-briefcase',)
    keywords = ('business', 'briefcase')

    def build(self):
        # Body owns the centered handle; 8-unit handle opening above its top.
        box(self,'body',4,16,44,40,4,nodes=((16,16),(32,16)))
        path(self,'handle',(16,16),[('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,16))])
        self.relate('connect','body','handle')

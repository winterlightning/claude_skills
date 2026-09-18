"""User Profile with Selection Square.
Symbol plan: Circular head and smooth shoulders use shared human reference, detached head-to-body ink gap 4. Separate modifier; deliberate left/right placement preserved.
User explicitly requested the complete combined subject on SOLO48.
References: supplied source render; local Lucide original and atomic geometry sheet
(triangle-alert, user-round-plus, file-up, battery-charging, plug-zap, scan-face,
clapperboard, badge-check, paw-print, car, wrench, shirt, chart-pie, delete).
Human subjects follow icon_set/references/human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
from ._container_content_batch import path, cross, contacts, bust, car, bolt

SOURCE_ICON_ID = '074e5864-86d5-4165-aa6c-bccd7b6883f3'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/074e5864-86d5-4165-aa6c-bccd7b6883f3.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'user-profile-with-selection-square-batch-033'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('user profile with selection square',)
    def build(self):
        bust(self,'user',cx=30,cy=14,r=6,left=16,right=44,bottom=40)
        self.add_polyline('card',(4,8),(12,8),(12,20),(4,20),closed=True)
        contacts(self)

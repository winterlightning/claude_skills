"""User Profile with ID Card.
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

SOURCE_ICON_ID = '91136439-ae9e-4bd7-833a-71e612217d7c'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/91136439-ae9e-4bd7-833a-71e612217d7c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'user-with-id-card-content'
    keyshape = Keyshape.HRECT_L
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('user profile with id card',)
    def build(self):
        bust(self,'user',cx=18,cy=14,r=6,left=4,right=32,bottom=40)
        self.add_polyline('card',(36,8),(44,8),(44,20),(36,20),closed=True)
        contacts(self)

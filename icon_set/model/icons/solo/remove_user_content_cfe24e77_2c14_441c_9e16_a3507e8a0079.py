"""Remove User Profile.
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

SOURCE_ICON_ID = 'cfe24e77-2c14-441c-9e16-a3507e8a0079'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/cfe24e77-2c14-441c-9e16-a3507e8a0079.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'remove-user-content'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('remove user profile',)
    def build(self):
        bust(self,'user',cx=18,cy=14,r=6,left=4,right=32,bottom=40)
        self.add_line('minus',(36,14),(44,14))
        contacts(self)

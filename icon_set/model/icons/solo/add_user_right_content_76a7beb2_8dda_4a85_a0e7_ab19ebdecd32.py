"""Add New User Profile.
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

SOURCE_ICON_ID = '76a7beb2-8dda-4a85-a0e7-ab19ebdecd32'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/76a7beb2-8dda-4a85-a0e7-ab19ebdecd32.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'add-user-right-content'
    keyshape = Keyshape.HRECT_L
    category = 'symbol'
    categories = ('symbol',)
    tags = ('sub icon',)
    keywords = ('add new user profile',)
    def build(self):
        bust(self,'user',cx=18,cy=14,r=6,left=4,right=32,bottom=40)
        cross(self,'plus',40,14,4)
        contacts(self)

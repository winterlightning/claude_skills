"""Car and Wrench Repair Icon.
Symbol plan: Car front beneath an open-ended wrench. Repeated wheel stems and mirrored car shape; simplified headlights.
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

SOURCE_ICON_ID = '7a2552f6-ae52-4b87-a510-432f8be7e0ec'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/7a2552f6-ae52-4b87-a510-432f8be7e0ec.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-wrench-service-content-top'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('car and wrench repair icon',)
    def build(self):
        car(self,'car',top=25,bottom=36)
        path(self,'wrench',(4,8),('A',(4,18),5,5,True))
        path(self,'wrench-right',(44,18),('A',(44,8),5,5,True))
        self.add_line('wrench-shaft',(9,13),(39,13))
        self.relate('connect','wrench','wrench-shaft')
        self.relate('connect','wrench-right','wrench-shaft')
        contacts(self)

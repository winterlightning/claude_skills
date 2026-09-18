"""Disabled Battery Symbol.
Symbol plan: Battery and diagonal disable stroke. Interrupted enclosure avoids cramped wedges.
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

SOURCE_ICON_ID = '49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'disabled-battery-content'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('disabled battery symbol',)
    def build(self):
        path(self,'body-top',(4,27),('L',(4,12)),('A',(8,8),4,4,True),('L',(32,8)),('A',(36,12),4,4,True),('L',(36,16)))
        path(self,'body-bottom',(36,28),('L',(36,36)),('A',(32,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True))
        self.add_line('terminal',(44,20),(44,28))
        self.add_line('slash',(4,40),(36,8))
        self.relate('connect','body-top','slash')
        self.relate('connect','body-bottom','slash')
        contacts(self)

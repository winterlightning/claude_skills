"""Battery with Charging Flash Symbol.
Symbol plan: Open battery outline reserves room for a large bolt, following Lucide battery-charging.
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

SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'charging-battery-104-solo'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('battery with charging flash symbol',)
    def build(self):
        path(self,'left',(14,8),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,36)),('A',(8,40),4,4,False),('L',(11,40)))
        path(self,'right',(36,14),('L',(36,36)),('A',(32,40),4,4,True),('L',(31,40)))
        self.add_line('terminal',(44,20),(44,28))
        bolt(self,'bolt',((25,8),(16,25),(25,25),(20,40)))
        contacts(self)

"""Automotive Service Car Lift.
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

SOURCE_ICON_ID = '245fc45b-1580-4530-93b9-2d61d874ff67'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/245fc45b-1580-4530-93b9-2d61d874ff67.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-wrench-service-content'
    keyshape = Keyshape.HRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('automotive service car lift',)
    def build(self):
        car(self,'car',top=8,bottom=20)
        path(self,'wrench',(4,30),('A',(4,40),5,5,True))
        path(self,'wrench-right',(44,40),('A',(44,30),5,5,True))
        self.add_line('wrench-shaft',(9,35),(39,35))
        self.relate('connect','wrench','wrench-shaft')
        self.relate('connect','wrench-right','wrench-shaft')
        contacts(self)

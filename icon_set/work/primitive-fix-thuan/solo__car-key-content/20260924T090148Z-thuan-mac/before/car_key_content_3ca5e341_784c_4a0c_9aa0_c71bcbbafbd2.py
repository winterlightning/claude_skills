"""Bed with Key.
Symbol plan: Front-view car beneath a horizontal key; rendered reference depicts a car, despite its old bed label.
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

SOURCE_ICON_ID = '3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-key-content'
    keyshape = Keyshape.VRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('bed with key',)
    def build(self):
        car(self,'car',top=26,bottom=40)
        circle(self,'key-bow',34,10,6)
        self.add_line('key-shaft',(8,10),(28,10))
        self.add_line('key-tooth',(14,10),(14,17))
        self.relate('connect','key-bow','key-shaft')
        contacts(self)

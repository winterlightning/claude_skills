"""Car with Dollar Sign.
Symbol plan: Car and dollar; currency will use existing glyph layout rather than this draft symbolic plan.
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

SOURCE_ICON_ID = 'f824dc04-d2a0-4ef6-9b58-21abe8b9584f'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f824dc04-d2a0-4ef6-9b58-21abe8b9584f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-dollar-content'
    keyshape = Keyshape.VRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('car with dollar sign',)
    def build(self):
        car(self,'car',top=26,bottom=40)
        path(self,'dollar',(28,4),('L',(22,4)),('A',(22,12),4,4,False),('L',(26,12)),('A',(26,20),4,4,True),('L',(20,20)))
        self.add_line('currency-stem-top',(24,2),(24,4))
        self.add_line('currency-stem-bottom',(24,20),(24,22))
        contacts(self)

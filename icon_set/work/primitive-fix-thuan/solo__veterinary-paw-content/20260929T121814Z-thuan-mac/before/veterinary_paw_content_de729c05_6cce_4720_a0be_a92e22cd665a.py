"""Veterinary Care Paw Print.
Symbol plan: Three-toe paw with medical plus in the broad pad; mirrored toes and pad.
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

SOURCE_ICON_ID = 'de729c05-6cce-4720-a0be-a92e22cd665a'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/de729c05-6cce-4720-a0be-a92e22cd665a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'veterinary-paw-content'
    keyshape = Keyshape.SQUARE
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('veterinary care paw print',)
    def build(self):
        circle(self,'toe-top',24,8,2)
        circle(self,'toe-left',8,14,2)
        circle(self,'toe-right',40,14,2)
        path(self,'pad',(14,42),('A',(8,36),6,6,True),('L',(8,34)),('A',(24,20),16,14,True),('A',(40,34),16,14,True),('L',(40,36)),('A',(34,42),6,6,True),('L',(14,42)),closed=True)
        cross(self,'medical',24,31,2)
        contacts(self)

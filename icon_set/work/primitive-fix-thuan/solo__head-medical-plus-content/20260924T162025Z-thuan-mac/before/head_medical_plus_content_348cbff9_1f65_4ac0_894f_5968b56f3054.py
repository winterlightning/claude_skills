"""Human Head with Medical Plus Sign.
Symbol plan: Side head silhouette with medical plus; retain forehead/nose direction and neck opening.
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

SOURCE_ICON_ID = '348cbff9-1f65-4ac0-894f-5968b56f3054'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/348cbff9-1f65-4ac0-894f-5968b56f3054.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'head-medical-plus-content'
    keyshape = Keyshape.VRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('human head with medical plus sign',)
    def build(self):
        path(self,'head',(12,44),('L',(12,34)),('A',(8,24),16,16,True),('L',(8,18)),('A',(22,4),14,14,True),('A',(36,18),14,14,True),('L',(40,26)),('L',(34,28)),('L',(34,36)),('L',(28,36)),('L',(28,44)))
        cross(self,'medical',22,20,5)
        contacts(self)

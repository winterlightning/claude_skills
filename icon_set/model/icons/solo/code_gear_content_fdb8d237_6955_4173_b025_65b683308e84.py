"""Code Programming Gear Settings.
Symbol plan: Gear silhouette with external angle brackets; restrained tooth count.
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

SOURCE_ICON_ID = 'fdb8d237-6955-4173-b025-65b683308e84'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/fdb8d237-6955-4173-b025-65b683308e84.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'code-gear-content'
    keyshape = Keyshape.HRECT_L
    category = 'symbol'
    categories = ('symbol',)
    tags = ('sub icon',)
    keywords = ('code programming gear settings',)
    def build(self):
        self.add_polyline('gear',(20,8),(28,8),(28,15),(34,19),(34,29),(28,33),(28,40),(20,40),(20,33),(14,29),(14,19),(20,15),closed=True)
        self.add_polyline('code-left',(6,18),(4,24),(6,30))
        self.add_polyline('code-right',(42,18),(44,24),(42,30))
        contacts(self)

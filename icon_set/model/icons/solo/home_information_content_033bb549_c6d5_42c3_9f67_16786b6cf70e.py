"""Home Property Information.
Symbol plan: House silhouette with two information rules; preserve source document-like layout.
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

SOURCE_ICON_ID = '033bb549-c6d5-42c3-9f67-16786b6cf70e'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/033bb549-c6d5-42c3-9f67-16786b6cf70e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'home-information-content'
    keyshape = Keyshape.VRECT_L
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('home property information',)
    def build(self):
        self.add_polyline('house',(8,18),(24,4),(40,18),(40,28),(8,28),closed=True)
        self.add_line('line-one',(8,36),(32,36))
        self.add_line('line-two',(8,44),(40,44))
        contacts(self)

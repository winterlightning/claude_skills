"""Fragile and This Side Up.
Symbol plan: Fragile wine glass beside upright shipping arrow; distinct shipping labels retain their side-by-side reading.
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

SOURCE_ICON_ID = '25d79f58-c01d-4a82-8565-6562d2773dd8'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/25d79f58-c01d-4a82-8565-6562d2773dd8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fragile-upright-content'
    keyshape = Keyshape.SQUARE
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('fragile and this side up',)
    def build(self):
        path(self,'glass',(6,6),('L',(20,6)),('L',(20,20)),('A',(6,20),7,7,True),('L',(6,6)),closed=True)
        self.add_line('stem',(13,27),(13,42))
        self.relate('connect','glass','stem')
        self.add_line('foot',(6,42),(20,42))
        self.add_polyline('arrow',(28,14),(35,6),(42,14))
        self.add_line('up',(35,6),(35,42))
        contacts(self)

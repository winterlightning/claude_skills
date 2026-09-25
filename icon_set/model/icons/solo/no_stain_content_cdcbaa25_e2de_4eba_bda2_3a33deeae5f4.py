"""No Stain Symbol.
Symbol plan: Organic stain and diagonal prohibition stroke; asymmetrical lobes distinguish a stain from a badge.
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

SOURCE_ICON_ID = 'cdcbaa25-e2de-4eba-bda2-3a33deeae5f4'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/cdcbaa25-e2de-4eba-bda2-3a33deeae5f4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'no-stain-content'
    keyshape = Keyshape.SQUARE
    category = 'symbol'
    categories = ('symbol',)
    tags = ('sub icon',)
    keywords = ('no stain symbol',)
    def build(self):
        path(self,'stain',(18,6),('A',(26,14),8,8,True),('L',(34,14)),('A',(42,22),8,8,True),('A',(34,30),8,8,True),('L',(26,30)),('A',(18,38),8,8,True),('A',(10,30),8,8,True),('L',(10,22)),('A',(6,18),4,4,True),('A',(14,10),8,8,True),('L',(18,6)),closed=True)
        self.add_line('slash',(6,6),(42,42))
        self.relate('connect','stain','slash')
        contacts(self)

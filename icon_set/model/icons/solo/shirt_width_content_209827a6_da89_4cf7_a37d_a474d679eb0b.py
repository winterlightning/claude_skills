"""Adjustable T-shirt width arrows.
Symbol plan: T-shirt above double-headed size arrow; neckline is intrinsic clothing detail.
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

SOURCE_ICON_ID = '209827a6-da89-4cf7-a37d-a474d679eb0b'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/209827a6-da89-4cf7-a37d-a474d679eb0b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'shirt-width-content'
    keyshape = Keyshape.HRECT_L
    category = 'symbol'
    tags = ('sub icon',)
    keywords = ('adjustable t-shirt width arrows',)
    def build(self):
        self.add_polyline('shirt',(16,8),(12,14),(16,18),(16,27),(32,27),(32,18),(36,14),(32,8))
        path(self,'neck',(32,8),('L',(28,8)),('A',(20,8),4,2,True),('L',(16,8)))
        self.relate('connect','shirt','neck')
        self.add_polyline('width',(4,35),(44,35))
        self.add_polyline('left',(8,30),(4,35),(9,40))
        self.add_polyline('right',(40,30),(44,35),(39,40))
        contacts(self)

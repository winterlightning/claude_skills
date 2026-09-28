"""Keyboard Backspace Key Symbol.
Symbol plan: Left-pointing backspace key with central X; shared center for diagonal marks.
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

SOURCE_ICON_ID = 'f52af45c-34ba-4c0c-a151-62677a3ff4ab'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f52af45c-34ba-4c0c-a151-62677a3ff4ab.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'backspace-key-content'
    keyshape = Keyshape.HRECT_M
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('keyboard backspace key symbol',)
    def build(self):
        self.add_polyline('key',(16,10),(44,10),(44,38),(16,38),(4,24),closed=True)
        self.add_polyline('x-one',(24,19),(29,24),(34,29))
        self.add_polyline('x-two',(24,29),(29,24),(34,19))
        contacts(self)

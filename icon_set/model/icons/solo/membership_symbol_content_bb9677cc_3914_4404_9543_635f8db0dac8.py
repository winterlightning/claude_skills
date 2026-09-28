"""Element Of Mathematical Symbol.
Symbol plan: Open membership mark with central bar; source shape retained, no substitute character.
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

SOURCE_ICON_ID = 'bb9677cc-3914-4404-9543-635f8db0dac8'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/bb9677cc-3914-4404-9543-635f8db0dac8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'membership-symbol-content'
    keyshape = Keyshape.VRECT_M
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('element of mathematical symbol',)
    def build(self):
        path(self,'bowl',(38,4),('L',(30,4)),('A',(10,24),20,20,False),('A',(30,44),20,20,False),('L',(38,44)))
        self.add_line('bar',(10,24),(34,24))
        self.relate('connect','bowl','bar')
        contacts(self)

"""Electric Plug with Lightning Bolt.
Symbol plan: Plug prongs and rounded body with central lightning mark; vertical symmetry except bolt.
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

SOURCE_ICON_ID = '1fed8230-55dc-4ab0-90b8-ea4b658f60cf'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/1fed8230-55dc-4ab0-90b8-ea4b658f60cf.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'electric-plug-bolt-content'
    keyshape = Keyshape.SQUARE
    category = 'symbol'
    categories = ('symbol',)
    tags = ('sub icon',)
    keywords = ('electric plug with lightning bolt',)
    def build(self):
        # Move the bolt beside the plug to retain a readable full-size mark.
        self.add_line('pin-left',(10,14),(10,22))
        self.add_line('pin-right',(18,14),(18,22))
        path(self,'body',(6,22),('L',(22,22)),('L',(22,26)),('A',(14,34),8,8,True),('A',(6,26),8,8,True),('L',(6,22)),closed=True)
        self.add_line('cord',(14,34),(14,42))
        self.relate('connect','body','pin-left')
        self.relate('connect','body','pin-right')
        self.relate('connect','body','cord')
        bolt(self,'bolt',((42,6),(30,17),(42,17),(32,28)))
        contacts(self)

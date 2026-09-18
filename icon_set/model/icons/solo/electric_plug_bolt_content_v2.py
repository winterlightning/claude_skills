# Variant of electric-plug-bolt-content; parent file remains unchanged.
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

class DrawingVariant2(Solo48):
    icon_id = 'electric-plug-bolt-content-v2'
    variant_of = 'electric-plug-bolt-content'
    variant_label = 'Embedded lightning'
    keyshape = Keyshape.VRECT_L
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('electric plug with lightning bolt',)

    def build(self):
        self.add_line('pin-left',(16,4),(16,10))
        self.add_line('pin-right',(32,4),(32,10))
        path(self,'body',(8,10),('L',(40,10)),('L',(40,26)),('A',(28,38),12,12,True),('L',(24,38)),('L',(20,38)),('A',(8,26),12,12,True),('L',(8,10)),closed=True)
        self.add_line('cord',(24,38),(24,44))
        for n in ['pin-left','pin-right','cord']:self.relate('connect','body',n)
        bolt(self,'bolt',((27,19),(18,25),(30,25),(22,29)))
        contacts(self)

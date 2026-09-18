"""Broaden the bottle body while retaining the pump and sloping shoulders.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class LiquidSoapDispenserBottleVariant2(Container64):
    icon_id = 'liquid-soap-dispenser-bottle-v2'
    variant_of = 'liquid-soap-dispenser-bottle'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'bottle',(26,12),[('L',(38,12)),('L',(41,18)),('L',(52,18)),('A',(58,24),6,6,True),('L',(58,56)),('A',(52,62),6,6,True),('L',(12,62)),('A',(6,56),6,6,True),('L',(6,24)),('A',(12,18),6,6,True),('L',(23,18)),('L',(26,12))],True)
        line('stem',(32,12),(32,2));path(self,'pump',(40,2),[('L',(24,2)),('A',(18,8),6,6,False)]);join('stem','bottle');join('stem','pump')

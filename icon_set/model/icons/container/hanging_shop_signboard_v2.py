"""Taller hanging sign with a shorter suspension and unchanged support.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class HangingShopSignboardVariant2(Container64):
    icon_id = 'hanging-shop-signboard-v2'
    variant_of = 'hanging-shop-signboard'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'panel',2,16,52,60,3)
        path(self,'support',(2,2),[('L',(56,2)),('A',(62,8),6,6,True),('L',(62,62))])
        for x in (12,44):
         line(f'hanger-{x}',(x,2),(x,16));join('support',f'hanger-{x}');join('panel',f'hanger-{x}')

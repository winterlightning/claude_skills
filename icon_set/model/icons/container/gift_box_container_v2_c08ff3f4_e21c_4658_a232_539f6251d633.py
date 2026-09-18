"""Use a compact bow and thin lid above a taller gift box.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'gpt-6'

class GiftBoxContainerVariant2(Container64):
    icon_id = 'gift-box-container-v2'
    variant_of = 'gift-box-container'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        line('lid',(2,20),(62,20))
        path(self,'box',(6,20),[('L',(6,56)),('A',(12,62),6,6,False),('L',(52,62)),('A',(58,56),6,6,False),('L',(58,20))]);join('box','lid')
        for side in (-1,1):
         def p(x,y):return (32+side*x,y)
         path(self,f'bow-{side}',p(0,12),[('L',p(10,2)),('A',p(18,10),8,8,side>0),('L',p(0,12))],True)
         # Bow loops attach to the short central knot.
        join('bow--1','bow-1')
        line('knot',(32,12),(32,20));join('knot','bow--1');join('knot','bow-1');join('knot','lid')

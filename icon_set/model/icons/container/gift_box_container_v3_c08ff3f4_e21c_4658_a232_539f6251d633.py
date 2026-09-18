"""Gift proportions before hosting size.
Human reference: icon_set/references/human_ref/full_body_ref.png.
The two figures retain circular outlined heads, torsos, arms and separate legs. Head ink to upper torso ink gap is exactly 4 units.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'gpt-6'

class GiftBoxContainerVariant3(Container64):
    icon_id = 'gift-box-container-v3'
    variant_of = 'gift-box-container-v2'
    variant_label = 'Gift proportions before hosting size'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()
    def build(self):
        line,poly=self.add_line,self.add_polyline
        def join(a,b):self.relate("connect",a,b)
        line('lid',(2,22),(62,22))
        path(self,'box',(6,22),[('L',(6,56)),('A',(12,62),6,6,False),('L',(52,62)),('A',(58,56),6,6,False),('L',(58,22))]);join('box','lid')
        for side in (-1,1):
         def p(x,y):return (32+side*x,y)
         path(self,f'bow-{side}',p(8,14),[('L',p(16,2)),('A',p(24,10),8,8,side>0),('A',p(8,14),16,8,side>0)],True)
        poly('knot',(24,14),(32,22),(40,14));join('knot','lid');join('knot','bow--1');join('knot','bow-1')

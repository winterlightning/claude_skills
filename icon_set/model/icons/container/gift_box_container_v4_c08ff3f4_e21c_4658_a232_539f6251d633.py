# Variant of gift-box-container; parent file remains unchanged.
"""Gift box with compact mirrored bow, overhanging lid, and deep body.
SQUARE visible extremes (0,0)-(64,64), native 4-unit stroke.
Lucide gift original and atomic-debug inform the lid and rounded bow loops.
Paired symbols measured separately; native 32 does not fit. Some 24-unit
prototypes fit; full-height people still require a compact redraw.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'gpt-6'

class GiftBoxContainerVariant4(Container64):
    icon_id = 'gift-box-container-v4'
    variant_of = 'gift-box-container'
    variant_label = 'Clear bow and overhanging lid'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('gift', 'box', 'container')

    def build(self):
        # Shared axis: mirrored rounded bow loops, projecting lid, deeper body.
        rect(self, 'lid', 2, 24, 62, 32, 2)
        path(self, 'box', (6,32), [('L',(6,58)),('A',(10,62),4,4,False),('L',(54,62)),('A',(58,58),4,4,False),('L',(58,32))])
        self.relate('connect','box','lid')
        for side in (-1,1):
            def p(x,y): return (32+side*x,y)
            path(self, f'bow-{side}', p(4,16), [('L',p(14,16)),('A',p(14,2),7,7,side<0),('A',p(7,9),7,7,side<0),('L',p(4,16))], True)
        self.add_polyline('knot',(28,16),(32,24),(36,16))
        for name in ('lid','bow--1','bow-1'):
            self.relate('connect','knot',name)

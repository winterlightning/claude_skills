# Variant of gift-box-container-v5; parent file remains unchanged.
"""Gift box following user reference: broad bow on lid, empty box face.
SQUARE visible extremes (0,0)-(64,64), native 4-unit stroke.
User clipboard b296dcc9-5ef6-4656-8612-b557f0b5702d is the visual reference.
Lucide gift informs geometric construction. Bow bases share the lid edge
without duplicate strokes; the ribbon detail appears on the lid only.
Paired symbols measured separately; native 32 does not fit. Some 24-unit
prototypes fit; full-height people still require a compact redraw.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'gpt-6'

class GiftBoxContainerVariant6(Container64):
    icon_id = 'gift-box-container-v6'
    variant_of = 'gift-box-container-v5'
    variant_label = 'Reference bow with empty box'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('gift', 'box', 'container')

    def build(self):
        # Broad mirrored loops converge directly onto the lid; no body ribbon.
        path(self, 'lid', (14,20), [('L',(6,20)),('A',(2,24),4,4,False),('L',(2,28)),('A',(6,32),4,4,False),('L',(58,32)),('A',(62,28),4,4,False),('L',(62,24)),('A',(58,20),4,4,False),('L',(50,20))])
        path(self, 'box', (6,32), [('L',(6,56)),('A',(12,62),6,6,False),('L',(52,62)),('A',(58,56),6,6,False),('L',(58,32))])
        self.relate('connect','box','lid')
        for side in (-1,1):
            def p(x,y): return (32+side*x,y)
            path(self, f'bow-{side}', p(0,20), [('A',p(18,2),18,18,side>0),('A',p(18,20),9,9,side>0),('L',p(0,20))], True)
            self.relate('connect', f'bow-{side}', 'lid')
        self.relate('connect', 'bow--1', 'bow-1')
        # Ribbon detail belongs to the lid only; the box face stays empty.
        for x, bow in ((26,'bow--1'),(38,'bow-1')):
            name=f'lid-ribbon-{x}'
            self.add_line(name,(x,20),(x,32))
            self.relate('connect',name,'lid')
            self.relate('connect',name,bow)

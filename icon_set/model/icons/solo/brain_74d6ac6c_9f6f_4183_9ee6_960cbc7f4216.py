'Brain: smooth paired lobes and a shared central fissure; retain a small fold in each hemisphere. Lucide brain informs rounded lobe construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74d6ac6c-9f6f-4183-9ee6-960cbc7f4216'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_74d6ac6c-9f6f-4183-9ee6-960cbc7f4216.svg'
AUTHOR = 'gpt-6'

class BrainArtificialIntelligence(Solo48):
    icon_id = 'brain-artificial-intelligence'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', 'artificial-intelligence')

    def build(self) -> None:
        # Mirrored hemispheres share a straight fissure; lobes use coherent smooth curves.
        for name,sign in (('left',-1),('right',1)):
            def p(x,y): return (24+sign*x,y)
            self.add_bezier(name+'-upper',p(0,12),(p(0,8),p(2,6),p(6,6)),(p(10,6),p(12,9),p(12,14)))
            self.add_bezier(name+'-outer',p(12,14),(p(16,14),p(18,18),p(18,22)),(p(18,26),p(16,29),p(14,30)))
            self.add_bezier(name+'-lower',p(14,30),(p(16,37),p(12,42),p(7,42)),(p(3,42),p(0,40),p(0,36)))
            self.add_contour(name,name+'-upper',name+'-outer',name+'-lower')
            self.add_bezier(name+'-fold',p(12,14),(p(12,17),p(11,20),p(9,20)))
            self.relate('connect',name,name+'-fold')
        self.add_line('fissure',(24,12),(24,36))
        self.relate('connect','fissure','left')
        self.relate('connect','fissure','right')
        self.relate('connect','left','right')

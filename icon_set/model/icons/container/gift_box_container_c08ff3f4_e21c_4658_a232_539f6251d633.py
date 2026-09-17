"""Gift Box with Bow: independently authored container.

Construction plan: Two mirrored bow loops attach to a horizontal lid above a rounded box; no unrequested ribbons.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg. Lucide gift original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'gpt-6'


class GiftBoxContainer(Container64):
    icon_id = 'gift-box-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('gift', 'box', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'lid',2,30,62,38,2)
        path(self,'box',(6,38),[('L',(6,56)),('A',(12,62),6,6,False),('L',(52,62)),('A',(58,56),6,6,False),('L',(58,38))]);join('box','lid')
        for side in (-1,1):
            def p(x,y):return (32+side*x,y)
            path(self,f'bow-{side}',p(8,22),[('L',p(16,2)),('A',p(26,12),10,10,side>0),('A',p(8,22),18,10,side>0)],True)
        poly('knot',(24,22),(32,30),(40,22))
        join('knot','lid');join('knot','bow--1');join('knot','bow-1')

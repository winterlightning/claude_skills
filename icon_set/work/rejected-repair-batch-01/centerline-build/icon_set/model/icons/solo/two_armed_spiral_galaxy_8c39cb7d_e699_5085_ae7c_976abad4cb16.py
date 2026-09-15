"""Two sweeping curved arms wind around a tight central spiral. The outer ends remain open on opposite sides, giving the galaxy a wide, slightly tilted oval silhouette.

HRECT_XL visible bounds (2,6)-(46,42); two rotationally paired open arms with coherent inward winding. Dense center turns reduced. No useful Lucide galaxy match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c39cb7d-e699-5085-ae7c-976abad4cb16'
SOURCE_PATH = 'pictographic-primitives/science/galaxy_8c39cb7d-e699-5085-ae7c-976abad4cb16.svg'
AUTHOR = 'gpt-6'

class TwoArmedSpiralGalaxy(Solo48):
    icon_id = 'two-armed-spiral-galaxy'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('galaxy', 'spiral', 'astronomy', 'space', 'cosmos', 'swirl')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        for n,side in [('upper',1),('lower',-1)]:
            def p(x,y):return (24+side*(x-24),24+side*(y-24))
            self.add_arc(n+'-outer',p(4,24),p(24,8),radius_x=20,radius_y=16)
            self.add_arc(n+'-turn',p(24,8),p(34,24),radius_x=10,radius_y=16)
            self.add_arc(n+'-inner',p(34,24),p(24,30),radius_x=10,radius_y=6)
            self.add_contour(n+'-arm',n+'-outer',n+'-turn',n+'-inner')

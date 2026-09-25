"""A large round central body is crossed by two diagonal elliptical orbits extending well beyond its edge. A smaller circle sits off-center toward the upper left inside the body.

SQUARE visible bounds (4,4)-(44,44); large central body and two diagonal orbits extending outside it. Interior crossing sections are hidden behind the body; small upper-left body reduced to a dot. Lucide atom informed the paired diagonal loops.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ad9ce8f-5d1f-4212-b082-ae7924f35080'
SOURCE_PATH = 'pictographic-primitives/science/molecules_0ad9ce8f-5d1f-4212-b082-ae7924f35080.svg'
AUTHOR = 'gpt-6'

class OrbitalAtomicModel(Solo48):
    icon_id = 'orbital-atomic-model'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('atom', 'orbit', 'model', 'physics', 'electron', 'science')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.circle('body',24,24,14)
        for name,side in [('northwest',1),('southeast',-1)]:
            def p(x,y):return(24+side*(x-24),24+side*(y-24))
            self.add_arc(name+'-a',p(10,24),p(6,6),radius_x=4,radius_y=18)
            self.add_arc(name+'-b',p(6,6),p(24,10),radius_x=18,radius_y=4)
            self.add_contour(name,name+'-a',name+'-b')
            self.relate('connect',name,'body')
        for name,side in [('northeast',1),('southwest',-1)]:
            def p(x,y):return(24+side*(x-24),24+side*(y-24))
            self.add_arc(name+'-a',p(24,10),p(42,6),radius_x=18,radius_y=4)
            self.add_arc(name+'-b',p(42,6),p(38,24),radius_x=4,radius_y=18)
            self.add_contour(name,name+'-a',name+'-b')
            self.relate('connect',name,'body')
        self.add_dot('inner-body',(20,20))

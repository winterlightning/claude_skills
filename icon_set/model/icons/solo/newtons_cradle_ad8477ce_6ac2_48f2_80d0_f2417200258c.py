"""Three circular balls hang from a horizontal support bar. Two hang vertically together at the left, while the rightmost ball swings outward on an angled line, leaving a wide gap between them.

HRECT_XL visible bounds (2,6)-(46,42); three suspended balls, right ball raised outward. No useful Lucide match. Ball sizes and positions adapted for spacing; rightward swing is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad8477ce-6ac2-48f2-80d0-f2417200258c'
SOURCE_PATH = 'pictographic-primitives/science/momentum_ad8477ce-6ac2-48f2-80d0-f2417200258c.svg'
AUTHOR = 'gpt-6'

class NewtonsCradle(Solo48):
    icon_id = 'newtons-cradle'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('newton', 'cradle', 'momentum', 'pendulum', 'physics', 'ball')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('support',(4,8),(10,8),(24,8),(32,8),(44,8))
        for n,x in [('left',10),('middle',24)]:
            self.add_line(n+'-string',(x,8),(x,30))
            self.circle(n+'-ball',x,35,5)
            self.relate('connect',n+'-string','support');self.relate('connect',n+'-string',n+'-ball')
        self.add_line('swing-string',(32,8),(40,24))
        self.circle('swing-ball',40,28,4)
        self.relate('connect','swing-string','support');self.relate('connect','swing-string','swing-ball')

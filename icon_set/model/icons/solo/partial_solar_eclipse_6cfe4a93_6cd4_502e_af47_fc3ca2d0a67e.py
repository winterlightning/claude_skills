"""A smaller circular moon overlaps the right side of a larger sun. Short rays radiate from the sun's exposed perimeter, while the moon remains a plain disk in front.

SQUARE visible extremes (4,4)-(44,44); exposed sun and foreground moon. Five clear rays replace seven source rays. Lucide eclipse informed the occluded arc; rightward overlap is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cfe4a93-6cd4-502e-af47-fc3ca2d0a67e'
SOURCE_PATH = 'pictographic-primitives/science/astronomy sun eclipse_6cfe4a93-6cd4-502e-af47-fc3ca2d0a67e.svg'
AUTHOR = 'gpt-6'

class PartialSolarEclipse(Solo48):
    icon_id = 'partial-solar-eclipse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('eclipse', 'sun', 'moon', 'solar', 'astronomy', 'sky')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.circle('moon',34,24,8)
        self.add_arc('sun-left',(24,16),(24,32),radius_x=8,sweep=False)
        self.add_line('sun-top',(34,16),(24,16))
        self.add_line('sun-bottom',(24,32),(34,32))
        self.add_contour('sun','sun-top','sun-left','sun-bottom')
        self.relate('connect','sun','moon')
        for n,a,b in [('top',(24,6),(24,7)),('bottom',(24,41),(24,42)),('left',(6,24),(7,24)),('upper-left',(8,8),(10,10)),('lower-left',(8,40),(10,38))]:
            self.add_line(n,a,b)

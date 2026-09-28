"""Three elongated elliptical orbits cross around a small circular nucleus. One orbit stands vertically and the other two slant in opposite directions, creating a balanced six-lobed outline around the center.

CIRCLE visible radius 22 about (24,24); three orbital paths and a central nucleus. Lucide atom informed the orbital hierarchy; loops re-authored with shared junctions and six lobes. Nucleus reduced to a dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdba40c2-6e27-5e35-8eb9-e73e06ff8b56'
SOURCE_PATH = 'pictographic-primitives/science/molecule_bdba40c2-6e27-5e35-8eb9-e73e06ff8b56.svg'
AUTHOR = 'gpt-6'

class AtomThreeOrbits(Solo48):
    icon_id = 'atom-three-orbits'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('atom', 'orbit', 'nucleus', 'electron', 'physics', 'science')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('vertical-top',(15,19),(33,19),radius_x=9,radius_y=15)
        self.add_line('vertical-right',(33,19),(33,29))
        self.add_arc('vertical-bottom',(33,29),(15,29),radius_x=9,radius_y=15)
        self.add_line('vertical-left',(15,29),(15,19))
        self.add_contour('vertical','vertical-top','vertical-right','vertical-bottom','vertical-left',closed=True)
        self.add_arc('ne-first',(24,15),(40,14),radius_x=9)
        self.add_arc('ne-second',(40,14),(33,29),radius_x=10)
        self.add_line('diagonal-a-lower',(33,29),(24,33))
        self.add_arc('sw-first',(24,33),(8,34),radius_x=9)
        self.add_arc('sw-second',(8,34),(15,19),radius_x=10)
        self.add_line('diagonal-a-upper',(15,19),(24,15))
        self.add_contour('diagonal-a','ne-first','ne-second','diagonal-a-lower','sw-first','sw-second','diagonal-a-upper',closed=True)
        self.add_arc('nw-first',(15,29),(8,14),radius_x=10)
        self.add_arc('nw-second',(8,14),(24,15),radius_x=9)
        self.add_line('diagonal-b-upper',(24,15),(33,19))
        self.add_arc('se-first',(33,19),(40,34),radius_x=10)
        self.add_arc('se-second',(40,34),(24,33),radius_x=9)
        self.add_line('diagonal-b-lower',(24,33),(15,29))
        self.add_contour('diagonal-b','nw-first','nw-second','diagonal-b-upper','se-first','se-second','diagonal-b-lower',closed=True)
        self.relate('connect','vertical','diagonal-a');self.relate('connect','vertical','diagonal-b');self.relate('connect','diagonal-a','diagonal-b')
        self.add_dot('nucleus',(24,24))

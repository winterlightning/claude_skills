"""A small irregular star-shaped cell body extends long branches in several directions. The branches fork into shorter angular tips, creating an uneven radial network around the open center.

SQUARE visible bounds (4,4)-(44,44); irregular open cell body with six forked branches. Lucide network informed connected junction construction. Natural uneven branching retained rather than forced radial symmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1954cd77-6e22-42e5-9c77-6024451a2dea'
SOURCE_PATH = 'pictographic-primitives/science/neurons_1954cd77-6e22-42e5-9c77-6024451a2dea.svg'
AUTHOR = 'gpt-6'

class BranchingNeuron(Solo48):
    icon_id = 'branching-neuron'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('neuron', 'nerve', 'cell', 'branch', 'biology', 'network')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('cell',(24,16),(32,21),(30,29),(23,32),(16,27),(16,20),closed=True)
        branches=[('upper',(24,16),(24,10),(18,6),(29,6)),('upper-right',(32,21),(37,16),(42,10),(42,18)),('lower-right',(30,29),(37,33),(42,30),(42,40)),('bottom',(23,32),(23,38),(22,42),(30,42)),('lower-left',(16,27),(10,32),(6,38),(6,30)),('upper-left',(16,20),(10,15),(6,9),(6,17))]
        for n,a,b,c,d in branches:
            self.add_polyline(n+'-main',a,b,c)
            self.add_line(n+'-fork',b,d)
            self.relate('connect','cell',n+'-main');self.relate('connect',n+'-main',n+'-fork')

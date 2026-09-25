"""Four circular stars of different sizes connect with straight lines. A central star branches down-left and down-right, while a longer diagonal connection reaches a larger star at the upper right.

SQUARE visible extremes (4,4)-(44,44); four stars retain unequal sizes and directional branch layout. Lucide chart-network informed circular nodes and endpoint connections.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '568c70fd-77b9-53b1-a9a7-549b7795e05e'
SOURCE_PATH = 'pictographic-primitives/science/astronomy constellation_568c70fd-77b9-53b1-a9a7-549b7795e05e.svg'
AUTHOR = 'gpt-6'

class BranchedConstellation(Solo48):
    icon_id = 'branched-constellation'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('constellation', 'star', 'astronomy', 'space', 'connection', 'sky')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        for name,x,y,r in [('hub',22,25,3),('upper',37,11,5),('left',9,39,3),('right',38,39,3)]:
            self.circle(name,x,y,r)
        self.add_line('branch-upper',(25,25),(32,11))
        self.add_line('branch-left',(19,25),(12,39))
        self.add_line('branch-right',(25,25),(35,39))
        for line,a,b in [('branch-upper','hub','upper'),('branch-left','hub','left'),('branch-right','hub','right')]:
            self.relate('connect',line,a)
            self.relate('connect',line,b)

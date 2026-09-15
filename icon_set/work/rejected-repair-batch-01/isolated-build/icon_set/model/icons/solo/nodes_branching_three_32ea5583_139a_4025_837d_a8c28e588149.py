"""Vertical stem splitting into three ring-ended branches. Lucide git-fork informs shared branch nodes and repeated ring radii; directional side branches retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='32ea5583-139a-4025-837d-a8c28e588149'
SOURCE_PATH='pictographic-primitives/symbol/three vertical lines with circles_32ea5583-139a-4025-837d-a8c28e588149.svg'
AUTHOR='gpt-6'

class NodesBranchingThree(Solo48):
    icon_id='nodes-branching-three'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('branch', 'nodes', 'usb', 'connection', 'network', 'split', 'hierarchy', 'share')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        for n,cx,cy in [('top',24,10),('left',10,20),('right',38,20)]:self.oval(n+'-ring',cx,cy,4)
        self.path('stem',[(24,14),(24,30),(24,36),(24,42)])
        self.relate('connect','stem','top-ring')
        self.path('left-branch',[(24,36),(10,28),(10,24)])
        self.path('right-branch',[(24,30),(38,28),(38,24)])
        for n in ('left','right'):
            self.relate('connect',n+'-branch','stem');self.relate('connect',n+'-branch',n+'-ring')

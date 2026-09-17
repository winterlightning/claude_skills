"""Three Dimensional Cube Rotation Tool.

Symbol plan: An isometric cube with three connected circular terminals; bilateral symmetry around x=24. Lucide box informs the three faces. Nodes are small complete circles.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1ebcd1c-faf5-4d0c-93f2-8b0f08933387'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/rotate 3d_a1ebcd1c-faf5-4d0c-93f2-8b0f08933387.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'isometric-cube-with-three-circular-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('three', 'dimensional', 'cube', 'rotation', 'tool')

    def build(self):
        a=24
        T=(24,15); L=(16,20); R=(32,20); C=(24,25); BL=(16,30); BR=(32,30); B=(24,35)
        self.graph([('tl',T,L),('tr',T,R),('lc',L,C),('rc',R,C),('left',L,BL),('right',R,BR),('bl',BL,B),('br',BR,B),('center',C,B),('top-stem',T,(24,12)),('left-stem',BL,(12,39)),('right-stem',BR,(36,39))])
        self.circle('node-top',24,9,3);self.circle('node-left',9,39,3);self.circle('node-right',39,39,3)
        self.relate('connect','top-stem','node-top')
        self.relate('connect','left-stem','node-left')
        self.relate('connect','right-stem','node-right')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def graph(self, edges):
        # Every relation below joins two edges at their shared endpoint.
        for name,a,b in edges: self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}: self.relate('connect',name,other)

"""Three Dimensional Room Perspective.

Symbol plan: Perspective room with vertical central corner and mirrored side planes. Lucide box informs hexagonal edge graph; one horizontal wall division preserves the lattice.
Keyshape: VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7271d6e-f0dd-599e-a793-70013ffb6b05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/grid perspective_c7271d6e-f0dd-599e-a793-70013ffb6b05.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'isometric-room-grid-with-central-corner'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('three', 'dimensional', 'room', 'perspective')

    def build(self):
        T=(24,4); L=(8,14); R=(40,14); BL=(8,34); BR=(40,34); B=(24,44); C=(24,24)
        self.graph([('tl',T,L),('tr',T,R),('left-top',L,(8,24)),('left-bottom',(8,24),BL),('right-top',R,(40,24)),('right-bottom',(40,24),BR),('bl',BL,B),('br',BR,B),('corner-upper',T,(24,14)),('corner-middle',(24,14),C),('corner-bottom',C,B),('floor-left',BL,C),('floor-right',BR,C),('wall-left',(8,24),(24,14)),('wall-right',(40,24),(24,14))])

    def graph(self, edges):
        # Every relation below joins two edges at their shared endpoint.
        for name,a,b in edges: self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}: self.relate('connect',name,other)

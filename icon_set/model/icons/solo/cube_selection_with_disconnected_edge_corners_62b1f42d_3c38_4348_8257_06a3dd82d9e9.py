"""Three Dimensional Selection Cube.

Symbol plan: Disconnected isometric cube corners with a central three-arm junction, mirrored across x=24; Lucide box gives the projection.
Keyshape: VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62b1f42d-3c38-4348-8257-06a3dd82d9e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/select 3d_62b1f42d-3c38-4348-8257-06a3dd82d9e9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cube-selection-with-disconnected-edge-corners'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ()
    keywords = ('three', 'dimensional', 'selection', 'cube')

    def build(self):
        a=24
        self.add_polyline('top',(20,6),(a,4),(28,6))
        self.add_polyline('left-upper',(14,12),(8,16),(8,22))
        self.add_polyline('right-upper',(34,12),(40,16),(40,22))
        self.add_polyline('left-lower',(8,30),(8,36),(12,38))
        self.add_polyline('right-lower',(40,30),(40,36),(36,38))
        self.add_polyline('bottom',(20,42),(24,44),(28,42))
        self.graph([('junction-left',(16,21),(24,26)),('junction-right',(24,26),(32,21)),('junction-down',(24,26),(24,34))])

    def graph(self, edges):
        # Every relation below joins two edges at their shared endpoint.
        for name,a,b in edges: self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}: self.relate('connect',name,other)

"""Upward Perspective Transform.

Symbol plan: An extrusion diagram: open upper plane, concave surface sides, broad lower plane and intrinsic upward axis. Shared x=24 mirror axis. Simplified lower perspective edge; no useful Lucide extrusion match.
Keyshape VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d311a90-f0ef-5dc9-8ffe-179d92671b21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/perspective_6d311a90-f0ef-5dc9-8ffe-179d92671b21.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'upward-perspective-plane-transformation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('upward', 'perspective', 'transform')

    def build(self):
        self.add_polyline('upper',(14,16),(10,24),(16,24),(24,24),(32,24),(38,24),(34,16))
        self.add_polyline('lower',(16,36),(8,36),(8,44),(40,44),(40,36),(32,36),(16,36))
        self.add_arc('surface-left',(16,24),(16,36),radius_x=12,sweep=True)
        self.add_arc('surface-right',(32,24),(32,36),radius_x=12,sweep=False)
        for side in ['surface-left','surface-right']:
            self.relate('connect',side,'upper');self.relate('connect',side,'lower')
        self.graph([('axis',(24,24),(24,4)),('arrow-left',(24,4),(18,10)),('arrow-right',(24,4),(30,10))])
        self.relate('connect','axis','upper')

    def graph(self,edges):
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}:self.relate('connect',name,other)

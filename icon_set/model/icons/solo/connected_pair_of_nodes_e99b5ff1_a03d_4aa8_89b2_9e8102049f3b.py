"""Connected Pair of Nodes.
Plan: Two identical radius8 nodes attach below a shared bar; mirrored about x24. Ink (2,6)-(46,42).
Reference construction: network.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e99b5ff1-a03d-4aa8-89b2-9e8102049f3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hierarchy 1_e99b5ff1-a03d-4aa8-89b2-9e8102049f3b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'connected-pair-of-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('connected', 'pair', 'of', 'nodes')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('bar',(12,24),(12,8),(36,8),(36,24))
        for x in (12,36):
         circle(f'node-{x}',x,32,8);self.relate('connect','bar',f'node-{x}')

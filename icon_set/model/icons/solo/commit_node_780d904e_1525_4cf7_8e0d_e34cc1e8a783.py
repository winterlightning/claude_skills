"""Commit Node.
Plan: Circular node radius8 and horizontal leads attach at its cardinal points; radial envelope22.
Reference construction: git-commit-horizontal.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '780d904e-1525-4cf7-8e0d-e34cc1e8a783'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/workflow commit_780d904e-1525-4cf7-8e0d-e34cc1e8a783.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'commit-node'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('commit', 'node')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        circle('node',24,24,8)
        for n,a,b in [('left',(4,24),(16,24)),('right',(32,24),(44,24))]:
         self.add_line(n,a,b);self.relate('connect',n,'node')

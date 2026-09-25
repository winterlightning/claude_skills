"""Double Down Chevron.
Plan: Two wide chevrons repeat at a sixteen-unit vertical step, mirrored about x24. Ink (2,6)-(46,42).
Reference construction: chevrons-down.
Reduction: Reduce the outlined chevron bands to clean open strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5df5499e-7159-49b5-bbef-3386211c2bc0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation down 2_5df5499e-7159-49b5-bbef-3386211c2bc0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'double-down-chevron'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('double', 'down', 'chevron')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,y in enumerate((8,24)):
         pts=[(4,y),(24,y+16),(44,y)]
         self.add_polyline(f'chevron-{j}',*pts)

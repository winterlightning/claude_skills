"""Double Up Chevron.
Plan: Two wide chevrons repeat at a sixteen-unit vertical step, mirrored about x24. Ink (2,6)-(46,42).
Reference construction: chevrons-up.
Reduction: Reduce the outlined chevron bands to clean open strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2166948b-8fde-4839-b0e8-539a342234ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation up_2166948b-8fde-4839-b0e8-539a342234ad.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'double-up-chevron'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('double', 'up', 'chevron')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,y in enumerate((8,24)):
         pts=[(4,y),(24,y+16),(44,y)]
         pts=[(x,48-v) for x,v in pts]
         self.add_polyline(f'chevron-{j}',*pts)

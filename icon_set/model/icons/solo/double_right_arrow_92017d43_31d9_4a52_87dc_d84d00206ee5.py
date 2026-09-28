"""Double Right Arrow.
Plan: Two equal right triangles share y24 and are separated by eight units. Ink (2,6)-(46,42).
Reference construction: fast-forward.
Reduction: Close the interrupted rear edges to clarify the two triangular arrows.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '92017d43-31d9-4a52-87dc-d84d00206ee5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation arrows right 1_92017d43-31d9-4a52-87dc-d84d00206ee5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'double-right-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('double', 'right', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,x in enumerate((4,28)):self.add_polyline(f'arrow-{j}',(x,8),(x+16,24),(x,40),closed=True)

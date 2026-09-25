"""Arrow Mouse Pointer.
Plan: One continuous angular outline preserves a broad diagonal tail; ink (4,4)-(44,44).
Reference construction: mouse-pointer-2.
Reduction: Simplify chamfer to one diagonal cap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f83d129d-0b0e-56c6-ab3d-2c624d2c45e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor_f83d129d-0b0e-56c6-ab3d-2c624d2c45e2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'arrow-mouse-pointer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('arrow', 'mouse', 'pointer')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('pointer',(6,6),(42,18),(30,22),(42,34),(34,42),(22,30),(18,42),closed=True)

"""Double Right Chevron.
Plan: Two equal right chevrons repeat sixteen units apart. Ink (6,2)-(42,46).
Reference construction: chevrons-right.
Reduction: Reduce each broad outlined band to a single open chevron.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ab2f5f4-03e2-4b3d-a4f9-b030ddde6df2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/web form progress_0ab2f5f4-03e2-4b3d-a4f9-b030ddde6df2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'double-right-chevron'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('double', 'right', 'chevron')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,x in enumerate((8,24)):self.add_polyline(f'chevron-{j}',(x,4),(x+16,24),(x,44))

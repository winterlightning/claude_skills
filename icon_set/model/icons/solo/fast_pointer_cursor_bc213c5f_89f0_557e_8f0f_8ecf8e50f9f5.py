"""Fast Pointer Cursor.
Plan: A left-side arrow cursor leaves the upper-right quadrant for three evenly spaced speed lines. Ink (4,4)-(44,44).
Reference construction: mouse-pointer-2.
Reduction: Keep all three speed marks; simplify the cursor notch and omit no defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc213c5f-89f0-557e-8f0f-8ecf8e50f9f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor speed_bc213c5f-89f0-557e-8f0f-8ecf8e50f9f5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fast-pointer-cursor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('fast', 'pointer', 'cursor')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('cursor',(6,6),(28,28),(18,30),(10,42),closed=True)

        for j,(x,y) in enumerate([(20,6),(30,14),(38,22)]):self.add_line(f'speed-{j}',(x,y),(42,y))

"""Curved Right Arrow.
Plan: One descending stroke turns into a shallow rightward sweep with a shared arrow tip. Ink (2,6)-(46,42).
Reference construction: corner-down-right.
Reduction: Smooth the irregular reference sweep into one coherent curve.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '178b88d2-bb46-4d0b-9622-73d1aea34874'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation right_178b88d2-bb46-4d0b-9622-73d1aea34874.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curved-right-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('curved', 'right', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_bezier('sweep',(4,8),((4,29),(18,30),(44,26)))
        self.add_polyline('head',(32,14),(44,26),(30,40))
        self.relate('connect','sweep','head')

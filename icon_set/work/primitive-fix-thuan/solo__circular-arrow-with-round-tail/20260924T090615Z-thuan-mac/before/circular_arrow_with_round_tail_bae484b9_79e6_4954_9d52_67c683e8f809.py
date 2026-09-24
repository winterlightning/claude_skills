"""Circular Arrow with Round Tail.
Plan: Round-ended rotation stroke sweeps around the lower circle and turns into an upper-left arrowhead. Radial envelope22.
Reference construction: rotate-ccw.
Reduction: Use the round stroke cap as the round tail terminal, omitting its separate ring.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bae484b9-79e6-4954-9d52-67c683e8f809'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/volume down_bae484b9-79e6-4954-9d52-67c683e8f809.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circular-arrow-with-round-tail'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('circular', 'arrow', 'with', 'round', 'tail')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('left',(12,8),(4,24),radius_x=20,sweep=False)
        self.add_arc('bottom',(4,24),(44,24),radius_x=20,sweep=False)
        self.add_bezier('turn',(44,24),((44,18),(40,14),(36,12)))
        self.add_contour('rotation','left','bottom','turn')
        self.add_polyline('arrow',(34,18),(36,12),(41,14))
        self.relate('connect','arrow','rotation')

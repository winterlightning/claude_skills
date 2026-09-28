"""Counterclockwise Refresh Arrow.
Plan: A circular radius18 sweep terminates in a downward head on the left; ink (4,4)-(44,44).
Reference construction: rotate-ccw.
Reduction: Use an asymmetric open head to keep it within the circular sweep envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77f5a2c6-8120-4350-aa53-7bb00704de7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize refresh arrow_77f5a2c6-8120-4350-aa53-7bb00704de7d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-refresh-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('counterclockwise', 'refresh', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('sweep',(24,42),(6,24),radius_x=18,large_arc=True,sweep=False)
        self.add_polyline('head',(6,16),(6,24),(14,18))
        self.relate('connect','sweep','head')

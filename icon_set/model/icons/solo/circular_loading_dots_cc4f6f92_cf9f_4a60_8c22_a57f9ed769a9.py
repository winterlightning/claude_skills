"""Circular Loading Dots.
Plan: Seven circles form a broken ring, with size decreasing toward the bottom-right gap. Ink (4,4)-(44,44).
Reference construction: loader.
Reduction: Smallest outlined dots become round filled dots; preserve seven marks and the incomplete ring.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc4f6f92-cf9f-4a60-8c22-a57f9ed769a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loading half_cc4f6f92-cf9f-4a60-8c22-a57f9ed769a9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circular-loading-dots'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('circular', 'loading', 'dots')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,(x,y,r) in enumerate([(24,9,3),(39,17,3),(10,15,3),(8,29,2),(15,40,2),(27,42,0),(37,34,0)]):
            if r:circle(f'loading-{j}',x,y,r)
            else:self.add_dot(f'loading-{j}',(x,y))

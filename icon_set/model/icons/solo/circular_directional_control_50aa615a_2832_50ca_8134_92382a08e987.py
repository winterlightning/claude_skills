"""Circular Directional Control.
Plan: One circular control with a central button dot and four rotationally repeated chevrons. Radial envelope22.
Reference construction: move.
Reduction: Reduce the central outlined button to a dot and shorten all four chevrons equally.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50aa615a-2832-50ca-8134-92382a08e987'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor move direction_50aa615a-2832-50ca-8134-92382a08e987.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circular-directional-control'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('circular', 'directional', 'control')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        circle('control',24,24,20)
        self.add_dot('button',(24,24))
        points=[(-2,-9),(0,-11),(2,-9)]
        for j in range(4):
            pts=[]
            for x,y in points:
                for _ in range(j):x,y=-y,x
                pts.append((24+x,24+y))
            self.add_polyline(f'direction-{j}',*pts)

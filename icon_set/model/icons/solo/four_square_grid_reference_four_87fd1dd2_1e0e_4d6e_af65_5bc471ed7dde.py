"""Four Square Grid.
Plan: One rounded-square definition repeated on a two-by-two grid with shared step and radius. Ink (4,4)-(44,44).
Construction reference: layout-grid.
Reduction: Retain the source essentials.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87fd1dd2-1e0e-4d6e-af65-5bc471ed7dde'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/picture polaroid four_87fd1dd2-1e0e-4d6e-af65-5bc471ed7dde.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-square-grid-reference-four'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'images'
    aliases = ()
    keywords = ('four', 'square', 'grid')
    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                if i%2: self.add_arc(f'{name}-{i}',a,b,radius_x=r)
                else: self.add_line(f'{name}-{i}',a,b)
            self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

        side, step, radius = 14, 22, 2
        for row in range(2):
            for col in range(2):
                rect(f'cell-{row}-{col}',6+col*step,6+row*step,side,side,radius)

"""Four Square Grid.
Plan: One rounded-square definition repeated on a two-by-two grid with shared step and radius. Ink (4,4)-(44,44).
Construction reference: layout-grid.
Reduction: Retain the source essentials.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f6be3b37-480a-4add-afa9-feedd34c007d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/picture polaroid album_f6be3b37-480a-4add-afa9-feedd34c007d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-square-grid-reference-album'
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

        side, step, radius = 12, 24, 2
        for row in range(2):
            for col in range(2):
                rect(f'cell-{row}-{col}',6+col*step,6+row*step,side,side,radius)

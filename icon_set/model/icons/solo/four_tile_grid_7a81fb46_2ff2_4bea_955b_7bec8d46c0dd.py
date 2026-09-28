"""Four Tile Grid.
Plan: Four equal rounded square tiles share a22-unit grid step and radius3 corners. Ink (4,4)-(44,44).
Reference construction: grid-2x2.
Reduction: Use independent tiles rather than a shared outside frame, as requested by the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a81fb46-2ff2-4bea-955b-7bec8d46c0dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/layout module 1_7a81fb46-2ff2-4bea-955b-7bec8d46c0dd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'four-tile-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('four', 'tile', 'grid')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,(x,y) in enumerate([(6,6),(28,6),(6,28),(28,28)]):
         pts=[(x+3,y),(x+11,y),(x+14,y+3),(x+14,y+11),(x+11,y+14),(x+3,y+14),(x,y+11),(x,y+3)]
         for k,a in enumerate(pts):
          b=pts[(k+1)%8]
          if k%2:self.add_arc(f'tile-{j}-{k}',a,b,radius_x=3)
          else:self.add_line(f'tile-{j}-{k}',a,b)
         self.add_contour(f'tile-{j}',*(f'tile-{j}-{k}' for k in range(8)),closed=True)

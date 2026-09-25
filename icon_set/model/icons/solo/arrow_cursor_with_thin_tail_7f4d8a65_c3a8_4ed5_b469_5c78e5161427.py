"""Arrow Cursor with Thin Tail.
Plan: A notched pointer owns the shared tail junction (26,26); ink (4,4)-(44,44).
Reference construction: mouse-pointer-2.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f4d8a65-c3a8-4ed5-b469-5c78e5161427'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor left 1_7f4d8a65-c3a8-4ed5-b469-5c78e5161427.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'arrow-cursor-with-thin-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('arrow', 'cursor', 'with', 'thin', 'tail')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('pointer',(6,6),(42,22),(26,26),(22,42),closed=True)
        self.add_line('tail',(26,26),(40,40))
        self.relate('connect','pointer','tail')

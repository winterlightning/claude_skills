"""Horizontal Double Arrow.
Plan: A horizontal shaft joins two equal outward-pointing open heads. Ink (2,8)-(46,40).
Reference construction: move-horizontal.
Reduction: Keep the balanced bidirectional construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e68e0b91-679b-48bd-af22-1af4244338d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand horizontal_e68e0b91-679b-48bd-af22-1af4244338d8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'horizontal-double-arrow'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('horizontal', 'double', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('shaft',(4,24),(44,24))
        self.add_polyline('left',(18,10),(4,24),(18,38))
        self.add_polyline('right',(30,10),(44,24),(30,38))
        self.relate('connect','shaft','left');self.relate('connect','shaft','right')

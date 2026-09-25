"""Crossing Shuffle Arrows.
Plan: One continuous S path crosses an interrupted opposing path; paired arrowheads share endpoint anchors. Ink (2,6)-(46,42).
Reference construction: shuffle.
Reduction: Widen the crossing interruption so the two paths remain distinct.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8b44d27f-5a11-5700-a00a-5afea52fe1c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/button shuffle_8b44d27f-5a11-5700-a00a-5afea52fe1c6.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'crossing-shuffle-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('crossing', 'shuffle', 'arrows')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('lower-start',(4,34),(10,34))
        self.add_bezier('cross',(10,34),((22,34),(26,14),(38,14)))
        self.add_line('upper-end',(38,14),(44,14))
        self.add_contour('rising','lower-start','cross','upper-end')
        self.add_bezier('upper-start',(4,14),((10,14),(13,14),(16,17)))
        self.add_bezier('lower-end',(32,31),((35,34),(38,34),(44,34)))
        for label,y,owner in [('top',14,'rising'),('bottom',34,'lower-end')]:
         self.add_polyline(label+'-head',(38,y-6),(44,y),(38,y+6));self.relate('connect',label+'-head',owner)

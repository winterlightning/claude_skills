"""Curved Right Arrow with Chevron.
Plan: Two right chevrons repeat twelve units apart; the main tip owns a tangent quarter-circle return. Ink (2,6)-(46,42).
Reference construction: corner-down-right; redo-2.
Reduction: Reduce the broad outlined shaft and triangular head to single strokes, retaining the extra forward chevron.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '772eef96-8468-5247-906a-447997fc654a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation direction right_772eef96-8468-5247-906a-447997fc654a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curved-right-arrow-with-chevron'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('curved', 'right', 'arrow', 'with', 'chevron')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('tail',(4,8),(4,12))
        self.add_arc('turn',(4,12),(16,24),radius_x=12,sweep=False)
        self.add_line('shaft',(16,24),(32,24));self.add_contour('route','tail','turn','shaft')
        self.add_polyline('main-head',(20,8),(32,24),(20,40))
        self.add_polyline('extra-head',(32,8),(44,24),(32,40))
        self.relate('connect','route','main-head')

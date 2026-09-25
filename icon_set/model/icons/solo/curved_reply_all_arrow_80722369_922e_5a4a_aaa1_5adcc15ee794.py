"""Curved Reply All Arrow.
Plan: Two left-pointing chevrons are separated by a twelve-unit horizontal step; the main arrow owns a quarter-circle tail. Ink (2,6)-(46,42).
Reference construction: reply-all.
Reduction: Reduce the broad outlined arrow to a single curved stroke with an open head, preserving reply-all identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80722369-922e-5a4a-aaa1-5adcc15ee794'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/navigation direction left_80722369-922e-5a4a-aaa1-5adcc15ee794.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curved-reply-all-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('curved', 'reply', 'all', 'arrow')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('extra-head',(16,8),(4,24),(16,40))
        self.add_polyline('main-head',(28,8),(16,24),(28,40))
        self.add_line('shaft',(16,24),(32,24))
        self.add_arc('curve',(32,24),(44,36),radius_x=12)
        self.add_line('tail',(44,36),(44,40))
        self.add_contour('return','shaft','curve','tail');self.relate('connect','main-head','return')

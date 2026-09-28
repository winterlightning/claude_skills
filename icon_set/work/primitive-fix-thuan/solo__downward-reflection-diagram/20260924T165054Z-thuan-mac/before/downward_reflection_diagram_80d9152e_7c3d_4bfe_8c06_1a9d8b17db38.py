"""Downward Reflection Diagram.
Plan: Two mirrored triangles face a horizontal reflection axis; a right-hand curved arrow points down. Ink (2,6)-(46,42).
Reference construction: flip-vertical-2.
Reduction: Use compact triangles and a single continuous reflection axis.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80d9152e-7c3d-4bfe-8c06-1a9d8b17db38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/reflect down_80d9152e-7c3d-4bfe-8c06-1a9d8b17db38.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'downward-reflection-diagram'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('downward', 'reflection', 'diagram')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('upper',(6,8),(26,8),(16,16),closed=True)
        self.add_polyline('lower',(6,40),(26,40),(16,32),closed=True)
        self.add_line('axis',(4,24),(28,24))
        self.add_bezier('turn',(36,12),((44,12),(44,20),(44,24)),((44,28),(40,34),(36,36)))
        self.add_polyline('head',(36,28),(36,36),(44,36));self.relate('connect','head','turn')

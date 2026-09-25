"""Horizontal Cycle Arrows.
Plan: Two tangent quarter-circle returns and horizontal arrows repeat under a half turn. Ink (2,6)-(46,42).
Reference construction: repeat.
Reduction: Open the curved returns enough to separate the two arrowheads.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c5af52d-65b1-489d-a409-897744f0b2b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/syncing_6c5af52d-65b1-489d-a409-897744f0b2b9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'horizontal-cycle-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('horizontal', 'cycle', 'arrows')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('top',False),('bottom',True)]:
         def pt(x,y):return (48-x,48-y) if flip else (x,y)
         self.add_arc(label+'-turn',pt(4,26),pt(16,14),radius_x=12)
         self.add_line(label+'-shaft',pt(16,14),pt(36,14))
         self.add_contour(label,label+'-turn',label+'-shaft')
         self.add_polyline(label+'-head',pt(30,8),pt(36,14),pt(30,20));self.relate('connect',label,label+'-head')

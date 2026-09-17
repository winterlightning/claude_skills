"""Horizontal Chain Connection.
Plan: Paired open chain ends mirror x24 around a clear horizontal connector. Ink (2,8)-(46,40).
Reference construction: link-2.
Reduction: Widen the open center to give the connector clear space; keep semicircular ends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '30888bf2-0b8e-56fe-982b-a281e9af88e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_30888bf2-0b8e-56fe-982b-a281e9af88e2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'horizontal-chain-connection'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('horizontal', 'chain', 'connection')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('left',False),('right',True)]:
         def pt(x,y):return (48-x,y) if flip else (x,y)
         self.add_line(label+'-top',pt(19,10),pt(18,10))
         self.add_arc(label+'-round',pt(18,10),pt(18,38),radius_x=14,sweep=flip)
         self.add_line(label+'-bottom',pt(18,38),pt(19,38))
         self.add_contour(label,label+'-top',label+'-round',label+'-bottom')
        self.add_line('bridge',(14,24),(34,24))

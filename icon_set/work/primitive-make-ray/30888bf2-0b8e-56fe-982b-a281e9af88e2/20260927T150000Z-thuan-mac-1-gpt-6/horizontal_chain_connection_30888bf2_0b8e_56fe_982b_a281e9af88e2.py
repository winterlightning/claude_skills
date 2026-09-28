"""Horizontal Chain Connection.
Plan: Paired open chain ends mirror x24 around a clear horizontal connector. Ink (2,8)-(46,40).
Reference construction: link-2.
Reduction: Widen the open center to give the connector clear space; keep semicircular ends.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '30888bf2-0b8e-56fe-982b-a281e9af88e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-chain-connection/20260927T145836Z-thuan-mac-1/reference/hyperlink_30888bf2-0b8e-56fe-982b-a281e9af88e2.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'horizontal-chain-connection'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('horizontal', 'chain', 'connection')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('left',False),('right',True)]:
         def pt(x,y):return (48-x,y) if flip else (x,y)
         self.add_arc(label+'-round',pt(18,10),pt(18,38),radius_x=14,sweep=flip)
         self.add_contour(label,label+'-round')
        self.add_line('bridge',(17,24),(31,24))

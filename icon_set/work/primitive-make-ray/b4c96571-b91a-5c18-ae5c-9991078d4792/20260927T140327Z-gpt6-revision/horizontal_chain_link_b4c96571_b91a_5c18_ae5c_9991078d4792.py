"""Horizontal Chain Link.
Plan: Paired open chain ends mirror x24 around a clear horizontal connector. Ink (2,8)-(46,40).
Reference construction: link-2.
Reduction: Widen the open center to give the connector clear space; keep rounded rectangular ends.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b4c96571-b91a-5c18-ae5c-9991078d4792'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-chain-link/20260927T135945Z-thuan-mac-1/reference/hyperlink_b4c96571-b91a-5c18-ae5c-9991078d4792.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'horizontal-chain-link'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    aliases = ()
    keywords = ('horizontal', 'chain', 'link')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('left',False),('right',True)]:
         def pt(x,y):return (48-x,y) if flip else (x,y)
         self.add_line(label+'-top',pt(20,12),pt(12,10))
         self.add_arc(label+'-a',pt(12,10),pt(4,18),radius_x=8,sweep=flip)
         self.add_line(label+'-side',pt(4,18),pt(4,30))
         self.add_arc(label+'-b',pt(4,30),pt(12,38),radius_x=8,sweep=flip)
         self.add_line(label+'-bottom',pt(12,38),pt(20,36))
         self.add_contour(label,label+'-top',label+'-a',label+'-side',label+'-b',label+'-bottom')
        self.add_line('bridge',(15,24),(33,24))

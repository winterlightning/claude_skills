"""Diagonal Chain Link.
Plan: Two equal open chain ends repeat under a half turn; one diagonal bridge sits in their shared opening. Ink (4,4)-(44,44).
Reference construction: link; link-2.
Reduction: Open the inner ends and use a straight joining stroke to keep the interlock readable with four-unit ink clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee4e9e4a-096c-56f9-a0cf-4ffbe3e3593c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_ee4e9e4a-096c-56f9-a0cf-4ffbe3e3593c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-chain-link-rounded'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('diagonal', 'chain', 'link')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('upper',False),('lower',True)]:
         def pt(x,y):return (48-x,48-y) if flip else (x,y)
         self.add_line(label+'-left',pt(20,12),pt(24,8))
         self.add_bezier(label+'-top',pt(24,8),(pt(26,6),pt(28,6),pt(30,6)))
         self.add_arc(label+'-round',pt(30,6),pt(42,18),radius_x=12)
         self.add_bezier(label+'-bottom',pt(42,18),(pt(42,20),pt(42,22),pt(40,24)))
         self.add_line(label+'-right',pt(40,24),pt(36,28))
         self.add_contour(label,label+'-left',label+'-top',label+'-round',label+'-bottom',label+'-right')
        self.add_line('bridge',(18,30),(30,18))

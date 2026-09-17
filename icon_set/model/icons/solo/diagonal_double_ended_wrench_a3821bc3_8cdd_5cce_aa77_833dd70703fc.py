"""Diagonal Double Ended Wrench.
Plan: Opposing open rounded jaws meet a diagonal handle at matching attachment points; half-turn symmetry. Ink (4,4)-(44,44).
Reference construction: wrench.
Reduction: Represent the narrow handle and crescent jaw walls as single strokes; retain two open ends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a3821bc3-8cdd-5cce-aa77-833dd70703fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/wrench double_a3821bc3-8cdd-5cce-aa77-833dd70703fc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-double-ended-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('diagonal', 'double', 'ended', 'wrench')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('upper',False),('lower',True)]:
         def pt(x,y):return (48-x,48-y) if flip else (x,y)
         self.add_bezier(label+'-a',pt(14,6),(pt(19,6),pt(22,9),pt(22,14)))
         self.add_bezier(label+'-b',pt(22,14),(pt(22,16),pt(21,18),pt(19,19)))
         self.add_bezier(label+'-c',pt(19,19),(pt(18,21),pt(16,22),pt(14,22)))
         self.add_bezier(label+'-d',pt(14,22),(pt(9,22),pt(6,19),pt(6,14)))
         self.add_contour(label,label+'-a',label+'-b',label+'-c',label+'-d')
        self.add_line('handle',(19,19),(29,29))
        self.relate('connect','handle','upper');self.relate('connect','handle','lower')

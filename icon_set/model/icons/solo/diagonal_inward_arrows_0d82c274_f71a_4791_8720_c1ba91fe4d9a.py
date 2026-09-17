"""Diagonal Inward Arrows.
Plan: Opposing inward arrows mirror through the center and leave a twelve-unit diagonal gap. Ink (4,4)-(44,44).
Reference construction: shrink.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0d82c274-f71a-4791-8720-c1ba91fe4d9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/shrink_0d82c274-f71a-4791-8720-c1ba91fe4d9a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-inward-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('diagonal', 'inward', 'arrows')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('lower',False),('upper',True)]:
         def pt(x,y):return (48-x,48-y) if flip else (x,y)
         self.add_line(label+'-shaft',pt(6,42),pt(20,28))
         self.add_polyline(label+'-head',pt(8,28),pt(20,28),pt(20,40))
         self.relate('connect',label+'-shaft',label+'-head')

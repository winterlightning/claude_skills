"""Diagonal Outward Arrows with Divider.
Plan: Two outward arrows share a diagonal axis; perpendicular divider occupies the center with8.5-unit tail clearance. Ink (4,4)-(44,44).
Reference construction: expand; move-diagonal.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eaf64fd4-ac17-4bc9-a695-f8825e7c1e5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand diagonal 2_eaf64fd4-ac17-4bc9-a695-f8825e7c1e5a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'diagonal-outward-arrows-with-divider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('diagonal', 'outward', 'arrows', 'with', 'divider')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_line('divider',(12,12),(36,36))
        for label,flip in [('lower',False),('upper',True)]:
         def pt(x,y):return (48-x,48-y) if flip else (x,y)
         self.add_line(label+'-shaft',pt(18,30),pt(6,42))
         self.add_polyline(label+'-head',pt(6,30),pt(6,42),pt(18,42))
         self.relate('connect',label+'-shaft',label+'-head')

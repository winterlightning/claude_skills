"""Horizontal Compression Arrows.
Plan: Opposing inward arrows share the midpoints of tall boundary lines. Ink (2,6)-(46,42).
Reference construction: move-horizontal.
Reduction: Keep the boundary lines and two inward heads with an eight-unit central gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '52c4b77f-eb6a-4345-81ae-209c3e0585c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/shrink horizontal_52c4b77f-eb6a-4345-81ae-209c3e0585c9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'horizontal-compression-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('horizontal', 'compression', 'arrows')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,flip in [('left',False),('right',True)]:
         def pt(x,y):return (48-x,y) if flip else (x,y)
         self.add_polyline(label+'-wall',pt(4,8),pt(4,24),pt(4,40))
         self.add_line(label+'-shaft',pt(4,24),pt(20,24))
         self.add_polyline(label+'-head',pt(14,18),pt(20,24),pt(14,30))
         self.relate('connect',label+'-wall',label+'-shaft');self.relate('connect',label+'-shaft',label+'-head')

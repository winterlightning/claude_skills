"""A single-storey lowercase a has an oval bowl and a right-hand descending stem.
Symbol plan: Vertically elongated elliptical bowl with integer cardinal endpoints; tangent right stem shares the rightmost bowl node.
Keyshape visible bounds: (6, 2, 42, 46).
Construction references: Supplied lowercase a reference: open oval counter and right stem. Lucide type was inspected but offers no useful match for this single-storey glyph..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '615e9ffb-b53e-40a6-9ba6-86b05b552fd0'
SOURCE_PATH = 'pictographic-primitives/typeface/a_615e9ffb-b53e-40a6-9ba6-86b05b552fd0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'a'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('a',)
    def build(self):
        cx,cy,rx,ry=24,24,16,20
        self.add_arc('bowl-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc('bowl-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour('bowl','bowl-upper','bowl-lower',closed=True)
        self.add_line('stem',(cx+rx,cy),(cx+rx,44))
        self.relate('connect','bowl','stem')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

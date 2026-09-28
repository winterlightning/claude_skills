"""An address book has a left spine and a user portrait on its cover.
Symbol plan: Horizontal book with spine 8 units from left edge; portrait has circular radius-4 head and cropped radius-6 shoulders, exact gap 34-(22+4)=8.
Keyshape visible bounds: (2, 6, 46, 42).
Construction references: Shared human_ref/user.svg: outlined head and smooth shoulder arch; Lucide notebook: separate spine; supplied reference: portrait on book cover..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b18b4462-5e10-44fd-99e3-3fb256fb4f34'
SOURCE_PATH = 'pictographic-primitives/phones/phone book_b18b4462-5e10-44fd-99e3-3fb256fb4f34.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'phone-book'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('phone', 'book')
    def build(self):
        self.box('book',4,8,44,40,4)
        self.add_line('spine',(12,8),(12,40))
        self.relate('connect','book','spine')
        cx,cy,r=28,22,4
        self.circle('head',cx,cy,r)
        self.add_arc('shoulder-left',(22,40),(28,34),radius_x=6)
        self.add_arc('shoulder-right',(28,34),(34,40),radius_x=6)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','book','shoulders')

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

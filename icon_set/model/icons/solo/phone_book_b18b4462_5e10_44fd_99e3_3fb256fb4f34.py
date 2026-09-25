'Contact address book.\nPlan: SQUARE permits a left spine and detached head/shoulders. Head (28,19), radius 4; shoulders top31: centerline gap8, ink gap4.\nReference: notebook; human_ref/user.svg; Separate spine; outlined circular head and smooth open shoulders.\nChanges: No parts omitted; shoulder arch is shallow to retain bottom clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b18b4462-5e10-44fd-99e3-3fb256fb4f34'
SOURCE_PATH = 'pictographic-primitives/phones/phone book_b18b4462-5e10-44fd-99e3-3fb256fb4f34.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'phone-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "phones"
    categories = ("phones", "primitives")
    aliases = ()
    keywords = ('phone', 'book')
    def build(self):
        self.box('book',6,6,42,42,4)
        self.add_line('spine',(14,6),(14,42))
        self.relate('connect','book','spine')
        cx,cy,r=28,19,4
        self.circle('head',cx,cy,r)
        self.add_arc('shoulder-left',(23,33),(28,31),radius_x=5,radius_y=2)
        self.add_arc('shoulder-right',(28,31),(33,33),radius_x=5,radius_y=2)
        self.add_contour('shoulders','shoulder-left','shoulder-right')


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

PARENT_MODULE = 'icon_set/model/icons/solo/phone_book_b18b4462_5e10_44fd_99e3_3fb256fb4f34.py'

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'a7306668788f4db89d94b85c92a6d9d11da1cecb27fbc420c3a1eee3fe6e67ec', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'b18b4462-5e10-44fd-99e3-3fb256fb4f34'}

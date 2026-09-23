"""crowdin logo. Reconstructed whole reference on SOLO48.
Plan: HRECT_L visible bounds (2, 6, 46, 42).
Construction: No useful exact Lucide logo match; coherent Bézier bands. Shared dimensions and relationships are recorded in build.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e89d9bcb-0e93-4a07-abd4-7740608fbbd7'
SOURCE_PATH = 'icon_set/work/todo-references/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crowdin-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('crowdin', 'logo')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Four swept bands preserve the logo's broken, nested C arrangement.
        # Each long boundary uses a coherent cubic with horizontal crest tangency.
        self.add_bezier('outer-upper',(44,12),((38,10),(34,8),(28,8)),((16,8),(6,14),(4,22)))
        self.add_line('upper-end',(4,22),(12,24))
        self.add_bezier('upper-inner',(12,24),((18,10),(32,12),(44,14)))
        self.add_contour('upper-band','outer-upper','upper-end','upper-inner')
        self.add_bezier('inner-upper',(42,20),((32,18),(23,19),(20,27)))
        self.add_line('inner-end',(20,27),(27,28))
        self.add_bezier('inner-return',(27,28),((30,22),(36,22),(40,22)))
        self.add_line('inner-tip',(40,22),(42,20))
        self.add_contour('inner-upper-band','inner-upper','inner-end','inner-return','inner-tip',closed=True)
        self.add_line('lower-end',(4,30),(12,31))
        self.add_bezier('lower-inner',(12,31),((13,36),(18,38),(24,39)))
        self.add_bezier('lower-outer',(24,40),((12,40),(4,37),(4,30)))
        self.add_contour('lower-band-inner','lower-end','lower-inner')
        self.relate('connect','lower-band-inner','lower-outer')
        self.add_line('small-end',(22,32),(29,33))
        self.add_bezier('small-inner',(29,33),((30,36),(34,37),(37,38)))
        self.add_bezier('small-outer',(37,38),((29,39),(23,38),(22,32)))
        self.add_contour('inner-lower-band','small-end','small-inner','small-outer',closed=True)


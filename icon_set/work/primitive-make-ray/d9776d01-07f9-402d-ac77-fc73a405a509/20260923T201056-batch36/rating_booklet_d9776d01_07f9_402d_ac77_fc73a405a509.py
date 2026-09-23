"""A rating booklet with an outlined star and text lines.
Symbol plan: Tall cover with a raised rear leaf contains a central star and two lower rules. Ink extremes (6,2)-(42,46).
Construction: star: five-point outline with purposeful corners; book: upright cover and offset leaf.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd9776d01-07f9-402d-ac77-fc73a405a509'
SOURCE_PATH = 'icon_set/work/todo-references/rating booklet_d9776d01-07f9-402d-ac77-fc73a405a509.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rating-booklet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rating', 'booklet')

    def build(self):
        self.add_polyline('cover',(8,12),(36,12),(40,12),(40,44),(8,44),closed=True)
        self.add_polyline('rear-leaf',(10,10),(36,4),(36,12))
        self.relate('connect','rear-leaf','cover')
        self.add_polyline('rating-star',(24,18),(27,24),(33,24),(28,28),(30,34),(24,30),(18,34),(20,28),(15,24),(21,24),closed=True)
        for i,y in enumerate((38,41)):self.add_line(f'text-{i}',(20,y),(28,y))

    def circle(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self,name,x,y,right,bottom,r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b:continue
            n=f'{name}-{i}'
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def opening_quote(self,name,x,closing=False):
        # A shared 15-unit body and 25-unit pitch own both repeated quotation marks.
        def p(v):
            a,b=v
            return (x+15-a,48-b) if closing else (x+a,b)
        def line(n,a,b):self.add_line(name+n,p(a),p(b))
        def arc(n,a,b):self.add_arc(name+n,p(a),p(b),radius_x=4)
        def bez(n,a,*segs):self.add_bezier(name+n,p(a),*[(p(a),p(b),p(c)) for a,b,c in segs])
        bez('-outer',(0,24),((0,16),(5,8),(11,8)))
        arc('-crown',(11,8),(15,12))
        arc('-return',(15,12),(11,16))
        bez('-inner',(11,16),((7,16),(7,20),(7,24)))
        line('-shelf',(7,24),(11,24))
        arc('-tr',(11,24),(15,28))
        line('-right',(15,28),(15,36))
        arc('-br',(15,36),(11,40))
        line('-bottom',(11,40),(4,40))
        arc('-bl',(4,40),(0,36))
        line('-left',(0,36),(0,24))
        self.add_contour(name,*[name+n for n in ('-outer','-crown','-return','-inner','-shelf','-tr','-right','-br','-bottom','-bl','-left')],closed=True)


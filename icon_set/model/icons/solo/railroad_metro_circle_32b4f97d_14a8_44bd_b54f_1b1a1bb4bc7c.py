"""A front-view metro train and rails inside a circular sign.
Symbol plan: Circular enclosure frames a symmetric train, windshield divider, overhead contact and rails. Ink radius22 about(24,24).
Construction: train-front: symmetric cabin and paired rail exits; input owns the enclosing circle and contact bar.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32b4f97d-14a8-44bd-b54f-1b1a1bb4bc7c'
SOURCE_PATH = 'icon_set/work/todo-references/railroad metro circle_32b4f97d-14a8-44bd-b54f-1b1a1bb4bc7c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'railroad-metro-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('railroad', 'metro', 'circle')

    def build(self):
        self.circle('roundel',24,24,20)
        self.box('train',15,20,33,36,4)
        self.add_line('window-divider',(15,28),(33,28))
        self.relate('connect','window-divider','train')
        self.add_line('contact-stem',(24,12),(24,20))
        self.add_polyline('contact-bar',(19,12),(24,12),(29,12))
        self.relate('connect','contact-stem','contact-bar')
        self.relate('connect','contact-stem','train')
        self.add_line('rail-left',(19,36),(12,40))
        self.add_line('rail-right',(29,36),(36,40))
        for n in ('rail-left','rail-right'):
            self.relate('connect',n,'train')
            self.relate('connect',n,'roundel')

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


"""An open head with an oval thought layer floating above it.
Symbol plan: Oval halo, open circular jaw and broad shoulder curve share a vertical axis. Ink extremes (6,2)-(42,46).
Construction: user-round: broad smooth shoulders; supplied source owns the open-head and oval-layer arrangement.
Human construction: human-reference.md and human_ref/user.svg: circular jaw radius12, lower jaw36, shoulder top40, giving zero ink gap with a scoped touching-bust connection. No detached stick figure is present.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fc8e8b95-766a-4f15-a80b-5e30979a5fc8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/psycho analysis 5_fc8e8b95-766a-4f15-a80b-5e30979a5fc8.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'psycho-analysis-5'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('psycho', 'analysis', '5')
    human_construction = "bust"

    def build(self):
        self.circle('thought-layer',24,8,12,4)
        self.add_line('rim',(12,24),(36,24))
        self.add_arc('jaw',(36,24),(12,24),radius_x=12)
        self.add_contour('head-bowl','rim','jaw',closed=True)
        self.add_line('head-left',(14,20),(12,24))
        self.add_line('head-right',(34,20),(36,24))
        for n in ('head-left','head-right'):self.relate('connect',n,'head-bowl')
        self.add_arc('shoulders',(8,44),(40,44),radius_x=16,radius_y=4)
        self.relate('connect','head-bowl','shoulders')

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


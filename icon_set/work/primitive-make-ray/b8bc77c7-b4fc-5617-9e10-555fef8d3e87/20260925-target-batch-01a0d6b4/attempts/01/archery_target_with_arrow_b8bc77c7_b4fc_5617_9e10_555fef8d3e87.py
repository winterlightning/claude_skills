from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b8bc77c7-b4fc-5617-9e10-555fef8d3e87'
SOURCE_PATH='pictographic-primitives/business/target center_b8bc77c7-b4fc-5617-9e10-555fef8d3e87.svg'
AUTHOR='gpt-6'
PLAN='Open circular target on two feet, restored middle scoring ring, and a clear diagonal arrow with two open feather strokes.'
CONSTRUCTION_REFERENCES='Lucide target: concentric rings; source owns the open upper-right quadrant, arrow and feet.'
OMISSIONS=['Tiny central arc reduced to the round-ended arrow tip; tail feathers kept open to avoid a tiny trapped pocket.']
class Drawing(Solo48):
    icon_id='archery-target-with-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('target', 'center')
    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def ellipse(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def box(self,n,l,t,r,b,k=4,split=False):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            ident=f'{n}-{i}';ids.append(ident);z=pts[(i+1)%8]
            if i%2:self.add_arc(ident,a,z,radius_x=k)
            else:self.add_line(ident,a,z)
        if split:
            for i in range(8):self.relate('connect',ids[i],ids[(i+1)%8])
        else:self.add_contour(n,*ids,closed=True)

    def avatar_body(self,top=32):
        self.add_line('body-left-side',(8,44),(8,top+8))
        self.add_arc('body-left-shoulder',(8,top+8),(16,top),radius_x=8)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,top+8),radius_x=8)
        self.add_line('body-right-side',(40,top+8),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-top-right','body-right-shoulder','body-right-side')
    def portrait_head(self):
        self.add_line('root-left',(14,18),(14,14))
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_line('root-right',(34,14),(34,18))
        self.add_arc('jaw',(34,18),(14,18),radius_x=10)
        self.add_contour('head','root-left','crown','root-right','jaw',closed=True)
        self.add_bezier('fringe',(14,18),((20,18),(22,13),(24,13)),((26,13),(28,18),(34,18)))
        self.relate('connect','head','fringe')
    def build(self):

        self.path('rim',(21,9),[('A',(6,24),15,15,False),('A',(12,36),15,15,False),('A',(30,36),15,15,False),('A',(36,24),15,15,False)])
        self.path('score',(21,18),[('A',(15,24),6,6,False),('A',(21,30),6,6,False),('A',(27,24),6,6,False)])
        self.add_line('arrow-shaft',(21,24),(34,12))
        self.add_polyline('arrow-feathers',(34,6),(34,12),(42,12))
        self.relate('connect','arrow-shaft','arrow-feathers')
        self.add_line('left-foot',(12,36),(6,42));self.add_line('right-foot',(30,36),(36,42))
        self.relate('connect','rim','left-foot');self.relate('connect','rim','right-foot')

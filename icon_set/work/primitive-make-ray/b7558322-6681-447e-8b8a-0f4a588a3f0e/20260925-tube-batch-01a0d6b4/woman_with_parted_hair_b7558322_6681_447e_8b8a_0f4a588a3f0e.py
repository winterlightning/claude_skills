from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b7558322-6681-447e-8b8a-0f4a588a3f0e'
SOURCE_PATH='pictographic-primitives/images/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg'
AUTHOR='gpt-6'
PLAN='Parted fringe above a circular lower face, flared hair ends and broad detached shoulders; restore the identifying hair missing from the current drawing.'
CONSTRUCTION_REFERENCES='human_ref/user.svg: circular jaw and broad shoulders; Lucide user-round: cardinal arc construction. Source owns the parted fringe.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='woman-with-parted-hair'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('woman',)

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

    def build(self):

        self.path('hair-cap',(14,18),[('L',(14,14)),('A',(24,4),10,10,True),('A',(34,14),10,10,True),('L',(34,18))])
        self.path('fringe',(14,18),[('C',(24,12),(18,18),(22,15)),('C',(34,18),(26,15),(30,18))])
        self.path('jaw',(14,18),[('A',(24,28),10,10,False),('A',(34,18),10,10,False)])
        self.path('shoulders',(8,44),[('A',(24,36),16,8,True),('A',(40,44),16,8,True)])
        self.add_line('hair-left',(14,18),(10,28));self.add_line('hair-right',(34,18),(38,28))
        for a,b in [('hair-cap','fringe'),('hair-cap','jaw'),('fringe','jaw'),('hair-left','jaw'),('hair-right','jaw'),('hair-left','fringe'),('hair-right','fringe'),('hair-left','hair-cap'),('hair-right','hair-cap')]:self.relate('connect',a,b)

HUMAN_CONSTRUCTION_REVIEW = {'reference': 'icon_set/references/human_ref/user.svg', 'jaw_center': [24, 18], 'jaw_radius': 10, 'shoulder_top': 36, 'head_to_body_ink_gap': 4, 'proof': '36-(18+10)-4=4 at the shared vertical axis. The circular jaw and shoulder ellipse are closest at their vertical extrema.'}

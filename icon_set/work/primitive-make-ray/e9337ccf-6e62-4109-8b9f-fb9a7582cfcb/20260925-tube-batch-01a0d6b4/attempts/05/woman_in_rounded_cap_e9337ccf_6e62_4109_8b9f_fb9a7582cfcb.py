from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e9337ccf-6e62-4109-8b9f-fb9a7582cfcb'
SOURCE_PATH='pictographic-primitives/avatars/detective woman_e9337ccf-6e62-4109-8b9f-fb9a7582cfcb.svg'
AUTHOR='gpt-6'
PLAN='Restore the reference rounded cap and curved visor, circular lower face, flipped bob hair and V-neck shoulders.'
CONSTRUCTION_REFERENCES='Lucide hat-glasses: separate crown and brim construction; human_ref/user.svg owns round jaw and shoulder vocabulary.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='woman-in-rounded-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('detective', 'woman')

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

        self.path('crown',(14,14),[('A',(24,4),10,10,True),('A',(34,14),10,10,True)])
        self.path('visor',(14,14),[('C',(34,14),(19,20),(29,20))])
        self.path('jaw',(14,14),[('L',(14,20)),('A',(24,30),10,10,False),('A',(34,20),10,10,False),('L',(34,14))])
        for side in (-1,1):
            p=lambda x,y:(x,y) if side==-1 else (48-x,y)
            n='hair'+str(side)
            self.path(n,p(14,20),[('C',p(8,28),p(14,25),p(11,28))])
            self.relate('connect',n,'jaw')
        self.path('shoulders',(8,44),[('C',(18,38),(8,40),(12,38)),('L',(24,43)),('L',(30,38)),('C',(40,44),(36,38),(40,40))])
        self.relate('connect','crown','visor');self.relate('connect','visor','jaw');self.relate('connect','crown','jaw')

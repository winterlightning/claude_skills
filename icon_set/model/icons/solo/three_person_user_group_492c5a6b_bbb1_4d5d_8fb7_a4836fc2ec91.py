from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='492c5a6b-bbb1-4d5d-8fb7-a4836fc2ec91'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/people_492c5a6b-bbb1-4d5d-8fb7-a4836fc2ec91.svg'
AUTHOR='gpt-6'
PLAN = 'Larger centered head above two smaller side heads, with broad curved shoulders layered in front of the side busts.'
CONSTRUCTION_REFERENCES='human_ref/user.svg: circular heads and open rounded shoulders; Lucide users-round: foreground/background arrangement.'
OMISSIONS = []
class Drawing(Solo48):
    icon_id='three-person-group'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('people',)
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
        self.human_construction='bust'
        self.circle('head',24,13,5)
        self.path('front-body',(14,40),[('L',(14,32)),('A',(24,22),10,10,True),('A',(34,32),10,10,True),('L',(34,40))])
        self.relate('connect','head','front-body')
        for side in (-1,1):
            p=lambda x,y:(x,y) if side==-1 else (48-x,y)
            n='left' if side==-1 else 'right'
            self.circle(n+'-head',8 if side==-1 else 40,18,3)
            self.path(n+'-body',p(4,40),[('L',p(4,29)),('A',p(8,25),4,4,side==-1),('A',p(14,32),6,7,side==-1)])
            self.relate('connect',n+'-body','front-body');self.relate('connect',n+'-head',n+'-body')

    icon_id = 'three-person-user-group'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'person', 'user', 'group')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

HUMAN_CONSTRUCTION_REVIEW = {'head_bottoms': [18, 21, 21], 'shoulder_tops': [22, 25, 25], 'reference': 'icon_set/references/human_ref/user.svg', 'specialization': 'icon-avatar', 'centerline_gap': 4, 'visible_ink_gap': 0, 'proof': 'Each shoulder apex is four centerline units below its own circular head or jaw bottom. With stroke width four, the ink edges touch. Avatar specialization requested by user.'}

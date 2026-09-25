from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from ...keyshapes import Keyshape
SOURCE_ICON_ID='f2eb39da-ca20-4f47-8b9c-8c8796ff574d'
SOURCE_PATH='pictographic-primitives/other/two users woman_f2eb39da-ca20-4f47-8b9c-8c8796ff574d.svg'
AUTHOR='gpt-6'
PLAN = 'Larger woman at front-left, smaller person lower behind-right; smooth parted hair and layered curved shoulders with touching head/body ink.'
CONSTRUCTION_REFERENCES='human_ref/user.svg and Lucide users-round: circular faces and overlapping busts. Reference owns the relative head heights.'
OMISSIONS = ['Small hair tips and V-neck seam omitted to avoid crowded extra strokes.']
class Drawing(Solo48):
    icon_id='woman-and-person-busts'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('two', 'users', 'woman')
    human_construction='bust'
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
        self.path('front-head',(8,20),[('L',(8,16)),('A',(16,8),8,8,True),('A',(24,16),8,8,True),('L',(24,20)),('A',(16,28),8,8,True),('A',(8,20),8,8,True)],True)
        self.add_bezier('front-fringe',(8,20),((12,20),(14,18),(16,18)),((18,18),(20,20),(24,20)))
        self.relate('connect','front-head','front-fringe')
        self.path('front-body',(4,40),[('A',(16,32),12,8,True),('A',(28,40),12,8,True)])
        self.circle('back-head',38,22,6)
        self.path('back-body',(28,40),[('A',(38,32),10,8,True),('A',(44,38),6,6,True)])
        self.relate('connect','front-head','front-body');self.relate('connect','back-head','back-body');self.relate('connect','front-body','back-body')

HUMAN_CONSTRUCTION_REVIEW = {'head_bottoms': [28, 28], 'shoulder_tops': [32, 32], 'reference': 'icon_set/references/human_ref/user.svg', 'specialization': 'icon-avatar', 'centerline_gap': 4, 'visible_ink_gap': 0, 'proof': 'Each shoulder apex is four centerline units below its own circular head or jaw bottom. With stroke width four, the ink edges touch. Avatar specialization requested by user.'}

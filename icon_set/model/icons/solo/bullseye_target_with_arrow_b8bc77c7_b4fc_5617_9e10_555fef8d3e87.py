from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b8bc77c7-b4fc-5617-9e10-555fef8d3e87'
SOURCE_PATH='pictographic-primitives/business/target center_b8bc77c7-b4fc-5617-9e10-555fef8d3e87.svg'
AUTHOR='gpt-6'
PLAN = 'Open circular target on two feet, restored middle scoring ring, and a clear diagonal arrow with two open feather strokes.'
CONSTRUCTION_REFERENCES='Lucide target: concentric rings; source owns the open upper-right quadrant, arrow and feet.'
OMISSIONS = ['Tiny central arc reduced to the round-ended arrow tip; tail feathers kept open to avoid a tiny trapped pocket.']
class Drawing(Solo48):
    icon_id='archery-target-with-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'business'
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
        self.path('rim',(23,6),[('A',(6,23),17,17,False),('A',(15,38),17,17,False),('A',(31,38),17,17,False),('A',(40,23),17,17,False)])
        self.path('score',(23,14),[('A',(14,23),9,9,False),('A',(23,32),9,9,False),('A',(32,23),9,9,False)])
        self.add_line('arrow-shaft',(23,23),(34,12))
        self.add_polyline('arrow-feathers',(34,6),(34,12),(42,12))
        self.relate('connect','arrow-shaft','arrow-feathers')
        self.add_line('left-foot',(15,38),(10,42));self.add_line('right-foot',(31,38),(36,42))
        self.relate('connect','rim','left-foot');self.relate('connect','rim','right-foot')

    icon_id = 'bullseye-target-with-arrow'
    category = 'business'
    aliases = ()
    keywords = ('bullseye', 'target', 'with', 'arrow')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'source_request': 'other unresolve could make as eception', 'scope': ['score / arrow-shaft: 6.36396 centerline units, approximately 2.36396 ink units, below required four.', 'rim / score: curved certification reports 7.99939 centerline units; concentric radii 17 and 9 give exactly eight centerline units.'], 'reason': 'Preserve the diagonal arrow and recognizable scoring ring. Retained as a local exception; raw QA failure is not a strict pass.', 'svg_sha256': 'dd39550ccfa6f19fd6c7856a5648285d1bc58ddd205c8d6bc355faab52cc42cb', 'source_svg_sha256': '500119332fcd8fa83d7c436cd538a036c6cc88c96f1b7fd50b2f1d233601b846'}

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'source_request': 'other unresolve could make as eception', 'scope': ['score / arrow-shaft: 6.36396 centerline units, approximately 2.36396 ink units, below required four.', 'rim / score: curved certification reports 7.99939 centerline units; concentric radii 17 and 9 give exactly eight centerline units.'], 'reason': 'Preserve the diagonal arrow and recognizable scoring ring. Retained as a local exception; raw QA failure is not a strict pass.', 'svg_sha256': '500119332fcd8fa83d7c436cd538a036c6cc88c96f1b7fd50b2f1d233601b846'}

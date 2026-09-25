from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from ...keyshapes import Keyshape
SOURCE_ICON_ID='f27e9ceb-3471-4f88-9ba7-afea584d2ef1'
SOURCE_PATH='pictographic-primitives/other/message bubble person_f27e9ceb-3471-4f88-9ba7-afea584d2ef1.svg'
AUTHOR='gpt-6'
PLAN = 'Rounded speech bubble with a lower-left tail and a larger circular portrait on curved touching shoulders.'
CONSTRUCTION_REFERENCES='Lucide message-circle: smooth bubble outline; human_ref/user.svg and icon-avatar: circular head and touching shoulder construction.'
OMISSIONS = []
class Drawing(Solo48):
    icon_id='speech-bubble-with-user'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('message', 'bubble', 'person')
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
        self.add_line('bubble-top',(12,4),(36,4))
        self.add_arc('bubble-tr',(36,4),(40,8),radius_x=4)
        self.add_line('bubble-right',(40,8),(40,33))
        self.add_arc('bubble-br',(40,33),(36,37),radius_x=4)
        self.add_polyline('bubble-tail',(36,37),(24,37),(16,44),(16,37),(12,37))
        self.add_arc('bubble-bl',(12,37),(8,33),radius_x=4)
        self.add_line('bubble-left',(8,33),(8,8))
        self.add_arc('bubble-tl',(8,8),(12,4),radius_x=4)
        parts=['bubble-top','bubble-tr','bubble-right','bubble-br','bubble-tail','bubble-bl','bubble-left','bubble-tl']
        for a,b in zip(parts,parts[1:]+parts[:1]):self.relate('connect',a,b)
        self.circle('head',24,16,4)
        self.path('body',(17,28),[('A',(24,24),7,4,True),('A',(31,28),7,4,True)])
        self.relate('connect','head','body')

HUMAN_CONSTRUCTION_REVIEW = {'head_bottoms': [20], 'shoulder_tops': [24], 'reference': 'icon_set/references/human_ref/user.svg', 'specialization': 'icon-avatar', 'centerline_gap': 4, 'visible_ink_gap': 0, 'proof': 'Each shoulder apex is four centerline units below its own circular head or jaw bottom. With stroke width four, the ink edges touch. Avatar specialization requested by user.'}

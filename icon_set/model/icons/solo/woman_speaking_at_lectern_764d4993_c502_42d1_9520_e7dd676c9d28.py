from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='764d4993-c502-42d1-9520-e7dd676c9d28'
SOURCE_PATH='pictographic-primitives/users/woman podium_764d4993-c502-42d1-9520-e7dd676c9d28.svg'
AUTHOR='gpt-6'
PLAN='Woman with parted bob hair and a real neck behind a broad lectern with inward-tapering sides.'
CONSTRUCTION_REFERENCES='Lucide presentation: straight podium ledge; human_ref/user.svg owns round jaw and smooth shoulders. Source owns hairstyle and lectern.'
OMISSIONS=['Hair ends shortened for neck clearance. Cropped lectern completed with a lower edge.']
class Drawing(Solo48):
    icon_id='woman-speaking-at-lectern'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases=()
    keywords=('woman', 'podium')

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
        self.path('hair-cap',(14,16),[('L',(14,14)),('A',(24,4),10,10,True),('A',(34,14),10,10,True),('L',(34,16))])
        self.path('fringe',(14,16),[('C',(24,12),(18,16),(22,15)),('C',(34,16),(26,15),(30,16))])
        self.path('jaw',(14,16),[('A',(18,24),10,10,False),('A',(24,26),10,10,False),('A',(30,24),10,10,False),('A',(34,16),10,10,False)])
        self.path('left-body',(18,24),[('L',(18,26)),('C',(12,34),(18,30),(12,30))])
        self.path('right-body',(30,24),[('L',(30,26)),('C',(36,34),(30,30),(36,30))])
        self.path('left-hair',(14,16),[('C',(10,22),(14,18),(12,21))])
        self.path('right-hair',(34,16),[('C',(38,22),(34,18),(36,21))])
        self.add_polyline('ledge',(8,34),(12,34),(36,34),(40,34))
        self.add_polyline('lectern',(12,34),(16,44),(32,44),(36,34))
        for a,b in [('hair-cap','fringe'),('hair-cap','jaw'),('fringe','jaw'),('jaw','left-body'),('jaw','right-body'),('left-body','ledge'),('right-body','ledge'),('lectern','ledge'),('left-hair','jaw'),('right-hair','jaw'),('left-hair','hair-cap'),('right-hair','hair-cap'),('left-hair','fringe'),('right-hair','fringe')]:self.relate('connect',a,b)

HUMAN_CONSTRUCTION_REVIEW = {'reference': 'icon_set/references/human_ref/user.svg', 'jaw_center': [24, 16], 'jaw_radius': 10, 'construction': 'Real neck connects at (18,24)/(30,24), exact points on the circular jaw. Detached-head spacing does not apply.'}

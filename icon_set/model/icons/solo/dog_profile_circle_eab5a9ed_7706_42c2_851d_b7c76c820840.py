from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='eab5a9ed-7706-42c2-851d-b7c76c820840'
SOURCE_PATH='pictographic-primitives/pets/dog head_eab5a9ed-7706-42c2-851d-b7c76c820840.svg'
AUTHOR='gpt-6'
PLAN='Left-facing pointed-ear dog profile, rounded muzzle and neck; back and neck attach to actual circle nodes.'
CONSTRUCTION_REFERENCES='Lucide dog: rounded animal contours; supplied source governs the angular ear and left-facing profile.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='dog-profile-circle'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('dog', 'head')

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
        self.path('rim',(24,44),[('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True),('A',(24,44),20,20,True)],True)
        self.path('dog',(24,44),[('L',(24,32)),('L',(17,32)),('C',(12,26),(14,32),(13,29)),('L',(12,24)),('L',(19,19)),('C',(21,15),(21,18),(21,17)),('L',(21,12)),('L',(40,36))])
        self.relate('connect','dog','rim')

from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9fea270f-2e24-4304-9328-79e02032c303'
SOURCE_PATH='pictographic-primitives/health/medical file_9fea270f-2e24-4304-9328-79e02032c303.svg'
AUTHOR='gpt-6'
PLAN='Beveled document with a balanced outlined medical cross; equal horizontal and vertical arms.'
CONSTRUCTION_REFERENCES='Lucide file-plus: page corners and medical placement; source cross remains outlined.'
OMISSIONS=['No extra inner fold seam added: source has only the beveled outline.']
class Drawing(Solo48):
    icon_id='medical-record-document'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('medical', 'file')

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
        pts=[(12,4),(30,4),(40,14),(40,40),(36,44),(12,44),(8,40),(8,8)]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];n=f'page-{i}'
            if i in (3,5,7):self.add_arc(n,a,b,radius_x=4)
            else:self.add_line(n,a,b)
        for i in range(8):self.relate('connect',f'page-{i}',f'page-{(i+1)%8}')
        self.add_polyline('cross',(20,18),(28,18),(28,22),(32,22),(32,30),(28,30),(28,34),(20,34),(20,30),(16,30),(16,22),(20,22),closed=True)

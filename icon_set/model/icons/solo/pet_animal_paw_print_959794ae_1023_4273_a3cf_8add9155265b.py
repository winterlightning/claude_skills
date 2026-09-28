from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='959794ae-1023-4273-a3cf-8add9155265b'
SOURCE_PATH='pictographic-primitives/other/paw print_959794ae-1023-4273-a3cf-8add9155265b.svg'
AUTHOR='gpt-6'
PLAN='Four oval toe pads above a broad, smoothly rounded triangular paw pad, with a shallow lower notch.'
CONSTRUCTION_REFERENCES='Lucide paw-print: independent pads; supplied source controls the four upright ovals and centered broad pad.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='pet-animal-paw-print'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('paw', 'print')

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
        for i,(x,y) in enumerate(((9,24),(16,10),(32,10),(39,24))):self.ellipse(f'toe-{i}',x,y,3,4)
        self.path('pad',(24,28),[('C',(14,36),(20,28),(18,33)),('C',(18,42),(12,38),(12,42)),('C',(24,41),(21,42),(22,41)),('C',(30,42),(26,41),(27,42)),('C',(34,36),(36,42),(36,38)),('C',(24,28),(30,33),(28,28))],True)

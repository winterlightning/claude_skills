from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='6a3e9b51-1d2b-5969-ac5c-503d8629e1bb'
SOURCE_PATH='pictographic-primitives/health/hearing aid ear_6a3e9b51-1d2b-5969-ac5c-503d8629e1bb.svg'
AUTHOR='gpt-6'
PLAN='Organic outer ear, distinct inner bowl and canal notch, with a rounded hearing-aid casing behind the right edge.'
CONSTRUCTION_REFERENCES='Lucide ear: coherent upper bowl and lower lobe curves; source owns the separate aid casing.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='ear-with-hearing-aid'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('hearing', 'aid', 'ear')

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

        self.path('ear',(8,16),[('C',(22,4),(8,8),(14,4)),('C',(32,14),(28,4),(32,8)),('C',(30,30),(35,21),(34,25)),('C',(24,38),(26,34),(24,34)),('C',(16,44),(24,42),(20,44)),('C',(8,36),(10,44),(8,40))])
        self.path('aid',(32,14),[('C',(40,20),(40,16),(40,18)),('L',(38,28)),('C',(30,30),(38,32),(34,32))])
        self.path('bowl',(16,16),[('C',(28,20),(16,8),(28,10)),('C',(24,28),(28,24),(26,26))])
        self.path('canal',(16,16),[('C',(16,28),(24,16),(24,26)),('C',(14,32),(13,28),(13,30))])
        self.relate('connect','ear','aid');self.relate('connect','bowl','canal')

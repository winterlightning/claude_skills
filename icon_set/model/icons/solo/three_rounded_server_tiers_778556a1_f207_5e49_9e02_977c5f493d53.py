from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='778556a1-f207-5e49-9e02-977c5f493d53'
SOURCE_PATH='pictographic-primitives/servers/server choose_778556a1-f207-5e49-9e02-977c5f493d53.svg'
AUTHOR='gpt-6'
PLAN='Three stacked tiers with separate convex rounded ends; preserve the scalloped sides rather than a single rounded box.'
CONSTRUCTION_REFERENCES='Lucide server: repeated horizontal trays; source owns the shared rails and bulging ends.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='three-rounded-server-tiers'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'servers'
    aliases=()
    keywords=('server', 'choose')

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

        self.path('outline',(10,8),[('L',(38,8)),('A',(38,18),6,5,True),('A',(38,30),6,6,True),('A',(38,40),6,5,True),('L',(10,40)),('A',(10,30),6,5,True),('A',(10,18),6,6,True),('A',(10,8),6,5,True)],True)
        for y in (18,30):
            self.add_line('rail-'+str(y),(10,y),(38,y));self.relate('connect','outline','rail-'+str(y))

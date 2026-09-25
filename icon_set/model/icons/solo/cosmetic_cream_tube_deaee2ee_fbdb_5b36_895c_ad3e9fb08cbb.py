from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='deaee2ee-fbdb-5b36-895c-ad3e9fb08cbb'
SOURCE_PATH='pictographic-primitives/beauty/tube_deaee2ee-fbdb-5b36-895c-ad3e9fb08cbb.svg'
AUTHOR='gpt-6'
PLAN='Restore the sloped shoulders between cap and tapered tube, upright oval label and lower crimp band.'
CONSTRUCTION_REFERENCES='Lucide pipette: rounded end and narrow attachment; source owns tube silhouette.'
OMISSIONS=['Upper horizontal shoulder seam omitted to preserve room for the upright label; sloped shoulders retained.']
class Drawing(Solo48):
    icon_id='cosmetic-cream-tube'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tube',)

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

        self.path('body',(16,12),[('L',(12,16)),('L',(8,36)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,36)),('L',(36,16)),('L',(32,12))])
        self.add_polyline('cap',(16,12),(16,4),(32,4),(32,12),(16,12))
        self.add_line('band',(8,36),(40,36))
        self.ellipse('label',24,24,3,4)
        self.relate('connect','body','cap');self.relate('connect','body','band')

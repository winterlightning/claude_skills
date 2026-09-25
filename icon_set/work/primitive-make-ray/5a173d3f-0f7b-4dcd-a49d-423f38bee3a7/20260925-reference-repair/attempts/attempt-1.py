from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='5a173d3f-0f7b-4dcd-a49d-423f38bee3a7'
SOURCE_PATH='pictographic-primitives/transportation/e scooter_5a173d3f-0f7b-4dcd-a49d-423f38bee3a7.svg'
AUTHOR='gpt-6'
PLAN='Tall slim scooter steering stem, short T handle, small circular wheels, rising deck and upper platform mark.'
CONSTRUCTION_REFERENCES='Lucide scooter: coherent stem/deck and circular wheels; source controls tall proportions and additional platform line.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='electric-kick-scooter'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('e', 'scooter')

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
        for n,x in [('rear',10),('front',38)]:self.circle(n+'-wheel',x,38,4)
        self.path('deck',(14,38),[('L',(26,38)),('L',(32,29)),('C',(36,26),(33,27),(34,26)),('L',(42,26))]);self.relate('connect','deck','rear-wheel')
        self.add_line('stem',(30,6),(36,26));self.relate('connect','stem','deck')
        self.add_polyline('handlebar',(24,6),(30,6),(36,6));self.relate('connect','handlebar','stem')
        self.add_line('platform',(16,30),(27,30))

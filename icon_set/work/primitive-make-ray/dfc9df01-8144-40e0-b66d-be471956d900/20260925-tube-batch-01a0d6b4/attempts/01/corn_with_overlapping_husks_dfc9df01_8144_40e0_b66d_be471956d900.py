from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='dfc9df01-8144-40e0-b66d-be471956d900'
SOURCE_PATH='pictographic-primitives/food/corn_dfc9df01-8144-40e0-b66d-be471956d900.svg'
AUTHOR='gpt-6'
PLAN='Long upright rounded cob above two tapering curved husks, with the right husk overlapping the left.'
CONSTRUCTION_REFERENCES='Lucide wheat: leaf curve construction only; source has a smooth cob with no kernel grid.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='corn-with-overlapping-husks'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('corn',)

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

        self.path('cob',(16,28),[('L',(16,12)),('A',(24,4),8,8,True),('A',(32,12),8,8,True),('L',(32,28))])
        self.path('left-leaf',(8,24),[('C',(16,28),(11,24),(14,26)),('C',(24,36),(20,31),(22,33)),('C',(22,44),(22,39),(22,42)),('C',(8,24),(10,44),(13,32))],True)
        self.path('right-leaf',(22,44),[('C',(32,28),(22,36),(28,30)),('C',(40,24),(34,26),(37,24)),('C',(22,44),(36,31),(40,44))],True)
        self.relate('connect','cob','left-leaf');self.relate('connect','cob','right-leaf');self.relate('connect','left-leaf','right-leaf')

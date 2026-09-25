from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='6ce17d6f-0a53-4eaa-b433-061d444307dc'
SOURCE_PATH='pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'
AUTHOR='gpt-6'
PLAN='Two equal large wheels with the source open frame, distinct saddle, and smoothly returned handlebar.'
CONSTRUCTION_REFERENCES='Lucide bike: circular wheel construction; supplied reference controls the open frame without a rider.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='simple-two-wheeled-bicycle'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'transportation'
    aliases=()
    keywords=('bicycle',)

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
        for n,x in [('rear',12),('front',36)]:self.circle(n+'-wheel',x,32,8)
        self.add_polyline('frame',(12,24),(20,16),(33,16));self.relate('connect','frame','rear-wheel')
        self.add_polyline('saddle',(12,10),(16,10),(18,10));self.add_line('seat-post',(16,10),(20,16))
        self.relate('connect','saddle','seat-post');self.relate('connect','seat-post','frame')
        self.path('fork',(26,8),[('L',(30,8)),('C',(33,16),(32,8),(32,12)),('C',(36,24),(34,20),(35,22))])
        self.relate('connect','fork','frame');self.relate('connect','fork','front-wheel')

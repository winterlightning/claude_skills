from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='764d4993-c502-42d1-9520-e7dd676c9d28'
SOURCE_PATH='pictographic-primitives/users/woman podium_764d4993-c502-42d1-9520-e7dd676c9d28.svg'
AUTHOR='gpt-6'
PLAN='Woman with parted bob hair and a real neck behind a broad lectern with inward-tapering sides.'
CONSTRUCTION_REFERENCES='Lucide presentation: straight podium ledge; human_ref/user.svg owns round jaw and smooth shoulders. Source owns hairstyle and lectern.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='woman-speaking-at-lectern'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
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

        self.path('hair',(13,24),[('C',(14,14),(15,22),(14,18)),('C',(24,4),(14,8),(18,4)),('C',(34,14),(30,4),(34,8)),('C',(35,24),(34,18),(33,22))])
        self.path('fringe',(18,14),[('C',(24,10),(21,13),(23,12)),('C',(30,14),(25,12),(27,13))])
        self.path('jaw',(18,14),[('A',(24,20),6,6,False),('A',(30,14),6,6,False)])
        self.path('body-left',(18,14),[('L',(18,23)),('C',(12,32),(18,28),(12,26))])
        self.path('body-right',(30,14),[('L',(30,23)),('C',(36,32),(30,28),(36,26))])
        self.add_polyline('ledge',(8,32),(12,32),(36,32),(40,32))
        self.add_polyline('lectern',(12,32),(16,44),(32,44),(36,32))
        for a,b in [('jaw','fringe'),('jaw','body-left'),('jaw','body-right'),('fringe','body-left'),('fringe','body-right'),('body-left','ledge'),('body-right','ledge'),('lectern','ledge')]:self.relate('connect',a,b)

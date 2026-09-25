from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0ec7e42f-2776-5a70-a652-9140ef5c56c7'
SOURCE_PATH='pictographic-primitives/transportation/truck_0ec7e42f-2776-5a70-a652-9140ef5c56c7.svg'
AUTHOR='gpt-6'
PLAN='Rounded parcel cargo with visible notched tape, open lower rear cab edge, short windscreen mark and two equal wheels.'
CONSTRUCTION_REFERENCES='Lucide truck: rounded cargo and circular wheels; source owns parcel tape and open cabin division.'
OMISSIONS=['Parcel notch is shallower and windscreen mark shorter; the cargo outline meets the rear wheel at its top to keep clear space.']
class Drawing(Solo48):
    icon_id='parcel-delivery-truck'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'transportation'
    aliases=()
    keywords=('truck',)

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

        self.path('cargo',(12,32),[('L',(8,32)),('A',(4,28),4,4,True),('L',(4,12)),('A',(8,8),4,4,True),('L',(12,8)),('L',(20,8)),('L',(24,8)),('A',(28,12),4,4,True),('L',(28,16)),('L',(28,30))])
        self.path('cab',(28,16),[('L',(34,16)),('L',(44,24)),('L',(44,32)),('A',(40,36),4,4,True)])
        self.circle('rear-wheel',12,36,4);self.circle('front-wheel',36,36,4)
        self.add_line('chassis',(16,36),(32,36));self.add_line('windscreen',(36,24),(44,24))
        self.add_polyline('parcel-tape',(12,8),(12,18),(16,15),(20,18),(20,8))
        for a,b in [('cargo','cab'),('cargo','rear-wheel'),('cargo','parcel-tape'),('cab','front-wheel'),('cab','windscreen'),('chassis','rear-wheel'),('chassis','front-wheel')]:self.relate('connect',a,b)

    icon_id = 'parcel-delivery-truck'
    category = 'transportation'
    aliases = ()
    keywords = ('delivery truck', 'parcel', 'package', 'shipping', 'courier', 'logistics', 'truck', 'box')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

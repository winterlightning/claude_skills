from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0005e7b2-b6eb-47bb-9376-770c2522288d'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/monitor upload_0005e7b2-b6eb-47bb-9376-770c2522288d.svg'
AUTHOR = 'gpt-6'
PLAN = 'Monitor with an upward upload arrow.'
CONSTRUCTION_REFERENCES = 'Lucide monitor: rounded screen, central stem and foot.'
OMISSIONS = 'No omissions.'

class Drawing(Solo48):
    icon_id = 'monitor-upload'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    categories = ("computers", "primitives")
    aliases = ()
    keywords = ('monitor', 'upload')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        nodes={'screen': [(24, 34)]}.get(n,[])
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if i%2:
                part=n+str(i);self.add_arc(part,a,z,radius_x=r);members.append(part)
            else:
                inner=[p for p in nodes if p!=a and p!=z and (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                inner.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                chain=[a]+inner+[z]
                for j,(u,v) in enumerate(zip(chain,chain[1:])):
                    part=n+str(i)+'-'+str(j);self.add_line(part,u,v);members.append(part)
        self.add_contour(n,*members,closed=True)
    def monitor(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')
    def person(self,x,y,r):
        # human_ref/user.svg: head and broad shoulders. Exact 8 centerline / 4 ink gap.
        self.circle('head',x,y,r)
        top=y+r+8
        self.add_arc('shoulders',(x-5,top+5),(x+5,top+5),radius_x=5)
    def play(self,x,y,w,h):
        self.add_polyline('play',(x,y),(x+w,y+h//2),(x,y+h),closed=True)

    def build(self):
        self.monitor()
        self.add_polyline('arrowhead',(18,21),(24,15),(30,21))
        self.add_line('shaft',(24,15),(24,25));self.relate('connect','arrowhead','shaft')

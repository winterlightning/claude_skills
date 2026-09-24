from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f180a84-a846-4671-b767-dbb6041f800a'
SOURCE_PATH = 'pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg'
AUTHOR = 'gpt-6'
PLAN = 'Passport booklet with globe and rear-cover reveal.'
CONSTRUCTION_REFERENCES = 'Lucide monitor rounded enclosure principle; symmetric globe construction.'
OMISSIONS = 'Rear-cover reveal simplified.'

class Drawing(Solo48):
    icon_id = 'passport'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('passport',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        nodes={'cover': [(8, 16), (36, 12)]}.get(n,[])
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
        self.box('cover',8,12,32,32,3)
        self.circle('globe',24,28,9)
        self.add_arc('meridian-left',(24,19),(24,37),radius_x=5,radius_y=9,sweep=False)
        self.add_arc('meridian-right',(24,19),(24,37),radius_x=5,radius_y=9)
        self.add_polyline('equator',(15,28),(24,28),(33,28))
        for a,b in [('globe','meridian-left'),('globe','meridian-right'),('globe','equator'),('meridian-left','meridian-right'),('meridian-left','equator'),('meridian-right','equator')]:self.relate('connect',a,b)
        self.add_polyline('rear-cover',(8,16),(8,8),(36,4),(36,12));self.relate('connect','cover','rear-cover')

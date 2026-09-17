"""Connected Device Network — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3686422f-b88b-44f4-b6bd-0475b11b685b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/internet/internet of thing graph service_3686422f-b88b-44f4-b6bd-0475b11b685b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'connected-device-network'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'internet'
    aliases = ()
    keywords = ('connected', 'device', 'network')

    def build(self):
        # Plan: taller central device and paired low devices with separate descending branches.
        # HRECT_L extremes4,8,44,40. Lucide network informs rounded nodes and elbows.
        # Drop the central button to retain useful interior clearance.
        self.box('center',16,8,16,12)
        for n,x,s in [('left',4,1),('right',36,-1)]:
            self.box(n,x,28,8,8)
            a=12 if s==1 else 36;z=a+s*2
            self.add_arc(n+'-elbow',(a,32),(z,34),radius_x=2,sweep=s==1)
            self.add_line(n+'-stem',(z,34),(z,40));self.add_contour(n+'-branch',n+'-elbow',n+'-stem')
        self.add_line('middle-stem',(24,20),(24,40));self.join_shared()


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h//2),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+h//2),(x,y+r)]
        ids=[]
        for i,(a,z) in enumerate(zip(pts,pts[1:]+pts[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if i in (2,5,8,11):self.add_arc(name,a,z,radius_x=r)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def join_shared(self):
        from icon_set.renderers.svg import build_paths
        paths=build_paths(self.draw())
        for i,a in enumerate(paths):
            ap={(p.start.x,p.start.y) for p in a['primitives']}|{(p.end.x,p.end.y) for p in a['primitives']}
            for z in paths[i+1:]:
                zp={(p.start.x,p.start.y) for p in z['primitives']}|{(p.end.x,p.end.y) for p in z['primitives']}
                if ap & zp:self.relate('connect',a['id'],z['id'])


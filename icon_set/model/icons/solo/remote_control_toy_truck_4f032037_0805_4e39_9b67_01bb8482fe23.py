"""Remote Control Toy Truck — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4f032037-0805-4e39-9b67-01bb8482fe23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys car push_4f032037-0805-4e39-9b67-01bb8482fe23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'remote-control-toy-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('remote', 'control', 'toy', 'truck')

    def build(self):
        # Plan: raised cab, pickup bed, round antenna tip and large wheels.
        # HRECT_L extremes4,8,44,40. Lucide truck supplies wheel/body construction.
        # Omit hubs and suspension; body attaches at the wheel tops with open clearance.
        self.circle('left-wheel',12,34,6);self.circle('right-wheel',36,34,6)
        self.add_polyline('body',(12,28),(4,20),(4,18),(12,18),(16,10),(24,10),(24,20),(32,20),(44,20),(36,28))
        self.add_line('axle',(18,34),(30,34))
        self.add_line('antenna',(32,20),(38,12));self.circle('tip',38,10,2);self.join_shared()

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

    def head(self,x,y,r):
        self.add_arc('head-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc('head-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)


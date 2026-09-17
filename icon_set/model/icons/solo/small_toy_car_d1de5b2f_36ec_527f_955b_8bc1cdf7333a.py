"""Small Toy Car — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd1de5b2f-36ec-527f-955b-8bc1cdf7333a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toy car roof_d1de5b2f-36ec-527f-955b-8bc1cdf7333a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-toy-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('small', 'toy', 'car')

    def build(self):
        # Plan: rounded toy-car roof, divided broad window and two matching wheels.
        # HRECT_L extremes4,8,44,40. Lucide car informs wheel/body connections.
        # Roof and window share their boundary; body tapers into the wheel tops.
        self.circle('rear-wheel',12,34,6);self.circle('front-wheel',36,34,6)
        self.add_polyline('left',(12,28),(4,20),(10,20))
        self.add_bezier('roof-left',(10,20),((12,8),(16,8),(24,8)))
        self.add_bezier('roof-right',(24,8),((32,8),(36,8),(38,20)))
        self.add_polyline('right',(38,20),(44,20),(36,28))
        self.add_polyline('window-base',(10,20),(24,20),(38,20))
        self.add_line('divider',(24,8),(24,20));self.add_line('axle',(18,34),(30,34));self.join_shared()

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


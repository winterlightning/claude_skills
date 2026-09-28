"""Ride On Toy Car — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14a87129-b940-584b-a5af-bccc42f092d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/pedal car walker stroller_14a87129-b940-584b-a5af-bccc42f092d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ride-on-toy-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('ride', 'on', 'toy', 'car')

    def build(self):
        # Plan: open ride-on body, high seatback, angled steering and paired wheels.
        # HRECT_L extremes4,8,44,40. Lucide car informs clean wheel/body connections.
        # Seatback and steering wheel reduce to simple strokes; no wheel hubs.
        self.circle('rear-wheel',12,34,6);self.circle('front-wheel',36,34,6)
        self.add_line('axle',(18,34),(30,34))
        self.add_polyline('rear',(12,28),(4,20),(10,20))
        self.add_polyline('seat',(10,8),(10,20),(18,20),(24,24),(32,20))
        self.add_line('front',(32,20),(44,20))
        self.add_line('hood',(44,20),(36,28))
        self.add_line('column',(24,24),(24,10));self.add_polyline('steering',(20,8),(24,10),(28,12));self.join_shared()

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


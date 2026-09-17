"""Sitting Rabbit — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5be03394-7f1d-5f44-a499-85162f13e538'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/rabbit animal shaped toy_5be03394-7f1d-5f44-a499-85162f13e538.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sitting-rabbit-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('sitting', 'rabbit', 'reference')

    def build(self):
        # Plan: one long backward ear, rounded right-facing head, tucked haunch and tail.
        # SQUARE extremes6,6,42,42. Lucide rabbit informs sweeping haunch and folded hind foot.
        # Omit facial dots and preserve the source's intentional right-facing asymmetry.
        self.add_bezier('ear',(26,16),((14,10),(14,6),(18,6)),((24,6),(30,10),(30,16)))
        self.add_bezier('face',(30,16),((38,12),(42,18),(42,22)),((42,26),(38,28),(34,28)))
        self.add_bezier('chest',(34,28),((34,32),(36,36),(38,42)))
        self.add_polyline('feet',(38,42),(24,42),(18,42))
        self.add_bezier('back-low',(18,42),((14,42),(12,38),(12,34)))
        self.add_bezier('back-high',(12,34),((12,26),(18,22),(26,24)))
        self.add_line('neck',(26,24),(26,16))
        self.add_bezier('tail',(12,34),((6,30),(6,36),(6,38)),((6,40),(12,42),(18,42)))
        self.add_bezier('haunch',(20,32),((26,32),(26,38),(24,42)));self.join_shared()


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


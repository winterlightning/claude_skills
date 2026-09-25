"""Toy Building Blocks — batch 56."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47582620-1b5b-45a1-bd6f-5b5ee3721b4c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys lego_47582620-1b5b-45a1-bd6f-5b5ee3721b4c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'toy-building-blocks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('toy', 'building', 'blocks')
    def build(self):
        # Plan: four shared-wall bricks form the right tower; two loose bricks at left.
        # SQUARE centerline extremes6,6,42,42. Lucide toy-brick informs studs atop rectangular bodies.
        # Studs reduce to upright strokes; straighten the tilted loose brick for clearance.
        self.add_polyline('tower-left',(26,10),(26,18),(26,26),(26,34),(26,42))
        self.add_polyline('tower-right',(42,10),(42,18),(42,26),(42,34),(42,42))
        self.add_polyline('tower-top',(26,10),(28,10),(40,10),(42,10))
        for y in (18,26,34,42):self.add_line(f'tower-seam-{y}',(26,y),(42,y))
        for x in (28,40):self.add_line(f'tower-stud-{x}',(x,6),(x,10))
        for n,y in [('upper',10),('lower',34)]:
            self.add_polyline(n+'-brick',(6,y),(12,y),(18,y),(18,y+8),(6,y+8),closed=True)
            self.add_line(n+'-stud',(12,y-4 if n=='upper' else y-8),(12,y))
        self.join_shared()


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


"""Furby Toy — batch 54."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c8ed2a82-660e-4fb3-97c4-3f6f0a34445d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys furby_c8ed2a82-660e-4fb3-97c4-3f6f0a34445d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'furby-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('furby', 'toy')

    def build(self):
        # Plan: rounded creature silhouette with pointed ears, paired eyes, beak and broad foot lobes.
        # SQUARE extremes6,6,42,42. Source silhouette; Lucide bird informs simplified beak identity.
        # Drop the beak seam and reduce the feet to silhouette lobes for clearance.
        self.add_polyline('ears',(6,18),(6,6),(18,10),(30,10),(42,6),(42,18))
        self.add_bezier('right',(42,18),((42,26),(42,34),(38,38)))
        self.add_polyline('feet',(38,38),(40,42),(28,42),(24,42),(20,42),(8,42),(10,38))
        self.add_bezier('left',(10,38),((6,34),(6,26),(6,18)))
        self.join_shared()
        for n,x in [('left-eye',17),('right-eye',31)]:self.add_arc(n+'-top',(x-2,20),(x+2,20),radius_x=2);self.add_arc(n+'-bottom',(x+2,20),(x-2,20),radius_x=2);self.add_contour(n,n+'-top',n+'-bottom',closed=True)
        self.add_arc('beak-top',(21,31),(27,31),radius_x=3)
        self.add_arc('beak-bottom',(27,31),(21,31),radius_x=3)
        self.add_contour('beak','beak-top','beak-bottom',closed=True)


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

    def trampoline(self):
        pts=[(8,38),(24,34),(40,38),(24,42)]
        for i in range(4):self.add_arc(f'mat-{i}',pts[i],pts[(i+1)%4],radius_x=16,radius_y=4)
        self.add_contour('mat',*[f'mat-{i}' for i in range(4)],closed=True)
        for i,(x,y) in enumerate(((8,38),(24,42),(40,38))):self.add_line(f'foot-{i}',(x,y),(x,44))


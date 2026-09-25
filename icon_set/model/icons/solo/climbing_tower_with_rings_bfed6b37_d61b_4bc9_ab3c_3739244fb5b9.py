"""Climbing Tower with Rings — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bfed6b37-d61b-4bc9-ab3c-3739244fb5b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors playhouse_bfed6b37-d61b-4bc9-ab3c-3739244fb5b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'climbing-tower-with-rings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('climbing', 'tower', 'with', 'rings')

    def build(self):
        # Plan: roofed narrow ladder and a projecting beam with two hanging circular rings.
        # HRECT_L extremes4,8,44,40. Source structure; no useful exact Lucide match.
        # Drop the far support so both rings keep full circular openings and required clearance.
        self.add_polyline('roof',(4,18),(8,8),(16,18),(12,18),(4,18))
        for n,x in [('left',4),('right',12)]:self.add_polyline(n,(x,18),(x,26),(x,34),(x,40))
        for i,y in enumerate((26,34)):self.add_line(f'rung-{i}',(4,y),(12,y))
        self.add_polyline('beam',(12,18),(16,18),(24,18),(41,18),(44,18))
        for i,x in enumerate((24,41)):
            self.add_line(f'strap-{i}',(x,18),(x,28));self.circle(f'ring-{i}',x,31,3)
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


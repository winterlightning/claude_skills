"""Playhouse and Swing Set — batch 54."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cfc68710-8c20-4cc9-9287-9f668901c75f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors playhouse swing_cfc68710-8c20-4cc9-9287-9f668901c75f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'playhouse-and-swing-set'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('playhouse', 'and', 'swing', 'set')

    def build(self):
        # Plan: elevated roofed playhouse, short ladder, supported beam and hanging swing.
        # HRECT_L extremes4,8,44,40. Source structure; no useful exact Lucide match.
        # Drop tiny window and inner doorway to preserve the house, ladder and swing at native size.
        self.add_polyline('roof',(28,18),(36,8),(44,18))
        self.add_polyline('house',(28,18),(44,18),(44,30),(40,30),(32,30),(28,30),closed=True)
        self.add_polyline('beam',(4,18),(12,18),(20,18),(28,18))
        self.add_line('post',(4,18),(4,40))
        self.add_polyline('swing',(12,18),(12,30),(20,30),(20,18))
        for n,x in [('left',32),('right',40)]:self.add_line(n+'-ladder',(x,30),(x,40))
        self.add_line('rung',(32,40),(40,40));self.join_shared()


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


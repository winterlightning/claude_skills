"""Plane Playground Ride — batch 54."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e51eaffb-6c93-4ef6-95ca-432ba53b26ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/playground plane_e51eaffb-6c93-4ef6-95ca-432ba53b26ee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plane-playground-ride'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('plane', 'playground', 'ride')

    def build(self):
        # Plan: left-facing plane, domed cockpit, raised tail, projecting wing and pedestal.
        # HRECT_L extremes4,8,44,40. Source silhouette; no useful exact Lucide match.
        # Propeller blades simplify to a single upright stroke with a shared shaft.
        self.add_polyline('propeller',(4,8),(4,22),(4,28));self.add_line('shaft',(4,22),(12,22))
        self.add_arc('nose-top',(16,18),(12,22),radius_x=4,sweep=False)
        self.add_arc('nose-bottom',(12,22),(16,26),radius_x=4,sweep=False)
        self.add_contour('nose','nose-top','nose-bottom')
        self.add_polyline('plane',(16,26),(18,26),(26,32),(38,32),(44,24),(44,8),(38,8),(32,18),(24,18),(16,18))
        self.add_arc('cockpit',(16,18),(32,18),radius_x=8)
        self.add_line('wing-seam',(32,18),(38,32))
        self.add_line('stand',(26,32),(26,40));self.add_polyline('base',(18,40),(26,40),(34,40));self.join_shared()


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


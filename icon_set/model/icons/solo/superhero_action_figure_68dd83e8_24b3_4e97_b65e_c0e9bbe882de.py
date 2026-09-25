"""Superhero Action Figure — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '68dd83e8-24b3-4e97-b65e-c0e9bbe882de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/figure figurine cape hero show model_68dd83e8-24b3-4e97-b65e-c0e9bbe882de.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'superhero-action-figure'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('superhero', 'action', 'figure')

    def build(self):
        # Plan: circular head, raised bent arms, broad stance and cape hanging behind the waist.
        # SQUARE extremes6,6,42,42. full_body_ref.png governs human head/torso vocabulary.
        # Head(24,11),r5; upper torso(24,24) has exact8 centerline /4 visible gap.
        # Reduce filled limbs to round strokes; omit neckline seam and foot baseline.
        self.head(24,11,5)
        self.add_polyline('arms',(6,14),(6,24),(24,24),(42,24),(42,14))
        self.add_line('torso',(24,24),(24,30))
        self.add_polyline('legs',(14,42),(24,30),(34,42))
        self.add_polyline('cape-left',(14,24),(6,34),(16,34))
        self.add_polyline('cape-right',(34,24),(42,34),(32,34))
        self.join_shared();self.mark_human_figure('hero',head='head',torso='torso',torso_junction='start')


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


"""Person Leaping above Trampoline — batch 54."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5848ae25-eae9-5c44-ae8a-00b63eee9a9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/jump launch pad trampoline_5848ae25-eae9-5c44-ae8a-00b63eee9a9e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-leaping-above-trampoline'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('person', 'leaping', 'above', 'trampoline')

    def build(self):
        # Plan: forward-leaning airborne figure, raised left arm and bent running legs above oval mat.
        # VRECT_L extremes8,4,40,44. Human construction: full_body_ref.png.
        # Head(33,9),r5; torso(21,14): sqrt(12^2+5^2)-5=8 centerline /4 ink gap.
        # Upper torso tangent(-12,5) is exactly aligned with the head-to-neck axis.
        self.head(33,9,5)
        self.add_bezier('torso',(21,14),((9,19),(21,18),(21,21)))
        self.add_polyline('arm',(21,14),(16,6),(8,10))
        self.add_polyline('left-leg',(21,21),(18,26),(10,27))
        self.add_polyline('right-leg',(21,21),(24,26),(28,26))
        self.trampoline();self.join_shared();self.mark_human_figure('jumper',head='head',torso='torso',torso_junction='start')

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


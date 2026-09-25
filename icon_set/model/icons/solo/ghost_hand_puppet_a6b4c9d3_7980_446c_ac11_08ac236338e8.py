"""Ghost Hand Puppet — batch 54."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a6b4c9d3-7980-446c-ac11-08ac236338e8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys hand ghost_a6b4c9d3-7980-446c-ac11-08ac236338e8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ghost-hand-puppet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('ghost', 'hand', 'puppet')

    def build(self):
        # Plan: rounded puppet above an open wrist and projecting thumb.
        # SQUARE extremes6,6,42,42. Lucide ghost and hand; human_ref guides simplified hand anatomy.
        # Eyes become short marks; omit zigzag mouth to preserve interior clearance.
        self.add_arc('cap',(14,20),(42,20),radius_x=14)
        self.add_polyline('puppet',(42,20),(42,30),(40,30),(14,30),(14,20))
        for n,x in [('eye-left',23),('eye-right',33)]:self.add_line(n,(x,20),(x,21))
        self.add_line('thumb',(6,24),(6,34))
        self.add_arc('palm-left',(6,34),(14,42),radius_x=8,sweep=False)
        self.add_line('palm-bottom',(14,42),(34,42))
        self.add_bezier('palm-right',(34,42),((40,42),(40,40),(40,36)))
        self.add_line('wrist',(40,36),(40,30))
        self.add_contour('hand','thumb','palm-left','palm-bottom','palm-right','wrist');self.join_shared()

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


"""Two Standing Children — batch 56."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '161a2ee8-8f26-48f5-bd6b-81fb11645a12'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/kids full body_161a2ee8-8f26-48f5-bd6b-81fb11645a12.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'two-standing-children'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('two', 'standing', 'children')
    def build(self):
        # Plan: two circular heads over a boy's simple limbs and a girl's flared dress.
        # SQUARE centerline extremes6,6,42,42. Shared full_body_ref.png owns human anatomy.
        # Both heads r4 at y10, actual torso junction y22: exact8 centerline /4 visible gap.
        # Omit the brim and garment seams; preserve the pair and their differing clothing.
        for n,x in [('boy',12),('girl',36)]:
            self.add_arc(n+'-head-top',(x-4,10),(x+4,10),radius_x=4)
            self.add_arc(n+'-head-bottom',(x+4,10),(x-4,10),radius_x=4)
            self.add_contour(n+'-head',n+'-head-top',n+'-head-bottom',closed=True)
        self.add_line('boy-torso',(12,22),(12,32))
        self.add_polyline('boy-arms',(6,30),(12,22),(18,30))
        self.add_polyline('boy-legs',(8,42),(12,32),(16,42))
        self.add_line('girl-torso',(36,22),(36,24))
        self.add_polyline('dress',(36,22),(42,34),(40,34),(32,34),(30,34),closed=True)
        for x in (32,40):self.add_line(f'girl-leg-{x}',(x,34),(x,42))
        self.join_shared()
        for n in ('boy','girl'):self.mark_human_figure(n,head=n+'-head',torso=n+'-torso',torso_junction='start')


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


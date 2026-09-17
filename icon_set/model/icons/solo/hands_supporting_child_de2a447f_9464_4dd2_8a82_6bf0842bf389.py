"""Hands Supporting Child — batch 54."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'de2a447f-9464-4dd2-8a82-6bf0842bf389'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/child care_de2a447f-9464-4dd2-8a82-6bf0842bf389.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-supporting-child'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('hands', 'supporting', 'child')

    def build(self):
        # Plan: circular child head, raised arms, short open torso and two upward cupping hands.
        # SQUARE extremes6,6,42,42. full_body_ref.png governs child anatomy; hand-heart informs cups.
        # Head(24,10),r4; torso begins(24,22): exact8 centerline /4 visible gap.
        # Omit individual finger/thumb contours to preserve space around the child.
        self.head(24,10,4)
        self.add_polyline('arms',(12,14),(16,22),(24,22),(32,22),(36,14))
        self.add_line('torso',(24,22),(24,28))
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.add_line(n+'-fingers',p(6,28),p(6,34))
            self.add_arc(n+'-palm',p(6,34),p(14,42),radius_x=8,sweep=s==-1)
            self.add_line(n+'-wrist',p(14,42),p(19,42))
            self.add_contour(n+'-hand',n+'-fingers',n+'-palm',n+'-wrist')
        self.join_shared();self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')


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


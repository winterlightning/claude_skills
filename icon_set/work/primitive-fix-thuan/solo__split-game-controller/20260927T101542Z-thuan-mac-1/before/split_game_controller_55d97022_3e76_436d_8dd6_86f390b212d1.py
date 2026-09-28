"""Split Game Controller — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '55d97022-3e76-436d-8dd6-86f390b212d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/nintendo switch controller logo_55d97022-3e76-436d-8dd6-86f390b212d1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'split-game-controller'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('split', 'game', 'controller')

    def build(self):
        # Plan: mirrored outward-rounded controller halves with a cross and circular button.
        # HRECT_L extremes4,8,44,40. Lucide gamepad-2 informs the minimal cross/button vocabulary.
        # Omit the straight inner walls so control marks have clear interior space.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.add_line(n+'-top',p(20,8),p(12,8))
            self.add_arc(n+'-corner-top',p(12,8),p(4,16),radius_x=8,sweep=s==-1)
            self.add_line(n+'-outer',p(4,16),p(4,32))
            self.add_arc(n+'-corner-bottom',p(4,32),p(12,40),radius_x=8,sweep=s==-1)
            self.add_line(n+'-bottom',p(12,40),p(20,40))
            self.add_contour(n+'-shell',n+'-top',n+'-corner-top',n+'-outer',n+'-corner-bottom',n+'-bottom')
        self.add_polyline('cross-h',(13,24),(16,24),(19,24));self.add_polyline('cross-v',(16,21),(16,24),(16,27))
        self.circle('button',33,24,2);self.join_shared()


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


"""Arched Climbing Frame — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6fd7c42-b9f3-5a3f-9970-de692147b0ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/playground_b6fd7c42-b9f3-5a3f-9970-de692147b0ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-climbing-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('arched', 'climbing', 'frame')

    def build(self):
        # Plan: concentric arch rails, matched ladder sides and three shared rung levels.
        # SQUARE extremes6,6,42,42. No useful exact Lucide match; source supplies the frame.
        for n,x,r in [('outer',6,18),('inner',16,8)]:
            self.add_polyline(n+'-left',(x,42),(x,33),(x,24))
            self.add_arc(n+'-arch',(x,24),(48-x,24),radius_x=r)
            self.add_polyline(n+'-right',(48-x,24),(48-x,33),(48-x,42))
        for j,y in enumerate((24,33,42)):
            self.add_line(f'left-rung-{j}',(6,y),(16,y));self.add_line(f'right-rung-{j}',(32,y),(42,y))
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


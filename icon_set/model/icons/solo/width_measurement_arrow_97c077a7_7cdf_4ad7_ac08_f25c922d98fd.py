"""Width Measurement Arrow — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97c077a7-7cdf-4ad7-ac08-f25c922d98fd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand horizontal 1_97c077a7-7cdf-4ad7-ac08-f25c922d98fd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'width-measurement-arrow-97c077a7-7cdf-4ad7-ac08-f25c922d98fd'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    aliases = ()
    keywords = ('width', 'measurement', 'arrow')

    def build(self):
        # Plan: horizontal bidirectional arrow separated from two upright boundaries.
        # HRECT_L extremes4,8,44,40. Lucide move-horizontal informs mirrored heads.
        for n,x in [('left',4),('right',44)]:self.add_line(n,(x,8),(x,40))
        self.add_line('shaft',(12,24),(36,24))
        self.add_polyline('left-head',(20,16),(12,24),(20,32))
        self.add_polyline('right-head',(28,16),(36,24),(28,32));self.join_shared()


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


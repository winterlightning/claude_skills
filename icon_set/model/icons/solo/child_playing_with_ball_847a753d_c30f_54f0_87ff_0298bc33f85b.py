"""Child Playing with Ball — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '847a753d-c30f-54f0-87ff-0298bc33f85b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/kids play ball_847a753d-c30f-54f0-87ff-0298bc33f85b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'child-playing-with-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('child', 'playing', 'with', 'ball')

    def build(self):
        # Plan: round head, upright torso, raised bent arms, spread legs and a separate ball.
        # SQUARE extremes6,6,42,42. Human style: icon_set/references/human_ref/full_body_ref.png.
        # Head(18,11), r5; torso starts(18,24): 24-(11+5)=8 centerline, 4 visible gap.
        self.add_arc('head-top',(13,11),(23,11),radius_x=5)
        self.add_arc('head-bottom',(23,11),(13,11),radius_x=5)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('torso',(18,24),(18,33))
        self.add_polyline('arms',(6,18),(10,24),(18,24),(26,24),(30,18))
        self.add_polyline('legs',(10,42),(18,33),(24,42))
        self.circle('ball',37,37,5);self.join_shared()
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')


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


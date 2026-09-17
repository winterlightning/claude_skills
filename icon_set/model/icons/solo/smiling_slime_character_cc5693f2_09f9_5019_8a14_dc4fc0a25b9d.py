"""Smiling Slime Character — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc5693f2-09f9-5019-8a14-dc4fc0a25b9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/dragonquest slime_cc5693f2-09f9-5019-8a14-dc4fc0a25b9d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-slime-character'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('smiling', 'slime', 'character')

    def build(self):
        # Plan: broad round teardrop silhouette, pointed crown, two circular eyes and upturned smile.
        # SQUARE extremes6,6,42,42. Source character; no useful exact Lucide match.
        self.add_bezier('left',(24,6),((22,14),(6,10),(6,26)),((6,42),(16,42),(24,42)))
        self.add_bezier('right',(24,42),((32,42),(42,42),(42,26)),((42,10),(26,14),(24,6)))
        self.add_contour('body','left','right',closed=True)
        for n,x in [('left-eye',18),('right-eye',30)]:self.circle(n,x,23,2)
        self.add_bezier('smile',(20,33),((22,34),(26,34),(28,33)))


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


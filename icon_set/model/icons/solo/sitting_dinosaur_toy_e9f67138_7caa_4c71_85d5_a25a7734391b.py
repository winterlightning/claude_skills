"""Sitting Dinosaur Toy — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e9f67138-7caa-4c71-85d5-a25a7734391b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys dinosaur_e9f67138-7caa-4c71-85d5-a25a7734391b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sitting-dinosaur-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('sitting', 'dinosaur', 'toy')

    def build(self):
        # Plan: right-facing round head, scalloped back, curled tail and large sitting foot.
        # SQUARE extremes6,6,42,42. Source profile; no useful exact Lucide match.
        # Omit tiny eye and inner arm line, retaining the smile, two plates and folded foot.
        self.add_bezier('head',(20,18),((20,6),(26,6),(32,6)),((42,6),(42,12),(42,16)),((42,20),(36,20),(32,20)))
        self.add_polyline('jaw',(32,20),(32,28),(42,28))
        self.add_line('foot-top',(42,28),(42,34))
        self.add_bezier('foot',(42,34),((42,40),(42,42),(36,42)))
        self.add_polyline('bottom',(36,42),(32,42),(18,42))
        self.add_bezier('tail',(18,42),((10,42),(6,38),(6,34)),((18,34),(20,30),(20,26)))
        self.add_bezier('plates',(20,26),((6,26),(10,18),(20,18)),((6,18),(12,10),(20,10)))
        self.add_bezier('leg',(32,42),((26,42),(26,32),(32,32)))
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

    def head(self,x,y,r):
        self.add_arc('head-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc('head-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)


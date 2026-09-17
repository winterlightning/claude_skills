"""Wastebasket with Paper — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '328263aa-6644-54d0-8a5b-118846e1bd30'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/bin paper_328263aa-6644-54d0-8a5b-118846e1bd30.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wastebasket-with-paper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    aliases = ()
    keywords = ('wastebasket', 'with', 'paper')

    def build(self):
        # Plan: tapered basket with two touching crumpled-paper silhouettes above its rim.
        # VRECT_L extremes8,4,40,44. Lucide trash-2 informs the shared rim.
        self.add_polyline('rim',(8,20),(10,20),(24,20),(36,20),(40,20))
        self.add_bezier('basket',(8,20),((10,28),(10,36),(12,42)),((12,44),(14,44),(16,44)))
        self.add_line('base',(16,44),(32,44))
        self.add_bezier('right',(32,44),((34,44),(36,44),(36,42)),((38,36),(38,28),(40,20)))
        self.add_contour('body','basket','base','right')
        self.add_polyline('paper-left',(10,20),(8,12),(18,8),(24,14),(24,20))
        self.add_polyline('paper-right',(24,14),(28,4),(38,10),(36,20))
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


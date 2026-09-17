"""Smiling Boy Face — batch 55."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0673820c-38b2-4d6f-9b2a-49663f3a128f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/boy head_0673820c-38b2-4d6f-9b2a-49663f3a128f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-boy-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('smiling', 'boy', 'face')

    def build(self):
        # Plan: swept fringe, paired ears, circular jaw and smiling face.
        # SQUARE extremes6,6,42,42. Shared human reference informs circular head anatomy.
        self.add_arc('cap-left',(10,20),(20,6),radius_x=10,radius_y=14)
        self.add_line('hair-1',(20,6),(24,14))
        self.add_line('hair-2',(24,14),(30,10))
        self.add_bezier('cap-right',(30,10),((36,12),(38,16),(38,20)))
        self.add_arc('ear-right',(38,20),(38,28),radius_x=4)
        self.add_arc('jaw-right',(38,28),(24,42),radius_x=14)
        self.add_arc('jaw-left',(24,42),(10,28),radius_x=14)
        self.add_arc('ear-left',(10,28),(10,20),radius_x=4)
        self.add_contour('face','cap-left','hair-1','hair-2','cap-right','ear-right','jaw-right','jaw-left','ear-left',closed=True)
        for n,x in [('left-eye',18),('right-eye',30)]:self.add_line(n,(x,23),(x,24))
        self.add_bezier('smile',(21,32),((23,33),(25,33),(27,32)))
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


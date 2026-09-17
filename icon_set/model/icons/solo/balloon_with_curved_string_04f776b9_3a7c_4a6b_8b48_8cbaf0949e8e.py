"""Balloon with Curved String — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '04f776b9-3a7c-4a6b-8b48-8cbaf0949e8e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys balloon_04f776b9-3a7c-4a6b-8b48-8cbaf0949e8e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'balloon-with-curved-string'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    aliases = ()
    keywords = ('balloon', 'with', 'curved', 'string')

    def build(self):
        # Plan: rounded balloon tapering to a shared string junction; loose curved tail.
        # VRECT_M extremes10,4,38,44. Lucide balloon informs taper and flowing string.
        # Omit the tiny closed triangular knot to avoid a pinched hole.
        self.add_arc('top',(10,18),(38,18),radius_x=14)
        self.add_bezier('right',(38,18),((38,25),(30,32),(24,32)))
        self.add_bezier('left',(24,32),((18,32),(10,25),(10,18)))
        self.add_contour('balloon','top','right','left',closed=True)
        self.add_bezier('string',(24,32),((24,42),(34,34),(34,44)));self.relate('connect','string','balloon')


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


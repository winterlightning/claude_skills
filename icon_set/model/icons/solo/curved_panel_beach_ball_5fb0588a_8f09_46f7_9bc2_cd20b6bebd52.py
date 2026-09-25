"""Curved Panel Beach Ball — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5fb0588a-8f09-46f7-9bc2-cd20b6bebd52'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys ball_5fb0588a-8f09-46f7-9bc2-cd20b6bebd52.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-panel-beach-ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('curved', 'panel', 'beach', 'ball')

    def build(self):
        # Plan: round ball, inset upper-right curved cap and two broad bowed panel seams.
        # CIRCLE center24,24 radius20. Source owns panel arrangement; no exact Lucide match.
        self.circle('edge',24,24,20)
        pts=[(24,4),(28,16),(32,20),(44,24)]
        for i in range(3):self.add_arc(f'cap-{i}',pts[i],pts[i+1],radius_x=20,sweep=False)
        self.add_contour('cap',*[f'cap-{i}' for i in range(3)])
        self.add_bezier('upper-seam',(4,24),((10,14),(18,10),(28,16)))
        self.add_bezier('lower-seam',(24,44),((34,38),(38,30),(32,20)))
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


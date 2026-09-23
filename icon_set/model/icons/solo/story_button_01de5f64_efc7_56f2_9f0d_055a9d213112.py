"""A story button with a circular center and broken outer ring.
Plan: Concentric circles; a large outer sweep and isolated upper-left arc.
Keyshape: CIRCLE; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01de5f64-efc7-56f2-9f0d-055a9d213112'
SOURCE_PATH = 'icon_set/work/todo-references/story button_01de5f64-efc7-56f2-9f0d-055a9d213112.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'story-button'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('story', 'button')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=4):
        # One owning rectangle; four equal tangent corner arcs.
        points = [(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                  (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,p,q,radius_x=r)
            else: self.add_line(n,p,q)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        # Four rays share the true intersection node.
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        ids=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));ids.append(n)
        for i,a in enumerate(ids):
            for b in ids[i+1:]: self.relate('connect',a,b)

    def build(self):

        self.circle('inner',24,24,11)
        self.add_arc('outer-main',(24,4),(4,24),radius_x=20,large_arc=True)
        self.add_arc('outer-dash',(8,12),(12,8),radius_x=20)

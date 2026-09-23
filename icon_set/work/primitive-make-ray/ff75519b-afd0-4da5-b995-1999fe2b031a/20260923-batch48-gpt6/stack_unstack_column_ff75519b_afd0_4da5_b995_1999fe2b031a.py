"""Five square blocks step downward beside two turning arrows.
Plan: Repeated 8-unit cells advance diagonally; arrows repeat at two levels.
Keyshape: VRECT_L; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ff75519b-afd0-4da5-b995-1999fe2b031a'
SOURCE_PATH = 'icon_set/work/todo-references/stack unstack column_ff75519b-afd0-4da5-b995-1999fe2b031a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stack-unstack-column'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('stack', 'unstack', 'column')

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

        # Adjacent cells share edges: emit the union outline plus dividers once.
        self.add_polyline('column',(8,4),(16,4),(16,20),(24,20),(24,36),(32,36),(32,44),(24,44),(24,36),(16,36),(16,20),(8,20),closed=True)
        self.add_line('split-top',(8,12),(16,12))
        self.add_line('split-middle',(16,28),(24,28))
        for name in ('split-top','split-middle'): self.relate('connect',name,'column')
        for i,(x,y) in enumerate(((24,8),(32,24))):
            self.add_arc(f'turn-{i}',(x,y),(x+8,y+8),radius_x=8)
            self.add_polyline(f'arrow-{i}',(x+8,y+8),(x,y+16),(x+8,y+16))
            self.relate('connect',f'turn-{i}',f'arrow-{i}')

"""A circular strainer with a diagonal rounded handle.
Plan: Large round bowl with a diagonal capsule handle at lower left.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5bcfe5e1-9b28-4166-b6be-071e05c0a87f'
SOURCE_PATH = 'icon_set/work/todo-references/strainer_5bcfe5e1-9b28-4166-b6be-071e05c0a87f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'strainer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('strainer',)

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

        self.circle('bowl',29,19,13)
        self.add_line('handle-left',(18,26),(7,37))
        self.add_arc('handle-end',(7,37),(13,43),radius_x=4,radius_y=4,sweep=False)
        self.add_line('handle-right',(13,43),(24,32))
        self.add_contour('handle','handle-left','handle-end','handle-right')

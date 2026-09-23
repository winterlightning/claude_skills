"""Scissors beside a partial female-operation symbol.
Plan: Two equal finger loops and converging blades; right curved symbol retains its diagonal cross.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '852044c0-c346-4658-9c9c-035df8dc7b7b'
SOURCE_PATH = 'icon_set/work/todo-references/stablization operation female_852044c0-c346-4658-9c9c-035df8dc7b7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stablization-operation-female'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('stablization', 'operation', 'female')

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

        for x in (12,26): self.circle(f'loop-{x}',x,36,6)
        self.add_polyline('blade-left',(18,36),(18,22),(20,8),(26,30))
        self.add_line('blade-cut',(18,28),(24,22))
        self.relate('connect','loop-12','blade-left')
        self.relate('connect','loop-26','blade-left')
        self.add_arc('female-arc',(30,14),(34,30),radius_x=10)
        self.add_line('female-shaft',(36,18),(42,12))
        self.cross('female-cross',38,10,4,True)

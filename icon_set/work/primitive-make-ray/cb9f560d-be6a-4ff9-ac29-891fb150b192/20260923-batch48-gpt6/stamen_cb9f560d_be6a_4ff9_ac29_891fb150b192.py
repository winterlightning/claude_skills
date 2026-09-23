"""Three pollen-bearing stamens rise from a rounded base.
Plan: Paired outer anthers mirror around one taller central filament.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cb9f560d-be6a-4ff9-ac29-891fb150b192'
SOURCE_PATH = 'icon_set/work/todo-references/stamen_cb9f560d-be6a-4ff9-ac29-891fb150b192.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stamen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('stamen',)

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

        self.rect('base',14,34,20,8,4)
        for name,x,y in [('left',10,14),('middle',24,10),('right',38,14)]:
            self.circle(name+'-anther',x,y,4)
            self.add_line(name+'-filament',(x,y+4),(24,30))
            self.relate('connect',name+'-anther',name+'-filament')
        self.add_line('stem',(24,30),(24,34))
        for name in ('left','middle','right'):
            self.relate('connect',name+'-filament','stem')
        for a,b in [('left','middle'),('left','right'),('middle','right')]: self.relate('connect',a+'-filament',b+'-filament')
        self.relate('connect','stem','base')

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb9f560d-be6a-4ff9-ac29-891fb150b192'
SOURCE_PATH = 'icon_set/work/todo-references/stamen_cb9f560d-be6a-4ff9-ac29-891fb150b192.svg'
AUTHOR = 'gpt-6'
PLAN = 'Three round anthers on radiating filaments above a capsule base.'
CONSTRUCTION_REFERENCE = 'circle: circular anthers; shared mirrored filament placement'

class Drawing(Solo48):
    icon_id = 'stamen'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('stamen',)

    def circle(self, name, x, y, r):
        self.add_arc(name+'-upper', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-lower', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, left, top, right, bottom, r):
        # One rounded rectangle definition owns all matching corners.
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8]; member=f'{name}-{i}'
            if i%2: self.add_arc(member,start,end,radius_x=r)
            else: self.add_line(member,start,end)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        ends = [(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):
            self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def bust_body(self):
        # Shared shoulder radii; badge occludes the right shoulder and hem.
        self.add_line('body-left',(6,42),(6,40))
        self.add_arc('shoulder-left',(6,40),(16,30),radius_x=10)
        self.add_line('shoulder-top',(16,30),(24,30))
        self.add_arc('shoulder-right',(24,30),(30,36),radius_x=6)
        self.add_contour('shoulders','body-left','shoulder-left','shoulder-top','shoulder-right')
        self.add_line('hem',(6,42),(36,42))
        self.circle('badge',36,36,6)
        self.relate('connect','hem','body-left')
        self.relate('connect','hem','badge-lower')
        self.relate('connect','shoulder-right','badge-upper','badge-lower')

    def build(self):
        self.box('base',16,36,32,44,4)
        self.circle('anther-center',24,6,2)
        for side in (-1,1):
            x=24+side*14
            self.circle(f'anther-{side}',x,10,2)
            self.add_bezier(f'filament-{side}',(x,12),((x,16),(24+side*4,22),(24,30)))
            self.relate('connect',f'anther-{side}',f'filament-{side}')
        self.add_line('stem',(24,8),(24,36))
        self.relate('connect','stem','anther-center','base')
        for side in (-1,1): self.relate('connect','stem',f'filament-{side}')

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bb90ccf0-9578-45c7-ad84-a7eb1350bdaf'
SOURCE_PATH = 'icon_set/work/todo-references/squeeze sides_bb90ccf0-9578-45c7-ad84-a7eb1350bdaf.svg'
AUTHOR = 'gpt-6'
PLAN = 'Phone with paired inward-bowing squeeze marks and a bottom separator.'
CONSTRUCTION_REFERENCE = 'smartphone: rounded vertical enclosure'

class Drawing(Solo48):
    icon_id = 'squeeze-sides'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('squeeze', 'sides')

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
        self.box('phone',10,4,38,44,4)
        self.add_line('footer',(10,36),(38,36))
        self.relate('connect','footer','phone-2','phone-6')
        for side in (-1,1):
            outer=24+side*8; inner=24+side*12
            self.add_bezier(f'pressure-{side}',(outer,13),((outer-side*7,19),(outer-side*7,23),(outer,29)))
            self.add_bezier(f'echo-{side}',(inner,17),((inner-side*3,20),(inner-side*3,22),(inner,25)))

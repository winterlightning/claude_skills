from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '852044c0-c346-4658-9c9c-035df8dc7b7b'
SOURCE_PATH = 'icon_set/work/todo-references/stablization operation female_852044c0-c346-4658-9c9c-035df8dc7b7b.svg'
AUTHOR = 'gpt-6'
PLAN = 'Closed surgical scissors beside a rotated female symbol.'
CONSTRUCTION_REFERENCE = 'circle: round scissor handles; no useful complete Lucide subject match'

class Drawing(Solo48):
    icon_id = 'stablization-operation-female'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('stablization', 'operation', 'female')

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
        self.circle('handle-left',12,36,6)
        self.circle('handle-right',28,36,6)
        self.add_polyline('blades',(18,36),(18,24),(20,6),(22,24),(22,36))
        self.add_line('blade-joint',(18,28),(22,24))
        self.relate('connect','blades','handle-left','handle-right','blade-joint')
        self.add_arc('female-bowl',(30,14),(36,32),radius_x=10)
        self.add_line('female-stem',(36,16),(42,10))
        self.add_polyline('female-cross',(36,6),(40,10),(42,12))
        self.relate('connect','female-stem','female-cross')

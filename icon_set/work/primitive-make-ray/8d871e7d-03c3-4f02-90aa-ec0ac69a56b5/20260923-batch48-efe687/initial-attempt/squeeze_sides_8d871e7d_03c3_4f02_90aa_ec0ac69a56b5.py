from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d871e7d-03c3-4f02-90aa-ec0ac69a56b5'
SOURCE_PATH = 'icon_set/work/todo-references/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg'
AUTHOR = 'gpt-6'
PLAN = 'Hand grips a phone while two arrows point inward; four repeated fingers and a curved thumb.'
CONSTRUCTION_REFERENCE = 'smartphone and move-horizontal: rounded phone and arrow strokes'

class Drawing(Solo48):
    icon_id = 'squeeze-sides'
    keyshape = Keyshape.SQUARE
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
        self.box('phone',16,6,34,42,4)
        # Four finger capsules, sharing the same width and pitch.
        for i in range(4):
            self.box(f'finger-{i}',8,16+6*i,22,22+6*i,3)
        self.add_bezier('thumb',(34,18),((40,18),(36,30),(42,30)))
        self.add_line('wrist',(34,40),(42,42))
        self.add_polyline('left-arrow',(6,6),(10,10),(6,14))
        self.add_line('left-shaft',(6,10),(10,10))
        self.relate('connect','left-arrow','left-shaft')
        self.add_polyline('right-arrow',(42,6),(38,10),(42,14))
        self.add_line('right-shaft',(38,10),(42,10))
        self.relate('connect','right-arrow','right-shaft')
        self.relate('connect','thumb','phone-2')

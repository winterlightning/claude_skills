from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5bcfe5e1-9b28-4166-b6be-071e05c0a87f'
SOURCE_PATH = 'icon_set/work/todo-references/strainer_5bcfe5e1-9b28-4166-b6be-071e05c0a87f.svg'
AUTHOR = 'gpt-6'
PLAN = 'Round strainer bowl with a diagonal open handle extending down-left.'
CONSTRUCTION_REFERENCE = 'circle: circular bowl; intentional diagonal handle asymmetry'

class Drawing(Solo48):
    icon_id = 'strainer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('strainer',)

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
        # Bowl centered at (29,19), radius 13; integer Pythagorean attachments.
        self.add_arc('rim-upper',(17,24),(29,6),radius_x=13)
        self.add_arc('rim-right',(29,6),(42,19),radius_x=13)
        self.add_arc('rim-lower',(42,19),(24,31),radius_x=13)
        self.add_arc('rim-attachment',(24,31),(17,24),radius_x=13)
        self.add_contour('rim','rim-upper','rim-right','rim-lower','rim-attachment',closed=True)
        self.add_polyline('handle',(17,24),(6,35),(6,38),(10,42),(13,42),(24,31))
        self.relate('connect','handle','rim-upper','rim-lower','rim-attachment')

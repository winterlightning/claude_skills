from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '073b7984-a3fe-4699-87e9-47bf76004f1c'
SOURCE_PATH = 'icon_set/work/todo-references/step sister_073b7984-a3fe-4699-87e9-47bf76004f1c.svg'
AUTHOR = 'gpt-6'
PLAN = 'Woman with a shoulder-length bob and circular lower-right relationship badge.'
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: circular jaw and broad curved shoulders'

class Drawing(Solo48):
    icon_id = 'step-sister'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('step', 'sister')

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
        self.bust_body()
        self.add_arc('jaw',(14,14),(30,14),radius_x=8,sweep=False)
        self.add_bezier('fringe',(30,14),((28,14),(27,13),(25,10)),((23,13),(19,14),(14,14)))
        self.add_contour('face','jaw','fringe',closed=True)
        self.add_arc('hair-top',(10,18),(34,18),radius_x=12)
        self.add_bezier('hair-right',(34,18),((34,22),(36,28),(30,28)))
        self.add_bezier('hair-left',(14,28),((8,28),(10,22),(10,18)))
        self.add_contour('hair','hair-left','hair-top','hair-right')
        # Jaw lowest y=22; shoulder top y=30: exactly 4 units of ink gap.

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b7404a4-2ffc-469e-852a-20c37dbea4d9'
SOURCE_PATH = 'icon_set/work/todo-references/study maths brain_6b7404a4-2ffc-469e-852a-20c37dbea4d9.svg'
AUTHOR = 'gpt-6'
PLAN = 'Side-profile head containing plus, minus and multiplication marks.'
CONSTRUCTION_REFERENCE = 'No useful Lucide profile-head match; brain inspected but its lobes do not apply'

class Drawing(Solo48):
    icon_id = 'study-maths-brain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('study', 'maths', 'brain')

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
        self.add_arc('skull-top',(10,22),(26,6),radius_x=16)
        self.add_arc('skull-back',(26,6),(42,22),radius_x=16)
        self.add_bezier('back-neck',(42,22),((42,31),(34,31),(34,38)))
        self.add_line('neck-right',(34,38),(34,42))
        self.add_polyline('face',(10,22),(6,29),(10,30),(10,35))
        self.add_arc('chin',(10,35),(14,39),radius_x=4,sweep=False)
        self.add_polyline('neck-left',(14,39),(20,39),(20,42))
        self.add_contour('profile','neck-left-2') if False else None
        self.relate('connect','skull-top','skull-back')
        self.relate('connect','skull-back','back-neck')
        self.relate('connect','back-neck','neck-right')
        self.relate('connect','face','skull-top','chin')
        self.relate('connect','chin','neck-left')
        self.cross('plus',24,16,3)
        self.add_line('minus',(18,28),(23,28))
        self.cross('times',33,28,2,True)

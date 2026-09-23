from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7bead6c0-72f2-44e3-81e8-617544d2ab4d'
SOURCE_PATH = 'icon_set/work/todo-references/stepdaughter_7bead6c0-72f2-44e3-81e8-617544d2ab4d.svg'
AUTHOR = 'gpt-6'
PLAN = 'Girl with long hair and circular lower-right relationship badge.'
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: circular jaw and broad shoulder construction'

class Drawing(Solo48):
    icon_id = 'stepdaughter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('stepdaughter',)

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
        self.add_bezier('fringe',(14,14),((19,14),(23,13),(25,10)),((27,13),(28,14),(30,14)))
        self.add_contour('face','jaw','fringe',closed=True)
        self.add_arc('hair-top',(10,18),(34,18),radius_x=12)
        self.add_line('hair-left',(10,18),(8,32))
        self.add_line('hair-right',(34,18),(36,28))
        self.relate('connect','hair-left','hair-top')
        self.relate('connect','hair-right','hair-top')
        # Jaw bottom y=22; shoulder top y=30 gives the required 4-unit ink gap.

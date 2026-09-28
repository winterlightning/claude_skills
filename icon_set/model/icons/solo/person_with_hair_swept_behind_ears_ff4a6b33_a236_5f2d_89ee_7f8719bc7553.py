"""Fresh reference repair. Construction reference: human_ref/user.svg and Lucide user.
Keyshape VRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ff4a6b33-a236-5f2d-89ee-7f8719bc7553'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_ff4a6b33-a236-5f2d-89ee-7f8719bc7553.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-with-parted-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman',)

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):

        # Human reference radius-10 circular jaw; parted hair and round ears; zero ink gap to shoulders.
        self.path('hair',(14,18),('C',(24,4),(14,10),(18,4)),('C',(34,18),(30,4),(34,10)))
        self.path('fringe',(14,18),('C',(24,12),(19,18),(22,15)),('C',(34,18),(26,15),(29,18)))
        self.path('ear-right',(34,18),('C',(40,20),(34,14),(40,14)),('C',(32,28),(40,26),(36,28)))
        self.path('ear-left',(16,28),('C',(8,20),(12,28),(8,26)),('C',(14,18),(8,14),(14,14)))
        self.add_arc('jaw',(32,28),(16,28),radius_x=10)
        self.add_arc('left-shoulder',(8,44),(16,36),radius_x=8)
        self.add_line('body-top-left',(16,36),(24,36))
        self.add_line('body-top-right',(24,36),(32,36))
        self.add_arc('right-shoulder',(32,36),(40,44),radius_x=8)
        self.add_contour('body','left-shoulder','body-top-left','body-top-right','right-shoulder')
        for a,b in [('hair','fringe'),('hair','ear-left'),('hair','ear-right'),('fringe','ear-left'),('fringe','ear-right'),('jaw','ear-left'),('jaw','ear-right'),('jaw','body')]:self.relate('connect',a,b)

    icon_id = 'person-with-hair-swept-behind-ears'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('person', 'with', 'hair', 'swept', 'behind', 'ears')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

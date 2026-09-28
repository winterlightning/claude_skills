"""A round head above a heart-shaped torso with smooth paired lobes.
Symbol plan: shared parameters and coherent contours.
Construction: heart: smooth lobes and a pointed tip; human_ref/user.svg: round detached head.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2aa1a351-da44-44d3-bef9-70273bc4350d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-angular-heart-torso/20260924T065933Z-thuan-mac/reference/phone digital well being heart 1_2aa1a351-da44-44d3-bef9-70273bc4350d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='person-with-angular-heart-torso'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('person', 'with', 'angular', 'heart', 'torso')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Circular head and paired lobes: center separation20, radii6+6 gives exact gap8.
        self.oval('head',24,12,6)
        self.path('heart',(24,34),[('L',(18,28)),('A',(6,28),6,6,False),('A',(10,34),10,10,False),('L',(24,42)),('L',(38,34)),('A',(42,28),10,10,False),('A',(30,28),6,6,False),('L',(24,34))],True)

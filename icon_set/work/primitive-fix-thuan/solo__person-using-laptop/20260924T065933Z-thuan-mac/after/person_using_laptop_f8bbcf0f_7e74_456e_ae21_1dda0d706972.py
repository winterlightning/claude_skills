"""A seated person reaches toward the keyboard of an open laptop.
Symbol plan: shared parameters and coherent contours.
Construction: human_ref/user.svg and full_body_ref.png: round head, bent arm and coherent torso.
Omissions: No omitted defining features; laptop keeps the source perspective.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f8bbcf0f-7e74-456e-ae21-1dda0d706972'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-using-laptop/20260924T065933Z-thuan-mac/reference/working remotely_f8bbcf0f-7e74-456e-ae21-1dda0d706972.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='person-using-laptop'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('person', 'using', 'laptop')

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
        # user.svg: head bottom16, shoulder top24 gives exactly8 centerline /4 ink gap.
        self.oval('head',14,11,5)
        self.path('back',(14,24),[('A',(6,32),8,8,False),('L',(6,36)),('A',(12,42),6,6,False),('L',(24,42))])
        self.add_polyline('arm',(14,24),(14,32),(27,32))
        self.add_polyline('screen',(24,42),(27,32),(30,22),(42,22),(36,42),closed=True)
        self.relate('connect','back','arm');self.relate('connect','screen','back');self.relate('connect','screen','arm')

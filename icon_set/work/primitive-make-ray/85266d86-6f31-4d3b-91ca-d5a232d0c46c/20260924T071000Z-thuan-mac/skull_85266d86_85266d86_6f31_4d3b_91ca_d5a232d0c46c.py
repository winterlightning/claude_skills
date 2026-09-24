"""Skull with a round cranium, narrowing cheekbones and three open lower teeth.
Symbol plan: shared parameters and coherent contours.
Construction: skull: coherent rounded cranium.
Omissions: Eye dots retained as the meaningful completion of the faint source eyes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='85266d86-6f31-4d3b-91ca-d5a232d0c46c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__skull-85266d86/20260924T065933Z-thuan-mac/reference/skull_85266d86-6f31-4d3b-91ca-d5a232d0c46c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='skull-85266d86'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('skull', '85266d86')

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
        self.path('cranium',(15,44),[('L',(15,38)),('L',(12,32)),('A',(8,20),20,20,True),('A',(40,20),16,16,True),('A',(36,32),20,20,True),('L',(33,38)),('L',(33,44))])
        self.add_line('tooth',(24,38),(24,44))
        for x in [18,30]:self.add_dot('eye-'+str(x),(x,23))

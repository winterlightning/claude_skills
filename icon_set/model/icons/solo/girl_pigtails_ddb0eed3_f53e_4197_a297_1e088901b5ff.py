"""Girl with circular head, paired pigtails and a smooth flared body.
Symbol plan: shared parameters and coherent contours.
Construction: human_ref/user.svg: circular head and broad open body; user-round: coherent shoulder arc.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ddb0eed3-f53e-4197-a297-1e088901b5ff'
SOURCE_PATH = 'pictographic-primitives/symbol/primitive symbols human_ddb0eed3-f53e-4197-a297-1e088901b5ff.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='girl-pigtails'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('girl', 'pigtails')

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
        # Shared human user.svg proportions, head radius8; body apex28 minus head bottom20 =8.
        self.oval('head',24,12,8)
        for i,s in enumerate([-1,1]):
            self.path('hair-'+str(i),(24+s*8,12),[('A',(24+s*15,22),12,12,s<0)])
            self.relate('connect','hair-'+str(i),'head')
        # Smooth elliptical arch reaches exact bottom and width without shoulder kinks.
        self.path('body',(8,44),[('A',(40,44),16,16,True)])

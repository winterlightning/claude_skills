"""Two people raise their inner arms to meet in a high five.
Symbol plan: shared parameters and coherent contours.
Construction: human_ref/user.svg and full_body_ref.png: paired round heads and raised limbs.
Omissions: Three contact rays reduced to one dot to keep the upper gap clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '635ece78-65ec-4140-9338-f24f52af0c2d'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork user high five_635ece78-65ec-4140-9338-f24f52af0c2d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='people-giving-high-five'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "work"
    categories = ("work", "primitives")
    aliases=()
    keywords=('people', 'giving', 'high', 'five')

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
        # Shared human head radius4; shoulder y28 minus head bottom20 gives exact 4 ink gap.
        for i,x in enumerate([10,38]):self.oval('head-'+str(i),x,16,4)
        for i in range(2):
            def q(x,y):return (x if i==0 else 48-x,y)
            self.path('shoulder-'+str(i),q(6,42),[('L',q(6,32)),('A',q(10,28),4,4,i==0),('L',q(14,28))])
            self.path('arm-'+str(i),q(14,28),[('A',q(24,18),10,10,i!=0)])
            self.add_line('torso-'+str(i),q(14,28),q(14,42))
            self.relate('connect','torso-'+str(i),'shoulder-'+str(i))
            self.relate('connect','arm-'+str(i),'shoulder-'+str(i))
            self.relate('connect','arm-'+str(i),'torso-'+str(i))
        self.relate('connect','arm-0','arm-1')
        self.add_dot('contact-ray',(24,6))

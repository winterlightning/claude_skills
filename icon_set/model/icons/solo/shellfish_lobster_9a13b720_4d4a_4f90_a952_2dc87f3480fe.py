"""An elongated lobster body, paired curling claws and two rounded tail lobes. Shared mirror axis x24; SQUARE centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a13b720-4d4a-4f90-a952-2dc87f3480fe'
SOURCE_PATH = 'pictographic-primitives/animals/shellfish lobster_9a13b720-4d4a-4f90-a952-2dc87f3480fe.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='shrimp: coherent crustacean body; supplied lobster establishes mirrored claws'
DESIGN_PLAN='An elongated lobster body, paired curling claws and two rounded tail lobes. Shared mirror axis x24; SQUARE centerlines (6,6)-(42,42).'
OMISSIONS='Small auxiliary legs reduced; main claws, body division and tail retained.'
class Drawing(Solo48):
    icon_id='lobster'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='animals/marine'
    aliases=()
    keywords=('lobster',)
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)



    def build(self):
        self.path('body',(24,12),[('C',(18,24),(20,15),(18,19)),('C',(20,34),(18,28),(19,32)),('C',(24,38),(21,36),(22,37)),('C',(28,34),(26,37),(27,36)),('C',(30,24),(29,32),(30,28)),('C',(24,12),(30,19),(28,15))],True)
        for side in (-1,1):
            p=lambda x,y:(24+side*(x-24),y)
            n=f'claw-{side}'
            self.path(n,p(14,13),[('C',p(16,9),p(17,12),p(17,11)),('C',p(12,6),p(16,7),p(14,6)),('C',p(6,12),p(9,6),p(6,8)),('C',p(12,24),p(6,18),p(10,22)),('L',p(18,24))]);self.relate('connect',n,'body')
            t=f'tail-{side}'
            self.path(t,p(20,34),[('C',p(14,42),p(13,36),p(11,42)),('C',(24,38),p(18,42),p(22,40))]);self.relate('connect',t,'body')
        self.relate('connect','tail--1','tail-1')
        self.add_line('division',(18,24),(30,24));self.relate('connect','body','division')
        for side in (-1,1):self.relate('connect',f'claw-{side}','division')

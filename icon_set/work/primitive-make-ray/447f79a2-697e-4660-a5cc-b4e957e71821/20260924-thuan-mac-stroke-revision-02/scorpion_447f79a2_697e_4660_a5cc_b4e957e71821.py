"""Scorpion with two open pincers, an oval body, paired legs and a curled tail with a barb. SQUARE centerlines (6,6)-(42,42). Share mirrored claw construction and keep the tail intentionally asymmetric."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='447f79a2-697e-4660-a5cc-b4e957e71821'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__scorpion/20260924T101756Z-thuan-mac/reference/insect scorpion_447f79a2-697e-4660-a5cc-b4e957e71821.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='bug: paired limb construction; source owns pincers and curled sting'
DESIGN_PLAN='Scorpion with two open pincers, an oval body, paired legs and a curled tail with a barb. SQUARE centerlines (6,6)-(42,42). Share mirrored claw construction and keep the tail intentionally asymmetric.'
OMISSIONS='Three leg pairs reduced to two pairs for spacing.'
class Drawing(Solo48):
    icon_id='scorpion'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('scorpion',)
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
        self.path('body',(24,16),[('A',(30,24),6,8,True),('A',(24,32),6,8,True),('A',(18,24),6,8,True),('A',(24,16),6,8,True)],True)
        for side in (-1,1):
            p=lambda x,y:(24+side*(x-24),y)
            self.path(f'claw-{side}',p(6,6),[('C',p(12,14),p(6,11),p(8,14)),('C',p(18,6),p(16,14),p(18,11))])
            self.add_line(f'arm-{side}',(24,16),p(12,14));self.relate('connect',f'arm-{side}','body');self.relate('connect',f'arm-{side}',f'claw-{side}')
            self.add_line(f'leg-upper-{side}',p(18,24),p(10,24));self.relate('connect',f'leg-upper-{side}','body')
            self.add_line(f'leg-lower-{side}',p(18,24),p(14,32));self.relate('connect',f'leg-lower-{side}','body');self.relate('connect',f'leg-upper-{side}',f'leg-lower-{side}')
        self.relate('connect','arm--1','arm-1')
        self.path('tail',(24,32),[('A',(15,42),9,10,True),('A',(6,32),9,10,True),('L',(10,36))]);self.relate('connect','body','tail')

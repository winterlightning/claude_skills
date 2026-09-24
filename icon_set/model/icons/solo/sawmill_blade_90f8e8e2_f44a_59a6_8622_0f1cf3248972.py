"""Circular saw blade with eight directional teeth and a round arbor hole. A shared quarter-turn definition produces uniform hooked teeth. SQUARE centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90f8e8e2-f44a-59a6-8622-0f1cf3248972'
SOURCE_PATH = 'pictographic-primitives/tools/sawmill_90f8e8e2-f44a-59a6-8622-0f1cf3248972.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='cog: rotationally repeated elements; source owns asymmetric hooked teeth'
DESIGN_PLAN='Circular saw blade with eight directional teeth and a round arbor hole. A shared quarter-turn definition produces uniform hooked teeth. SQUARE centerlines (6,6)-(42,42).'
OMISSIONS='Table baseline omitted; circular cutting blade and arbor retained.'
class Drawing(Solo48):
    icon_id='sawmill-blade'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/tools'
    aliases=()
    keywords=('sawmill', 'blade')
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
        commands=[]
        def turn(p,k):
            x,y=p[0]-24,p[1]-24
            for _ in range(k):x,y=-y,x
            return (x+24,y+24)
        for k in range(4):
            commands.extend([('C',turn((24,12),k),turn((24,9),k),turn((25,11),k)),('L',turn((36,9),k)),('C',turn((34,18),k),turn((36,14),k),turn((35,16),k)),('L',turn((42,24),k))])
        self.path('blade',(24,6),commands,True)
        self.circle('arbor',24,24,3)

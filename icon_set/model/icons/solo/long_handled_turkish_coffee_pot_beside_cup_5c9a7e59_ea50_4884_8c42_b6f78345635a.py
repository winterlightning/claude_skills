"""A waisted long-handled coffee pot and a smaller cup. HRECT_L centerlines (4,8)-(44,40); preserve unequal vessel scale and diagonal handle. Continuous pot curves replace the pinched arc chain."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c9a7e59-ea50-4884-8c42-b6f78345635a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee turkish_5c9a7e59-ea50-4884-8c42-b6f78345635a.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='coffee: rounded cup and external handle'
DESIGN_PLAN='A waisted long-handled coffee pot and a smaller cup. HRECT_L centerlines (4,8)-(44,40); preserve unequal vessel scale and diagonal handle. Continuous pot curves replace the pinched arc chain.'
OMISSIONS='Steam and saucer baseline omitted to preserve two distinct vessels.'
class Drawing(Solo48):
    icon_id='long-handled-turkish-coffee-pot-beside-cup'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='drinks'
    aliases=()
    keywords=('long', 'handled', 'turkish', 'coffee', 'pot', 'beside', 'cup')
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
        self.path('pot',(4,18),[('L',(20,18)),('C',(16,26),(18,21),(16,23)),('C',(20,35),(16,30),(20,31)),('C',(15,40),(20,39),(18,40)),('L',(9,40)),('C',(4,35),(6,40),(4,39)),('C',(8,26),(4,31),(8,30)),('C',(4,18),(8,23),(6,21))],True)
        self.add_line('long-handle',(20,18),(38,8));self.relate('connect','pot','long-handle')
        self.path('cup',(29,26),[('L',(37,26)),('L',(37,36)),('A',(33,40),4,4,True),('A',(29,36),4,4,True),('L',(29,26))],True)
        self.path('cup-handle',(37,26),[('A',(44,31),7,5,True),('A',(37,36),7,5,True)]);self.relate('connect','cup','cup-handle')

"""Two counterclockwise circular arrows form a magnifying lens with a lower-right handle. Shared radius 15 and exact integer points on its circle; SQUARE centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cddee393-b2d9-4824-86a6-013321aa73e8'
SOURCE_PATH = 'pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='refresh-cw: separated circular arrows; source owns counterclockwise direction'
DESIGN_PLAN='Two counterclockwise circular arrows form a magnifying lens with a lower-right handle. Shared radius 15 and exact integer points on its circle; SQUARE centerlines (6,6)-(42,42).'
OMISSIONS='None; two arrowheads and handle retained.'
class Drawing(Solo48):
    icon_id='magnifier-refresh'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases=()
    keywords=('magnifier', 'refresh')
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
        self.path('left-loop',(21,6),[('A',(6,21),15,15,False),('A',(12,33),15,15,False)])
        self.add_polyline('left-head',(6,31),(12,33),(14,25));self.relate('connect','left-loop','left-head')
        self.path('right-loop',(21,36),[('A',(33,30),15,15,False),('A',(36,21),15,15,False),('A',(30,9),15,15,False)])
        self.add_polyline('right-head',(38,11),(30,9),(28,17));self.relate('connect','right-loop','right-head')
        self.add_line('handle',(33,30),(42,42));self.relate('connect','right-loop','handle')

"""Upright toothed pick and a diagonal bent pick with separate capsule grips. Integer 3-4-5 geometry owns the diagonal rounded cap; centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81ef6eef-313b-4e94-9969-a0db39ee190f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools loackpick_81ef6eef-313b-4e94-9969-a0db39ee190f.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='No direct Lucide match; rounded capsule construction'
DESIGN_PLAN='Upright toothed pick and a diagonal bent pick with separate capsule grips. Integer 3-4-5 geometry owns the diagonal rounded cap; centerlines (6,6)-(42,42).'
OMISSIONS='Tiny extra bend on right shaft simplified.'
class Drawing(Solo48):
    icon_id='lockpicking-tool-pair'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'crime'
    aliases=()
    keywords=('lockpicking', 'tool', 'pair')
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
        self.path('left-grip',(10,24),[('A',(14,28),4,4,True),('L',(14,38)),('A',(10,42),4,4,True),('A',(6,38),4,4,True),('L',(6,28)),('A',(10,24),4,4,True)],True)
        self.add_polyline('left-shaft',(10,24),(10,14),(10,6),(18,6));self.relate('connect','left-grip','left-shaft')
        self.add_line('tooth',(10,14),(16,14));self.relate('connect','tooth','left-shaft')
        self.path('right-grip',(24,33),[('L',(30,25)),('A',(37,24),5,5,True),('A',(38,31),5,5,True),('L',(32,39)),('A',(24,33),5,5,True)],True)
        self.add_polyline('right-shaft',(37,24),(42,18),(42,10),(38,10));self.relate('connect','right-shaft','right-grip')

"""Diagonal optical tube, smooth semicircular support arm, separate specimen stage and broad base. VRECT_L centerlines (8,4)-(40,44). Keep deliberate diagonal optics; omit the tiny ocular collars. Arm has matched tangent arcs and a horizontal base attachment."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '101aaf57-5431-5ae4-a7e5-f05c16647c10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/microscope_101aaf57-5431-5ae4-a7e5-f05c16647c10.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'microscope'
DESIGN_PLAN = 'Diagonal optical tube, smooth semicircular support arm, separate specimen stage and broad base. VRECT_L centerlines (8,4)-(40,44). Keep deliberate diagonal optics; omit the tiny ocular collars. Arm has matched tangent arcs and a horizontal base attachment.'
class Drawing(Solo48):
    icon_id = 'laboratory-microscope-101aaf57'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('laboratory', 'microscope', '101aaf57')
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
        self.add_polyline('optics',(20,4),(28,8),(20,24),(12,20),closed=True)
        self.path('arm',(28,8),[('A',(40,26),12,18,True),('A',(28,44),12,18,True)])
        self.relate('connect','optics','arm')
        self.add_line('stage',(8,33),(20,33))
        self.add_polyline('base',(8,44),(28,44),(40,44));self.relate('connect','arm','base')

'A circular outline is divided into three unequal sectors by straight lines meeting near the center. One divider rises vertically, while the other two angle down toward the lower left and right.\nPlan: Three unequal pie sectors inside a circle. Exact integer 12-16-20 points connect radial dividers to the rim.\nConstruction reference: chart-pie: radial divisions; original complete circle and three sectors retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e20da946-96cf-4a3e-abf7-b6101183f00f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/sectional_e20da946-96cf-4a3e-abf7-b6101183f00f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-chart-with-three-sectors'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('circular', 'chart', 'with', 'three', 'sectors')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        path('rim',(24,4),[('A',(40,36),20,20,True),('A',(12,40),20,20,True),('A',(24,4),20,20,True)],True)
        for name,end in [('up',(24,4)),('right',(40,36)),('left',(12,40))]:line(name,(24,24),end);join(name,'rim')
        join('up','right');join('up','left');join('left','right')

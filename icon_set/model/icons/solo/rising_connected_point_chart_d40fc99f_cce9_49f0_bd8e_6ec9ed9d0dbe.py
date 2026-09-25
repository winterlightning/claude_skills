"""Growing Data Point Chart.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
Three outlined nodes are connected at their boundaries, preserving the rising, dipping chart without crossing their openings. The initial segment from the axis origin is omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: chart-network.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd40fc99f-cce9-49f0-bd8e-6ec9ed9d0dbe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chart network_d40fc99f-cce9-49f0-bd8e-6ec9ed9d0dbe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rising-connected-point-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('rising', 'connected', 'point', 'chart')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('axes',(6,6),(6,42),(42,42))
        circle('point-left',18,18,3);circle('point-mid',30,30,3)
        path('point-high',(39,6),[('A',(42,9),3,3,True),('A',(39,12),3,3,True),('A',(36,9),3,3,True),('A',(39,6),3,3,True)],True)
        line('segment-a',(21,18),(27,30));line('segment-b',(33,30),(39,12))
        join('segment-a','point-left');join('segment-a','point-mid');join('segment-b','point-mid');join('segment-b','point-high')

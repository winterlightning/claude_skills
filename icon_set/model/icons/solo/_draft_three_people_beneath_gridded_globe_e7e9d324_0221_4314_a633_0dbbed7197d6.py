"""Global User Community.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Unresolved: the compact globe and three busts retain the source arrangement, but opposing head/shoulder arcs trigger three internal-spacing warnings (minimum ink gap 3.7635 versus required 4). Larger figures would displace the globe or break the SOLO48 envelope; the simpler globe reduction lost the grid identity. Retain this faithful candidate as a draft; do not publish.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: users-round.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7e9d324-0221-4314-a633-0dbbed7197d6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/multiple users network_e7e9d324-0221-4314-a633-0dbbed7197d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-people-beneath-gridded-globe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "objects"
    aliases = ()
    keywords = ('three', 'people', 'beneath', 'gridded', 'globe')

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

        path('globe',(24,4),[('A',(35,15),11,11,True),('A',(24,26),11,11,True),('A',(13,15),11,11,True),('A',(24,4),11,11,True)],True)
        poly('equator',(13,15),(24,15),(35,15));poly('meridian',(24,4),(24,15),(24,26));join('equator','meridian');join('equator','globe');join('meridian','globe')
        for j,x in enumerate([10,24,38]):
         circle(f'head-{j}',x,36,2)
         path(f'body-{j}',(x-2,44),[('A',(x+2,44),2,2,True)])
         join(f'head-{j}',f'body-{j}')

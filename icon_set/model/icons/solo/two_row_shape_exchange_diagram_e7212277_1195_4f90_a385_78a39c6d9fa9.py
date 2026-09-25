"""Geometric Shapes and Directional Arrows.

Plan: HRECT_L, centerline extremes (4, 8, 44, 40); 48 x 48, stroke 4.
Opposing directional arrows and both shape rows remain distinct. Short arrow shafts preserve the available separation.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7212277-1195-4f90-a385-78a39c6d9fa9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon s3 tiering access pattern_e7212277-1195-4f90-a385-78a39c6d9fa9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-row-shape-exchange-diagram'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('two', 'row', 'shape', 'exchange', 'diagram')

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

        circle('circle',8,12,4);poly('triangle',(20,20),(26,8),(32,20),closed=True)
        poly('arrow-right',(40,8),(44,14),(40,20));line('shaft-right',(40,14),(44,14));join('arrow-right','shaft-right')
        poly('arrow-left',(8,28),(4,34),(8,40));line('shaft-left',(4,34),(12,34));join('arrow-left','shaft-left')
        rect('square-a',20,30,8,8,2);rect('square-b',36,30,8,8,2)

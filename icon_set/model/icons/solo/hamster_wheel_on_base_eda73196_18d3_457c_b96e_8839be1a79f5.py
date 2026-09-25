"""Hamster Exercise Wheel.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Wheel, central hub, triangular support and separate base remain recognizable.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eda73196-18d3-457c-b96e-8839be1a79f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hamster toy_eda73196-18d3-457c-b96e-8839be1a79f5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hamster-wheel-on-base'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hamster', 'wheel', 'on', 'base')

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

        circle('wheel',24,20,16);circle('hub',24,20,3)
        poly('support',(14,36),(24,23),(34,36));join('support','hub');join('support','wheel')
        line('base',(8,44),(40,44))

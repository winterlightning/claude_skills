"""Sputnik Space Satellite.

Plan: Sphere at upper-right, three long trailing rods. Bounds6,6,42,42. Omit seam if crowding; keep antenna directions.
Construction reference: satellite.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fed86c8-339a-58f8-8d09-3b8778a24cc4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/exploration sputnik_4fed86c8-339a-58f8-8d09-3b8778a24cc4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sputnik-space-satellite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('sputnik', 'space', 'satellite')

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

        path('sphere',(30,6),[('A',(42,18),12,12,True),('A',(30,30),12,12,True),('A',(18,18),12,12,True),('A',(30,6),12,12,True)],True)
        line('antenna-left',(18,18),(6,24));join('sphere','antenna-left')
        line('antenna-down',(30,30),(24,42));join('sphere','antenna-down')
        line('antenna-diagonal',(18,18),(6,42));join('sphere','antenna-diagonal')

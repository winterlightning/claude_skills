"""Unrolled Architectural Blueprint.

Plan: Wide sheet with right scroll curl; bounds4,8,44,40. Roll defined by shared radius6, side gap12.
Construction reference: scroll.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f4ecb94-3a73-4380-95f8-a8bd0a7bf26d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/blueprint 1_0f4ecb94-3a73-4380-95f8-a8bd0a7bf26d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unrolled-paper-right-curl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('unrolled', 'paper', 'right', 'curl')

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

        path('sheet',(38,8),[('L',(4,8)),('L',(4,40)),('L',(38,40)),('A',(44,34),6,6,False),('L',(44,14)),('A',(38,8),6,6,False)],True)
        path('curl',(38,8),[('A',(32,14),6,6,False),('L',(32,28)),('L',(38,28)),('A',(44,34),6,6,True)]);join('curl','sheet')

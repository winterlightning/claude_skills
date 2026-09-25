"""Secure Padlock Symbol.

Plan: Centered arch above rectangular lock. Bounds8,4,40,44. Simplify keyhole to short slot.
Construction reference: lock-keyhole.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26e00f91-ffb7-4269-a976-24c5834354ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/crypto encryption lock_26e00f91-ffb7-4269-a976-24c5834354ca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-padlock'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('closed', 'padlock')

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

        path('body',(12,24),[('L',(16,24)),('L',(32,24)),('L',(36,24)),('A',(40,28),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,28)),('A',(12,24),4,4,True)],True)
        path('shackle',(16,24),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,24))]);join('shackle','body')
        line('keyhole',(24,33),(24,35))

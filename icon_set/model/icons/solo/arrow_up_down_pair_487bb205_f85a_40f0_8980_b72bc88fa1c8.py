"""Vertical Up and Down Arrows.

Plan: Opposing vertical arrows; bounds8,4,40,44. Both arrows share40u height and matching heads with separate shafts.
Construction reference: arrow-up-down.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '487bb205-f85a-40f0-8980-b72bc88fa1c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/opposite arrows_487bb205-f85a-40f0-8980-b72bc88fa1c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-up-down-pair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('arrow', 'up', 'down', 'pair')

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

        poly('down-head',(8,34),(16,44),(24,34));line('down-shaft',(16,4),(16,44));join('down-head','down-shaft')
        poly('up-head',(24,14),(32,4),(40,14));line('up-shaft',(32,4),(32,44));join('up-head','up-shaft')

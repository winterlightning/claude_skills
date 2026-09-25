"""Fishing Reel with Crank Handle.

Plan: Round reel with center bearing, hanging mount and right crank; bounds6,6,42,42. Crank grip simplified.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01503457-9580-4fc3-af04-5c52d2d80f5c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/reel_01503457-9580-4fc3-af04-5c52d2d80f5c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fishing-reel-with-side-crank'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('fishing', 'reel', 'with', 'side', 'crank')

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

        path('reel',(20,6),[('A',(34,20),14,14,True),('A',(20,34),14,14,True),('A',(6,20),14,14,True),('A',(20,6),14,14,True)],True)
        circle('hub',20,20,4)
        poly('mount',(16,34),(16,42),(24,42),(24,34));join('mount','reel')
        poly('crank',(34,20),(42,20),(42,32));join('crank','reel')

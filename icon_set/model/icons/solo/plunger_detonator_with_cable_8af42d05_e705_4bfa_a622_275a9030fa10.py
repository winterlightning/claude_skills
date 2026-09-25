"""Explosive Detonator Plunger.

Plan: Box, plunger and looped cable. Bounds6,6,42,42. Plunger handle simplified to thick horizontal bar.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8af42d05-e705-4bfa-a622-275a9030fa10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bomb detonator_8af42d05-e705-4bfa-a622-275a9030fa10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plunger-detonator-with-cable'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('plunger', 'detonator', 'with', 'cable')

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

        poly('box',(6,22),(16,22),(26,22),(26,32),(26,42),(6,42),closed=True)
        line('handle',(8,6),(24,6));line('plunger',(16,6),(16,22));join('handle','plunger');join('box','plunger')
        path('cable',(26,32),[('L',(30,32)),('A',(34,28),4,4,False),('L',(34,24)),('A',(42,24),4,4,True),('L',(42,42))]);join('cable','box')

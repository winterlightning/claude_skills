"""Pointed Metal Carpentry Nail.

Plan: Nail centered on x24, broad capsule head spanning10..38 at y4..12, shaft to pointed y44. Keep open shaft width8.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fad88318-92eb-4c60-9a02-1fdce0a4dc04'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nail_fad88318-92eb-4c60-9a02-1fdce0a4dc04.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-headed-carpentry-nail'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'headed', 'carpentry', 'nail')

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

        path('head',(14,4),[('L',(34,4)),('A',(38,8),4,4,True),('A',(34,12),4,4,True),('L',(28,12)),('L',(20,12)),('L',(14,12)),('A',(10,8),4,4,True),('A',(14,4),4,4,True)],True)
        poly('shaft',(20,12),(20,32),(24,44),(28,32),(28,12));join('shaft','head')

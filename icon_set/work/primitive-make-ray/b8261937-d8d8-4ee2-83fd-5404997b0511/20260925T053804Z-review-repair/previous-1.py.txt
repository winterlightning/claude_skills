"""Simple Clothes Hanger.

Plan: Symmetric shoulders, flat base, central open hook; bounds4,8,44,40. Smooth coherent hook and rounded triangular ends.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8261937-d8d8-4ee2-83fd-5404997b0511'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hanger_b8261937-d8d8-4ee2-83fd-5404997b0511.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clothes-hanger'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('clothes', 'hanger')

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

        path('frame',(24,24),[('L',(42,32)),('C',(44,36),(43,33),(44,34)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('C',(6,32),(4,34),(5,33)),('L',(24,24))],True)
        path('hook',(16,16),[('A',(24,8),8,8,True),('A',(32,16),8,8,True),('A',(24,24),8,8,True)]);join('hook','frame')

"""Simple Hamburger Fast Food.

Plan: Domed top bun, broad filling layer and rounded bottom bun retained with shared horizontal seams. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd328ea7d-4599-4236-ba2c-ee74bc46d030'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bun_d328ea7d-4599-4236-ba2c-ee74bc46d030.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-three-layer-burger'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('plain', 'three', 'layer', 'burger')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('top',(4,24),[('C',(24,8),(4,15),(13,8)),('C',(44,24),(35,8),(44,15)),('L',(4,24))],True)
        path('middle',(4,24),[('L',(4,32)),('L',(44,32)),('L',(44,24))]);join('top','middle')
        path('bottom',(4,32),[('A',(12,40),8,8,False),('L',(36,40)),('A',(44,32),8,8,False)]);join('bottom','middle')

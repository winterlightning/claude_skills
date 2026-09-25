"""Simple Bird House.

Plan: Steep roof, house body and circular entrance retained. Omitted the tiny perch to keep the entrance clear. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide birdhouse: circular entrance beneath gable; tiny perch omitted for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7bdc838-94c4-4ba8-b272-6c84718f26a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/birdhouse_c7bdc838-94c4-4ba8-b272-6c84718f26a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pitched-roof-birdhouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pitched', 'roof', 'birdhouse')

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

        poly('roof',(8,20),(24,4),(40,20))
        poly('walls',(10,18),(10,44),(38,44),(38,18));join('walls','roof')
        circle('entrance',24,27,5)

"""Simple Farm Chicken Hen.

Plan: Left-facing hen, small beak, rounded body, raised tail and one foot retained. Reduced crest lobes and two small feet to a readable outline and single foot. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ee8a983-7ca0-48b0-a3c8-3fbe81bd8f23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chicken animal_5ee8a983-7ca0-48b0-a3c8-3fbe81bd8f23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-facing-hen-with-split-crest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('left', 'facing', 'hen', 'with', 'split', 'crest')

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

        path('hen',(12,8),[('C',(20,15),(18,8),(20,10)),('C',(29,22),(20,20),(24,22)),('C',(44,12),(36,22),(41,12)),('L',(42,26)),('C',(25,32),(42,31),(34,32)),('C',(8,24),(13,32),(8,30)),('L',(8,20)),('L',(4,17)),('L',(8,14)),('C',(12,8),(6,10),(8,8))],True)
        poly('foot',(25,32),(25,40),(18,40));join('foot','hen')

"""Side View Passenger Car.

Plan: Plain curved cabin, rounded chassis and equal wheel pair retained; tiny body details omitted. Keyshape HRECT_M uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide car original and atomic-debug: interrupted chassis attached to wheel boundaries.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd57d66fe-ac03-4d2b-874b-b8f4c037b46d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/driving_d57d66fe-ac03-4d2b-874b-b8f4c037b46d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compact-side-view-car-with-plain-cabin'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('compact', 'side', 'view', 'car', 'with', 'plain', 'cabin')

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

        path('body',(12,34),[('L',(8,34)),('A',(4,30),4,4,True),('L',(4,24)),('A',(8,20),4,4,True),('L',(10,20)),('C',(18,10),(12,10),(14,10)),('L',(28,10)),('C',(36,20),(32,10),(34,14)),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,30)),('A',(40,34),4,4,True),('L',(36,34))])
        line('cabin',(10,20),(36,20));join('cabin','body')
        for x in [16,32]:
         circle(f'wheel{x}',x,34,4);join(f'wheel{x}','body')
        line('under',(20,34),(28,34));join('under','wheel16');join('under','wheel32')

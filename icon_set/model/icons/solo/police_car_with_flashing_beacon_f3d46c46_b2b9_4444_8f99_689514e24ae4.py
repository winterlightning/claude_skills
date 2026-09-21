"""Police Patrol Car with Siren.

Plan: Side car with beacon and two wheels at shared axle y36. Bounds4,8,44,40. Omit cabin divider and minor flashes to retain spacing.
Construction reference: Lucide car: wheels integrated at shared body endpoints
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3d46c46-b2b9-4444-8f99-689514e24ae4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/police car_f3d46c46-b2b9-4444-8f99-689514e24ae4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'police-car-with-flashing-beacon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('police', 'car', 'with', 'flashing', 'beacon')

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

        path('body',(8,24),[('L',(12,24)),('L',(36,24)),('L',(40,24)),('A',(44,28),4,4,True),('A',(40,32),4,4,True),('L',(36,32)),('L',(12,32)),('L',(8,32)),('A',(4,28),4,4,True),('A',(8,24),4,4,True)],True)
        for x in (12,36):circle('wheel-'+str(x),x,36,4);join('wheel-'+str(x),'body')
        poly('cabin',(12,24),(18,16),(20,16),(28,16),(30,16),(36,24));join('cabin','body')
        poly('beacon',(20,16),(20,8),(28,8),(28,16));join('beacon','cabin')

        line('flash-left',(8,8),(10,10))
        line('flash-right',(38,10),(40,8))

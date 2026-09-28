"""Formula One Racing Car.

Plan: Low pointed racer with cockpit, two wheels and rear wing. Bounds4,8,44,40. Omit suspension marks.
Construction reference: car-front.
Final review: Raised racer body for wheel clearance; simplified low shell and rear wing.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f803b66-a6f0-4bdf-b4c8-49f7ac21db0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dragster_9f803b66-a6f0-4bdf-b4c8-49f7ac21db0e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-racing-car-with-raised-rear-wing'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('low', 'racing', 'car', 'with', 'raised', 'rear', 'wing')

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

        circle('front-wheel',12,35,5);circle('rear-wheel',36,35,5)
        poly('shell',(4,20),(10,16),(20,16),(26,12),(32,16),(44,20))
        line('wing',(32,8),(44,8));line('wing-strut',(40,8),(40,19));join('wing','wing-strut');join('wing-strut','shell')

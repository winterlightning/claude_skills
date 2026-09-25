"""Side View Passenger Car.

Plan: Retained the left-facing passenger car, curved cabin roof, window line and two wheels. Omitted minor body contour changes.
Construction reference: Lucide car: coherent body and exposed circular wheels; reference cabin layout and orientation retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67782b7a-1201-46f2-95fd-506d2f21aa39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/coupe_67782b7a-1201-46f2-95fd-506d2f21aa39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-passenger-car-in-side-view'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('low', 'passenger', 'car', 'in', 'side', 'view')

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

        def p(x,y):return (x if 50==49 else 48-x,y)
        path('body',p(12,34),[('L',p(8,34)),('A',p(4,30),4,4,50==49),('L',p(4,24)),('C',p(10,20),p(4,20),p(8,20)),('C',p(24,10),p(16,10),p(20,10)),('C',p(36,20),p(30,10),p(34,18)),('C',p(44,26),p(42,20),p(44,22)),('L',p(44,30)),('A',p(40,34),4,4,50==49),('L',p(36,34))])
        line('under',(20,34),(28,34));circle('wheel-a',16,34,4);circle('wheel-b',32,34,4)
        for wheel in ('wheel-a','wheel-b'):join(wheel,'body');join(wheel,'under')
        line('window',p(10,20),p(36,20));join('window','body')

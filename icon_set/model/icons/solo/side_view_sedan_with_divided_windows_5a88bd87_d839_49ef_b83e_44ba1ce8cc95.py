"""Side View Passenger Car.

Plan: Retained the right-facing sedan, both wheels and central window divider. Rounded the lower corners for wheel clearance.
Construction reference: Lucide car: coherent body and exposed circular wheels; reference cabin layout and orientation retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a88bd87-d839-49ef-b83e-44ba1ce8cc95'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/motorcar_5a88bd87-d839-49ef-b83e-44ba1ce8cc95.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-sedan-with-divided-windows'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('side', 'view', 'sedan', 'with', 'divided', 'windows')

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

        def p(x,y):return (x if 49==49 else 48-x,y)
        path('body',p(12,34),[('L',p(8,34)),('A',p(4,30),4,4,49==49),('L',p(4,24)),('C',p(10,20),p(4,20),p(8,20)),('L',p(16,10)),('L',p(30,10)),('L',p(36,20)),('C',p(44,26),p(42,20),p(44,22)),('L',p(44,30)),('A',p(40,34),4,4,49==49),('L',p(36,34))])
        line('under',(20,34),(28,34));circle('wheel-a',16,34,4);circle('wheel-b',32,34,4)
        for wheel in ('wheel-a','wheel-b'):join(wheel,'body');join(wheel,'under')
        line('window',p(10,20),p(36,20));join('window','body');line('divider',(24,10),(24,20));join('divider','body');join('divider','window')

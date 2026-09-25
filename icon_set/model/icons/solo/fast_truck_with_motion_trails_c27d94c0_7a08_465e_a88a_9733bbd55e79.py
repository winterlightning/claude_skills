"""Fast Delivery Truck.

Plan: Right-facing truck with open rear and integrated trails. Bounds4,8,44,40. Omit tiny window to preserve cab clearance.
Construction reference: truck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c27d94c0-7a08-465e-a88a-9733bbd55e79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shipping truck fast_c27d94c0-7a08-465e-a88a-9733bbd55e79.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fast-truck-with-motion-trails'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('fast', 'truck', 'with', 'motion', 'trails')

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

        path('cargo',(4,8),[('L',(24,8)),('A',(28,12),4,4,True),('L',(28,16)),('L',(28,32))])
        poly('cab',(28,16),(36,16),(44,24),(44,32),(34,32),(28,32));join('cargo','cab')
        poly('floor',(6,32),(14,32),(28,32));join('floor','cargo')
        line('trail',(4,20),(14,20))
        for n,x in [('left',14),('right',34)]:
         path(n,(x,32),[('A',(x+4,36),4,4,True),('A',(x,40),4,4,True),('A',(x-4,36),4,4,True),('A',(x,32),4,4,True)],True)
        join('left','floor');join('right','cab')

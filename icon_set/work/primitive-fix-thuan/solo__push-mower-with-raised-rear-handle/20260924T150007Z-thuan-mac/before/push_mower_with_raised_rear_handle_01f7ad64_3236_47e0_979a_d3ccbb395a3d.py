"""Push Lawn Mower.

Plan: Lawn mower bounds4,8,44,40. Two wheels, raised motor and rear handle. Wheels share body axle endpoints.
Construction reference: Lucide car: chassis and paired round wheels
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01f7ad64-3236-47e0-979a-d3ccbb395a3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mower_01f7ad64-3236-47e0-979a-d3ccbb395a3d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'push-mower-with-raised-rear-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('push', 'mower', 'with', 'raised', 'rear', 'handle')

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

        path('body',(8,28),[('A',(12,24),4,4,True),('L',(28,24)),('A',(32,28),4,4,True),('L',(32,32)),('L',(8,32)),('L',(8,28))],True)
        for x in (8,32):circle('wheel-'+str(x),x,36,4);join('wheel-'+str(x),'body')
        poly('motor',(12,24),(12,16),(22,16),(22,24));join('motor','body')
        poly('handle',(32,24),(40,8),(44,8))
        line('handle-link',(32,24),(28,24));join('handle','handle-link');join('handle-link','body')

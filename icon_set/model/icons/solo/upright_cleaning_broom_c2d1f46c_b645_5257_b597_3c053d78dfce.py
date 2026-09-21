"""Traditional Cleaning Broom.

Plan: Long handle and flared bristle head; bounds8,4,40,44. One binding and two symmetric bristle cuts.
Construction reference: brush.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2d1f46c-b645-5257-b597-3c053d78dfce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cleaning_c2d1f46c-b645-5257-b597-3c053d78dfce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-cleaning-broom'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('upright', 'cleaning', 'broom')

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

        path('head',(16,24),[('L',(24,24)),('L',(32,24)),('L',(40,44)),('L',(8,44)),('L',(16,24))],True)
        line('handle',(24,4),(24,24));join('handle','head')
        line('binding',(13,32),(35,32));join('binding','head')

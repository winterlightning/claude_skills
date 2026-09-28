"""Praying Hands with Christian Cross.

Plan: Cross above paired cupped hands. Cross reduced to two joined strokes; mirrored hands retain raised fingers. Bounds8,4,40,44.
Construction reference: human_ref/user.svg: simple rounded anatomy; source hand pose
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2d21f34-88f5-4119-9e01-c79ec40a8337'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/religion hands_b2d21f34-88f5-4119-9e01-c79ec40a8337.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cupped-hands-beneath-a-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cupped', 'hands', 'beneath', 'a', 'cross')

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

        poly('cross-stem',(24,4),(24,12),(24,24));poly('cross-arm',(16,12),(24,12),(32,12));join('cross-stem','cross-arm')
        for side in (-1,1):
         def pt(x,y): return (24+side*x,y)
         path('hand-'+str(side),pt(16,44),[('L',pt(16,30)),('C',pt(8,30),pt(16,25),pt(8,25)),('L',pt(4,36)),('L',pt(4,44))])

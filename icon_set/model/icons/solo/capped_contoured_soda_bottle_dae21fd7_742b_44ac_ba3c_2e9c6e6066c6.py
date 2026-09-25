"""Glass Soda Bottle.

Plan: VRECT_M, centerline extremes (10, 4, 38, 44); 48 x 48, stroke 4.
Cap and curved waist identify the contoured bottle; the body remains blank.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: milk.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dae21fd7-742b-44ac-ba3c-2e9c6e6066c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coke_dae21fd7-742b-44ac-ba3c-2e9c6e6066c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'capped-contoured-soda-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('capped', 'contoured', 'soda', 'bottle')

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

        path('bottle',(18,4),[('L',(30,4)),('L',(30,12)),('C',(38,24),(30,18),(38,18)),('C',(34,34),(38,28),(34,30)),('C',(38,40),(34,37),(38,37)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('C',(14,34),(10,37),(14,37)),('C',(10,24),(14,30),(10,28)),('C',(18,12),(10,18),(18,18)),('L',(18,4))],True)
        line('cap',(18,12),(30,12));join('cap','bottle')

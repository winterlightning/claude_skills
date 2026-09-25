"""Glass Bottle with Liquid.

Plan: VRECT_M, centerline extremes (10, 4, 38, 44); 48 x 48, stroke 4.
Cap, neck, rounded shoulders and a single liquid wave remain distinct.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: milk.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a8e98f3-8ccd-4f04-9ec2-b8079a01bc37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/molasses_8a8e98f3-8ccd-4f04-9ec2-b8079a01bc37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'capped-bottle-with-wavy-liquid-surface'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('capped', 'bottle', 'with', 'wavy', 'liquid', 'surface')

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

        path('bottle',(18,4),[('L',(30,4)),('L',(30,14)),('C',(38,24),(30,18),(38,18)),('L',(38,28)),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,28)),('L',(10,24)),('C',(18,14),(10,18),(18,18)),('L',(18,4))],True)
        line('cap',(18,12),(30,12));join('cap','bottle')
        path('liquid',(10,28),[('C',(24,28),(16,28),(18,26)),('C',(38,28),(30,30),(32,28))]);join('liquid','bottle')

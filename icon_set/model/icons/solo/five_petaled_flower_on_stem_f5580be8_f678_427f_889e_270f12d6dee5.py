"""Simple Flower with Stem and Leaf.

Plan: Five distinct petals and an upright stem retained. Reduced the circular center to a dot and omitted the small leaf for clear spacing. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide flower: scalloped unified petals and a clear circular center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5580be8-f678-427f-889e-270f12d6dee5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/poppy_f5580be8-f678-427f-889e-270f12d6dee5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-petaled-flower-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('five', 'petaled', 'flower', 'on', 'stem')

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

        path('flower',(24,4),[('C',(30,13),(31,4),(33,9)),('C',(40,18),(37,10),(40,13)),('C',(33,24),(40,23),(37,25)),('C',(31,34),(37,31),(35,34)),('C',(24,29),(27,34),(25,32)),('C',(17,34),(23,32),(21,34)),('C',(15,24),(13,34),(11,31)),('C',(8,18),(11,25),(8,23)),('C',(18,13),(8,13),(11,10)),('C',(24,4),(15,9),(17,4))],True)
        self.add_dot('center',(24,20))
        line('stem',(24,29),(24,44));join('stem','flower')

"""Simple Flower with Stem and Leaves.

Plan: Six distinct petals and an upright stem retained. Reduced the circular center to a dot and omitted the crowded pair of leaves. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide flower: scalloped unified petals and a clear circular center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8d7fa28-dd1e-4789-91aa-95c3e894044c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/begonia_b8d7fa28-dd1e-4789-91aa-95c3e894044c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-petal-flower-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('six', 'petal', 'flower', 'on', 'stem')

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

        path('flower',(24,4),[('C',(30,11),(29,4),(31,7)),('C',(40,14),(35,7),(40,9)),('C',(35,21),(40,18),(38,20)),('C',(40,28),(38,22),(40,24)),('C',(30,31),(40,33),(35,34)),('C',(24,36),(30,35),(28,36)),('C',(18,31),(20,36),(18,35)),('C',(8,28),(13,34),(8,33)),('C',(13,21),(8,24),(10,22)),('C',(8,14),(10,20),(8,18)),('C',(18,11),(8,9),(13,7)),('C',(24,4),(17,7),(19,4))],True)
        self.add_dot('center',(24,20));line('stem',(24,36),(24,44));join('stem','flower')

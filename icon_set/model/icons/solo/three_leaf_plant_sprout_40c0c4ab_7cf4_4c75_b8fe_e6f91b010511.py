"""Three Leaf Plant Sprout.

Plan: Three pointed lobes form one continuous leaf-cluster outline joined to the central stem; internal seams removed to open the leaf spaces. Bounds8,4,40,44; bilateral side leaves with central upright leaf.
Construction reference: sprout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40c0c4ab-7cf4-4c75-b8fe-e6f91b010511'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf_40c0c4ab-7cf4-4c75-b8fe-e6f91b010511.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-leaf-plant-sprout'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'leaf', 'plant', 'sprout')

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

        # One continuous three-lobed leaf cluster; remove internal leaf seams.
        # The notches and three pointed lobes preserve the source sprout identity.
        path('leaves',(24,4),[('C',(30,24),(34,16),(30,20)),('C',(40,20),(34,20),(38,20)),('C',(24,36),(40,32),(34,36)),('C',(8,20),(14,36),(8,32)),('C',(18,24),(10,20),(14,20)),('C',(24,4),(18,20),(14,16))],True)
        line('stem',(24,36),(24,44));join('leaves','stem')

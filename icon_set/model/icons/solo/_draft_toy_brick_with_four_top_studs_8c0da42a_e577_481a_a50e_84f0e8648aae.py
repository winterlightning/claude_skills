"""Four-stud toy brick, revised top view with a thickness edge.
VRECT_L envelope (8,4)-(40,44). Four radius-2 studs share a 12-unit grid;
body owns the thickness divider and its split attachment nodes. Lucide
 toy-brick was inspected for body/stud hierarchy; reference supplies count.
Valid with zero warnings, but the native appearance still resembles a button
or die. Perspective and protruding studs are unresolved; do not export.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c0da42a-e577-481a-a50e-84f0e8648aae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toy-brick-with-four-top-studs'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('toy', 'brick', 'with', 'four', 'top', 'studs')

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

        poly('body',(8,36),(8,4),(40,4),(40,36),(40,44),(8,44),(8,36),closed=True)
        line('thickness',(8,36),(40,36))
        join('thickness','body-1');join('thickness','body-6')
        join('thickness','body-3');join('thickness','body-4')
        for j,(x,y) in enumerate([(18,14),(30,14),(18,26),(30,26)]):circle(f'stud-{j}',x,y,2)

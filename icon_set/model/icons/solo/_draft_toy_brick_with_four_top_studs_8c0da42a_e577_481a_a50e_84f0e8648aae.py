"""Four Stud Toy Building Brick.

Plan: Four stud brick in top view with lower thickness lip. Bounds6,6,42,42. Simplify perspective while preserving four studs.
Construction reference: No useful local Lucide match.
Final review: Not released: top-view four-stud reduction passes geometry but reads as dice/button; the two-stud alternative changes the reference count.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c0da42a-e577-481a-a50e-84f0e8648aae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toy-brick-with-four-top-studs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
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

        rect('brick',6,6,36,36,4)
        for j,(x,y) in enumerate([(17,17),(31,17),(17,31),(31,31)]):circle(f'stud-{j}',x,y,2)

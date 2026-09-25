"""Target Crosshair Symbol.

Plan: Circle radius16 and four radial ticks, quarter arcs share cardinal nodes. Radial outer centerline radius20. Empty center.
Construction reference: crosshair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10290e98-0137-48f2-92b6-b7ba707eaffa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/target 1_10290e98-0137-48f2-92b6-b7ba707eaffa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-target-crosshair'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases = ()
    keywords = ('circular', 'target', 'crosshair')

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

        points=[(24,8),(40,24),(24,40),(8,24),(24,8)]
        for j,(a,b) in enumerate(zip(points,points[1:])): self.add_arc(f'ring-{j}',a,b,radius_x=16)
        self.add_contour('ring',*(f'ring-{j}' for j in range(4)),closed=True)
        for j,(a,b) in enumerate([((24,4),(24,14)),((44,24),(34,24)),((24,44),(24,34)),((4,24),(14,24))]):
         line(f'tick-{j}',a,b);join('ring',f'tick-{j}')

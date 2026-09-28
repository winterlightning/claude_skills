"""School Backpack with Front Pocket.

Plan: Retained the backpack, top handle, both side pockets and front pocket seam. Narrow pocket outlines share the body edges.
Construction reference: Lucide backpack: rounded body and attached pockets, rebuilt on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4914cfa4-c50c-4ca0-bc00-75e542cb8d84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/backpack_4914cfa4-c50c-4ca0-bc00-75e542cb8d84.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-backpack-with-side-pockets'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('rounded', 'backpack', 'with', 'side', 'pockets')

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

        rect('body',16,12,16,32,4)
        poly('handle',(20,12),(20,4),(28,4),(28,12));join('handle','body')
        path('left',(16,24),[('L',(8,24)),('L',(8,40)),('L',(16,40))]);join('left','body')
        path('right',(32,24),[('L',(40,24)),('L',(40,40)),('L',(32,40))]);join('right','body')
        line('pocket',(16,30),(32,30));join('pocket','body')

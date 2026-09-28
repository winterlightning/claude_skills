"""Left-facing bird on a broad semicircular nest, smoothly rounded crown; extremes 6,6,42,42.
Construction: bird: continuous crown and belly
Reduction: Fine nest hatching and tiny eye omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ee71767-8c7b-4b67-8c9c-982b7a27e635'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nestling_8ee71767-8c7b-4b67-8c9c-982b7a27e635.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-resting-in-nest'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('bird', 'resting', 'in', 'nest')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('bird',(14,26),[('L',(14,20)),('L',(6,14)),('L',(14,14)),('A',(30,14),8,8,True),('A',(34,22),4,8,False),('L',(42,14)),('L',(38,26))])
        path('nest',(6,26),[('L',(14,26)),('L',(38,26)),('L',(42,26)),('A',(6,26),18,16,True)],True)
        join('bird','nest')

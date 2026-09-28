"""Right-facing boar with curved skull, upright ear, projecting snout and upward tusk; extremes 4,8,44,40.
Construction: No useful direct Lucide match
Reduction: Tiny nostril and eye omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4dc687d-cffd-4881-a57d-b884d2cbce23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boar_a4dc687d-cffd-4881-a57d-b884d2cbce23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boar-head-with-tusks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('boar', 'head', 'with', 'tusks')
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

        path('head',(10,40),[('A',(4,34),6,6,True),('L',(4,24)),('A',(14,14),10,10,True),('L',(14,8)),('A',(26,16),14,14,True),('A',(36,20),14,14,False),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,28)),('A',(40,32),4,4,True),('L',(34,32)),('L',(28,26)),('L',(24,36)),('L',(32,36)),('L',(24,40)),('L',(10,40))],True)

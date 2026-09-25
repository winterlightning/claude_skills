"""Chick rises from jagged eggshell; rounded crown and deep bowl share contact nodes; extremes 6,6,42,42.
Construction: bird: rounded crown and projecting beak
Reduction: Tiny eye omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9a66ec5-6720-4213-9bfe-b9572cfa84f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/35-d9a66ec5-6720-4213-9bfe-b9572cfa84f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chick-emerging-from-egg'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('chick', 'emerging', 'from', 'egg')
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

        path('chick',(14,30),[('L',(14,18)),('L',(14,16)),('A',(34,16),10,10,True),('L',(42,18)),('L',(34,22)),('L',(34,30))])
        path('shell',(6,22),[('L',(14,30)),('L',(24,23)),('L',(34,30)),('L',(42,22)),('A',(6,22),18,20,True)],True)
        join('chick','shell')

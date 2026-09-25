"""Counterclockwise arrival clock uses centered circular rim and inward opening at upper left.
Construction: refresh-cw: continuous circular rim and attached head
Reduction: No omissions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7420a5ad-20b8-4125-a020-7f6c31b74aac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shipping logistic estimate time arrival 1_7420a5ad-20b8-4125-a020-7f6c31b74aac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clock-with-counterclockwise-arrival-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('clock', 'with', 'counterclockwise', 'arrival', 'arrow')
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

        path('rim',(24,6),[('A',(42,24),18,18,True),('A',(24,42),18,18,True),('A',(6,24),18,18,True)])
        poly('tip',(6,34),(6,24),(16,24));join('rim','tip')
        poly('hands',(24,15),(24,26),(33,26))

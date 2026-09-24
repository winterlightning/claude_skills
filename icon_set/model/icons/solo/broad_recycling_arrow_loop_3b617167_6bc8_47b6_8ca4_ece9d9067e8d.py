"""Three clockwise arrows retain triangular loop with equal stroke width and clear open arrowheads; extremes 6,6,42,42.
Construction: recycle: three separated bent arrows
Reduction: Outlined broad shafts simplified to centerline arrows for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b617167-6bc8-47b6-8ca4-ece9d9067e8d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/recycle_3b617167-6bc8-47b6-8ca4-ece9d9067e8d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-recycling-arrow-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('broad', 'recycling', 'arrow', 'loop')
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

        path('top',(15,14),[('L',(19,8)),('A',(25,8),3,2,True),('L',(32,19))]);poly('top-tip',(23,17),(32,19),(35,10));join('top','top-tip')
        path('right',(39,28),[('L',(42,34)),('A',(38,38),4,4,True),('L',(25,38))]);poly('right-tip',(30,32),(25,38),(30,42));join('right','right-tip')
        path('left',(16,38),[('L',(10,38)),('A',(6,34),4,4,True),('L',(12,23))]);poly('left-tip',(6,25),(12,23),(15,30));join('left','left-tip')

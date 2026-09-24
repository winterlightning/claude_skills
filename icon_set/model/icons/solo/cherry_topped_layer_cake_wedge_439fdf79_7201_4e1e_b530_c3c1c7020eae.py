"""Cherry-topped layer cake has a curved rear edge and a cherry stem; extremes 6,6,42,42.
Construction: cake-slice: curved back and spaced layer
Reduction: One horizontal layer retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '439fdf79-7201-4e1e-b530-c3c1c7020eae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dessert_439fdf79-7201-4e1e-b530-c3c1c7020eae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cherry-topped-layer-cake-wedge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cherry', 'topped', 'layer', 'cake', 'wedge')
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

        path('cake',(26,12),[('A',(42,24),16,12,True),('L',(42,33)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,33)),('L',(6,24)),('L',(18,12))])
        circle('cherry',22,12,4);join('cherry','cake')
        line('stem',(22,8),(26,6));join('stem','cherry')
        line('top',(6,24),(42,24));join('top','cake')
        line('layer',(6,33),(42,33));join('layer','cake')

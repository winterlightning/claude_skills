"""Cherry-topped triangular cake slice with a broad layer and rounded lower corners; extremes 6,6,42,42.
Construction: cake-slice: continuous wedge silhouette and layer rule
Reduction: Cherry stem omitted; one layer retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6b3e7a5a-f418-4efc-be04-216b265ddec8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cherry-topped-cheesecake-slice/20260924T111346Z-thuan-mac/reference/cheesecake_6b3e7a5a-f418-4efc-be04-216b265ddec8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cherry-topped-cheesecake-slice'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cherry', 'topped', 'cheesecake', 'slice')
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

        path('cake',(6,24),[('L',(20,14)),('L',(28,14)),('L',(42,22)),('L',(42,32)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,32)),('L',(6,24))],True)
        circle('cherry',24,10,4);join('cherry','cake')
        line('top',(6,24),(42,22));join('top','cake')
        line('layer',(6,32),(42,32));join('layer','cake')

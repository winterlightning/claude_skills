"""French horn has a circular coil and flared upper-right bell with a single inner tube end; extremes 6,6,42,42.
Construction: No useful direct Lucide match
Reduction: Fine valves and pedestal omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e0e5259b-1f4e-49b1-b4fe-796abc5994f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__coiled-french-horn/20260924T111346Z-thuan-mac/reference/instrument french horn_e0e5259b-1f4e-49b1-b4fe-796abc5994f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coiled-french-horn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('coiled', 'french', 'horn')
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

        path('tube',(18,29),[('L',(27,29)),('A',(19,42),13,13,True),('A',(6,29),13,13,True),('A',(19,16),13,13,True),('L',(24,16)),('A',(42,6),22,22,False),('L',(42,26)),('A',(24,16),22,22,False)])

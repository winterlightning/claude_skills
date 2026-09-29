"""A slanted diamond emblem with five radiating sparks.
Review before drawing: The current diamond is too small and squat, and six short rays replace the source five longer rays.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Tall slanted diamond with gently rounded lower-left and upper-right corners; five individually placed rays preserve the source arrangement.
Construction reference: No useful direct Lucide match found; source diamond and five-ray arrangement reconstructed with shared uniform stroke and coherent contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6eb3ab9d-a18e-4405-bdb2-8886b3a934b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitshares-diamond-spark/20260928T164600Z-thuan-mac/reference/virtual coin crypto bitshares_6eb3ab9d-a18e-4405-bdb2-8886b3a934b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitshares-diamond-spark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bitshares', 'diamond', 'spark')

    def build(self):

        def path(n, start, steps, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                p=f'{n}-{i}'
                if kind=='L': self.add_line(p,here,end)
                elif kind=='A': self.add_arc(p,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(p,here,(args[0],args[1],end))
                here=end;members.append(p)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def poly(n,*pts): self.add_polyline(n,*pts,closed=pts[0]==pts[-1])
        def line(n,a,b): self.add_line(n,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('diamond',(6,6),[('L',(20,14)),('C',(22,18),(22,15),(22,16)),('L',(22,28)),('L',(8,20)),('C',(6,16),(6,19),(6,18)),('L',(6,6))],True)
        for i,(a,b) in enumerate([((32,22),(38,16)),((36,30),(42,30)),((32,38),(36,42)),((24,36),(24,42)),((6,34),(14,34))]):line(f'ray-{i}',a,b)

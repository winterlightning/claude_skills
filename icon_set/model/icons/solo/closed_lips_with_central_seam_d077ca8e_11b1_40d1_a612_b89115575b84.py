"""Mirrored lips use smooth rounded upper lobes and a broad lower arc around one seam; extremes 4,10,44,38.
Construction: No useful direct Lucide match
Reduction: Central seam simplified to a shallow straight stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd077ca8e-11b1-40d1-a612-b89115575b84'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/lip_d077ca8e-11b1-40d1-a612-b89115575b84.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-lips-with-central-seam'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('closed', 'lips', 'with', 'central', 'seam')
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

        path('outline',(4,24),[('A',(16,10),12,14,True),('A',(24,13),8,3,True),('A',(32,10),8,3,True),('A',(44,24),12,14,True),('A',(24,38),20,14,True),('A',(4,24),20,14,True)],True)
        line('seam',(4,24),(44,24));join('seam','outline')

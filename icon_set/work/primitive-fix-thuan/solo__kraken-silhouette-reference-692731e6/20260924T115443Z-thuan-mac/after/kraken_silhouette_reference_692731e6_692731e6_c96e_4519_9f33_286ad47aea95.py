"""Symmetric kraken silhouette with a rounded crown and two smoothly curled tentacle tips. Extrema 4,8,44,40.
Construction: No useful Lucide kraken match; mirrored arcs and shared radii
Reduction: No source features omitted; open bottom retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='692731e6-c96e-4519-9f33-286ad47aea95'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__kraken-silhouette-reference-692731e6/20260924T115443Z-thuan-mac/reference/kraken_692731e6-c96e-4519-9f33-286ad47aea95.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='kraken-silhouette-reference-692731e6'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('kraken', 'silhouette', 'reference', '692731e6')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('kraken',(4,28),[('A',(6,30),2,2,True),('L',(6,36)),('A',(14,36),4,4,False),('L',(14,18)),('A',(24,8),10,10,True),('A',(34,18),10,10,True),('L',(34,36)),('A',(42,36),4,4,False),('L',(42,30)),('A',(44,28),2,2,True)])

"""corn.
The cob was blank and the husks heavy and misshapen. Restore an upright cob, two sweeping husks and a sparse kernel pattern.
Original corn silhouette; no useful exact Lucide match.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dfc9df01-8144-40e0-b66d-be471956d900'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__corn/20260928T164738Z-thuan-mac/reference/corn_dfc9df01-8144-40e0-b66d-be471956d900.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'corn'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('corn',)

    def build(self):

        def path(n,start,*commands,closed=False):
            pt=start; members=[]
            for i,c in enumerate(commands):
                mid=f'{n}-{i}'
                if c[0]=='L': self.add_line(mid,pt,c[1]); end=c[1]
                elif c[0]=='A':
                    _,end,rx,ry,sweep=c
                    self.add_arc(mid,pt,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif c[0]=='C':
                    _,a,b,end=c; self.add_bezier(mid,pt,(a,b,end))
                pt=end;members.append(mid)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def box(n,l,t,r,b,rad=2):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def bez(n,start,*s): self.add_bezier(n,start,*s)
        def join(a,b): self.relate('connect',a,b)
        path('cob',(16,27),('L',(16,12)),('A',(32,12),8,8,True),('L',(32,27)))
        bez('left-husk',(24,44),((12,43),(9,31),(8,23)),((16,24),(21,28),(24,35)))
        bez('right-husk',(24,44),((36,42),(39,31),(40,23)),((29,24),(24,33),(24,44)))
        join('left-husk','right-husk')
        for n,p in enumerate([(24,14),(24,22)]):self.add_dot(f'kernel-{n}',p)

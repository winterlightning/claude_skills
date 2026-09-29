"""gregorian new year party.
The squat bowl read as a goblet and only one dense burst survived. Lengthen the flute and restore two airy firework bursts.
Lucide cup-soda informs the clear vessel silhouette; source owns fireworks.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c59a36b0-fb72-53a5-9d44-6dad3255ce67'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__champagne-glass-with-fireworks-batch-014-03/20260928T164738Z-thuan-mac/reference/gregorian new year party_c59a36b0-fb72-53a5-9d44-6dad3255ce67.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'champagne-glass-with-fireworks-batch-014-03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('champagne', 'glass', 'with', 'fireworks', 'batch', '014', '03')

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
        path('bowl',(7,18),('L',(19,18)),('L',(21,30)),('C',(22,36),(18,38),(14,38)),('C',(10,38),(6,36),(6,32)),('L',(7,18)),closed=True)
        line('stem',(14,38),(14,44));line('foot',(9,44),(19,44));join('bowl','stem');join('stem','foot')
        for i,(a,b) in enumerate([((32,4),(32,8)),((24,7),(27,10)),((40,7),(37,10)),((24,17),(27,14)),((40,17),(37,14)),((32,20),(32,16)),((34,30),(34,34)),((27,34),(30,37)),((41,34),(38,37)),((34,44),(34,40))]):line(f'ray-{i}',a,b)

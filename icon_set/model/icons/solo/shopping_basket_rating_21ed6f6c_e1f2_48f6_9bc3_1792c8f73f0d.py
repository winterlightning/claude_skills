"""Rating basket with three five-ray stars, middle raised. Lucide shopping-basket informs trapezoid and handles. Replace tiny closed star holes with open five-ray stars and omit basket ribs. HRECT_L widens rating row.
Plan: shared dimensions and attachment nodes; exact HRECT_L envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='21ed6f6c-e1f2-48f6-9bc3-1792c8f73f0d'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shopping basket rating_21ed6f6c-e1f2-48f6-9bc3-1792c8f73f0d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='shopping-basket-rating'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('shopping basket rating',)
    def build(self):
        for n,x,y in [('left',8,16),('middle',24,12),('right',40,16)]:
            members=[]
            for k,(dx,dy) in enumerate([(0,-4),(4,-1),(2,3),(-2,3),(-4,-1)]):
                eid=f'{n}-{k}';self.add_line(eid,(x,y),(x+dx,y+dy));members.append(eid)
            for k,a in enumerate(members):
                for b in members[k+1:]:self.relate('connect',a,b)
        self.add_polyline('basket',(6,27),(12,40),(36,40),(42,27),(34,27),(14,27),closed=True)
        self.add_line('handle-left',(14,27),(18,22));self.relate('connect','handle-left','basket')
        self.add_line('handle-right',(34,27),(30,22));self.relate('connect','handle-right','basket')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l=6,t=6,r=42,b=42,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        for k in range(8):
            if k%2:self.add_arc(f'{n}-{k}',pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(f'{n}-{k}',pts[k],pts[(k+1)%8])
        self.add_contour(n,*(f'{n}-{k}' for k in range(8)),closed=True)
    def cross(self,n,x,y,r):
        ids=[]
        for k,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            ident=f'{n}-{k}';self.add_line(ident,(x,y),(x+dx,y+dy));ids.append(ident)
        for k,a in enumerate(ids):
            for b in ids[k+1:]:self.relate('connect',a,b)

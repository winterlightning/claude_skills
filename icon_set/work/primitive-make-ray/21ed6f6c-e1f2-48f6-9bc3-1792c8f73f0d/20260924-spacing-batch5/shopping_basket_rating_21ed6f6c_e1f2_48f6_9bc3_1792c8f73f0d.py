"""shopping basket rating. Three rating stars reduced to open four-ray glints; omitted ribs and double rim to preserve clearance.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
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
        for i,x in enumerate((8,24,40)): self.cross('star-'+str(i),x,12,4)
        self.add_polyline('basket',(8,28),(16,28),(32,28),(40,28),(36,40),(12,40),closed=True)
        self.add_line('handle-left',(16,28),(20,24));self.relate('connect','basket','handle-left')
        self.add_line('handle-right',(32,28),(28,24));self.relate('connect','basket','handle-right')

    def circle(self,n,x,y,r):
        pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
        for i in range(4): self.add_arc(f'{n}-{i}',pts[i],pts[i+1],radius_x=r)
        self.add_contour(n,*(f'{n}-{i}' for i in range(4)),closed=True)
    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        for i in range(8):
            if i%2:self.add_arc(f'{n}-{i}',pts[i],pts[(i+1)%8],radius_x=q)
            else:self.add_line(f'{n}-{i}',pts[i],pts[(i+1)%8])
        self.add_contour(n,*(f'{n}-{i}' for i in range(8)),closed=True)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i):self.relate('connect',f'{n}-{i}',f'{n}-{j}')

# Contract keyshape visible bounds: (2, 6, 46, 42).

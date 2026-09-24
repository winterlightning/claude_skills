"""tea cup herbal. Enlarged cup interior and rebalance leaf; omitted leaf stem and separate saucer to keep clear openings. Wide rounded bowl and herbal leaf retained.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fd3519ca-61c2-4e48-a98b-ef47a0103f4c'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/tea cup herbal_fd3519ca-61c2-4e48-a98b-ef47a0103f4c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tea-cup-herbal'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tea cup herbal',)
    def build(self):
        self.add_line('rim-a',(4,28),(4,10))
        self.add_line('rim-b',(4,10),(34,10))
        self.add_line('rim-c',(34,10),(34,14))
        self.add_line('rim-d',(34,14),(34,28))
        self.add_arc('bottom-right',(34,28),(24,38),radius_x=10)
        self.add_line('bottom',(24,38),(14,38))
        self.add_arc('bottom-left',(14,38),(4,28),radius_x=10)
        self.add_contour('cup','rim-a','rim-b','rim-c','rim-d','bottom-right','bottom','bottom-left',closed=True)
        self.add_arc('handle',(34,14),(34,28),radius_x=10,radius_y=7)
        self.relate('connect','cup','handle')
        self.add_bezier('leaf-upper',(14,28),((13,19),(19,19),(25,19)))
        self.add_bezier('leaf-lower',(25,19),((25,25),(23,30),(14,28)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)

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

# Contract keyshape visible bounds: (2, 8, 46, 40).

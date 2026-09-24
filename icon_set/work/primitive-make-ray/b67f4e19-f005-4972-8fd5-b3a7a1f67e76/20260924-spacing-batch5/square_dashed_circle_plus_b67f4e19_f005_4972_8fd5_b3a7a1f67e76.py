"""square dashed circle plus. Four symmetric curved ring dashes replace eight crowded dashes; centered plus and outer rounded square retained.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b67f4e19-f005-4972-8fd5-b3a7a1f67e76'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/square dashed circle plus_b67f4e19-f005-4972-8fd5-b3a7a1f67e76.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-dashed-circle-plus'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('square dashed circle plus',)
    def build(self):
        self.box('frame',6,6,42,42,4)
        for i,(sx,sy) in enumerate(((1,1),(-1,1),(1,-1),(-1,-1))):
            def p(x,y):return (24+sx*(x-24),24+sy*(y-24))
            self.add_bezier('dash-'+str(i),p(15,18),(p(15,17),p(17,15),p(18,15)))
        self.cross('plus',24,24,3)

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

# Contract keyshape visible bounds: (4, 4, 44, 44).

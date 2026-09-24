"""smiley decode. Broad mouth cover lowered to enlarge eye band; rounded face, angry eyes and chin retained.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2421c5d7-2ff1-480c-8526-9252cbdd43cf'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smiley decode_2421c5d7-2ff1-480c-8526-9252cbdd43cf.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='angry-face-with-broad-mouth-cover'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smiley decode',)
    def build(self):
        self.add_arc('dome',(6,24),(42,24),radius_x=18)
        self.add_line('left',(6,24),(6,26));self.relate('connect','left','dome')
        self.add_line('right',(42,24),(42,26));self.relate('connect','right','dome')
        self.add_polyline('cover',(6,26),(42,26),(42,34),(36,34),(12,34),(6,34),closed=True)
        for n in ('left','right'):self.relate('connect',n,'cover')
        self.add_arc('chin',(36,34),(12,34),radius_x=12,radius_y=8)
        self.relate('connect','chin','cover')
        self.add_line('eye-left',(19,16),(20,17))
        self.add_line('eye-right',(29,16),(28,17))

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

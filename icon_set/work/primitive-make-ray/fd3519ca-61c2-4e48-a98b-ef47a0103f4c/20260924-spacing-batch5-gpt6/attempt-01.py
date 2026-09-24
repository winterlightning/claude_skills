"""Herbal tea cup with complete leaf, rounded handle and saucer. Widened and deepened bowl; omit short leaf stem to clear bowl wall. Leaf asymmetry and right handle preserve source. No exact useful Lucide match.
Plan: shared dimensions and attachment nodes; exact HRECT_L envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fd3519ca-61c2-4e48-a98b-ef47a0103f4c'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/tea cup herbal_fd3519ca-61c2-4e48-a98b-ef47a0103f4c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tea-cup-herbal'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tea cup herbal',)
    def build(self):
        self.add_polyline('walls',(4,24),(4,8),(32,8),(32,10),(32,22),(32,24))
        self.add_arc('bowl-right',(32,24),(18,40),radius_x=14,radius_y=16)
        self.add_arc('bowl-left',(18,40),(4,24),radius_x=14,radius_y=16)
        self.add_contour('cup',*(f'walls-{i}' for i in range(1,6)),'bowl-right','bowl-left',closed=True)
        self.add_line('handle-top',(32,10),(38,10))
        self.add_arc('handle-round',(38,10),(38,22),radius_x=6)
        self.add_line('handle-bottom',(38,22),(32,22))
        self.add_contour('handle','handle-top','handle-round','handle-bottom');self.relate('connect','cup','handle')
        self.add_polyline('saucer',(4,40),(18,40),(34,40));self.relate('connect','cup','saucer')
        self.add_bezier('leaf-upper',(14,28),((12,21),(16,18),(23,17)))
        self.add_bezier('leaf-lower',(23,17),((24,24),(21,28),(14,28)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)

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

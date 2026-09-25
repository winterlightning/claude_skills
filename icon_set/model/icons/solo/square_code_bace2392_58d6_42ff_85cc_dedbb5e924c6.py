"""Code brackets and slash within a rounded enclosure. Lucide code informs mirrored chevrons. Widened keyshape retains all three code marks with independent gaps.
Plan: shared dimensions and attachment nodes; exact HRECT_L envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bace2392-58d6-42ff-85cc-dedbb5e924c6'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/square code_bace2392-58d6-42ff-85cc-dedbb5e924c6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-code-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('square code',)
    def build(self):
        self.box('frame',4,8,44,40,4)
        self.add_polyline('left',(15,20),(13,24),(15,28))
        self.add_polyline('right',(33,20),(35,24),(33,28))
        self.add_line('slash',(25,18),(23,30))

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

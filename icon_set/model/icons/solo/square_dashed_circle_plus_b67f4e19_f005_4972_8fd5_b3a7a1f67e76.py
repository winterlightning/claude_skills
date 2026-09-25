"""Plus within dashed circular ring and rounded square. Reduce eight dashes to four diagonal arc dashes, reserving 8 units around the central plus. Shared ring radius and mirrored dash endpoints.
Plan: shared dimensions and attachment nodes; exact SQUARE envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b67f4e19-f005-4972-8fd5-b3a7a1f67e76'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/square dashed circle plus_b67f4e19-f005-4972-8fd5-b3a7a1f67e76.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-dashed-circle-plus'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('square dashed circle plus',)
    def build(self):
        self.box('frame')
        for i,(a,b) in enumerate([((16,18),(18,16)),((30,16),(32,18)),((32,30),(30,32)),((18,32),(16,30))]):
            self.add_arc(f'dash-{i}',a,b,radius_x=10)
        self.cross('plus',24,24,2)

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

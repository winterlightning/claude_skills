"""Slashed wireless signal within interrupted circle. Keep diagonal direction; reduce two wireless arcs to one and hollow dot to solid dot. No useful exact Lucide match.
Plan: shared dimensions and attachment nodes; exact CIRCLE envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='945b25be-2ad9-4b54-9548-b41ff357244a'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/signal slash_945b25be-2ad9-4b54-9548-b41ff357244a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='signal-slash'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('signal slash',)
    def build(self):
        self.add_arc('ring-upper',(24,4),(44,24),radius_x=20)
        self.add_arc('ring-lower',(24,44),(4,24),radius_x=20)
        self.add_line('slash',(10,10),(38,38))
        self.add_arc('wave',(28,14),(34,20),radius_x=11)
        self.add_dot('signal-dot',(18,30))

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

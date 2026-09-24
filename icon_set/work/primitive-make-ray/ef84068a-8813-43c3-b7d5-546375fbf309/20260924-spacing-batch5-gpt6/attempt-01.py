"""Folded map alongside four-node learning network. Reduce redundant root-to-node edges to one spanning chain; preserve all four circular nodes and map fold. No useful exact Lucide match.
Plan: shared dimensions and attachment nodes; exact HRECT_L envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ef84068a-8813-43c3-b7d5-546375fbf309'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/start your machine learning journey_ef84068a-8813-43c3-b7d5-546375fbf309.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='start-your-machine-learning-journey'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('start your machine learning journey',)
    def build(self):
        self.add_polyline('map',(4,19),(4,8),(12,12),(20,8),(20,19))
        self.add_line('fold',(12,12),(12,19));self.relate('connect','map','fold')
        self.circle('root',13,35,5)
        self.circle('top',34,11,3)
        self.circle('right',41,24,3)
        self.circle('bottom',34,37,3)
        self.add_line('root-link',(18,35),(31,37));self.relate('connect','root','root-link');self.relate('connect','bottom','root-link')
        self.add_line('upper-link',(34,14),(41,21));self.relate('connect','top','upper-link');self.relate('connect','right','upper-link')
        self.add_line('lower-link',(41,27),(34,34));self.relate('connect','right','lower-link');self.relate('connect','bottom','lower-link')

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

"""start your machine learning journey. Folded map remains above-left of the network. Simplified four-node network to three connected nodes; preserve cyclic learning diagram.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
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
        self.add_polyline('map',(4,24),(4,8),(12,12),(20,8),(20,16))
        self.add_line('fold',(12,12),(12,20));self.relate('connect','map','fold')
        self.circle('root',20,34,6)
        self.circle('upper-node',41,16,3)
        self.circle('lower-node',41,37,3)
        self.add_line('upper-link',(20,28),(38,16))
        self.add_line('lower-link',(26,34),(38,37))
        self.add_line('chain',(41,19),(41,34))
        for link,node in [('upper-link','root'),('upper-link','upper-node'),('lower-link','root'),('lower-link','lower-node'),('chain','upper-node'),('chain','lower-node')]:self.relate('connect',link,node)

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

"""signal slash. Broken outer ring and interrupted wireless signal retain diagonal cancellation; one inner wave omitted for spacing.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='945b25be-2ad9-4b54-9548-b41ff357244a'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/signal slash_945b25be-2ad9-4b54-9548-b41ff357244a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='signal-slash'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('signal slash',)
    def build(self):
        self.add_arc('ring-upper',(24,4),(44,24),radius_x=20)
        self.add_arc('ring-lower',(24,44),(4,24),radius_x=20)
        self.add_line('slash',(10,10),(38,38))
        self.add_arc('wave',(27,14),(34,21),radius_x=10)
        self.add_dot('dot',(16,32))

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

# Contract keyshape visible bounds: (2, 2, 46, 46).

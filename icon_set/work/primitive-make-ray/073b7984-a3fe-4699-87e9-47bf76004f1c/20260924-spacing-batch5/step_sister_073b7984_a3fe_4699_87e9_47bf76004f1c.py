"""step sister. Rebalanced paired hair locks upward to clear badge. Circular face, open hair tufts and shoulder; exact detached head22 to torso30 ink gap4. Fringe and right shoulder omitted.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='073b7984-a3fe-4699-87e9-47bf76004f1c'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/step sister_073b7984-a3fe-4699-87e9-47bf76004f1c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='step-sister'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('step sister',)
    def build(self):
        self.circle('head',20,14,8)
        for n,a,b in [('left',(12,14),(6,22)),('right',(28,14),(34,22))]:
            self.add_line('hair-'+n,a,b);self.relate('connect','head','hair-'+n)
        self.add_arc('torso',(20,30),(6,42),radius_x=14,radius_y=12,sweep=False)
        self.add_line('base',(6,42),(20,42));self.relate('connect','base','torso')
        self.circle('badge',36,36,6)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

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

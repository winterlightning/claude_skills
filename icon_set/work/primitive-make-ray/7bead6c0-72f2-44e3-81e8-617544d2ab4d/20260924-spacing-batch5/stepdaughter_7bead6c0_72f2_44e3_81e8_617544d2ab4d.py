"""stepdaughter. Longer downturned hair locks distinguish girl silhouette; fringe and crowded right shoulder omitted. Circular face22 to torso30 gives exact4 ink gap; badge retained.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7bead6c0-72f2-44e3-81e8-617544d2ab4d'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/stepdaughter_7bead6c0-72f2-44e3-81e8-617544d2ab4d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stepdaughter'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('stepdaughter',)
    def build(self):
        self.circle('head',20,14,8)
        for n,a,b in [('left',(12,14),(8,23)),('right',(28,14),(32,22))]:
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

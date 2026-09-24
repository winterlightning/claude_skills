"""shoemaker. Half shoulder silhouette and apron beside foreground shoe; omit crowded right shoulder. Head bottom 18 to torso 26 gives exact 4 ink gap.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4a1b8b06-db68-40b2-adfe-7ecac75aaa72'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shoemaker_4a1b8b06-db68-40b2-adfe-7ecac75aaa72.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='shoemaker'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('shoemaker',)
    def build(self):
        self.circle('head',16,12,6)
        self.add_arc('torso',(16,26),(6,36),radius_x=10,sweep=False)
        self.add_line('side',(6,36),(6,42));self.relate('connect','side','torso')
        self.add_line('apron',(16,26),(16,42));self.relate('connect','apron','torso')
        self.add_polyline('shoe',(24,30),(32,34),(42,34),(42,42),(24,42),closed=True)
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

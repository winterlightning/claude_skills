"""Girl with long hair and circular relationship badge. Shared human user.svg circular head and open shoulder proportions; exact detached gap22 to30. Omit tiny hair part, neckline and body baseline. Asymmetric shoulders make room for badge. Source differs in minor neckline only; reduced drawings coincide.
Plan: shared dimensions and attachment nodes; exact SQUARE envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7bead6c0-72f2-44e3-81e8-617544d2ab4d'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/stepdaughter_7bead6c0-72f2-44e3-81e8-617544d2ab4d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stepdaughter'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('stepdaughter',)
    def build(self):
        self.circle('head',16,14,8)
        self.add_arc('torso',(16,30),(6,42),radius_x=10,radius_y=12,sweep=False)
        self.add_bezier('right-shoulder',(16,30),((18,30),(20,30),(22,32)));self.relate('connect','torso','right-shoulder')
        self.circle('badge',36,36,6)
        self.add_line('hair-left',(8,14),(8,23));self.relate('connect','hair-left','head')
        self.add_line('hair-right',(24,14),(24,23));self.relate('connect','hair-right','head')
        self.mark_human_figure('girl',head='head',torso='torso',torso_junction='start')

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

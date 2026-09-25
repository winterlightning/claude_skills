"""User bust within rounded square. Shared human user.svg informs open shoulders and circular head. Head bottom21 and torso top29 give exact 4-unit ink gap. Omit body baseline to avoid shallow enclosed hole.
Plan: shared dimensions and attachment nodes; exact SQUARE envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='55360bd5-b0c0-48c8-b255-4f7c05d395d6'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/square user_55360bd5-b0c0-48c8-b255-4f7c05d395d6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-user'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('square user',)
    def build(self):
        self.box('frame')
        self.circle('head',24,18,3)
        self.add_arc('shoulder-left',(16,33),(24,29),radius_x=8,radius_y=4)
        self.add_arc('torso',(24,29),(32,33),radius_x=8,radius_y=4)
        self.add_contour('body','shoulder-left','torso')
        self.mark_human_figure('user',head='head',torso='torso',torso_junction='start')

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

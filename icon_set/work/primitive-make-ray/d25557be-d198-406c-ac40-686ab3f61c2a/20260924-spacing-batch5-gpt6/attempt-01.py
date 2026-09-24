"""Sparkle-eyed face with deliberately uneven smile. Closed tiny sparkle eyes become open four-ray sparkles, keeping their identity without pinched holes. No useful exact Lucide match.
Plan: shared dimensions and attachment nodes; exact CIRCLE envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d25557be-d198-406c-ac40-686ab3f61c2a'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smiley bright_d25557be-d198-406c-ac40-686ab3f61c2a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smiley-bright'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smiley bright',)
    def build(self):
        self.circle('face',24,24,20)
        for x in (18,30):self.cross(f'sparkle-{x}',x,19,2)
        self.add_bezier('smile',(17,31),((24,33),(31,33),(31,30)))

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

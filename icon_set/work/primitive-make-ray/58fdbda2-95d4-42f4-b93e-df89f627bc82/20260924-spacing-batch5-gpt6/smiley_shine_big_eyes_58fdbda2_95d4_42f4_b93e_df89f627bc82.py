"""Sparkle-eyed smiling face with symmetric broad smile. Open four-ray eyes replace tiny pinched closed sparkles. No useful exact Lucide match.
Plan: shared dimensions and attachment nodes; exact CIRCLE envelope."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='58fdbda2-95d4-42f4-b93e-df89f627bc82'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smiley shine big eyes_58fdbda2-95d4-42f4-b93e-df89f627bc82.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smiley-shine-big-eyes'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smiley shine big eyes',)
    def build(self):
        self.circle('face',24,24,20)
        for x in (18,30):self.cross(f'sparkle-{x}',x,19,2)
        self.add_bezier('smile',(16,30),((20,35),(28,35),(32,30)))

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

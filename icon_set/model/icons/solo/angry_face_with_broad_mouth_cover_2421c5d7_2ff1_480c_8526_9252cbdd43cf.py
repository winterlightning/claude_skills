"""Angry face and broad mouth cover. Lower chin arc omitted to give the cover a full-height clear opening. Circular upper face and symmetric angry eyes. No useful exact Lucide match.
Plan: shared dimensions and attachment nodes; exact SQUARE envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2421c5d7-2ff1-480c-8526-9252cbdd43cf'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smiley decode_2421c5d7-2ff1-480c-8526-9252cbdd43cf.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='angry-face-with-broad-mouth-cover'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smiley decode',)
    def build(self):
        self.add_arc('dome',(6,24),(42,24),radius_x=18)
        self.add_line('right-neck',(42,24),(42,26))
        self.add_line('right',(42,26),(42,38))
        self.add_arc('bottom-right',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bottom-left',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,26))
        self.add_line('left-neck',(6,26),(6,24))
        self.add_contour('outline','dome','right-neck','right','bottom-right','bottom','bottom-left','left','left-neck',closed=True)
        self.add_line('cover-top',(6,26),(42,26));self.relate('connect','outline','cover-top')
        self.add_line('eye-left',(19,16),(20,17))
        self.add_line('eye-right',(29,16),(28,17))

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

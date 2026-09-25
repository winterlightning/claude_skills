"""A lightning bolt with three motion rays.
Plan: SQUARE leaves room for the large bolt and left-hand rays.
Reduction: No defining part omitted; lower bolt valley widened.
Construction: Source bolt; no exact useful Lucide motion-bolt match.
Layout: Directional bolt and rays preserve reference asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c67c9f34-aa4a-4561-aba3-e1d5e5f4f809'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/spasm_c67c9f34-aa4a-4561-aba3-e1d5e5f4f809.svg'
AUTHOR = "gpt-6"
# Plan: Large angular spasm bolt with three short motion rays on its left.
# References: No useful exact local Lucide match; coherent polygon and detached motion strokes.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'spasm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('spasm',)

    def build(self):
        self.add_polyline('bolt',(26,6),(38,6),(30,20),(42,20),(20,42),(27,28),(16,28),closed=True)
        for n,a,b in [('upper',(6,16),(8,18)),('middle',(6,26),(8,26)),('lower',(6,36),(8,34))]:self.add_line(n,a,b)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

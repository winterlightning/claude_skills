from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50f8b937-c3ef-4dbe-b3bb-69d8a2f54940'
SOURCE_PATH = 'icon_set/work/todo-references/rune stone_50f8b937-c3ef-4dbe-b3bb-69d8a2f54940.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded standing stone containing a vertical angular rune with a triangular upper branch.
# Reference: No exact local Lucide match; coherent curved stone outline and joined rune strokes.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'rune-stone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rune', 'stone')

    def build(self):
        self.add_bezier('stone',(12,44),((8,44),(8,42),(8,38)),((9,27),(9,18),(12,12)),((15,4),(21,4),(24,4)),((32,4),(37,10),(38,18)),((39,27),(40,36),(40,40)),((40,44),(36,44),(32,44)),((25,44),(18,44),(12,44)))
        self.add_polyline('rune',(19,34),(19,16),(29,22),(19,28),(29,35))

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

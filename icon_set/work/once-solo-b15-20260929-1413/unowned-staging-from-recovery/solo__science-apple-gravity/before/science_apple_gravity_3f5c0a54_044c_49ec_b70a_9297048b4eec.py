from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f5c0a54-044c-49ec-b70a-9297048b4eec'
SOURCE_PATH = 'icon_set/work/todo-references/science apple gravity_3f5c0a54-044c-49ec-b70a-9297048b4eec.svg'
AUTHOR = 'gpt-6'
# Plan: Apple with a short curved stem and three downward gravity arrows.
# Reference: apple: mirrored lobes, full shoulders and indented base; arrow construction.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'science-apple-gravity'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('science', 'apple', 'gravity')

    def build(self):
        self.add_bezier('apple',(24,13),((13,6),(8,13),(10,19)),((12,25),(19,25),(24,23)),((29,25),(36,25),(38,19)),((40,13),(35,6),(24,13)))
        self.add_bezier('stem',(24,13),((24,9),(26,6),(29,6)));self.relate('connect','stem','apple')
        for n,x,y in [('left',9,40),('center',24,42),('right',39,40)]:
            self.add_line(n+'-shaft',(x,y-8),(x,y));self.add_polyline(n+'-head',(x-3,y-3),(x,y),(x+3,y-3));self.relate('connect',n+'-shaft',n+'-head')

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

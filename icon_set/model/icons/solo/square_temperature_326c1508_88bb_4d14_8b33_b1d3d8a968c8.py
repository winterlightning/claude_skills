from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '326c1508-88bb-4d14-8b33-b1d3d8a968c8'
SOURCE_PATH = 'icon_set/work/todo-references/square temperature_326c1508-88bb-4d14-8b33-b1d3d8a968c8.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square enclosing a degree mark and the letter C.
# References: No exact local Lucide typography match; circular C arc and degree dot.
# Reduction: Reconstructed the tiny source degree mark as a degree dot.

class AuthoredIcon(Solo48):
    icon_id = 'square-temperature'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("combination", "other", "primitives-generate")
    aliases = ()
    keywords = ('square', 'temperature')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_dot('degree',(15,15))
        self.add_bezier('c',(33,18),((28,13),(21,16),(21,25)),((21,34),(28,35),(33,31)))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

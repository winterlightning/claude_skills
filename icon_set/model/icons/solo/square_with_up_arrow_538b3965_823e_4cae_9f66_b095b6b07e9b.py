from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '538b3965-823e-4cae-9f66-b095b6b07e9b'
SOURCE_PATH = 'icon_set/work/todo-references/square with up arrow_538b3965-823e-4cae-9f66-b095b6b07e9b.svg'
AUTHOR = 'gpt-6'
# Plan: Upward arrow emerging through the open top of a squared enclosure.
# References: square-arrow-up: coherent arrow shaft and head; open frame follows source.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-with-up-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('square', 'with', 'up', 'arrow')

    def build(self):
        self.add_polyline('frame',(14,20),(6,20),(6,42),(42,42),(42,20),(34,20))
        self.add_line('shaft',(24,30),(24,6));self.add_polyline('head',(18,12),(24,6),(30,12));self.relate('connect','shaft','head')

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

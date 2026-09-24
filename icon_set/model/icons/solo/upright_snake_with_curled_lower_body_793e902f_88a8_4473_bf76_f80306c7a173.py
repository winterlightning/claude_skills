from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='793e902f-88a8-4473-bf76-f80306c7a173'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/snake_793e902f-88a8-4473-bf76-f80306c7a173.svg'
AUTHOR='gpt-6'
PLAN='Repair4 widens neck from both edges and raises coil crest to increase body thickness; retain full snake outline and exact SQUARE extrema.'
class Drawing(Solo48):
    icon_id='upright-snake-with-curled-lower-body'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

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

    def build(self):
        self.add_bezier('snake',(6,14),((6,8),(10,6),(14,6)),((22,6),(24,10),(24,16)),((24,22),(16,25),(16,30)),((16,34),(20,32),(24,31)),((28,27),(30,23),(34,23)),((40,23),(42,29),(42,34)),((42,40),(38,42),(32,42)),((34,40),(36,37),(34,36)),((30,34),(27,42),(16,42)),((6,42),(6,37),(6,32)),((6,25),(12,20),(12,16)),((12,14),(10,14),(6,14)))
        self.add_contour('outline','snake',closed=True)

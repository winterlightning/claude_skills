from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='793e902f-88a8-4473-bf76-f80306c7a173'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/snake_793e902f-88a8-4473-bf76-f80306c7a173.svg'
AUTHOR='gpt-6'
PLAN='Outlined upright snake with raised rounded head and lower right curl. Widened head and neck and opened lower coil; SQUARE target6,6–42,42. Deliberate asymmetry follows source; no exact useful Lucide match.'
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
        self.add_bezier('snake',(6,14),((6,8),(10,6),(16,6)),((24,6),(28,10),(28,16)),((28,24),(14,29),(14,34)),((14,41),(22,34),(25,30)),((30,23),(35,22),(39,26)),((45,32),(42,40),(32,42)),((35,37),(37,34),(34,32)),((31,30),(28,38),(23,40)),((12,46),(6,40),(6,34)),((6,27),(18,20),(18,16)),((18,14),(12,14),(6,14)))
        self.add_contour('outline','snake',closed=True)

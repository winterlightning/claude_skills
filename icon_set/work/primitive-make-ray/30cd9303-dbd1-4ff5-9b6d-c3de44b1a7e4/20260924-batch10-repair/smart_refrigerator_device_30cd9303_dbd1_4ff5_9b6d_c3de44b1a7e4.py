from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='30cd9303-dbd1-4ff5-9b6d-c3de44b1a7e4'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smart refrigerator device_30cd9303-dbd1-4ff5-9b6d-c3de44b1a7e4.svg'
AUTHOR='gpt-6'
PLAN='Fridge behind smartphone and wireless arc. SQUARE6,6–42,42. Lucide refrigerator door division and wifi arch inform construction; handles reduced to dots, phone footer and inner radio arc omitted.'
class Drawing(Solo48):
    icon_id='smart-refrigerator-device'
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
        self.add_polyline('fridge',(18,42),(6,42),(6,24),(6,6),(23,6),(23,12))
        self.add_line('freezer-seam',(6,24),(18,24));self.relate('connect','freezer-seam','fridge')
        for i,y in enumerate((15,33)):self.add_dot(f'handle-{i}',(15,y))
        self.add_arc('wireless',(32,16),(42,6),radius_x=10)
        self.box('phone',27,25,42,42,3)

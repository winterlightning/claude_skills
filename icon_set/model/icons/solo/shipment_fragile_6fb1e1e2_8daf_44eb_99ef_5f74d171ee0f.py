from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6fb1e1e2-8daf-44eb-99ef-5f74d171ee0f'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shipment fragile_6fb1e1e2-8daf-44eb-99ef-5f74d171ee0f.svg'
AUTHOR='gpt-6'
PLAN='Fragile parcel with glass, shared axis24 radius8; omit packing ribbon and redundant arrow for spacing. SQUARE6,6–42,42.'
class Drawing(Solo48):
    icon_id='shipment-fragile'
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
        self.add_polyline('box',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('bowl-left',(16,18),(16,15))
        self.add_line('bowl-rim',(16,15),(32,15))
        self.add_line('bowl-right',(32,15),(32,18))
        self.add_arc('bowl-lower-right',(32,18),(24,26),radius_x=8)
        self.add_arc('bowl-lower-left',(24,26),(16,18),radius_x=8)
        self.add_contour('glass','bowl-left','bowl-rim','bowl-right','bowl-lower-right','bowl-lower-left',closed=True)
        self.add_line('stem',(24,26),(24,34));self.relate('connect','stem','glass')
        self.add_polyline('foot',(18,34),(24,34),(30,34));self.relate('connect','stem','foot')

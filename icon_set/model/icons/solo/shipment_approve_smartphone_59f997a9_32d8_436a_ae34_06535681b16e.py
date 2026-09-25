from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='59f997a9-32d8-436a-ae34-06535681b16e'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shipment approve smartphone_59f997a9-32d8-436a-ae34-06535681b16e.svg'
AUTHOR='gpt-6'
PLAN='Large parcel behind overlapping approval phone. Front-on carton replaces tiny perspective seams; hidden edges genuinely terminate at phone. SQUARE6,6–42,42. Phone footer omitted; preserve check and overlapping composition.'
class Drawing(Solo48):
    icon_id='shipment-approve-smartphone'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
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
        self.add_polyline('parcel',(30,18),(30,6),(6,6),(6,30),(18,30))
        self.add_polyline('phone',(18,18),(30,18),(42,18),(42,42),(18,42),(18,30),closed=True)
        self.relate('connect','parcel','phone')
        self.add_polyline('check',(27,28),(30,31),(33,27))

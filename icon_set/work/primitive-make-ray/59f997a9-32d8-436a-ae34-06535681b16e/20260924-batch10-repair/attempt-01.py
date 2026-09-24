from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='59f997a9-32d8-436a-ae34-06535681b16e'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/shipment approve smartphone_59f997a9-32d8-436a-ae34-06535681b16e.svg'
AUTHOR='gpt-6'
PLAN='Parcel behind approval phone, perspective reduced to a clear parcel rectangle; tiny phone footer and cube seams omitted. HRECT_L4,8–44,40 separates objects. Lucide package enclosure principles.'
class Drawing(Solo48):
    icon_id='shipment-approve-smartphone'
    keyshape=Keyshape.HRECT_L
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
        self.add_polyline('parcel',(4,8),(16,8),(16,32),(4,32),closed=True)
        self.box('phone',24,16,44,40,3)
        self.add_polyline('check',(32,26),(34,28),(36,24))

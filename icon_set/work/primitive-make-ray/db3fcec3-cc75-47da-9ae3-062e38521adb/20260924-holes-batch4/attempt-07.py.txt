from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'db3fcec3-cc75-47da-9ae3-062e38521adb'
SOURCE_PATH = 'pictographic-primitives/other/smartwatch circle_db3fcec3-cc75-47da-9ae3-062e38521adb.svg'
AUTHOR = 'gpt-6'
# Plan: Circular smartwatch face with paired upper and lower strap loops.
# References: watch: dominant circular face with symmetric strap attachments.
# Reduction: No parts omitted; source has an empty watch face.

class AuthoredIcon(Solo48):
    icon_id = 'smartwatch-circle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('smartwatch', 'circle')

    def build(self):
        # A near-circular face with tangent-continuous mirrored cubic shoulders.
        # The rounded straps attach at actual shared face nodes.
        self.add_bezier('face-top',(10,24),((10,20),(12,16),(16,14)),((20,12),(28,12),(32,14)),((36,16),(38,20),(38,24)))
        self.add_bezier('face-bottom',(38,24),((38,28),(36,32),(32,34)),((28,36),(20,36),(16,34)),((12,32),(10,28),(10,24)))
        self.add_contour('face','face-top','face-bottom',closed=True)
        for n,pts in [('upper',((16,14),(16,4),(32,4),(32,14))),('lower',((16,34),(16,44),(32,44),(32,34)))]:
            self.add_polyline(n,*pts)
            self.relate('connect',n,'face')

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

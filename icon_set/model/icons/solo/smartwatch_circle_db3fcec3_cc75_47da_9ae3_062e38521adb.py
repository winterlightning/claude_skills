from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db3fcec3-cc75-47da-9ae3-062e38521adb'
SOURCE_PATH = 'pictographic-primitives/other/smartwatch circle_db3fcec3-cc75-47da-9ae3-062e38521adb.svg'
AUTHOR = 'gpt-6'
# Plan: Circular smartwatch face with paired upper and lower strap loops.
# References: watch: dominant circular face with symmetric strap attachments.
# Reduction: No parts omitted; source has an empty watch face.

class AuthoredIcon(Solo48):
    icon_id = 'smartwatch-circle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('smartwatch', 'circle')

    def build(self):
        # Rounded watch face and symmetric straps; broad upper/lower openings.
        self.add_bezier('face',(12,16),((16,11),(32,11),(36,16)),((39,19),(40,21),(40,24)),((40,27),(39,29),(36,32)),((32,37),(16,37),(12,32)),((9,29),(8,27),(8,24)),((8,21),(9,19),(12,16)))
        self.add_contour('face-outline','face',closed=True)
        for n,pts in [('upper',((12,16),(12,4),(36,4),(36,16))),('lower',((12,32),(12,44),(36,44),(36,32)))]:
            self.add_polyline(n,*pts)
            self.relate('connect',n,'face-outline')

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

# Final repair review: Paired straps around a broad, rounded face; symmetric attachments.
# VRECT_L keeps full strap height while widening the face.
# Changes: Face made wider and shallower to enlarge both strap openings; no parts omitted.
# validate_icon: valid; build gate: pass with zero errors and zero warnings.

"""A smartwatch pound symbol reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f2d45871-ff3d-44d5-84a8-774df3bd6ba3'
SOURCE_PATH = 'pictographic-primitives/other/smart watch circle pound sign_f2d45871-ff3d-44d5-84a8-774df3bd6ba3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartwatch-pound-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartwatch', 'pound', 'symbol')

    def rounded(self, name, left, top, right, bottom, radius=4):
        p = [(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(left+radius,bottom),
             (left,bottom-radius),(left,top+radius),(left+radius,top)]
        ids=[]
        for j,(a,b) in enumerate(zip(p,p[1:]),1):
            elem=f"{name}-{j}"
            if j%2: self.add_line(elem,a,b)
            else: self.add_arc(elem,a,b,radius_x=radius)
            ids.append(elem)
        self.add_contour(name,*ids,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def build(self) -> None:
        # Merge face and straps at the top/bottom; no narrow enclosed strap seams.
        self.add_bezier('face-left',(16,10),((11,12),(8,17),(8,24)),((8,31),(11,36),(16,38)))
        self.add_bezier('face-right',(32,38),((37,36),(40,31),(40,24)),((40,17),(37,12),(32,10)))
        self.add_polyline('upper-band',(32,10),(31,4),(17,4),(16,10))
        self.add_polyline('lower-band',(16,38),(17,44),(31,44),(32,38))
        self.relate('connect','face-left','upper-band');self.relate('connect','face-right','upper-band')
        self.relate('connect','face-left','lower-band');self.relate('connect','face-right','lower-band')
        self.add_bezier('pound-bow',(28,19),((27,15),(21,15),(21,20)))
        self.add_polyline('pound-stem',(21,20),(21,23),(21,31))
        self.add_polyline('pound-bar',(17,23),(21,23))
        self.add_polyline('pound-base',(20,31),(21,31),(28,31))
        self.relate('connect','pound-bow','pound-stem')
        self.relate('connect','pound-stem','pound-bar');self.relate('connect','pound-stem','pound-base')

"""A euro payment smartwatch reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '73571a2b-4ed5-4ead-96e1-495841cb43da'
SOURCE_PATH = 'pictographic-primitives/other/smart watch circle euro sign_73571a2b-4ed5-4ead-96e1-495841cb43da.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'euro-payment-smartwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('euro', 'payment', 'smartwatch')

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

        # Six smooth face curves share the band attachment points.
        curves = [
            ((8,24),(8,17),(11,12),(16,10)),
            ((16,10),(20,7),(28,7),(32,10)),
            ((32,10),(37,12),(40,17),(40,24)),
            ((40,24),(40,31),(37,36),(32,38)),
            ((32,38),(28,41),(20,41),(16,38)),
            ((16,38),(11,36),(8,31),(8,24)),
        ]
        for j,(a,c1,c2,b) in enumerate(curves,1):
            self.add_bezier(f"face-{j}",a,(c1,c2,b))
        self.add_contour('face',*(f"face-{j}" for j in range(1,7)),closed=True)
        self.add_polyline('upper-band',(16,10),(17,4),(31,4),(32,10))
        self.add_polyline('lower-band',(16,38),(17,44),(31,44),(32,38))
        self.relate('connect','face','upper-band')
        self.relate('connect','face','lower-band')

        self.add_bezier('euro-outline',(29,18),((21,16),(18,20),(18,24)),
                        ((18,28),(22,32),(29,30)))
        self.add_line('euro-bar',(17,24),(28,24))
        self.relate('connect','euro-outline','euro-bar')


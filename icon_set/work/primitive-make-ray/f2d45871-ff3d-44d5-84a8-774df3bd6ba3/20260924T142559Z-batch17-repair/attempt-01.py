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
        self.add_line('upper-left',(16,10),(17,4))
        self.add_line('upper-right',(32,10),(31,4))
        self.add_line('lower-left',(16,38),(17,44))
        self.add_line('lower-right',(32,38),(31,44))
        for n in ['upper-left','upper-right','lower-left','lower-right']:self.relate('connect','face',n)

        self.add_arc('pound-hook',(29,21),(21,21),radius_x=4,sweep=False)
        self.add_polyline('pound-stem',(21,21),(21,24),(21,30))
        self.add_polyline('pound-bar',(18,24),(21,24),(25,24))
        self.add_polyline('pound-base',(18,30),(21,30),(28,30))
        self.relate('connect','pound-hook','pound-stem');self.relate('connect','pound-stem','pound-bar');self.relate('connect','pound-stem','pound-base')

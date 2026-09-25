"""A smartwatch dollar sign reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b9fab53-d945-4f18-86b9-fcc5bd5840ce'
SOURCE_PATH = 'pictographic-primitives/combination/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'smartwatch-dollar-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartwatch', 'dollar', 'sign')

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
        # Face and symmetric straps have deeper negative spaces above and below the dial.
        curves=[((10,24),(10,19),(12,16),(16,14)),((16,14),(20,11),(28,11),(32,14)),((32,14),(36,16),(38,19),(38,24)),((38,24),(38,29),(36,32),(32,34)),((32,34),(28,37),(20,37),(16,34)),((16,34),(12,32),(10,29),(10,24))]
        for j,(a,c1,c2,b) in enumerate(curves):self.add_bezier(f'face-{j}',a,(c1,c2,b))
        self.add_contour('face',*(f'face-{j}' for j in range(6)),closed=True)
        for name,y,end in [('upper-band',14,4),('lower-band',34,44)]:
            self.add_polyline(name,(16,y),(16,end),(32,end),(32,y));self.relate('connect','face',name)
        self.add_bezier('dollar-upper',(28,19),((20,16),(18,22),(24,24)))
        self.add_bezier('dollar-lower',(24,24),((30,26),(28,32),(20,29)))
        self.add_contour('dollar','dollar-upper','dollar-lower')
        self.add_line('tick-top',(24,16),(24,18));self.add_line('tick-bottom',(24,30),(24,32))
        self.relate('connect','dollar','tick-top');self.relate('connect','dollar','tick-bottom')


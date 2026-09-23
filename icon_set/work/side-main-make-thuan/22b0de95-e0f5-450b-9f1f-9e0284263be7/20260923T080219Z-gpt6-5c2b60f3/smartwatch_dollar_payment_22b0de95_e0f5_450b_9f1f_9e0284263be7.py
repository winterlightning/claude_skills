"""A smartwatch dollar payment reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '22b0de95-e0f5-450b-9f1f-9e0284263be7'
SOURCE_PATH = 'pictographic-primitives/other/smart watch square dollar sign_22b0de95-e0f5-450b-9f1f-9e0284263be7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartwatch-dollar-payment'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartwatch', 'dollar', 'payment')

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

        self.rounded('case',10,10,38,38,4)
        self.add_polyline('upper-band',(16,10),(17,4),(31,4),(32,10))
        self.add_polyline('lower-band',(16,38),(17,44),(31,44),(32,38))
        self.relate('connect','case','upper-band')
        self.relate('connect','case','lower-band')

        self.add_bezier('dollar-upper',(27,19),((20,17),(19,22),(24,24)))
        self.add_bezier('dollar-lower',(24,24),((30,26),(28,30),(21,29)))
        self.add_line('dollar-stem',(24,18),(24,31))
        self.relate('connect','dollar-upper','dollar-lower')
        self.relate('connect','dollar-upper','dollar-stem')
        self.relate('connect','dollar-lower','dollar-stem')


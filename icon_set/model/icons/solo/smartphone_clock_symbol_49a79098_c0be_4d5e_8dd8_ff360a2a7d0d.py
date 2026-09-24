"""A smartphone clock symbol reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49a79098-c0be-4d5e-8dd8-ff360a2a7d0d'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone clock_49a79098-c0be-4d5e-8dd8-ff360a2a7d0d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartphone-clock-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartphone', 'clock', 'symbol')

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

        self.rounded('phone',10,4,38,44,4)
        self.add_line('bottom-separator',(10,36),(38,36))
        self.relate('connect','phone','bottom-separator')

        self.add_polyline('clock-hands',(23,17),(23,25),(29,25))


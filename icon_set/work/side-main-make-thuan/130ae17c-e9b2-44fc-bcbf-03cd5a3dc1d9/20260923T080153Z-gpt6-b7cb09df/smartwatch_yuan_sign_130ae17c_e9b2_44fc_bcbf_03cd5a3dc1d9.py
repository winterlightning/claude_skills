"""A smartwatch yuan sign reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '130ae17c-e9b2-44fc-bcbf-03cd5a3dc1d9'
SOURCE_PATH = 'pictographic-primitives/combination/smart watch square yuan sign_130ae17c-e9b2-44fc-bcbf-03cd5a3dc1d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartwatch-yuan-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartwatch', 'yuan', 'sign')

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

        self.add_polyline('yuan-forks',(19,18),(24,25),(29,18))
        self.add_line('yuan-bar',(20,25),(28,25))
        self.add_line('yuan-stem',(24,25),(24,31))
        self.relate('connect','yuan-forks','yuan-bar')
        self.relate('connect','yuan-forks','yuan-stem')
        self.relate('connect','yuan-bar','yuan-stem')


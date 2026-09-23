"""A smartwatch with pound symbol reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2c0ac7cd-8681-4e21-803e-6437b35eb4a2'
SOURCE_PATH = 'pictographic-primitives/other/smart watch square pound sign_2c0ac7cd-8681-4e21-803e-6437b35eb4a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartwatch-with-pound-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartwatch', 'with', 'pound', 'symbol')

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

        self.add_bezier('pound-bow',(28,19),((21,16),(19,20),(21,24)))
        self.add_line('pound-descender',(21,24),(21,30))
        self.add_line('pound-bar',(19,24),(28,24))
        self.add_line('pound-base',(18,31),(30,31))
        self.relate('connect','pound-bow','pound-descender')
        self.relate('connect','pound-descender','pound-bar')


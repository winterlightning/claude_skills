"""A smartphone check mark reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94d3c6cc-58a9-4369-a2d0-f4c8bcd61cc3'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone check_94d3c6cc-58a9-4369-a2d0-f4c8bcd61cc3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartphone-check-mark'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartphone', 'check', 'mark')

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

        self.add_polyline('check',(19,23),(22,28),(29,18))


"""A digital product barcode symbol reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1b86c327-4937-4a5b-b8e0-6124c33765a0'
SOURCE_PATH = 'pictographic-primitives/other/rectangle vertical lines_1b86c327-4937-4a5b-b8e0-6124c33765a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'digital-product-barcode-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/commerce'
    aliases = ()
    keywords = ('digital', 'product', 'barcode', 'symbol')

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

        self.rounded('label',4,8,44,40,4)
        for j,x in enumerate((13,24,35),1):
            self.add_line(f'barcode-{j}',(x,18),(x,30))


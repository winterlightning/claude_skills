"""A smartwatch dollar sign reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b9fab53-d945-4f18-86b9-fcc5bd5840ce'
SOURCE_PATH = 'pictographic-primitives/combination/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'smartwatch-dollar-sign'
    keyshape = Keyshape.VRECT_L
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
        # Round dial owns four strap endpoints. Omit the nonessential transverse end seams
        # rather than close the strap openings into tiny counters.
        curves=[((8,24),(8,17),(11,12),(16,10)),((16,10),(20,7),(28,7),(32,10)),((32,10),(37,12),(40,17),(40,24)),((40,24),(40,31),(37,36),(32,38)),((32,38),(28,41),(20,41),(16,38)),((16,38),(11,36),(8,31),(8,24))]
        for j,(a,c1,c2,b) in enumerate(curves):self.add_bezier(f'face-{j}',a,(c1,c2,b))
        self.add_contour('face',*(f'face-{j}' for j in range(6)),closed=True)
        for side,x in [('left',16),('right',32)]:
            for name,y,end in [('upper',10,4),('lower',38,44)]:
                n=f'{name}-strap-{side}';self.add_line(n,(x,y),(x,end));self.relate('connect','face',n)
        self.add_bezier('dollar-top',(24,18),((16,18),(16,24),(24,24)))
        self.add_bezier('dollar-bottom',(24,24),((32,24),(32,30),(24,30)))
        self.add_contour('dollar','dollar-top','dollar-bottom')
        self.add_line('tick-top',(24,16),(24,18));self.add_line('tick-bottom',(24,30),(24,32))
        self.relate('connect','dollar','tick-top');self.relate('connect','dollar','tick-bottom')


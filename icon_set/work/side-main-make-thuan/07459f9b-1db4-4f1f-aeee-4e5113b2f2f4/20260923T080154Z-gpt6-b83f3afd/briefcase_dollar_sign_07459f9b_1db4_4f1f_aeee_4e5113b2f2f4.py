"""A briefcase dollar sign reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '07459f9b-1db4-4f1f-aeee-4e5113b2f2f4'
SOURCE_PATH = 'pictographic-primitives/other/briefcase dollar_07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'briefcase-dollar-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/bag'
    aliases = ()
    keywords = ('briefcase', 'dollar', 'sign')

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

        self.rounded('case',4,14,44,40,4)
        self.add_polyline('handle',(17,14),(17,8),(31,8),(31,14))
        self.relate('connect','case','handle')

        self.add_bezier('dollar-upper',(27,19),((20,17),(19,22),(24,24)))
        self.add_bezier('dollar-lower',(24,24),((30,26),(28,30),(21,29)))
        self.add_line('dollar-stem',(24,18),(24,31))
        self.relate('connect','dollar-upper','dollar-lower')
        self.relate('connect','dollar-upper','dollar-stem')
        self.relate('connect','dollar-lower','dollar-stem')


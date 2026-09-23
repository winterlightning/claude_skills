"""A escalator transport railing reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '82d1bc9a-4a6d-4782-88a6-dc554653bd7d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/escalator_82d1bc9a-4a6d-4782-88a6-dc554653bd7d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'escalator-transport-railing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transport'
    aliases = ()
    keywords = ('escalator', 'transport', 'railing')

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

        self.add_polyline('rail',(4,34),(9,34),(31,12),(38,8),(42,8),
                          (44,11),(44,16),(40,20),(35,20),(15,40),
                          (9,40),(4,38),closed=True)


"""A smart home power button reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '95e78717-28bd-4a88-951a-54d6ae9c18e6'
SOURCE_PATH = 'pictographic-primitives/other/house power_95e78717-28bd-4a88-951a-54d6ae9c18e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smart-home-power-button'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/building'
    aliases = ()
    keywords = ('smart', 'home', 'power', 'button')

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

        self.add_polyline('house',(6,22),(24,6),(42,22),(42,42),(6,42),closed=True)
        self.add_bezier('power-ring',(16,27),((14,31),(19,33),(24,33)),
                         ((29,33),(34,31),(32,27)))
        self.add_line('power-stem',(24,17),(24,22))


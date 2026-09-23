"""A secure home padlock reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a7f1734e-4fae-4c0a-9d33-80bf4a3da78f'
SOURCE_PATH = 'pictographic-primitives/other/house lock_a7f1734e-4fae-4c0a-9d33-80bf4a3da78f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'secure-home-padlock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/building'
    aliases = ()
    keywords = ('secure', 'home', 'padlock')

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
        self.rounded('lock-body',17,27,31,37,3)
        self.add_arc('shackle',(19,27),(29,27),radius_x=5,large_arc=False)
        self.relate('connect','lock-body','shackle')


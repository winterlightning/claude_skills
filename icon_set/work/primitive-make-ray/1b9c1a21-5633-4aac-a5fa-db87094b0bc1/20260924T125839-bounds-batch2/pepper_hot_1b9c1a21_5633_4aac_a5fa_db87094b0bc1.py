"""pepper hot.
Curved tapered chili, upright stem and separate flame retain the heat concept.
Square extrema are explicit endpoints; asymmetry follows the chili.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1b9c1a21-5633-4aac-a5fa-db87094b0bc1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pepper hot_1b9c1a21-5633-4aac-a5fa-db87094b0bc1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A hot chili pepper beside a flame.
    Plan: Asymmetric tapered pepper with a short stem; detached flame silhouette on the left.
    Reference: No useful Lucide pepper match; smooth arc silhouette and asymmetry preserve the source.
    """
    icon_id = 'pepper-hot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pepper', 'hot')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rounded(self,n,l,t,r,b,k=4):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        members=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];name=f'{n}-{i}';members.append(name)
            if i%2:self.add_arc(name,p,q,radius_x=k)
            else:self.add_line(name,p,q)
        self.add_contour(n,*members,closed=True)

    def dollar(self):
        self.add_line('s-top',(29,16),(24,16))
        self.add_arc('s-left',(24,16),(24,24),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,24),(24,32),radius_x=4)
        self.add_line('s-bottom',(24,32),(19,32))
        self.add_contour('dollar','s-top','s-left','s-right','s-bottom')
        self.add_line('stem-top',(24,12),(24,16));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,32),(24,36));self.relate('connect','stem-bottom','dollar')

    def bust(self,n,x,y,r,width,body_y,body_ry):
        # Detached head bottom = y+r; shoulder apex = body_y-body_ry.
        # Author parameters require their difference to be exactly eight.
        self.circle(n+'-head',x,y,r)
        self.add_arc(n+'-shoulders',(x-width,body_y),(x+width,body_y),radius_x=width,radius_y=body_ry)

    def build(self) -> None:
        self.add_arc('pepper-cap-left',(28,19),(35,12),radius_x=7)
        self.add_arc('pepper-cap-right',(35,12),(42,19),radius_x=7)
        self.add_bezier('pepper-outer',(42,19),((42,33),(34,42),(22,42)))
        self.add_bezier('pepper-inner',(22,42),((32,34),(26,26),(28,19)))
        self.add_contour('pepper','pepper-cap-left','pepper-cap-right','pepper-outer','pepper-inner',closed=True)
        self.add_line('stem',(35,6),(35,12))
        self.relate('connect','stem','pepper')
        self.add_bezier('flame-right',(12,14),((12,22),(18,22),(18,28)))
        self.add_arc('flame-bottom',(18,28),(6,28),radius_x=6)
        self.add_bezier('flame-left',(6,28),((6,22),(12,22),(12,14)))
        self.add_contour('flame','flame-right','flame-bottom','flame-left',closed=True)

# Repair plan: Curved tapered chili, upright stem and separate flame retain the heat concept.
# Omissions: Inner flame notch omitted.
# Construction references: No additional useful local Lucide match used.
# Keyshape and proportions: Square extrema are explicit endpoints; asymmetry follows the chili.

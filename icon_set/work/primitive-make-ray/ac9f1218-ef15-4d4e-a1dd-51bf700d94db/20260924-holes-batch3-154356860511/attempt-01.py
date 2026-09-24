"""A dollar symbol is centered inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: None; S curve and currency stem retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ac9f1218-ef15-4d4e-a1dd-51bf700d94db'
SOURCE_PATH = 'pictographic-primitives/other/house dollar sign_ac9f1218-ef15-4d4e-a1dd-51bf700d94db.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-dollar-sign'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'dollar', 'sign')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def house(self):
        # One mirrored envelope, x=24 axis; centerline extremes 6,6,42,42.
        self.add_line('roof-1',(6,18),(24,6))
        self.add_line('roof-2',(24,6),(42,18))
        self.add_line('wall-right',(42,18),(42,40))
        self.add_arc('corner-right',(42,40),(40,42),radius_x=2)
        self.add_line('floor',(40,42),(8,42))
        self.add_arc('corner-left',(8,42),(6,40),radius_x=2)
        self.add_line('wall-left',(6,40),(6,18))
        self.add_contour('house','roof-1','roof-2','wall-right','corner-right','floor','corner-left','wall-left',closed=True)

    def lock_body(self):
        # Shared shackle nodes are vertices in the top rail.
        self.add_polyline('lock-body',(17,26),(19,26),(29,26),(31,26),(31,34),(17,34),closed=True)

    def build(self):

        self.house()
        self.add_bezier('s-top',(29,21),((18,17),(16,26),(24,27)))
        self.add_bezier('s-bottom',(24,27),((34,28),(30,36),(19,32)))
        self.add_contour('currency-s','s-top','s-bottom')
        self.add_polyline('currency-stem',(24,18),(24,27),(24,33))
        self.relate('connect','currency-s','currency-stem')

# Final visible envelope: (4,4)-(44,44)
# Visual review: Currency S and vertical stem remain recognizable, though the small interior is heavy at four-unit stroke.

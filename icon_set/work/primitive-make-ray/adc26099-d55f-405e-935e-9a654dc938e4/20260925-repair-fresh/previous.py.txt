"""A four-bladed ventilation fan is inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: None; all four blades and hub retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='adc26099-d55f-405e-935e-9a654dc938e4'
SOURCE_PATH='icon_set/work/todo-references/house ventilator_adc26099-d55f-405e-935e-9a654dc938e4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-ventilator'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'ventilator')

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

        self.house();self.circle('hub',24,26,2)
        # Four identical curved blades, quarter-turn series around shared hub.
        for i in range(4):
            def rot(p):
                x,y=p[0]-24,p[1]-27
                for _ in range(i):x,y=-y,x
                return (24+x,26+y)
            n='blade-'+str(i)
            self.add_bezier(n,rot((24,25)),(rot((22,20)),rot((27,18)),rot((30,21))),(rot((33,25)),rot((29,25)),rot((26,27))))
            self.relate('connect',n,'hub')

# Final visible envelope: (4,4)-(44,44)
# Visual review: All four rotated blades and hub are present, but native-size output reads too much like a flower. Numeric validation passes; visual approval is withheld.

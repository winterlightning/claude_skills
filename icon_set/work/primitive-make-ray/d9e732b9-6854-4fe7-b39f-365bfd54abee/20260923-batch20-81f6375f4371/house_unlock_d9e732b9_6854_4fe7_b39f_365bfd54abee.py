"""An open padlock sits inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Body corner fillets reduced to round joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d9e732b9-6854-4fe7-b39f-365bfd54abee'
SOURCE_PATH='icon_set/work/todo-references/house unlock_d9e732b9-6854-4fe7-b39f-365bfd54abee.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-unlock'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'unlock')

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
        self.add_polyline('lock-body',(17,25),(19,25),(29,25),(31,25),(31,33),(17,33),closed=True)

    def build(self):

        self.house();self.lock_body()
        self.add_line('shackle-left',(19,25),(19,22))
        self.add_arc('shackle-top',(19,22),(24,17),radius_x=5)
        self.add_line('open-tip',(24,17),(26,17))
        self.add_contour('open-shackle','shackle-left','shackle-top','open-tip')
        self.relate('connect','open-shackle','lock-body')

# Final visible envelope: (4,4)-(44,44)
# Visual review: Open lock reads from its lifted short shackle. Opening and body have been rebalanced; open hook is deliberately asymmetric.

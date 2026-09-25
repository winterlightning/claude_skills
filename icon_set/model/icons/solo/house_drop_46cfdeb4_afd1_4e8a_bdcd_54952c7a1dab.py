"""A pointed water drop sits inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='46cfdeb4-afd1-4e8a-bdcd-54952c7a1dab'
SOURCE_PATH='icon_set/work/todo-references/house drop_46cfdeb4-afd1-4e8a-bdcd-54952c7a1dab.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-drop'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('house', 'drop')

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
        self.add_bezier('drop-right',(24,18),((27,23),(31,26),(31,28)),((31,32),(28,33),(24,33)))
        self.add_bezier('drop-left',(24,33),((20,33),(17,32),(17,28)),((17,26),(21,23),(24,18)))
        self.add_contour('drop','drop-right','drop-left',closed=True)

# Final visible envelope: (4,4)-(44,44)
# Visual review: Pointed droplet and rounded basin remain clear. Mirrored sides balance the composition.

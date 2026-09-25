"""A house encloses a light bulb.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Small base divider omitted because its short parallel gap cannot meet SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='177bdc8f-a349-4eb2-9256-4dda4aaf2d56'
SOURCE_PATH='icon_set/work/todo-references/house bulb_177bdc8f-a349-4eb2-9256-4dda4aaf2d56.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-bulb'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('house', 'bulb')

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
        self.add_arc('bulb-crown',(18,24),(30,24),radius_x=6)
        self.add_bezier('bulb-right',(30,24),((30,28),(28,28),(28,31)))
        self.add_line('bulb-base-1',(28,31),(28,33))
        self.add_line('bulb-base-2',(28,33),(20,33))
        self.add_line('bulb-base-3',(20,33),(20,31))
        self.add_bezier('bulb-left',(20,31),((20,28),(18,28),(18,24)))
        self.add_contour('bulb','bulb-crown','bulb-right','bulb-base-1','bulb-base-2','bulb-base-3','bulb-left',closed=True)

# Final visible envelope: (4,4)-(44,44)
# Visual review: Bulb silhouette and flattened base read at native size. The base divider is omitted; bilateral curves are smooth.

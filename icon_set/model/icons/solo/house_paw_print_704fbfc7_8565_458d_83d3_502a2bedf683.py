"""Three rounded toe pads and a triangular paw pad sit inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: None; the reference uses three toes and a triangular lower pad.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='704fbfc7-8565-458d-83d3-502a2bedf683'
SOURCE_PATH='icon_set/work/todo-references/house paw print_704fbfc7-8565-458d-83d3-502a2bedf683.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-paw-print'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'paw', 'print')

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
        for n,x,y in [('left',16,25),('top',24,19),('right',32,25)]:self.circle(n,x,y,2)
        self.add_polyline('pad',(24,28),(18,34),(30,34),closed=True)

# Final visible envelope: (4,4)-(44,44)
# Visual review: The three toes and triangular pad remain identifiable but crowd each other. Not visually approved; MIC fails between toes and pad.

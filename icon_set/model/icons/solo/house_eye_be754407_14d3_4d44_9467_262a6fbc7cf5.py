"""An almond-shaped eye is centered inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Subpixel central speck in the reference omitted; no substantial pupil outline appears in the reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='be754407-14d3-4d44-9467-262a6fbc7cf5'
SOURCE_PATH='icon_set/work/todo-references/house eye_be754407-14d3-4d44-9467-262a6fbc7cf5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-eye'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('house', 'eye')

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
        x,y=24,27
        self.add_bezier('eye-upper',(x-9,y),((x-4,y-8),(x+4,y-8),(x+9,y)))
        self.add_bezier('eye-lower',(x+9,y),((x+4,y+8),(x-4,y+8),(x-9,y)))
        self.add_contour('eye','eye-upper','eye-lower',closed=True)

# Final visible envelope: (4,4)-(44,44)
# Visual review: Almond eye is clear and horizontally balanced. Reference central speck omitted as below usable detail size.

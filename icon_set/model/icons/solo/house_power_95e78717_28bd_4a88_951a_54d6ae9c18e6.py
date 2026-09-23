"""An open power ring and vertical switch mark sit inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Upper ring shoulders simplified into vertical tangents.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='95e78717-28bd-4a88-951a-54d6ae9c18e6'
SOURCE_PATH='icon_set/work/todo-references/house power_95e78717-28bd-4a88-951a-54d6ae9c18e6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-power'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'power')

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
        self.add_line('ring-left',(15,22),(15,24))
        self.add_arc('ring-bottom',(15,24),(33,24),radius_x=9,sweep=False)
        self.add_line('ring-right',(33,24),(33,22))
        self.add_contour('power-ring','ring-left','ring-bottom','ring-right')
        self.add_line('power-stem',(24,18),(24,24))

# Final visible envelope: (4,4)-(44,44)
# Visual review: Power mark remains clear, centered and symmetric. The lower semicircle meets its vertical sides tangentially.

"""A liquid thermometer is contained inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: None; tube, bulb and mercury stroke retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c6485cd4-824d-44f8-a250-201a66d4bd70'
SOURCE_PATH='icon_set/work/todo-references/house thermometer_c6485cd4-824d-44f8-a250-201a66d4bd70.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-thermometer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'thermometer')

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
        self.add_arc('cap',(20,22),(28,22),radius_x=4)
        self.add_line('tube-right',(28,22),(28,27))
        self.add_bezier('bulb',(28,27),((34,34),(14,38),(20,27)))
        self.add_line('tube-left',(20,27),(20,22))
        self.add_contour('thermometer','cap','tube-right','bulb','tube-left',closed=True)
        self.add_line('mercury',(24,22),(24,30))

# Final visible envelope: (4,4)-(44,44)
# Visual review: Mercury merges into the tube at native size. Required four-unit ink spacing is unavailable in this retained composition; not approved.

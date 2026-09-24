"""A prohibition ring and slash cross a delivery truck.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 CIRCLE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Small cab corner fillets and wheel hubs omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c8de8135-2038-41da-8f58-2aeec3bdf7fd'
SOURCE_PATH='icon_set/work/todo-references/illegal logistic_c8de8135-2038-41da-8f58-2aeec3bdf7fd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='illegal-logistic'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('illegal', 'logistic')

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

        self.add_arc('ring-a',(12,8),(36,40),radius_x=20)
        self.add_arc('ring-b',(36,40),(12,8),radius_x=20)
        self.add_contour('prohibition','ring-a','ring-b',closed=True)
        self.add_polyline('cargo',(12,29),(12,18),(27,18),(27,29))
        self.add_polyline('cab',(27,21),(32,21),(36,27),(36,31),(34,31))
        self.relate('connect','cargo','cab')
        self.circle('wheel-left',17,31,2)
        self.circle('wheel-right',31,31,2)
        self.add_line('chassis',(19,31),(29,31))
        self.relate('connect','chassis','wheel-left')
        self.relate('connect','chassis','wheel-right')
        self.add_line('slash',(12,8),(36,40))
        self.relate('connect','prohibition','slash')

# Final visible envelope: radius 22 about (24,24)
# Visual review: Truck, wheels, prohibition circle and slash remain visible. Slash crosses the right wheel and leaves an unresolved MIC warning; not approved.

"""Fresh repair. Parent preserved in previous.py.txt. Supplied reference re-inspected.
See findings.md for current omissions and review; inherited comments describe the parent design.
"""
"""A diagonal telephone receiver appears inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Tiny receiver corner fillets merged into coherent curves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7c7ae497-e683-4449-9d47-32e2c0e677e7'
SOURCE_PATH = 'pictographic-primitives/other/house phone_7c7ae497-e683-4449-9d47-32e2c0e677e7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-phone'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/buildings'
    aliases=()
    keywords=('house', 'phone')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def house(self):
        # One mirrored envelope, x=24 axis; centerline extremes 6,6,42,42.
        self.add_line('roof-1',(6,14),(24,6))
        self.add_line('roof-2',(24,6),(42,14))
        self.add_line('wall-right',(42,14),(42,40))
        self.add_arc('corner-right',(42,40),(40,42),radius_x=2)
        self.add_line('floor',(40,42),(8,42))
        self.add_arc('corner-left',(8,42),(6,40),radius_x=2)
        self.add_line('wall-left',(6,40),(6,14))
        self.add_contour('house','roof-1','roof-2','wall-right','corner-right','floor','corner-left','wall-left',closed=True)

    def lock_body(self):
        # Shared shackle nodes are vertices in the top rail.
        self.add_polyline('lock-body',(17,26),(19,26),(29,26),(31,26),(31,34),(17,34),closed=True)

    def build(self):
        self.house()
        # Shared receiver arc and two genuine terminal attachments, no small loops.
        self.add_arc('receiver',(16,21),(31,33),radius_x=15,sweep=False)
        self.add_line('earpiece',(16,21),(20,24))
        self.add_line('mouthpiece',(31,33),(28,29))
        self.relate('connect','receiver','earpiece')
        self.relate('connect','receiver','mouthpiece')


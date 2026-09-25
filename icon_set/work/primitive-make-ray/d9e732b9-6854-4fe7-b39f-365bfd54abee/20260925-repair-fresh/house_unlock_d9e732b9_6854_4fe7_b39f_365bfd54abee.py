"""Fresh repair. Parent preserved in previous.py.txt. Supplied reference re-inspected.
See findings.md for current omissions and review; inherited comments describe the parent design.
"""
"""An open padlock sits inside a house.
Plan: one enclosing symbol and one content symbol; symmetry and repeated parts share parameters.
SOLO48 SQUARE; use Keyshape.bounds_for for visible envelope. Curved nodes are authored on the integer grid.
Lucide house: coherent roof/wall contour with tangent lower corner arcs.
Omissions: Body corner fillets reduced to round joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d9e732b9-6854-4fe7-b39f-365bfd54abee'
SOURCE_PATH = 'pictographic-primitives/other/house unlock_d9e732b9-6854-4fe7-b39f-365bfd54abee.svg'
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
        self.add_polyline('lock-body',(17,25),(19,25),(29,25),(31,25),(31,33),(17,33),closed=True)

    def build(self):
        self.house()
        self.add_polyline('lock-body',(16,25),(20,25),(32,25),(32,33),(16,33),closed=True)
        self.add_line('shackle-rise',(20,25),(20,20))
        self.add_arc('shackle-bend',(20,20),(24,16),radius_x=4)
        self.add_line('open-tip',(24,16),(26,16))
        self.add_contour('shackle','shackle-rise','shackle-bend','open-tip')
        self.relate('connect','shackle','lock-body')


"""unlock: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aa8fd4e-dd20-4ab4-9374-89370bfa9188'
SOURCE_PATH = 'pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Unlock(Solo48):
    icon_id = 'unlock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('unlock', 'state')

    def build(self):
        # Plan: VRECT_L; equal body corners and one circular open shackle.
        # Reference: Geometric rounded box and tangent arch.
        def box(name,l,t,r,b,corner):
            points=[(l+corner,t),(r-corner,t),(r,t+corner),(r,b-corner),(r-corner,b),(l+corner,b),(l,b-corner),(l,t+corner)]
            members=[]
            for i,a in enumerate(points):
                z=points[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
                if i%2:self.add_arc(eid,a,z,radius_x=corner)
                else:self.add_line(eid,a,z)
            self.add_contour(name,*members,closed=True)

        box('body',8,22,40,44,4)
        self.add_line('shackle-side',(14,22),(14,14))
        self.add_arc('shackle-arch',(14,14),(34,14),radius_x=10)
        self.add_contour('shackle','shackle-side','shackle-arch')
        self.relate('connect','shackle','body')

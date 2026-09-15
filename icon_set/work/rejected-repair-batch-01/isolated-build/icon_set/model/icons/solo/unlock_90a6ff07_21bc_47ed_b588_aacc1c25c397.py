"""unlock-90a6ff07: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90a6ff07-21bc-47ed-b588-aacc1c25c397'
SOURCE_PATH = 'pictographic-primitives/symbol/unlock_90a6ff07-21bc-47ed-b588-aacc1c25c397.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Unlock90a6ff07(Solo48):
    icon_id = 'unlock-90a6ff07'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

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

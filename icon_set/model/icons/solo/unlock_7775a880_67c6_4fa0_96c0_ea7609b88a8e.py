"""unlock-symbol: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7775a880-67c6-4fa0-96c0-ea7609b88a8e'
SOURCE_PATH = 'pictographic-primitives/symbol/unlock_7775a880-67c6-4fa0-96c0-ea7609b88a8e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class UnlockSymbol(Solo48):
    icon_id = 'unlock-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        # Plan: VRECT_L; coherent open circular shackle and equal corner radii.
        # Reference: Geometric rounded box and tangent arch.
        def box(name,l,t,r,b,corner):
            points=[(l+corner,t),(r-corner,t),(r,t+corner),(r,b-corner),(r-corner,b),(l+corner,b),(l,b-corner),(l,t+corner)]
            members=[]
            for i,a in enumerate(points):
                z=points[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
                if i%2:self.add_arc(eid,a,z,radius_x=corner)
                else:self.add_line(eid,a,z)
            self.add_contour(name,*members,closed=True)

        box('body',16,22,40,44,4)
        self.add_line('shackle-left',(8,18),(8,14))
        self.add_arc('shackle-top',(8,14),(28,14),radius_x=10)
        self.add_line('shackle-right',(28,14),(28,22))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','body')

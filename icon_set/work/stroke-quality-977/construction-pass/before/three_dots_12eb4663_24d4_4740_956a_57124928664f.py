"""three-dots: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12eb4663-24d4-4740-956a-57124928664f'
SOURCE_PATH = 'pictographic-primitives/state/three dots_12eb4663-24d4-4740-956a-57124928664f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ThreeDots(Solo48):
    icon_id = 'three-dots'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'dots', 'state')

    def build(self):
        # Plan: VRECT_L; straight parallel walls, matching corners and centered repeated dots.
        # Reference: Geometric rounded rectangle.
        def box(name,l,t,r,b,corner):
            points=[(l+corner,t),(r-corner,t),(r,t+corner),(r,b-corner),(r-corner,b),(l+corner,b),(l,b-corner),(l,t+corner)]
            members=[]
            for i,a in enumerate(points):
                z=points[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
                if i%2:self.add_arc(eid,a,z,radius_x=corner)
                else:self.add_line(eid,a,z)
            self.add_contour(name,*members,closed=True)

        box('frame',8,4,40,44,3)
        for y in (13,24,35):self.add_dot('dot-'+str(y),(24,y))

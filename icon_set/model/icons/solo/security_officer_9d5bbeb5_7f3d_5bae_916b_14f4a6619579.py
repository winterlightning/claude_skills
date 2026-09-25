"""A security officer wears a peaked cap and V-collar with one arm angled left.

Construction: user-round: semicircular face and rounded shoulder; hat-glasses: crown and projecting brim.
Reduction: Removed sleeve seam and reduced the bent arm to a single gesture stroke. The arm makes the otherwise centered bust deliberately asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d5bbeb5-7f3d-5bae-916b-14f4a6619579'
SOURCE_PATH = 'pictographic-primitives/travel/security officer_9d5bbeb5-7f3d-5bae-916b-14f4a6619579.svg'
AUTHOR = 'gpt-6'

class SecurityOfficer(Solo48):
    icon_id = 'security-officer'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('security', 'officer', 'guard', 'police', 'checkpoint', 'airport', 'uniform', 'person')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        runs = {}

        def run(name, *points):
            ids = []
            for n, (a, b) in enumerate(zip(points, points[1:])):
                part = f'{name}-{n}'
                self.add_line(part, a, b)
                ids.append(part)
            runs[name] = ids
        self.add_polyline('cap', (20, 4), (36, 4), (34, 14), (20, 14), closed=True)
        self.add_arc('face', (34, 14), (20, 14), radius_x=7)
        self.relate('connect', 'cap', 'face')
        self.add_line('brim', (16, 14), (20, 14))
        self.relate('connect', 'cap', 'brim')
        self.relate('connect', 'face', 'brim')
        run('torso-top', (20, 44), (20, 29), (34, 29))
        self.add_arc('shoulder', (34, 29), (40, 35), radius_x=6)
        run('torso-right', (40, 35), (40, 44), (20, 44))
        self.add_contour('torso', *runs['torso-top'], 'shoulder', *runs['torso-right'], closed=True)
        self.add_line('arm', (20, 29), (8, 44))
        self.relate('connect', 'arm', 'torso')

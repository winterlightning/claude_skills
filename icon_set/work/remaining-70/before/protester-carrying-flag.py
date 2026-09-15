"""Flag protester: give the head clearance from the flag and pole as well as its own shoulder. Radius4 head (24,18), torso (24,30), exact4 ink gap. Hands meet the pole at (12,24); retain the source walking stance and full_body_ref.png vocabulary.

Flag protester: remove the duplicated line that ran into the head. Radius4 head at (32,16), actual shoulder (32,28), exact4 ink gap. Curved torso and two walking legs preserve the source flag-carrying action. full_body_ref.png owns human proportions.

Protester Carrying a Flag. Flag, diagonal pole and striding figure; closed limb contours reduced to strokes.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0f3f951b-efd9-4984-97c6-cd6a6f95b6fd'
SOURCE_PATH = 'pictographic-primitives/war/protester flag_0f3f951b-efd9-4984-97c6-cd6a6f95b6fd.svg'
AUTHOR = 'gpt-6'

class ProtesterCarryingFlag(Solo48):
    icon_id = 'protester-carrying-flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('protester', 'flag', 'person', 'march', 'pole', 'demonstration')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        """Flag protester: give the head clearance from the flag and pole as well as its own shoulder. Radius4 head (24,18), torso (24,30), exact4 ink gap. Hands meet the pole at (12,24); retain the source walking stance and full_body_ref.png vocabulary."""
        self.ring('head', 24, 18, 4)
        self.add_bezier('torso', (24, 30), ((24, 33), (27, 35), (28, 37)))
        self.branches([('arm', [(24, 30), (14, 30), (12, 24)]), ('left-leg', [(28, 37), (20, 39), (16, 44)]), ('right-leg', [(28, 37), (35, 40), (39, 44)]), ('pole', [(8, 4), (12, 24), (14, 34)]), ('flag', [(8, 4), (40, 4), (34, 10)])])
        for p in ['arm-0', 'left-leg-0', 'right-leg-0']:
            self.relate('connect', 'torso', p)

"""Seated prayer: draw a real shoulder junction and torso behind two bent arms whose palms meet at(24,26). Radius4 head(24,8), actual shoulder(24,20), exact4 painted clearance; the palms do not substitute for the shoulder. VRECT_L gives both arm counters room above the crossed legs. Original prayer source and full_body_ref.png inspected.

Seated prayer: radius5 head center(24,11) sits exactly4 painted units above the shoulder/palm junction(24,24). Preserve the prayer gesture and crossed legs; original and full_body_ref.png inspected.

A cross-legged figure holds both hands together in a pointed prayer shape at the center of the chest. Rounded bent arms enclose the hands beneath a separate circular head.
Construction: Bounds (6,6)-(42,42). Joined palms at chest and paired bent elbows above crossed legs. Omit finger detail and duplicated outlines.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a24a87c9-e913-450e-89fa-1364d53ddeea'
SOURCE_PATH = 'pictographic-primitives/sports/yoga meditation pose_a24a87c9-e913-450e-89fa-1364d53ddeea.svg'
AUTHOR = 'gpt-6'

class SeatedPrayerPose(Solo48):
    icon_id = 'seated-prayer-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('seated', 'prayer', 'pose', 'yoga', 'exercise')

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
        """Seated prayer: draw a real shoulder junction and torso behind two bent arms whose palms meet at(24,26). Radius4 head(24,8), actual shoulder(24,20), exact4 painted clearance; the palms do not substitute for the shoulder. VRECT_L gives both arm counters room above the crossed legs. Original prayer source and full_body_ref.png inspected."""
        self.ring('head', 24, 8, 4)
        self.branches([('torso', [(24, 20), (24, 26), (24, 40)]), ('left-arm', [(24, 20), (8, 26), (18, 30), (24, 26)]), ('right-arm', [(24, 20), (40, 26), (30, 30), (24, 26)]), ('left-leg', [(8, 36), (24, 40), (40, 44)]), ('right-leg', [(40, 36), (24, 40), (8, 44)])])

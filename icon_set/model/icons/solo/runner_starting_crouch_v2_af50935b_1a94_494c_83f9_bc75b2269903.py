"""Reconstruct runner starting crouch using its inspected source pose and full_body_ref.png. Head radius 5, center (11, 11), actual torso junction (23, 16): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct runner starting crouch using its inspected source pose and full_body_ref.png. Head radius 5, center (11, 11), actual torso junction (23, 16): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct runner starting crouch using its inspected source pose and full_body_ref.png. Head radius 5, center (11, 11), actual torso junction (23, 16): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Runner in Starting Crouch, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af50935b-1a94-494c-83f9-bc75b2269903'
SOURCE_PATH = 'pictographic-primitives/sports/running ready starting posture_af50935b-1a94-494c-83f9-bc75b2269903.svg'
AUTHOR = 'gpt-6'

class RunnerStartingCrouchVariant2(Solo48):
    icon_id = 'runner-starting-crouch-v2'
    variant_of = 'runner-starting-crouch'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('runner', 'start', 'crouch', 'sprint', 'athletics', 'running')

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
        """Reconstruct runner starting crouch using its inspected source pose and full_body_ref.png. Head radius 5, center (11, 11), actual torso junction (23, 16): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (6, 11), (16, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (16, 11), (6, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('back-1', (23, 16), *(((26.36, 17.4), (28.25, 22.0), (30, 24)),))
        self.add_line('back-2', (30, 24), (42, 36))
        self.add_line('arm', (23, 16), (13, 42))
        self.add_line('bent-leg-1', (30, 24), (22, 34))
        self.add_line('bent-leg-2', (22, 34), (30, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('bent-leg', *('bent-leg-1', 'bent-leg-2'), closed=False)
        self.relate('connect', *('arm', 'back'))
        self.relate('connect', *('back', 'bent-leg'))
        self.add_contour('back', *('back-1',), closed=False)
        self.add_contour('back-section-1', *('back-2',), closed=False)
        self.relate('connect', 'back-1', 'back-2')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'back-1', 'back-2')
        self.relate('connect', 'back-1', 'arm')
        self.relate('connect', 'back-1', 'bent-leg-1')
        self.relate('connect', 'back-2', 'bent-leg-1')
        self.relate('connect', 'bent-leg-1', 'bent-leg-2')

"""Reconstruct tree pose using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct tree pose using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A figure balances on one straight leg while the opposite foot rests against its inner side, forming a triangular knee opening. Both arms curve overhead around the circular head.
Construction: Bounds (8,6)-(40,42). Mirror overhead arms, but retain the single folded knee and straight supporting leg. Triangle of bent knee remains open.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd308a08-5d16-5ba7-ba3b-4c7cff751329'
SOURCE_PATH = 'pictographic-primitives/sports/yoga tree pose_cd308a08-5d16-5ba7-ba3b-4c7cff751329.svg'
AUTHOR = 'gpt-6'

class TreePoseVariant2(Solo48):
    icon_id = 'tree-pose-v2'
    variant_of = 'tree-pose'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tree', 'pose', 'yoga', 'exercise')

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
        """Reconstruct tree pose using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (19, 11), (29, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (29, 11), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('arm-l', (8, 4), (8, 16))
        self.add_arc('shoulder-l', (8, 16), (16, 24), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('arms', (16, 24), (24, 24))
        self.add_line('arms-right', (24, 24), (32, 24))
        self.add_arc('shoulder-r', (32, 24), (40, 16), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('arm-r', (40, 16), (40, 4))
        self.add_bezier('body-1', (24, 24), *(((24.0, 26.0), (24.0, 27.75), (24, 29)),))
        self.add_line('body-2', (24, 29), (24, 44))
        self.add_line('bent-leg-1', (24, 29), (38, 36))
        self.add_line('bent-leg-2', (38, 36), (24, 44))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('left-arm', *('arm-l', 'shoulder-l'), closed=False)
        self.add_contour('right-arm', *('shoulder-r', 'arm-r'), closed=False)
        self.add_contour('bent-leg', *('bent-leg-1', 'bent-leg-2'), closed=False)
        self.relate('connect', *('left-arm', 'arms'))
        self.relate('connect', *('arms', 'arms-right'))
        self.relate('connect', *('arms-right', 'right-arm'))
        self.relate('connect', *('arms', 'body'))
        self.relate('connect', *('body', 'bent-leg'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2',), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'arm-l', 'shoulder-l')
        self.relate('connect', 'shoulder-l', 'arms')
        self.relate('connect', 'arms', 'arms-right')
        self.relate('connect', 'arms', 'body-1')
        self.relate('connect', 'arms-right', 'shoulder-r')
        self.relate('connect', 'arms-right', 'body-1')
        self.relate('connect', 'shoulder-r', 'arm-r')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-1', 'bent-leg-1')
        self.relate('connect', 'body-2', 'bent-leg-1')
        self.relate('connect', 'body-2', 'bent-leg-2')
        self.relate('connect', 'bent-leg-1', 'bent-leg-2')

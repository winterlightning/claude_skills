"""Meditating figure: radius5 head center(24,11), shoulder(24,24), exact4 painted gap. Preserve crossed legs and two separate curved resting arms; full_body_ref.png proportions.

Meditating figure: radius5 head center(24,11), shoulder(24,24), exact4 painted gap. Preserve crossed legs and two separate curved resting arms; full_body_ref.png proportions.

A figure sits upright with two crossed legs beneath a rounded torso. Both arms curve inward toward the abdomen, leaving a small central gap below the circular head.
Construction: Bounds (6,6)-(42,42). Mirrored arms curve inward over crossed legs; remove double limb contours and fingers.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ded0b984-4a7d-5b44-8214-e8c48cf563e0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga meditate_ded0b984-4a7d-5b44-8214-e8c48cf563e0.svg'
AUTHOR = 'gpt-6'

class SeatedMeditationCurvedArms(Solo48):
    icon_id = 'seated-meditation-curved-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('seated', 'meditation', 'curved', 'arms', 'yoga', 'exercise')

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
        """Meditating figure: radius5 head center(24,11), shoulder(24,24), exact4 painted gap. Preserve crossed legs and two separate curved resting arms; full_body_ref.png proportions."""
        self.add_arc('head-a', (19, 11), (29, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (29, 11), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('shoulder-l', (10, 28), *(((13, 24), (19, 24), (24, 24)),))
        self.add_bezier('shoulder-r', (24, 24), *(((29, 24), (35, 24), (38, 28)),))
        self.add_line('arm-l-1', (10, 28), (10, 32))
        self.add_line('arm-l-2', (10, 32), (18, 32))
        self.add_line('arm-r-1', (38, 28), (38, 32))
        self.add_line('arm-r-2', (38, 32), (30, 32))
        self.add_line('torso', (24, 24), (24, 38))
        self.add_line('leg-l-1', (6, 34), (24, 38))
        self.add_line('leg-l-2', (24, 38), (42, 42))
        self.add_line('leg-r-1', (42, 34), (24, 38))
        self.add_line('leg-r-2', (24, 38), (6, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('shoulders', *('shoulder-l', 'shoulder-r'), closed=False)
        self.add_contour('arm-l', *('arm-l-1', 'arm-l-2'), closed=False)
        self.add_contour('arm-r', *('arm-r-1', 'arm-r-2'), closed=False)
        self.add_contour('leg-l', *('leg-l-1', 'leg-l-2'), closed=False)
        self.add_contour('leg-r', *('leg-r-1', 'leg-r-2'), closed=False)
        self.relate('connect', *('shoulders', 'arm-l'))
        self.relate('connect', *('shoulders', 'arm-r'))
        self.relate('connect', *('shoulders', 'torso'))
        self.relate('connect', *('leg-l', 'leg-r'))
        self.relate('connect', *('torso', 'leg-l'))
        self.relate('connect', *('torso', 'leg-r'))

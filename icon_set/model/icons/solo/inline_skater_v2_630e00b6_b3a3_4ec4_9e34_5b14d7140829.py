"""Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Inline skater, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '630e00b6-b3a3-4ec4-9e34-5b14d7140829'
SOURCE_PATH = 'pictographic-primitives/sports/rollerblades person_630e00b6-b3a3-4ec4-9e34-5b14d7140829.svg'
AUTHOR = 'gpt-6'

class InlineSkaterVariant2(Solo48):
    icon_id = 'inline-skater-v2'
    variant_of = 'inline-skater'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('inline', 'skater')

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
        """Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (25, 11), (35, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (35, 11), (25, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('arms-1', (13, 19), (25, 23))
        self.add_line('arms-2', (25, 23), (32, 26))
        self.add_line('arms-3', (32, 26), (42, 25))
        self.add_bezier('torso-1', (25, 23), *(((24.129714730847326, 25.088684645966417), (22.0, 26.0), (21, 27)),))
        self.add_line('torso-2', (21, 27), (30, 30))
        self.add_line('torso-3', (30, 30), (28, 34))
        self.add_line('back-leg-1', (21, 27), (13, 29))
        self.add_line('back-leg-2', (13, 29), (6, 26))
        self.add_line('skate-front', (25, 34), (33, 34))
        self.add_line('wheel-front-25', (25, 42), (25, 42))
        self.add_line('wheel-front-33', (33, 42), (33, 42))
        self.add_line('wheel-rear-a', (6, 35), (6, 35))
        self.add_line('wheel-rear-b', (14, 39), (14, 39))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2', 'arms-3'), closed=False)
        self.add_contour('torso', *('torso-1', 'torso-2', 'torso-3'), closed=False)
        self.add_contour('back-leg', *('back-leg-1', 'back-leg-2'), closed=False)
        self.relate('connect', *('arms', 'torso'))
        self.relate('connect', *('back-leg', 'torso'))
        self.relate('connect', *('torso', 'skate-front'))

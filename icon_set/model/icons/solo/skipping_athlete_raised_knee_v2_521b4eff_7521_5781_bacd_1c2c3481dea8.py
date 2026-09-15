"""Reconstruct skipping athlete raised knee using its inspected source pose and full_body_ref.png. Head radius 4, center (24, 10), actual torso junction (24, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A front-facing athlete holds a rope out to both sides while lifting one bent knee. The rope curves downward in a broad loop beneath the suspended feet.

Broad rope loop and paired hands retained; compact joined limbs distinguish the lifted knee and inward bent leg poses.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '521b4eff-7521-5781-bacd-1c2c3481dea8'
SOURCE_PATH = 'pictographic-primitives/sports/fitness jumping rope_521b4eff-7521-5781-bacd-1c2c3481dea8.svg'
AUTHOR = 'gpt-6'

class SkippingAthleteRaisedKneeVariant2(Solo48):
    icon_id = 'skipping-athlete-raised-knee-v2'
    variant_of = 'skipping-athlete-raised-knee'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('skipping', 'rope', 'jumping', 'athlete', 'fitness', 'exercise')

    def circle(self, name, x, y, r):
        self.add_arc(name + '-top', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-bottom', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skeleton(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for index, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{index}'
                members.append(key)
                self.add_line(key, a, b)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for index, (a, p, q) in enumerate(parts):
            for b, r, s in parts[index + 1:]:
                if p in (r, s) or q in (r, s):
                    self.relate('connect', a, b)

    def rounded(self, name, x, y, w, h, r):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        members = []
        for index, a in enumerate(pts):
            b = pts[(index + 1) % 8]
            key = f'{name}-{index}'
            members.append(key)
            if index % 2:
                self.add_arc(key, a, b, radius_x=r)
            else:
                self.add_line(key, a, b)
        self.add_contour(name, *members, closed=True)

    def weight(self, name, x, y, w, h, r):
        middle = y + h // 2
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, middle), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, middle), (x, y + r)]
        members = []
        for index, a in enumerate(pts):
            b = pts[(index + 1) % len(pts)]
            key = f'{name}-{index}'
            members.append(key)
            if index in [1, 4, 6, 9]:
                self.add_arc(key, a, b, radius_x=r)
            else:
                self.add_line(key, a, b)
        self.add_contour(name, *members, closed=True)

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
        """Reconstruct skipping athlete raised knee using its inspected source pose and full_body_ref.png. Head radius 4, center (24, 10), actual torso junction (24, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 24, 10, 4)
        self.add_bezier('torso-0', (24, 22), *(((24.0, 24.0), (24.0, 25.75), (24, 27)),))
        self.add_line('left-arm-0', (24, 22), (15, 22))
        self.add_line('left-arm-1', (15, 22), (6, 22))
        self.add_line('right-arm-0', (24, 22), (33, 22))
        self.add_line('right-arm-1', (33, 22), (42, 22))
        self.add_line('left-leg-0', (24, 27), (20, 32))
        self.add_line('right-leg-0', (24, 27), (30, 28))
        self.add_line('right-leg-1', (30, 28), (28, 32))
        self.add_arc('rope', (6, 22), (42, 22), radius_x=18, radius_y=20, large_arc=False, sweep=False)
        self.add_contour('left-arm', *('left-arm-0', 'left-arm-1'), closed=False)
        self.add_contour('right-arm', *('right-arm-0', 'right-arm-1'), closed=False)
        self.add_contour('right-leg', *('right-leg-0', 'right-leg-1'), closed=False)
        self.relate('connect', *('torso-0', 'left-arm-0'))
        self.relate('connect', *('torso-0', 'right-arm-0'))
        self.relate('connect', *('torso-0', 'left-leg-0'))
        self.relate('connect', *('torso-0', 'right-leg-0'))
        self.relate('connect', *('left-arm-0', 'left-arm-1'))
        self.relate('connect', *('left-arm-0', 'right-arm-0'))
        self.relate('connect', *('right-arm-0', 'right-arm-1'))
        self.relate('connect', *('left-leg-0', 'right-leg-0'))
        self.relate('connect', *('right-leg-0', 'right-leg-1'))
        self.relate('connect', *('rope', 'left-arm-1'))
        self.relate('connect', *('rope', 'right-arm-1'))

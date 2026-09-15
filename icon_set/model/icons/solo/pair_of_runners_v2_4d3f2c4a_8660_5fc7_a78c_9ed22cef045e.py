"""Reconstruct pair of runners using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 11), actual torso junction (14, 23): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct pair of runners using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 11), actual torso junction (14, 23): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Two running figures move side by side, with one slightly behind and to the left. Both have circular heads, bent swinging arms, and legs separated into active strides.

Two distinct heads and active strides retained. The figures use joined strokes with staggered arms and legs, preserving a pair rather than merging bodies."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d3f2c4a-8660-5fc7-a78c-9ed22cef045e'
SOURCE_PATH = 'pictographic-primitives/sports/group running_4d3f2c4a-8660-5fc7-a78c-9ed22cef045e.svg'
AUTHOR = 'gpt-6'

class PairOfRunnersVariant2(Solo48):
    icon_id = 'pair-of-runners-v2'
    variant_of = 'pair-of-runners'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('running', 'runner', 'pair', 'group', 'athlete', 'fitness')

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
        """Reconstruct pair of runners using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 11), actual torso junction (14, 23): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('left-head-a', (10, 11), (18, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('left-head-b', (18, 11), (10, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('right-head-a', (30, 11), (38, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('right-head-b', (38, 11), (30, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('left-body-0', (14, 23), *(((14.0, 25.8), (14.0, 28.25), (14, 30)),))
        self.add_line('left-back-arm-0', (14, 23), (6, 23))
        self.add_line('left-back-arm-1', (6, 23), (6, 28))
        self.add_line('left-front-arm-0', (14, 23), (20, 26))
        self.add_line('left-back-leg-0', (14, 30), (6, 40))
        self.add_line('left-front-leg-0', (14, 30), (18, 36))
        self.add_line('left-front-leg-1', (18, 36), (16, 42))
        self.add_line('right-body-0', (34, 23), (32, 30))
        self.add_line('right-front-arm-0', (34, 23), (42, 18))
        self.add_line('right-back-arm-0', (34, 23), (28, 24))
        self.add_line('right-back-arm-1', (28, 24), (28, 27))
        self.add_line('right-back-leg-0', (32, 30), (26, 40))
        self.add_line('right-front-leg-0', (32, 30), (40, 36))
        self.add_line('right-front-leg-1', (40, 36), (42, 42))
        self.add_contour('left-head', *('left-head-a', 'left-head-b'), closed=True)
        self.add_contour('right-head', *('right-head-a', 'right-head-b'), closed=True)
        self.add_contour('left-back-arm', *('left-back-arm-0', 'left-back-arm-1'), closed=False)
        self.add_contour('left-front-leg', *('left-front-leg-0', 'left-front-leg-1'), closed=False)
        self.add_contour('right-back-arm', *('right-back-arm-0', 'right-back-arm-1'), closed=False)
        self.add_contour('right-front-leg', *('right-front-leg-0', 'right-front-leg-1'), closed=False)
        self.relate('connect', *('left-body-0', 'left-back-arm-0'))
        self.relate('connect', *('left-body-0', 'left-front-arm-0'))
        self.relate('connect', *('left-body-0', 'left-back-leg-0'))
        self.relate('connect', *('left-body-0', 'left-front-leg-0'))
        self.relate('connect', *('left-back-arm-0', 'left-back-arm-1'))
        self.relate('connect', *('left-back-arm-0', 'left-front-arm-0'))
        self.relate('connect', *('left-back-leg-0', 'left-front-leg-0'))
        self.relate('connect', *('left-front-leg-0', 'left-front-leg-1'))
        self.relate('connect', *('right-body-0', 'right-front-arm-0'))
        self.relate('connect', *('right-body-0', 'right-back-arm-0'))
        self.relate('connect', *('right-body-0', 'right-back-leg-0'))
        self.relate('connect', *('right-body-0', 'right-front-leg-0'))
        self.relate('connect', *('right-front-arm-0', 'right-back-arm-0'))
        self.relate('connect', *('right-back-arm-0', 'right-back-arm-1'))
        self.relate('connect', *('right-back-leg-0', 'right-front-leg-0'))
        self.relate('connect', *('right-front-leg-0', 'right-front-leg-1'))

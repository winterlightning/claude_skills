# Refinement: Raise the discus and lower the hip to open clearance on both sides of the throwing arm.
# Repair: Raise the holding elbow away from the rear thigh, retaining the circular discus.
"""Reconstruct discus thrower using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct discus thrower using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

An athlete twists in a wide stepping stance with one arm extended diagonally to the right. The opposite arm bends back on the left, holding a small round discus beside the head.

Kept the smaller held discus distinct from the larger head, with a twisting stance and extended opposite arm.
Source throwing orientation; Lucide person-standing informed the head and jointed limbs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0d788345-a3f5-5d41-acb9-ca84042b3f45'
SOURCE_PATH = 'pictographic-primitives/sports/discus throwing_0d788345-a3f5-5d41-acb9-ca84042b3f45.svg'
AUTHOR = 'gpt-6'

class DiscusThrower(Solo48):
    icon_id = 'discus-thrower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('discus', 'throw', 'athletics', 'athlete', 'field', 'sport')

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
        """Reconstruct discus thrower using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (24, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (19, 11), (29, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (29, 11), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('discus-right', (9, 13), (9, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('discus-left', (9, 19), (9, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('torso-0', (24, 24), *(((24.0, 27.29848450049413), (22.5, 30.0), (22, 34)),))
        self.add_line('holding-arm-0', (24, 24), (12, 29))
        self.add_line('holding-arm-1', (12, 29), (9, 19))
        self.add_line('extended-arm-0', (24, 24), (42, 24))
        self.add_line('rear-leg-0', (22, 34), (14, 38))
        self.add_line('rear-leg-1', (14, 38), (6, 42))
        self.add_line('front-leg-0', (22, 34), (30, 38))
        self.add_line('front-leg-1', (30, 38), (28, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('discus', *('discus-right', 'discus-left'), closed=True)
        self.add_contour('holding-arm', *('holding-arm-0', 'holding-arm-1'), closed=False)
        self.add_contour('rear-leg', *('rear-leg-0', 'rear-leg-1'), closed=False)
        self.add_contour('front-leg', *('front-leg-0', 'front-leg-1'), closed=False)
        self.relate('connect', *('torso-0', 'holding-arm-0'))
        self.relate('connect', *('torso-0', 'extended-arm-0'))
        self.relate('connect', *('torso-0', 'rear-leg-0'))
        self.relate('connect', *('torso-0', 'front-leg-0'))
        self.relate('connect', *('holding-arm-0', 'holding-arm-1'))
        self.relate('connect', *('holding-arm-0', 'extended-arm-0'))
        self.relate('connect', *('rear-leg-0', 'rear-leg-1'))
        self.relate('connect', *('rear-leg-0', 'front-leg-0'))
        self.relate('connect', *('front-leg-0', 'front-leg-1'))
        self.relate('connect', *('holding-arm-1', 'discus-right'))
        self.relate('connect', *('holding-arm-1', 'discus-left'))

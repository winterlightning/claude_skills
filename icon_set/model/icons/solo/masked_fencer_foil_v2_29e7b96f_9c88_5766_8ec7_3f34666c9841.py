"""A front-facing fencer bust wears a round mesh mask divided by horizontal and vertical bars. A long foil rises diagonally at the right, with a curved guard beside the shoulder.

Mask mesh reduced to one cross; shoulder, curved guard and diagonal foil retained.
Inspected source rendering; Lucide bike, sword, dumbbell and person-standing informed sparse equipment and figure construction where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '29e7b96f-9c88-5766-8ec7-3f34666c9841'
SOURCE_PATH = 'pictographic-primitives/sports/fencing person_29e7b96f-9c88-5766-8ec7-3f34666c9841.svg'
AUTHOR = 'gpt-6'

class MaskedFencerFoilVariant2(Solo48):
    icon_id = 'masked-fencer-foil-v2'
    variant_of = 'masked-fencer-foil'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('fencing', 'fencer', 'mask', 'foil', 'sword', 'sport')

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

    def build(self):
        """Move the foil attachment to the guard midpoint so the blade does not trap a tiny counter against its right tip."""
        pts = [(16, 6), (26, 16), (16, 26), (6, 16)]
        for i in range(4):
            self.add_arc(f'mask-{i}', pts[i], pts[(i + 1) % 4], radius_x=10)
        self.add_contour('mask', *[f'mask-{i}' for i in range(4)], closed=True)
        self.skeleton([('vertical', [(16, 6), (16, 16), (16, 26)]), ('horizontal', [(6, 16), (16, 16), (26, 16)]), ('bust', [(6, 42), (6, 38), (16, 35), (26, 32)]), ('blade', [(42, 6), (32, 32), (31, 42)])])
        for line, arcs in [('vertical-0', [0, 3]), ('vertical-1', [1, 2]), ('horizontal-0', [2, 3]), ('horizontal-1', [0, 1])]:
            for i in arcs:
                self.relate('connect', line, f'mask-{i}')
        self.add_arc('guard-left', (26, 32), (32, 32), radius_x=6, sweep=False)
        self.add_arc('guard-right', (32, 32), (38, 32), radius_x=6, sweep=False)
        self.add_contour('guard', 'guard-left', 'guard-right')
        self.relate('connect', 'bust-2', 'guard-left')
        for a in ['guard-left', 'guard-right']:
            for b in ['blade-0', 'blade-1']:
                self.relate('connect', a, b)

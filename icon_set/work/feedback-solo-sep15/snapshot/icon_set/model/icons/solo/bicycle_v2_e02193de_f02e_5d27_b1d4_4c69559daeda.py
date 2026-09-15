"""Enlarge both bicycle wheels equally and rebalance the frame above them. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e02193de-f02e-5d27-b1d4-4c69559daeda'
SOURCE_PATH = 'pictographic-primitives/sports/fitness bicycle_e02193de-f02e-5d27-b1d4-4c69559daeda.svg'
AUTHOR = 'gpt-6'

class BicycleVariant2(Solo48):
    icon_id = 'bicycle-v2'
    variant_of = 'bicycle'
    variant_label = 'Enlarge both bicycle wheels equally and rebalance the frame above them.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('bicycle', 'bike', 'cycling', 'frame', 'transport', 'pedal')

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
        """Symbol plan: Enlarge both bicycle wheels equally and rebalance the frame above them. Reference: Lucide bike: shared wheel radii and simple frame."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        for n, x in [('rear', 11), ('front', 37)]:
            oval(n, x, 33, 7, 7)
        poly('rear-frame', (11, 26), (18, 17), (34, 17))
        poly('fork', (37, 26), (34, 17), (30, 8), (37, 8))
        poly('seat', (12, 8), (18, 8), (22, 8))
        line('post', (18, 8), (18, 17))
        for a, b in [('rear-frame', 'rear'), ('fork', 'front'), ('fork', 'rear-frame'), ('post', 'rear-frame'), ('post', 'seat')]:
            join(a, b)

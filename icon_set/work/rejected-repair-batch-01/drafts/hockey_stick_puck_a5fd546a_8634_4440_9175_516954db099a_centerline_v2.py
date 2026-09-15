"""Replace the hockey stick’s kinked heel with a curve tangent to both shaft and blade; keep the puck separate and the blade level.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a5fd546a-8634-4440-9175-516954db099a'
SOURCE_PATH = 'pictographic-primitives/sports/hockey puck stick_a5fd546a-8634-4440-9175-516954db099a.svg'
AUTHOR = 'gpt-6'

class HockeyStickPuck(Solo48):
    icon_id = 'hockey-stick-puck-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('hockey', 'stick', 'puck', 'equipment', 'sport', 'ice')

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
        self.circle('puck', 10, 26, 4)
        self.add_line('shaft', (42, 6), (31, 35))
        self.add_bezier('heel', (31, 35), ((29, 40), (29, 42), (24, 42)))
        self.add_line('blade', (24, 42), (6, 42))
        self.add_contour('stick', 'shaft', 'heel', 'blade')
    variant_of = 'hockey-stick-puck'
    variant_label = 'Batch 01 centerline repair'

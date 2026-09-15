"""Kite skier: distinguish the reaching arm from the curved backward-leaning torso and bend both legs into the skiing action. Radius4 head (11,15), shoulder (11,27), exact4 painted clearance and vertical torso tangent. Original reference and full_body_ref.png inspected. Shared kite corner is the real tether attachment; keep its asymmetry.

Kite skier: distinguish the reaching arm from the curved backward-leaning torso and bend both legs into the skiing action. Radius4 head (11,15), shoulder (11,27), exact4 painted clearance and vertical torso tangent. Original reference and full_body_ref.png inspected. Shared kite corner is the real tether attachment; keep its asymmetry.

A skier leans back on two short upturned skis while reaching toward a kite above the right side. An angular tether connects the hands to the curved triangular kite.

Curved kite, tether, leaning skier and upturned ski end retained. The overlapping skis use one shared silhouette; extra rigging is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '580efdc2-15e9-4ed3-a2ce-d59eca2c1be1'
SOURCE_PATH = 'pictographic-primitives/sports/kite skiing_580efdc2-15e9-4ed3-a2ce-d59eca2c1be1.svg'
AUTHOR = 'gpt-6'

class KiteSkierVariant2(Solo48):
    icon_id = 'kite-skier-v2'
    variant_of = 'kite-skier'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('kite', 'skiing', 'skier', 'snow', 'wind', 'sport')

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
        """Kite skier: distinguish the reaching arm from the curved backward-leaning torso and bend both legs into the skiing action. Radius4 head (11,15), shoulder (11,27), exact4 painted clearance and vertical torso tangent. Original reference and full_body_ref.png inspected. Shared kite corner is the real tether attachment; keep its asymmetry."""
        self.add_arc('kite-canopy', (26, 6), (42, 22), radius_x=16)
        self.add_polyline('kite-edges', (42, 22), (26, 22), (26, 6))
        self.relate('connect', 'kite-canopy', 'kite-edges')
        self.ring('head', 11, 15, 4)
        self.add_bezier('torso', (11, 27), ((11, 30), (15, 32), (15, 35)))
        self.branches([('arm', [(11, 27), (20, 27), (26, 22)]), ('rear-leg', [(15, 35), (10, 42)]), ('front-leg', [(15, 35), (23, 34), (27, 39)]), ('ski', [(6, 42), (10, 42), (26, 42), (31, 38)])])
        for p in ['arm-0', 'rear-leg-0', 'front-leg-0']:
            self.relate('connect', 'torso', p)
        self.relate('connect', 'arm-1', 'kite-edges')

# Repair: Level the skier thigh exactly between the arm and ski; preserve the kite canopy and exact detached head spacing.
"""Kite skier: distinguish the reaching arm from the curved backward-leaning torso and bend both legs into the skiing action. Radius4 head (11,15), shoulder (11,27), exact4 painted clearance and vertical torso tangent. Original reference and full_body_ref.png inspected. Shared kite corner is the real tether attachment; keep its asymmetry.

Kite skier: distinguish the reaching arm from the curved backward-leaning torso and bend both legs into the skiing action. Radius4 head (11,15), shoulder (11,27), exact4 painted clearance and vertical torso tangent. Original reference and full_body_ref.png inspected. Shared kite corner is the real tether attachment; keep its asymmetry.

A skier leans back on two short upturned skis while reaching toward a kite above the right side. An angular tether connects the hands to the curved triangular kite.

Curved kite, tether, leaning skier and upturned ski end retained. The overlapping skis use one shared silhouette; extra rigging is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '580efdc2-15e9-4ed3-a2ce-d59eca2c1be1'
SOURCE_PATH = 'pictographic-primitives/sports/kite skiing_580efdc2-15e9-4ed3-a2ce-d59eca2c1be1.svg'
AUTHOR = 'gpt-6'

class KiteSkier(Solo48):
    icon_id = 'kite-skier'
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
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'kite',(26,6),('A',16,16,True,(42,22)),('L',(26,22)),('L',(26,6)),closed=True)
        path(self,'head',(7,14),('A',4,4,True,(15,14)),('A',4,4,True,(7,14)),closed=True)
        path(self,'torso',(11,26),('C',(11,29),(15,31),(15,34)))
        poly(self,'arm',(11,26),(20,26),(26,22))
        line(self,'rear-leg',(15,34),(10,42))
        poly(self,'front-leg',(15,34),(23,34),(27,42))
        poly(self,'ski',(6,42),(10,42),(27,42),(32,38))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')

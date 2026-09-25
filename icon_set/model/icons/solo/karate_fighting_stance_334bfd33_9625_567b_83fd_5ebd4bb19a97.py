# Repair: Level the guard and open the arm-to-thigh gap while preserving the fighting stance.
"""Karate guard: enlarged radius-5 circular head at (24,11), shoulder (24,24), exactly4 painted clearance. Torso curve starts vertically at shoulder, matching head axis; wide bent knees and raised fist preserve the original fighting stance. Human references full_body_ref.png and approved approaching-ball comparison; Lucide person-standing shared limb joints.

Karate guard: enlarged radius-5 circular head at (24,11), shoulder (24,24), exactly4 painted clearance. Torso arc radius10 starts vertically at shoulder, matching head axis; wide bent knees and raised fist preserve the original fighting stance. Human references full_body_ref.png and approved approaching-ball comparison; Lucide person-standing shared limb joints.

A martial artist stands with legs spread and knees bent, turning the torso slightly to the right. One arm guards across the chest while the other bends upward in front.

Bent knees, spread feet and raised guarding fist retained; garment folds and doubled outlines omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '334bfd33-9625-567b-83fd-5ebd4bb19a97'
SOURCE_PATH = 'pictographic-primitives/sports/martial arts karate_334bfd33-9625-567b-83fd-5ebd4bb19a97.svg'
AUTHOR = 'gpt-6'

class KarateFightingStance(Solo48):
    icon_id = 'karate-fighting-stance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('karate', 'martial', 'stance', 'combat', 'athlete', 'sport')

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
        """Karate guard: enlarged radius-5 circular head at (24,11), shoulder (24,24), exactly4 painted clearance. Torso curve starts vertically at shoulder, matching head axis; wide bent knees and raised fist preserve the original fighting stance. Human references full_body_ref.png and approved approaching-ball comparison; Lucide person-standing shared limb joints."""
        self.ring('head', 24, 11, 5)
        self.add_bezier('torso', (24, 24), ((24, 27), (20, 29), (20, 32)))
        self.branches([('guard-left', [(24, 24), (14, 24), (6, 21)]), ('guard-right', [(24, 24), (36, 26), (39, 17), (42, 17)]), ('leg-left', [(20, 32), (12, 35), (6, 42)]), ('leg-right', [(20, 32), (33, 35), (38, 42)])])
        for name in ['guard-left-0', 'guard-right-0', 'leg-left-0', 'leg-right-0']:
            self.relate('connect', 'torso', name)
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')

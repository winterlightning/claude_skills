"""Hang-glider pilot: move the harness to the actual chest and give the prone torso a horizontal tangent toward the head. Radius3 head(38,27), shoulder(27,27), exact11 center distance and4 painted clearance. The arm descends from that shoulder and extends forward; the leg trails behind. Source prone pilot and full_body_ref.png inspected; the wing retains its deliberate triangular asymmetry.

Hang Glider, independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '46124d39-e8cc-47e1-a905-ab2eb126c524'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__triangular-hang-glider/20260927T101610Z-thuan-mac-1/reference/sport paragliding_46124d39-e8cc-47e1-a905-ab2eb126c524.svg'
AUTHOR = 'gpt-6'

class TriangularHangGlider(Solo48):
    icon_id = 'triangular-hang-glider'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('hang', 'glider', 'pilot', 'flight', 'wing', 'sport')

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
        """Hang-glider pilot: move the harness to the actual chest and give the prone torso a horizontal tangent toward the head. Radius3 head(38,27), shoulder(27,27), exact11 center distance and4 painted clearance. The arm descends from that shoulder and extends forward; the leg trails behind. Source prone pilot and full_body_ref.png inspected; the wing retains its deliberate triangular asymmetry."""
        self.branches([('wing', [(4, 8), (44, 14), (24, 18), (12, 24), (4, 8)]), ('harness', [(24, 18), (27, 27)]), ('arm', [(27, 27), (27, 38), (42, 40)]), ('leg', [(17, 31), (8, 40)])])
        self.ring('head', 38, 27, 3)
        self.add_bezier('torso', (27, 27), ((23, 27), (21, 29), (17, 31)))
        for p in ['harness-0', 'arm-0', 'leg-0']:
            self.relate('connect', 'torso', p)

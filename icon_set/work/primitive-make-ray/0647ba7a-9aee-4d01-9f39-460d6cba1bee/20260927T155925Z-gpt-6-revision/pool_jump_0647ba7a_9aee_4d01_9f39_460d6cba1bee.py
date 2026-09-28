# Repair: Open the tuck between the raised arm and bent thigh while keeping the pool-edge clearance.
"""Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Pool Jump, independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0647ba7a-9aee-4d01-9f39-460d6cba1bee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pool-jump/20260927T153747Z-thuan-mac-1/reference/swimming jump_0647ba7a-9aee-4d01-9f39-460d6cba1bee.svg'
AUTHOR = "gpt-6"

class PoolJump(Solo48):
    icon_id = 'pool-jump'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('pool', 'jump', 'swimmer', 'water', 'diving', 'sport')

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
        # Bent swimmer launches beside a short pool edge into open rippling water.
        self.add_arc('head-top', (31, 18), (41, 18), radius_x=5)
        self.add_arc('head-bottom', (41, 18), (31, 18), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body-upper', (16, 6), (24, 23))
        self.add_bezier('body-middle', (24, 23), ((20, 24), (15, 22), (10, 26)))
        self.add_polyline('legs', (10, 26), (23, 31), (20, 31))
        self.add_line('arm', (24, 23), (12, 13))
        self.add_polyline('edge', (6, 42), (14, 42))
        self.add_polyline('water', (14, 42), (21, 40), (28, 42), (35, 40), (42, 42))
        for a,b in (('body-upper','body-middle'),('body-middle','legs'),('arm','body-upper'),('arm','body-middle'),('edge','water')):
            self.relate('connect',a,b)
        self.mark_human_figure('swimmer',head='head',torso='body-middle',torso_junction='start')

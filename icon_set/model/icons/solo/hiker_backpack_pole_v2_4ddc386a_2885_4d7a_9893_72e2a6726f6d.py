"""Reconstruct hiker backpack pole using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct hiker backpack pole using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Right-facing hiker with backpack, striding legs and held pole. Lucide person-standing and backpack inform a sparse articulated figure; double body outlines simplified to coherent strokes.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ddc386a-2885-4d7a-9893-72e2a6726f6d'
SOURCE_PATH = 'pictographic-primitives/symbol/trekking_4ddc386a-2885-4d7a-9893-72e2a6726f6d.svg'
AUTHOR = 'gpt-6'

class HikerBackpackPoleVariant2(Solo48):
    icon_id = 'hiker-backpack-pole-v2'
    variant_of = 'hiker-backpack-pole'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('hiking', 'trekking', 'hiker', 'backpack', 'walking', 'outdoors', 'mountain', 'adventure')

    def oval(self, n, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(n + '-top', (cx - rx, cy), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc(n + '-bottom', (cx + rx, cy), (cx - rx, cy), radius_x=rx, radius_y=ry)
        self.add_contour(n, n + '-top', n + '-bottom', closed=True)

    def raw(self, n, points):
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(n + '-' + str(j), a, b)

    def path(self, n, points, closed=False):
        self.add_polyline(n, *points, closed=closed)

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
        """Reconstruct hiker backpack pole using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (24, 11), (34, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (34, 11), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('body-1', (24, 23), *(((22.6, 26.36), (21.0, 29.75), (20, 32)),))
        self.add_line('body-2', (20, 32), (6, 42))
        self.add_line('front-leg-1', (20, 32), (30, 34))
        self.add_line('front-leg-2', (30, 34), (34, 42))
        self.add_line('pack-1', (14, 19), (24, 23))
        self.add_bezier('pack-2', (24, 23), *(((22.6, 26.36), (21.0, 29.75), (20, 32)),))
        self.add_line('pack-3', (20, 32), (10, 27))
        self.add_line('pack-4', (10, 27), (14, 19))
        self.add_line('arm-1', (24, 23), (32, 28))
        self.add_line('arm-2', (32, 28), (42, 28))
        self.add_line('pole-1', (42, 16), (42, 28))
        self.add_line('pole-2', (42, 28), (42, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('body', *('body-1', 'body-2'), closed=False)
        self.add_contour('front-leg', *('front-leg-1', 'front-leg-2'), closed=False)
        self.add_contour('pack', *('pack-1', 'pack-2', 'pack-3', 'pack-4'), closed=True)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('pole', *('pole-1', 'pole-2'), closed=False)
        self.relate('connect', *('body', 'front-leg'))
        self.relate('connect', *('pack', 'body'))
        self.relate('connect', *('arm', 'body'))
        self.relate('connect', *('arm', 'pack'))
        self.relate('connect', *('pole', 'arm'))

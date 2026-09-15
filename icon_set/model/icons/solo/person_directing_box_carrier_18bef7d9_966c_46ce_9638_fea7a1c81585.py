"""Center each radius4 head over its own shoulder at y22, with head centers y10 and exact4 painted clearance. The pointing person and box carrier remain distinct. Original scene and full_body_ref.png inspected; both heads share radius and vertical spacing. Curve the carrier upper torso so its tangent aligns with its own head.

Center each radius4 head over its own shoulder at y22, with head centers y10 and exact4 painted clearance. The pointing person and box carrier remain distinct. Original scene and full_body_ref.png inspected; both heads share radius and vertical spacing.

A person carrying a rectangular box walks left with a lowered head. A second figure stands behind on the right, extending one arm horizontally toward the departing worker.
Lucide user circles and shared limb joints. Box carrier and pointing director remain distinct figures; hands, feet outlines and clothing omitted. Leftward departure retained.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18bef7d9-966c-46ce-9638-fea7a1c81585'
SOURCE_PATH = 'pictographic-primitives/work/worker lay off fired user finger box_18bef7d9-966c-46ce-9638-fea7a1c81585.svg'
AUTHOR = 'gpt-6'

class PersonDirectingBoxCarrier(Solo48):
    icon_id = 'person-directing-box-carrier'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('person', 'box', 'worker', 'leaving', 'dismissal', 'carrying')

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
        """Center each radius4 head over its own shoulder at y22, with head centers y10 and exact4 painted clearance. The pointing person and box carrier remain distinct. Original scene and full_body_ref.png inspected; both heads share radius and vertical spacing. Curve the carrier upper torso so its tangent aligns with its own head."""
        self.add_arc('carrier-head-a', (14, 10), (22, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('carrier-head-b', (22, 10), (14, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('director-head-a', (32, 10), (40, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('director-head-b', (40, 10), (32, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('box-1', (6, 24), (16, 24))
        self.add_line('box-2', (16, 24), (16, 32))
        self.add_line('box-3', (16, 32), (6, 32))
        self.add_line('box-4', (6, 32), (6, 24))
        self.add_bezier('carrier-1', (18, 22), *(((18, 26), (23, 29), (24, 32)),))
        self.add_line('carrier-2', (24, 32), (18, 42))
        self.add_line('back-leg', (24, 32), (28, 42))
        self.add_line('carrying-arm', (18, 22), (16, 32))
        self.add_line('director-1', (36, 22), (36, 42))
        self.add_line('director-2', (36, 42), (42, 42))
        self.add_line('pointing-arm', (36, 22), (18, 22))
        self.add_contour('carrier-head', *('carrier-head-a', 'carrier-head-b'), closed=True)
        self.add_contour('director-head', *('director-head-a', 'director-head-b'), closed=True)
        self.add_contour('box', *('box-1', 'box-2', 'box-3', 'box-4'), closed=True)
        self.add_contour('carrier', *('carrier-1', 'carrier-2'), closed=False)
        self.add_contour('director', *('director-1', 'director-2'), closed=False)
        self.relate('connect', *('back-leg', 'carrier'))
        self.relate('connect', *('carrying-arm', 'carrier'))
        self.relate('connect', *('carrying-arm', 'box'))
        self.relate('connect', *('pointing-arm', 'director'))
        self.relate('connect', *('pointing-arm', 'carrier'))
        self.relate('connect', *('pointing-arm', 'carrying-arm'))

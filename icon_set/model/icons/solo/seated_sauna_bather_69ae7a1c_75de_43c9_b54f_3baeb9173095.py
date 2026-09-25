"""Seated bather: radius5 head (14,11), shoulder (14,24), exact4 gap. Arm at24, lap32 and bench40 each leave8 centerline units; preserve the bent legs and heat wisps.

Seated bather: radius5 head (14,11), shoulder (14,24), exact4 gap. Arm at24, lap32 and bench40 each leave8 centerline units; preserve the bent legs and heat wisps.

Reconstruct seated sauna bather using its inspected source pose and full_body_ref.png. Head radius 5, center (14, 11), actual torso junction (14, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Keep the raised hand separate from the lap.

Reconstruct seated sauna bather using its inspected source pose and full_body_ref.png. Head radius 5, center (14, 11), actual torso junction (14, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct seated sauna bather using its inspected source pose and full_body_ref.png. Head radius 5, center (14, 11), actual torso junction (14, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Seated person facing right with heat and low bench. Square extremes 6,6–42,42. Lucide user-round circular head; intentional profile asymmetry; one heat wisp, one leg and simplified arm."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '69ae7a1c-75de-43c9-b54f-3baeb9173095'
SOURCE_PATH = 'pictographic-primitives/spas/sauna heat person_69ae7a1c-75de-43c9-b54f-3baeb9173095.svg'
AUTHOR = 'gpt-6'

class SeatedSaunaBather(Solo48):
    icon_id = 'seated-sauna-bather'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    categories = ('primitives', 'spas')
    aliases = ()
    keywords = ('spa', 'wellness', 'seated-sauna-bather')

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
        """Seated bather: radius5 head (14,11), shoulder (14,24), exact4 gap. Arm at24, lap32 and bench40 each leave8 centerline units; preserve the bent legs and heat wisps."""
        self.add_arc('head-a', (9, 11), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (19, 11), (9, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('person-1', (14, 24), *(((14, 27), (14, 30), (14, 32)),))
        self.add_line('person-2', (14, 32), (30, 32))
        self.add_line('person-3', (30, 32), (36, 42))
        self.add_line('arm', (14, 24), (25, 24))
        self.add_line('bench-1', (6, 42), (6, 40))
        self.add_line('bench-2', (6, 40), (23, 40))
        self.add_line('bench-3', (23, 40), (23, 42))
        self.add_arc('heat-top', (40, 6), (40, 14), radius_x=2, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('heat-bottom', (40, 14), (40, 22), radius_x=2, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('bench', *('bench-1', 'bench-2', 'bench-3'), closed=False)
        self.add_contour('heat', *('heat-top', 'heat-bottom'), closed=False)
        self.add_contour('person', *('person-1',), closed=False)
        self.add_contour('person-section-1', *('person-2', 'person-3'), closed=False)
        self.relate('connect', *('person', 'arm'))
        self.relate('connect', *('person-1', 'person-2'))
        self.relate('connect', *('person-2', 'person-3'))
        self.relate('connect', *('head-a', 'head-b'))
        self.relate('connect', *('person-1', 'person-2'))
        self.relate('connect', *('person-1', 'arm'))
        self.relate('connect', *('person-2', 'person-3'))
        self.relate('connect', *('bench-1', 'bench-2'))
        self.relate('connect', *('bench-2', 'bench-3'))
        self.relate('connect', *('heat-top', 'heat-bottom'))

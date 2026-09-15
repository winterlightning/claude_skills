# Repair: Lower the skis away from the seated thigh and keep the boot on the ski.
"""Reconstruct skier chairlift using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 10), actual torso junction (12, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct skier chairlift using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 10), actual torso junction (12, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Skier on Chairlift, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '866aaa81-68b6-4d73-8186-65f79fe8a1e7'
SOURCE_PATH = 'pictographic-primitives/sports/skiing cable car_866aaa81-68b6-4d73-8186-65f79fe8a1e7.svg'
AUTHOR = 'gpt-6'

class SkierChairlift(Solo48):
    icon_id = 'skier-chairlift'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('ski', 'chairlift', 'skier', 'lift', 'snow', 'winter')

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
        """Reconstruct skier chairlift using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 10), actual torso junction (12, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (8, 10), (16, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (16, 10), (8, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('rider-1', (12, 22), *(((12.0, 25.36), (13.5, 29.5), (14, 32)),))
        self.add_line('rider-2', (14, 32), (29, 32))
        self.add_line('rider-3', (29, 32), (35, 40))
        self.add_line('arm-1', (12, 22), (23, 23))
        self.add_line('arm-2', (23, 23), (32, 23))
        self.add_line('suspension-1', (32, 6), (32, 16))
        self.add_line('suspension-2', (32, 16), (32, 23))
        self.add_line('seat', (6, 32), (14, 32))
        self.add_line('ski-1', (12, 42), (35, 40))
        self.add_line('ski-2', (35, 40), (42, 37))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('suspension', *('suspension-1', 'suspension-2'), closed=False)
        self.add_contour('ski', *('ski-1', 'ski-2'), closed=False)
        self.relate('connect', *('rider', 'arm'))
        self.relate('connect', *('arm', 'suspension'))
        self.relate('connect', *('seat', 'rider'))
        self.relate('connect', *('rider', 'ski'))
        self.add_contour('rider', *('rider-1',), closed=False)
        self.add_contour('rider-section-1', *('rider-2', 'rider-3'), closed=False)
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-1', 'arm-1')
        self.relate('connect', 'rider-1', 'seat')
        self.relate('connect', 'rider-2', 'rider-3')
        self.relate('connect', 'rider-2', 'seat')
        self.relate('connect', 'rider-3', 'ski-1')
        self.relate('connect', 'rider-3', 'ski-2')
        self.relate('connect', 'arm-1', 'arm-2')
        self.relate('connect', 'arm-2', 'suspension-2')
        self.relate('connect', 'suspension-1', 'suspension-2')
        self.relate('connect', 'ski-1', 'ski-2')
        self.mark_human_figure('person', head='head', torso='rider-1', torso_junction='start')

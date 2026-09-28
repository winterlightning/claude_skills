"""Reconstruct snow scooter rider using its inspected source pose and full_body_ref.png. Head radius 5, center (25, 11), actual torso junction (20, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct snow scooter rider using its inspected source pose and full_body_ref.png. Head radius 5, center (25, 11), actual torso junction (20, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct snow scooter rider using its inspected source pose and full_body_ref.png. Head radius 5, center (25, 11), actual torso junction (20, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Snow Scooter Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87213404-4655-52bf-a1d8-6be4687cfea8'
SOURCE_PATH = 'pictographic-primitives/sports/skiing snow scooter person_87213404-4655-52bf-a1d8-6be4687cfea8.svg'
AUTHOR = 'gpt-6'

class SnowScooterRider(Solo48):
    icon_id = 'snow-scooter-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('snow', 'scooter', 'rider', 'winter', 'handlebar', 'sport')

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
        """Reconstruct snow scooter rider using its inspected source pose and full_body_ref.png. Head radius 5, center (25, 11), actual torso junction (20, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (20, 11), (30, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (30, 11), (20, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('body-1', (20, 23), *(((18.6, 26.36), (14.0, 26.75), (12, 28)),))
        self.add_line('body-2', (12, 28), (20, 33))
        self.add_line('body-3', (20, 33), (17, 40))
        self.add_line('arms-1', (20, 23), (27, 26))
        self.add_line('arms-2', (27, 26), (38, 25))
        self.add_line('stem-1', (39, 20), (38, 25))
        self.add_line('stem-2', (38, 25), (30, 42))
        self.add_line('runner-1', (6, 38), (17, 40))
        self.add_line('runner-2', (17, 40), (30, 42))
        self.add_line('runner-3', (30, 42), (36, 42))
        self.add_line('runner-4', (36, 42), (42, 36))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('stem', *('stem-1', 'stem-2'), closed=False)
        self.add_contour('runner', *('runner-1', 'runner-2', 'runner-3', 'runner-4'), closed=False)
        self.relate('connect', *('body', 'arms'))
        self.relate('connect', *('arms', 'stem'))
        self.relate('connect', *('body', 'runner'))
        self.relate('connect', *('stem', 'runner'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2', 'body-3'), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-1', 'arms-1')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'body-3', 'runner-1')
        self.relate('connect', 'body-3', 'runner-2')
        self.relate('connect', 'arms-1', 'arms-2')
        self.relate('connect', 'arms-2', 'stem-1')
        self.relate('connect', 'arms-2', 'stem-2')
        self.relate('connect', 'stem-1', 'stem-2')
        self.relate('connect', 'stem-2', 'runner-2')
        self.relate('connect', 'stem-2', 'runner-3')
        self.relate('connect', 'runner-1', 'runner-2')
        self.relate('connect', 'runner-2', 'runner-3')
        self.relate('connect', 'runner-3', 'runner-4')

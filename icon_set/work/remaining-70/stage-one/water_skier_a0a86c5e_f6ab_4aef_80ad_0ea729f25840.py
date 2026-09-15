# Repair: Lower the ski knee away from the towing arm.
"""Water skier: radius4 head (15,12), shoulder (15,24), exact4 gap. Lower the raised knee to open the trapped recess under the towing arm; retain both upturned ski curves.

Reconstruct water skier using its inspected source pose and full_body_ref.png. Head radius 4, center (15, 12), actual torso junction (15, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct water skier using its inspected source pose and full_body_ref.png. Head radius 4, center (15, 12), actual torso junction (15, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct water skier using its inspected source pose and full_body_ref.png. Head radius 4, center (15, 12), actual torso junction (15, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Water Skier, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH = 'pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
AUTHOR = 'gpt-6'

class WaterSkier(Solo48):
    icon_id = 'water-skier'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('water', 'skier', 'skiing', 'rider', 'glide', 'sport')

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
        """Water skier: radius4 head (15,12), shoulder (15,24), exact4 gap. Lower the raised knee to open the trapped recess under the towing arm; retain both upturned ski curves."""
        self.add_arc('head-a', (11, 12), (19, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (19, 12), (11, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('body-1', (15, 24), *(((15.0, 26.82842712474619), (14.25, 29.25), (14, 32)),))
        self.add_line('body-2', (14, 32), (22, 33))
        self.add_line('body-3', (22, 33), (24, 34))
        self.add_line('arm-1', (6, 27), (15, 24))
        self.add_line('arm-2', (15, 24), (30, 24))
        self.add_line('arm-3', (30, 24), (44, 21))
        self.add_arc('ski-left', (4, 34), (24, 34), radius_x=10, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('ski-right', (24, 34), (44, 34), radius_x=10, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arm', *('arm-1', 'arm-2', 'arm-3'), closed=False)
        self.add_contour('ski', *('ski-left', 'ski-right'), closed=False)
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2', 'body-3'), closed=False)
        self.relate('connect', *('arm', 'body'))
        self.relate('connect', *('ski', 'body'))
        self.relate('connect', *('body-1', 'body-2'))
        self.relate('connect', *('body-2', 'body-3'))
        self.relate('connect', *('head-a', 'head-b'))
        self.relate('connect', *('body-1', 'body-2'))
        self.relate('connect', *('body-1', 'arm-1'))
        self.relate('connect', *('body-1', 'arm-2'))
        self.relate('connect', *('body-2', 'body-3'))
        self.relate('connect', *('body-3', 'ski-left'))
        self.relate('connect', *('body-3', 'ski-right'))
        self.relate('connect', *('arm-1', 'arm-2'))
        self.relate('connect', *('arm-2', 'arm-3'))
        self.relate('connect', *('ski-left', 'ski-right'))

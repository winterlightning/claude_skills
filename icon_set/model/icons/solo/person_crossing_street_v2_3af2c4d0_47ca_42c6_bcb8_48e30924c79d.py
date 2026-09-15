"""Reconstruct person crossing street using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person crossing street using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person walks toward the right with one knee bent and the arms swinging apart. Two pairs of short slanted road markings flank the legs to suggest a crossing.

Construction: Walking figure above two road crossing stripes. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3af2c4d0-47ca-42c6-bcb8-48e30924c79d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking cross street_3af2c4d0-47ca-42c6-bcb8-48e30924c79d.svg'
AUTHOR = 'gpt-6'

class PersonCrossingStreetVariant2(Solo48):
    icon_id = 'person-crossing-street-v2'
    variant_of = 'person-crossing-street'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'crossing', 'street', 'walking', 'pedestrian', 'road')

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
        """Reconstruct person crossing street using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('person-head-a', (24, 11), (34, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('person-head-b', (34, 11), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('person-body-1', (24, 23), *(((23.02699148917896, 25.335220425970498), (22.5, 27.5), (22, 29)),))
        self.add_line('person-arms-1', (12, 27), (24, 23))
        self.add_line('person-arms-2', (24, 23), (36, 28))
        self.add_line('person-legs-1', (14, 39), (22, 29))
        self.add_line('person-legs-2', (22, 29), (31, 39))
        self.add_line('stripe-left', (6, 34), (6, 42))
        self.add_line('stripe-right', (42, 34), (42, 42))
        self.add_contour('person-head', *('person-head-a', 'person-head-b'), closed=True)
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))

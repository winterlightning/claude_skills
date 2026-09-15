"""Rebalance the diagonal hull with matched tangent controls and a broader middle section; remove the unequal bow/stern curvature while preserving the paddle and cockpit arrangement.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a056c9dc-e8dd-5493-9902-c9d72635972e'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_a056c9dc-e8dd-5493-9902-c9d72635972e.svg'
AUTHOR = 'gpt-6'

class KayakCockpitPaddle(Solo48):
    icon_id = 'kayak-cockpit-paddle-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('kayak', 'paddle', 'cockpit', 'canoe', 'boat', 'water sports', 'paddling', 'outdoor')

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
        """Diagonal kayak and matching teardrop paddle blades reconstructed from the original source and the inspected Lucide kayak original/atomic-debug. Shared bow/stern and shaft nodes preserve exact contacts. The cockpit variant uses a larger elliptical opening and shows the shaft outside the raised cockpit rim; the center portion is occluded by the seat. Deliberate diagonal orientation fits the complete subject on SQUARE without broken paddle tips."""
        self.add_bezier('hull-upper-left', (42, 6), ((30, 6), (20, 8), (14, 14)))
        self.add_bezier('hull-lower-left', (14, 14), ((8, 20), (6, 30), (6, 42)))
        self.add_bezier('hull-lower-right', (6, 42), ((18, 42), (28, 40), (34, 34)))
        self.add_bezier('hull-upper-right', (34, 34), ((40, 28), (42, 18), (42, 6)))
        self.add_contour('hull', 'hull-upper-left', 'hull-lower-left', 'hull-lower-right', 'hull-upper-right', closed=True)
        self.add_arc('blade-nw', (14, 10), (10, 14), radius_x=4, large_arc=True, sweep=False)
        self.add_line('blade-nw-base', (10, 14), (14, 14))
        self.add_line('blade-nw-side', (14, 14), (14, 10))
        self.add_contour('blade-left', 'blade-nw', 'blade-nw-base', 'blade-nw-side', closed=True)
        self.add_arc('blade-se', (34, 38), (38, 34), radius_x=4, large_arc=True, sweep=False)
        self.add_line('blade-se-base', (38, 34), (34, 34))
        self.add_line('blade-se-side', (34, 34), (34, 38))
        self.add_contour('blade-right', 'blade-se', 'blade-se-base', 'blade-se-side', closed=True)
        self.relate('connect', 'hull', 'blade-left')
        self.relate('connect', 'hull', 'blade-right')
        k = 0.5522847498307936
        self.add_bezier('cockpit-ne', (20, 20), ((20 + 6 * k, 20 - 6 * k), (30 - 4 * k, 18 - 4 * k), (30, 18)))
        self.add_bezier('cockpit-se', (30, 18), ((30 + 4 * k, 18 + 4 * k), (28 + 6 * k, 28 - 6 * k), (28, 28)))
        self.add_bezier('cockpit-sw', (28, 28), ((28 - 6 * k, 28 + 6 * k), (18 + 4 * k, 30 + 4 * k), (18, 30)))
        self.add_bezier('cockpit-nw', (18, 30), ((18 - 4 * k, 30 - 4 * k), (20 - 6 * k, 20 + 6 * k), (20, 20)))
        self.add_contour('cockpit', 'cockpit-ne', 'cockpit-se', 'cockpit-sw', 'cockpit-nw', closed=True)
        self.add_line('shaft-left', (14, 14), (20, 20))
        self.add_line('shaft-right', (28, 28), (34, 34))
        for name in ['shaft-left', 'shaft-right']:
            self.relate('connect', name, 'hull')
            self.relate('connect', name, 'cockpit')
        self.relate('connect', 'shaft-left', 'blade-left')
        self.relate('connect', 'shaft-right', 'blade-right')
    variant_of = 'kayak-cockpit-paddle'
    variant_label = 'Batch 01 centerline repair'

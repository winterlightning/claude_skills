"""Rebalance the diagonal hull with matched tangent controls and a broader middle section; remove the unequal bow/stern curvature while preserving the paddle and cockpit arrangement.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a66c4e2-1e93-4712-9eb5-ab0c546777d9'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_7a66c4e2-1e93-4712-9eb5-ab0c546777d9.svg'
AUTHOR = 'gpt-6'

class KayakWithPaddle(Solo48):
    icon_id = 'kayak-with-paddle-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('kayak', 'paddle', 'canoe', 'boat', 'water sports', 'rowing', 'river', 'outdoor')

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
        self.add_line('shaft', (14, 14), (34, 34))
        self.relate('connect', 'shaft', 'hull')
        self.relate('connect', 'shaft', 'blade-left')
        self.relate('connect', 'shaft', 'blade-right')
    variant_of = 'kayak-with-paddle'
    variant_label = 'Batch 01 centerline repair'

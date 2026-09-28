"""Diagonal kayak and matching teardrop paddle blades reconstructed from the original source and the inspected Lucide kayak original/atomic-debug. Shared bow/stern and shaft nodes preserve exact contacts. The cockpit variant uses a larger elliptical opening and shows the shaft outside the raised cockpit rim; the center portion is occluded by the seat. Deliberate diagonal orientation fits the complete subject on SQUARE without broken paddle tips.

Horizontal pointed kayak with a full double-ended paddle above it; keep the elongated cockpit in the cockpit variant. All four hull quarters share smooth tangents at the widest points. Source kayak and Lucide sailboat inspected; the horizontal layout preserves complete paddle blades without trapping wedges against the hull.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Kayak with Cockpit and Paddle, re-authored from its reference on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a056c9dc-e8dd-5493-9902-c9d72635972e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kayak-cockpit-paddle/20260927T082307Z-thuan-mac-1/reference/kayak_a056c9dc-e8dd-5493-9902-c9d72635972e.svg'
AUTHOR = "gpt-6"

class KayakCockpitPaddle(Solo48):
    icon_id = 'kayak-cockpit-paddle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
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

    def build(self) -> None:
        self.add_arc('boat-upper-left', (24, 6), (12, 24), radius_x=60, radius_y=30, sweep=False)
        self.add_arc('boat-lower-left', (12, 24), (24, 42), radius_x=60, radius_y=30, sweep=False)
        self.add_arc('boat-lower-right', (24, 42), (36, 24), radius_x=60, radius_y=30, sweep=False)
        self.add_arc('boat-upper-right', (36, 24), (24, 6), radius_x=60, radius_y=30, sweep=False)
        self.add_contour('boat', 'boat-upper-left', 'boat-lower-left', 'boat-lower-right', 'boat-upper-right', closed=True)
        self.add_arc('cockpit-top', (20, 24), (28, 24), radius_x=4, radius_y=6, sweep=True)
        self.add_arc('cockpit-bottom', (28, 24), (20, 24), radius_x=4, radius_y=6, sweep=True)
        self.add_contour('cockpit', 'cockpit-top', 'cockpit-bottom', closed=True)
        self.add_line('paddle-left-1', (12, 24), (6, 36))
        self.add_line('paddle-left-2', (6, 36), (6, 42))
        self.add_contour('paddle-left', 'paddle-left-1', 'paddle-left-2', closed=False)
        self.add_line('paddle-right-1', (36, 24), (42, 12))
        self.add_line('paddle-right-2', (42, 12), (42, 6))
        self.add_contour('paddle-right', 'paddle-right-1', 'paddle-right-2', closed=False)
        self.relate("connect", 'boat', 'paddle-left')
        self.relate("connect", 'boat', 'paddle-right')

"""Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Kayak with Cockpit and Paddle, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a056c9dc-e8dd-5493-9902-c9d72635972e'
SOURCE_PATH = 'pictographic-primitives/transportation/kayak_a056c9dc-e8dd-5493-9902-c9d72635972e.svg'
AUTHOR = 'gpt-6'

class KayakCockpitPaddleVariant2(Solo48):
    icon_id = 'kayak-cockpit-paddle-v2'
    variant_of = 'kayak-cockpit-paddle'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.HRECT_L
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
        """Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry."""
        axis = 16
        for name, top in [('upper', 8), ('lower', 28)]:
            self.add_arc(name + '-t1', (36, top + 4), (40, top), radius_x=4)
            self.add_arc(name + '-t2', (40, top), (44, top + 4), radius_x=4)
            self.add_line(name + '-r', (44, top + 4), (44, top + 8))
            self.add_arc(name + '-base', (44, top + 8), (40, top + 12), radius_x=4)
            self.add_arc(name + '-bl', (40, top + 12), (36, top + 8), radius_x=4)
            self.add_line(name + '-l', (36, top + 8), (36, top + 4))
            self.add_contour(name, name + '-t1', name + '-t2', name + '-r', name + '-base', name + '-bl', name + '-l', closed=True)
        self.add_line('shaft', (40, 20), (40, 28))
        self.relate('connect', 'shaft', 'upper')
        self.relate('connect', 'shaft', 'lower')
        self.add_bezier('hull-rt', (17, 8), ((25, 14), (30, 18), (30, 24)))
        self.add_bezier('hull-rb', (30, 24), ((30, 30), (25, 34), (17, 40)))
        self.add_bezier('hull-lb', (17, 40), ((9, 34), (4, 30), (4, 24)))
        self.add_bezier('hull-lt', (4, 24), ((4, 18), (9, 14), (17, 8)))
        self.add_contour('hull', 'hull-rt', 'hull-rb', 'hull-lb', 'hull-lt', closed=True)
        self.add_arc('cockpit-r', (17, 18), (17, 30), radius_x=4, radius_y=6)
        self.add_arc('cockpit-l', (17, 30), (17, 18), radius_x=4, radius_y=6)
        self.add_contour('cockpit', 'cockpit-r', 'cockpit-l', closed=True)

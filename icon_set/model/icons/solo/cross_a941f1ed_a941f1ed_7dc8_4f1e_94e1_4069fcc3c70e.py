"""Medical cross with four equal arms and consistently rounded outer corners."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e'
SOURCE_PATH = 'pictographic-primitives/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.svg'
AUTHOR = 'gpt-6'

class CrossA941f1ed(Solo48):
    icon_id = 'cross-a941f1ed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('cross', 'health')

    def build(self):
        # Plan: four identical arms rotated about (24,24). SQUARE centerline
        # extremes (6,6)-(42,42); arm width 12, outer radius 2.
        # Lucide cross: repeated tangent quarter-circle corners.
        axis, arm, low, high, radius = 24, 6, 6, 42, 2
        def rotate(p, turn):
            x, y = p
            for _ in range(turn):
                x, y = 2 * axis - y, x
            return x, y
        parts = []
        for turn in range(4):
            points = [(axis-arm, axis-arm), (axis-arm, low+radius),
                      (axis-arm+radius, low), (axis+arm-radius, low),
                      (axis+arm, low+radius), (axis+arm, axis-arm)]
            points = [rotate(p, turn) for p in points]
            for i, (a, b) in enumerate(zip(points, points[1:])):
                name = f'arm-{turn}-{i}'
                if i in (1, 3):
                    self.add_arc(name, a, b, radius_x=radius)
                else:
                    self.add_line(name, a, b)
                parts.append(name)
        self.add_contour('cross-outline', *parts, closed=True)

"""Three repeated elliptical orbits rotated by 60 degrees, sharing every true crossing node, around a central dot. Lucide atom informs smooth cubic loops. Parameters own all repeated geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd36538a0-eba4-47cf-8fa5-4782d3bb6574'
SOURCE_PATH = 'pictographic-primitives/logos/react native logo_d36538a0-eba4-47cf-8fa5-4782d3bb6574.svg'
AUTHOR = 'gpt-6'

class ReactLogo(Solo48):
    icon_id = 'react-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('react', 'react-native', 'atom', 'javascript', 'logo', 'brand', 'developer')

    def build(self):
        """Narrow the repeated elliptical orbits together to rebalance all six counters without breaking rotation symmetry."""
        import math
        rx, ry = (20, 10)
        angles = [0, math.pi / 3, 2 * math.pi / 3]

        def polar_radius(theta, a):
            return 1 / math.sqrt((math.cos(theta - a) / rx) ** 2 + (math.sin(theta - a) / ry) ** 2)

        def xy(a, t):
            return (rx * math.cos(t) * math.cos(a) - ry * math.sin(t) * math.sin(a), rx * math.cos(t) * math.sin(a) + ry * math.sin(t) * math.cos(a))

        def tangent(a, t):
            return (-rx * math.sin(t) * math.cos(a) - ry * math.cos(t) * math.sin(a), -rx * math.sin(t) * math.sin(a) + ry * math.cos(t) * math.cos(a))
        for j, a in enumerate(angles):
            knots = [k * math.pi / 2 for k in range(4)]
            for b in angles:
                if a == b:
                    continue
                for k in range(4):
                    theta = (a + b) / 2 + k * math.pi / 2
                    rr = polar_radius(theta, a)
                    t = math.atan2(rr * math.sin(theta - a) / ry, rr * math.cos(theta - a) / rx) % (2 * math.pi)
                    knots.append(t)
            knots = sorted(set((round(t, 10) for t in knots)))
            points = [tuple((round(24 + v) for v in xy(a, t))) for t in knots]
            members = []
            for k, t in enumerate(knots):
                nxt = (k + 1) % len(knots)
                u = knots[nxt] + (2 * math.pi if nxt == 0 else 0)
                if points[k] == points[nxt]:
                    continue
                factor = 4 / 3 * math.tan((u - t) / 4)
                da, db = (tangent(a, t), tangent(a, u))
                c1 = tuple((points[k][z] + factor * da[z] for z in range(2)))
                c2 = tuple((points[nxt][z] - factor * db[z] for z in range(2)))
                name = f'orbit-{j}-{k}'
                members.append(name)
                self.add_bezier(name, points[k], (c1, c2, points[nxt]))
            self.add_contour(f'orbit-{j}', *members, closed=True)
        for a, b in [(0, 1), (0, 2), (1, 2)]:
            self.relate('connect', f'orbit-{a}', f'orbit-{b}')
        self.add_dot('nucleus', (24, 24))

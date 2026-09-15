"""Open the web into a taller six-spoke construction with one scalloped outer ring and no inner polygon; derive every spoke from the same center. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2907e972-c65a-5ccd-863c-542e656a809e'
SOURCE_PATH = 'pictographic-primitives/animals/spider web_2907e972-c65a-5ccd-863c-542e656a809e.svg'
AUTHOR = 'gpt-6'

class SpiderWebVariant2(Solo48):
    icon_id = 'spider-web-v2'
    variant_of = 'spider-web'
    variant_label = 'Open the web into a taller six-spoke construction with one scalloped outer ring and no inner polygon; derive every spoke from the same center.'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('spider', 'web', 'cobweb', 'hexagon', 'net', 'halloween', 'geometric', 'trap')

    def build(self):
        """Symbol plan: Open the web into a taller six-spoke construction with one scalloped outer ring and no inner polygon; derive every spoke from the same center. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        from itertools import combinations
        points = [(24, 4), (40, 12), (40, 36), (24, 44), (8, 36), (8, 12)]
        controls = [((28, 10), (34, 13)), ((33, 18), (33, 30)), ((34, 35), (28, 38)), ((20, 38), (14, 35)), ((15, 30), (15, 18)), ((14, 13), (20, 10))]
        nodes = []
        for j, (a, b) in enumerate(zip(points, points[1:] + points[:1])):
            c, d = controls[j]
            path(f'web-{j}', a, [('C', b, c, d)])
            line(f'ray-{j}', a, (24, 24))
            nodes.extend([(f'web-{j}', {a, b}), (f'ray-{j}', {a, (24, 24)})])
        for (a, p), (b, q) in combinations(nodes, 2):
            if p & q:
                join(a, b)

"""Replace the plain oval sheep body with broad wool scallops, a dropped oval head and two short legs attached to a level belly. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ea7bc336-5e90-4137-8f7c-a8a19de4d28f'
SOURCE_PATH = 'pictographic-primitives/animals/sheep body_ea7bc336-5e90-4137-8f7c-a8a19de4d28f.svg'
AUTHOR = 'gpt-6'

class WoollySheepVariant2(Solo48):
    icon_id = 'woolly-sheep-v2'
    variant_of = 'woolly-sheep'
    variant_label = 'Replace the plain oval sheep body with broad wool scallops, a dropped oval head and two short legs attached to a level belly.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/farm'
    aliases = ()
    keywords = ('sheep', 'wool', 'fluffy', 'farm', 'lamb', 'ewe', 'livestock', 'animal')

    def build(self):
        """Symbol plan: Replace the plain oval sheep body with broad wool scallops, a dropped oval head and two short legs attached to a level belly. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('fleece', (36, 26), [('C', (28, 38), (36, 34), (32, 38)), ('L', (16, 38)), ('C', (6, 26), (10, 38), (6, 32)), ('C', (12, 16), (6, 20), (8, 16)), ('C', (22, 10), (10, 10), (16, 6)), ('C', (28, 10), (24, 6), (28, 6))])
        path('head', (28, 10), [('C', (36, 26), (28, 18), (30, 26)), ('C', (42, 10), (40, 26), (42, 18)), ('C', (28, 10), (42, 6), (28, 6))], True)
        join('head', 'fleece')
        line('ear', (42, 10), (42, 6))
        join('ear', 'head')
        for x in [16, 28]:
            line('leg-' + str(x), (x, 38), (x, 42))
            join('leg-' + str(x), 'fleece')

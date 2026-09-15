"""Replace the flattened oval dust cloud with a smooth raised crown and round end curl; retain the long horizontal gust with a clear gap underneath.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7895f6a0-0d28-4ebd-9d17-c0b740f48b84'
SOURCE_PATH = 'pictographic-primitives/weather/dust storm_7895f6a0-0d28-4ebd-9d17-c0b740f48b84.svg'
AUTHOR = 'gpt-6'

class DustCloudGusts(Solo48):
    icon_id = 'dust-cloud-gusts-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('dust', 'cloud', 'wind', 'gust', 'storm', 'weather')
    variant_of = 'dust-cloud-gusts'
    variant_label = 'Batch 01 centerline repair'

    def build(self):

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, (kind, end, *args) in enumerate(commands):
                name = f'{n}-{j}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x, y - r), r, r, True), ('A', (x + r, y), r, r, True), ('A', (x, y + r), r, r, True), ('A', (x - r, y), r, r, True)], True)

        def rounded(n, x0, y0, x1, y1, r):
            path(n, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('cloud', (18, 22), [('C', (4, 16), (10, 22), (4, 20)), ('C', (18, 8), (4, 10), (10, 8)), ('C', (32, 14), (25, 8), (32, 10)), ('C', (44, 18), (39, 14), (44, 14)), ('C', (36, 22), (44, 21), (40, 22))])
        path('gust', (13, 30), [('A', (8, 35), 5, 5, False), ('A', (13, 40), 5, 5, False), ('L', (42, 40))])

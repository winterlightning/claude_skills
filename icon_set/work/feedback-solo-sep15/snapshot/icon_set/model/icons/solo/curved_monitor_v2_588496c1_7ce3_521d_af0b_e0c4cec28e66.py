"""Use continuous smooth screen curves and a single centered stand. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '588496c1-7ce3-521d-af0b-e0c4cec28e66'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/screen curved_588496c1-7ce3-521d-af0b-e0c4cec28e66.svg'
AUTHOR = 'gpt-6'

class CurvedMonitorVariant2(Solo48):
    icon_id = 'curved-monitor-v2'
    variant_of = 'curved-monitor'
    variant_label = 'Use continuous smooth screen curves and a single centered stand.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('monitor', 'curved', 'screen', 'display', 'widescreen', 'gaming', 'computer', 'ultrawide')

    def build(self):
        """Symbol plan: Use continuous smooth screen curves and a single centered stand. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('screen', (4, 8), [('C', (44, 8), (16, 12), (32, 12)), ('L', (44, 32)), ('C', (24, 30), (38, 30), (30, 30)), ('C', (4, 32), (18, 30), (10, 30)), ('L', (4, 8))], True)
        line('stand', (24, 30), (24, 40))
        join('stand', 'screen')
        poly('base', (14, 40), (24, 40), (34, 40))
        join('stand', 'base')

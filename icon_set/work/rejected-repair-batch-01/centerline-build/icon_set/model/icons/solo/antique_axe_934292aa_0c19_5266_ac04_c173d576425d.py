"""Replace the outlined axe handle with one diagonal stick aligned to the blade socket. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '934292aa-0c19-5266-ac04-c173d576425d'
SOURCE_PATH = 'pictographic-primitives/war/antique axe_934292aa-0c19-5266-ac04-c173d576425d.svg'
AUTHOR = 'gpt-6'

class AntiqueAxe(Solo48):
    icon_id = 'antique-axe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'antique-axe')

    def build(self):
        """Symbol plan: Replace the outlined axe handle with one diagonal stick aligned to the blade socket. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f'{name}-{index}'
                kind, end, *args = command
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C':
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)

        def circle(name, cx, cy, r):
            path(name, (cx - r, cy), [('A', (cx + r, cy), r, r, True), ('A', (cx - r, cy), r, r, True)], True)

        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        path('head', (18, 12), [('L', (24, 6)), ('L', (32, 14)), ('L', (42, 14)), ('C', (30, 34), (42, 27), (36, 34)), ('L', (30, 24)), ('L', (24, 18)), ('L', (18, 12))], True)
        line('handle', (27, 21), (6, 42))
        join('handle', 'head')
